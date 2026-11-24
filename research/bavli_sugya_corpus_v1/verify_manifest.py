"""Public-byte integrity check. Does not regenerate annotations or contact services."""
import pipeline as p
def main():
    manifest=p.read(p.HERE/'delivery_manifest.json')
    for f,h in manifest['files'].items():assert p.sha((p.HERE/f).read_bytes())==h,f+' changed'
    print('PASS:',len(manifest['files']),'public artifact hashes; semantic truth is not certified.')
if __name__=='__main__':main()
