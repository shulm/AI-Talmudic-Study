"""Adversarial data corruption tests, no duplicate source extraction."""
import copy
import jsonschema
import pipeline as p
import validate as v

def main():
    original=v.load_data();v.validate(original,check_source=False);tests=[]
    def rejects(name,mutate):
        d=copy.deepcopy(original);mutate(d)
        try:v.validate(d,check_source=False)
        except (AssertionError,KeyError,jsonschema.ValidationError):tests.append(name)
        else:raise AssertionError('Accepted corrupted dataset: '+name)
    rejects('one-daf offset',lambda d:d['segments'][0].update(ref='Berakhot 3a:1'))
    rejects('rewritten source text',lambda d:d['segments'][0].update(text='rewritten'))
    rejects('duplicate stable ID',lambda d:d['segments'].append(d['segments'][0]))
    rejects('unknown schema property',lambda d:d['positions'][0].update(guessed=True))
    rejects('dangling graph endpoint',lambda d:d['relations'][0].update(target_id='absent'))
    rejects('overlapping primary coverage',lambda d:d['sugyot'].append({**d['sugyot'][0],'id':'other'}))
    rejects('quote not exact substring',lambda d:d['statements'][0]['evidence'][0].update(quote='fabricated'))
    def guess(d):
        r=next(s for s in d['statements'] if s['speaker_candidates']);r['attributed_authority_id']=r['speaker_candidates'][0]
    rejects('name-order assignment to unresolved alternative',guess)
    # Stable source identity is address+edition, not text deduplication or current boundary.
    assert p.stable('seg','Berakhot',p.VERSION,'2','0')!=p.stable('seg','Berakhot',p.VERSION,'2','1')
    report=dict(passed=True,corruption_tests=len(tests),tests=tests,scope='mechanical safeguards, not scholarly accuracy')
    p.write(p.HERE/'test_report.json',report);print(report)
if __name__=='__main__':main()
