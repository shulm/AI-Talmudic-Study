# Exact source access, 2026-11-25

All six lanes have verified original-source access on this Windows host. All 37 named-edition files, 37 source schemas, and the original table of contents match the pinned inventory. The nonempty segment total is 81,793. This is source readiness only; it does not establish semantic extraction, lane ownership, or review completion.

Portability correction: the pinned Git `ASSIGNMENTS.json` blob has LF bytes and SHA-256 `cebe3248155bc225321c9f924104a8f250c6b91a5fc32e9dfe641e014e5c2beb`. Windows checkout/package metadata has CRLF bytes and SHA-256 `2135b23fe5cb89434ff895b83c9ab636af53df5abeddcae25ac01ec8c010b56d`. Their parsed content is identical. The verifier checks the approved LF assignment hash, then reproduces the already frozen CRLF package metadata on every host. Original source, source schemas, and pinned source manifest are never normalized. Existing ZIP hashes are unchanged.

The source manifest is `research/bavli_sugya_corpus_v1/source_manifest.json`, SHA-256 `11997b5ed2c4e2faf84f625164e93f85084fc36c54ce8ba874644835ce071e9c`. `SOURCE_ACCESS_AUDIT.json` records every actual source/schema hash, source count, edition metadata, and package hash. The authoritative source root remains `F:/Sefaria-Export-master`, read-only throughout this work.

## Packages available to transfer

Six actual transferable ZIP artifacts are stored at `F:/Sefaria_QA/bavli_source_packages_v1/`. They contain only the lane's exact original files and source schemas, the pinned table of contents, source manifest, static assignments, package manifest, and original export license notice. Archive members preserve original relative paths. ZIP timestamps, ordering, permissions, and storage encoding are fixed; repeated construction was byte-identical. Full source texts are outside Git history.

| Lane | Tractates | Segments | ZIP file | SHA-256 |
|---|---:|---:|---|---|
| L01 | 6 | 13,657 | L01.zip | `94ffd2301a9ae6ce9820857c26ed579ab434dfb65db1f1a05bf27be762fb7e80` |
| L02 | 5 | 13,669 | L02.zip | `452e7306b8dcd4daad3347b2ca71d3b63f7d0588127b46c153b2762f424cc242` |
| L03 | 7 | 13,635 | L03.zip | `820487dce3d741f6009979eb2b2c8d399951471ba4d2978ebc2be50c2a9605d3` |
| L04 | 7 | 13,593 | L04.zip | `b027a02a43e48b5f16bff6a12886e5d812bcf2e1ca246767b8875896ed70f983` |
| L05 | 6 | 13,598 | L05.zip | `1d4b3615e6048ed84f094e35197c97b5a441e4efc99fe0d87b3fb7a4921b2b18` |
| L06 | 6 | 13,641 | L06.zip | `4327c2601dcd0cace17890844d8fd77a0d4c4ff28f57419a3b0092dca8d74202` |

No remote upload, cloud mount, or other-platform receipt has occurred. A platform without this host's F: drive must receive its named ZIP through an authorized artifact transfer, then verify it. A repository checkout alone does not supply source bytes. This is the exact outstanding remote source-access step for every lane deployed elsewhere. Independent source-only readers can receive the same verified source package without production annotations.

## Verification and use

Use Python 3.10+ with the standard library, from the repository root. Verify this machine's complete source inventory:

```powershell
python -X utf8 research/bavli_source_access_v1/source_packages.py --source-root F:/Sefaria-Export-master
```

After transferring L01.zip, check its ZIP hash against the table and verify every source/schema member against the pinned repository inventory. Substitute the appropriate lane and destination path:

```powershell
Get-FileHash -Algorithm SHA256 F:/Sefaria_QA/bavli_source_packages_v1/L01.zip
python -X utf8 research/bavli_source_access_v1/source_packages.py --lane L01 --package F:/Sefaria_QA/bavli_source_packages_v1/L01.zip
python -m zipfile -e F:/Sefaria_QA/bavli_source_packages_v1/L01.zip F:/Sefaria_QA/lane_sources/L01
python -X utf8 research/bavli_source_access_v1/source_packages.py --lane L01 --source-root F:/Sefaria_QA/lane_sources/L01
```

On Linux/macOS, use `sha256sum /path/L01.zip` for the archive hash and the same Python commands with local absolute paths. Use the extraction directory as the production source-root argument. Do not extract into the repository or overwrite the historical source export. A valid verifier prints `PASS`, the lane's tractate count, and segment total; any mismatched source, schema, TOC, edition, title, count, or inventory pin raises an error and exits unsuccessfully.

Recreate packages without changing original bytes:

```powershell
python -X utf8 research/bavli_source_access_v1/source_packages.py --source-root F:/Sefaria-Export-master --build-dir F:/Sefaria_QA/bavli_source_packages_v1 --report research/bavli_source_access_v1/SOURCE_ACCESS_AUDIT.json
```

Existing identical packages are retained; different existing files are rejected. Build destinations inside this checkout or the original source root are rejected. `--report` is an explicit report output path; never point it into the original corpus.

## Distribution metadata preserved

Every selected source file declares `license: CC-BY-SA`, `versionTitle: Wikisource Talmud Bavli`, and its original Wikisource `versionSource` URL. The export's `LICENSE.md` says individual text license fields govern; it does not declare one license for the entire export. The selected files do not specify a CC-BY-SA version. No version or separate schema license has been inferred. Packages retain exact metadata and the export's license notice; any public derivative should retain this attribution/provenance and resolve applicable distribution requirements before release. These local package checks do not constitute an independent licensing determination.

## Verification evidence

The complete original-source check passed for 37 tractates / 81,793 segments. Each of the six ZIPs was separately reopened and validated against the repository manifest, assignments, TOC, source hashes, schema hashes, edition, counts, and package manifest. Rebuilding each archive twice in memory produced identical bytes. These checks establish byte fidelity and source portability, not scholarly accuracy.
