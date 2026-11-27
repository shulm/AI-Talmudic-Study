"""Byte-pinned source audit and deterministic, external-only lane packaging."""
import argparse
import hashlib
import json
from pathlib import Path
import zipfile

PIN = '11997b5ed2c4e2faf84f625164e93f85084fc36c54ce8ba874644835ce071e9c'
ASSIGNMENT_PIN = 'cebe3248155bc225321c9f924104a8f250c6b91a5fc32e9dfe641e014e5c2beb'
REPO = Path(__file__).resolve().parents[2]

def sha(data):
    return hashlib.sha256(data).hexdigest()

def encoded(value):
    return (json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + '\n').encode('utf-8')

def require(ok, message):
    if not ok:
        raise ValueError(message)

def inventory():
    manifest_bytes = (REPO / 'research/bavli_sugya_corpus_v1/source_manifest.json').read_bytes()
    require(sha(manifest_bytes) == PIN, 'Pinned source manifest mismatch')
    local_assignments = (REPO / 'research/bavli_multiplatform_launch_v1/ASSIGNMENTS.json').read_bytes()
    canonical_assignments = local_assignments.replace(b'\r\n', b'\n')
    require(sha(canonical_assignments) == ASSIGNMENT_PIN, 'Pinned assignment content mismatch')
    # Existing v1 archives froze Windows CRLF metadata. Reproduce those bytes on
    # every host without normalizing ANY original source or source schema.
    assignments_bytes = canonical_assignments.replace(b'\n', b'\r\n')
    assignments = json.loads(assignments_bytes)
    manifest = json.loads(manifest_bytes)
    require(assignments['source_manifest_sha256'] == PIN, 'Assignment pin mismatch')
    items = {item['title']: item for item in manifest['tractates']}
    seen = []
    for lane in assignments['lanes']:
        for job in lane['jobs']:
            seen.append(job['tractate'])
            expected = items[job['tractate']]
            for jk, mk in [('source_path', 'source_path'), ('expected_source_sha256', 'source_sha256'), ('source_schema_path', 'schema_path'), ('source_schema_sha256', 'schema_sha256')]:
                require(job[jk] == expected[mk], 'Assignment/manifest mismatch: ' + jk)
    require(len(seen) == 37 and len(set(seen)) == 37 and set(seen) == set(items), 'Tractate inventory mismatch')
    require(sum(j['expected_source_segments'] for l in assignments['lanes'] for j in l['jobs']) == 81793, 'Segment baseline mismatch')
    return assignments, assignments_bytes, manifest, manifest_bytes

def verify_lane(read, lane):
    records = []
    for job in lane['jobs']:
        raw = read(job['source_path'])
        schema = read(job['source_schema_path'])
        require(sha(raw) == job['expected_source_sha256'], job['tractate'] + ' source hash mismatch')
        require(sha(schema) == job['source_schema_sha256'], job['tractate'] + ' schema hash mismatch')
        json.loads(schema)
        doc = json.loads(raw)
        require(doc['title'] == job['tractate'] and doc['versionTitle'] == 'Wikisource Talmud Bavli', 'Edition/title mismatch')
        require(isinstance(doc['text'], list) and all(isinstance(p, list) for p in doc['text']), 'Unexpected source shape')
        require(all(isinstance(s, str) for p in doc['text'] for s in p), 'Nonstring segment')
        count = sum(bool(s.strip()) for p in doc['text'] for s in p)
        require(count == job['expected_source_segments'], job['tractate'] + ' count mismatch')
        records.append({'job_id': job['job_id'], 'tractate': job['tractate'], 'source_path': job['source_path'], 'source_sha256': sha(raw), 'source_bytes': len(raw), 'source_schema_path': job['source_schema_path'], 'source_schema_sha256': sha(schema), 'nonempty_segments': count, 'license_metadata': doc.get('license'), 'versionSource': doc.get('versionSource'), 'status': 'VERIFIED'})
    return records

def make_zip(entries):
    import io
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, 'w', compression=zipfile.ZIP_STORED) as z:
        for name, data in sorted(entries.items()):
            info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            z.writestr(info, data)
    return buffer.getvalue()

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source-root', type=Path)
    p.add_argument('--lane', choices=['L01', 'L02', 'L03', 'L04', 'L05', 'L06'])
    p.add_argument('--package', type=Path)
    p.add_argument('--build-dir', type=Path)
    p.add_argument('--report', type=Path)
    args = p.parse_args()
    assignments, ab, manifest, mb = inventory()
    lanes = [l for l in assignments['lanes'] if not args.lane or l['lane_id'] == args.lane]
    report = {'format_version': '1.0.1', 'source_manifest_sha256': PIN, 'assignments_sha256': sha(ab), 'pinned_git_assignments_sha256': ASSIGNMENT_PIN, 'assignment_bytes_note': 'v1 package metadata fixed CRLF; Git blob fixed LF; exact source bytes never normalized', 'lanes': []}
    if args.package:
        require(bool(args.lane), '--package requires --lane')
        require(not args.build_dir, 'Cannot build and verify package together')
        with zipfile.ZipFile(args.package) as z:
            require(z.read('source_manifest.json') == mb and z.read('ASSIGNMENTS.json') == ab, 'Package metadata does not match repository')
            records = verify_lane(z.read, lanes[0])
            require(sha(z.read(manifest['source_toc_path'])) == manifest['source_toc_sha256'], 'TOC hash mismatch')
            packaged = json.loads(z.read('PACKAGE_MANIFEST.json'))
            require(packaged['files'] == records and packaged['lane_id'] == args.lane, 'Package manifest mismatch')
        report['lanes'].append({'lane_id': args.lane, 'files': records, 'package_sha256': sha(args.package.read_bytes()), 'status': 'VERIFIED_PACKAGE'})
    else:
        require(args.source_root is not None, '--source-root required')
        root = args.source_root.resolve()
        read = lambda name: (root / name).read_bytes()
        require(sha(read(manifest['source_toc_path'])) == manifest['source_toc_sha256'], 'TOC hash mismatch')
        if args.build_dir:
            dest = args.build_dir.resolve()
            require(not dest.is_relative_to(REPO), 'Full sources must remain outside repository')
            require(not dest.is_relative_to(root), 'Never write into source corpus')
            dest.mkdir(parents=True, exist_ok=True)
        for lane in lanes:
            records = verify_lane(read, lane)
            row = {'lane_id': lane['lane_id'], 'files': records, 'source_root': str(root), 'local_status': 'VERIFIED_AVAILABLE', 'remote_status': 'NOT_TRANSFERRED', 'source_segments': sum(r['nonempty_segments'] for r in records)}
            if args.build_dir:
                entries = {name: read(name) for j in lane['jobs'] for name in (j['source_path'], j['source_schema_path'])}
                entries.update({'source_manifest.json': mb, 'ASSIGNMENTS.json': ab, manifest['source_toc_path']: read(manifest['source_toc_path']), 'SEFARIA_LICENSE.md': read('LICENSE.md')})
                pm = {'lane_id': lane['lane_id'], 'source_manifest_sha256': PIN, 'assignments_sha256': sha(ab), 'files': records}
                entries['PACKAGE_MANIFEST.json'] = encoded(pm)
                payload = make_zip(entries)
                require(payload == make_zip(entries), 'Deterministic packaging failed')
                target = dest / (lane['lane_id'] + '.zip')
                if target.exists():
                    require(target.read_bytes() == payload, 'Refusing to replace different existing package: ' + str(target))
                else:
                    target.write_bytes(payload)
                row.update(package_path=str(target), package_sha256=sha(payload), package_bytes=len(payload), package_manifest_sha256=sha(entries['PACKAGE_MANIFEST.json']), deterministic_rebuild='PASS')
            report['lanes'].append(row)
    if args.report:
        args.report.write_bytes(encoded(report))
    print(json.dumps({'status': 'PASS', 'lanes': len(lanes), 'tractates': sum(len(r['files']) for r in report['lanes']), 'segments': sum(f['nonempty_segments'] for r in report['lanes'] for f in r['files'])}))

if __name__ == '__main__':
    main()
