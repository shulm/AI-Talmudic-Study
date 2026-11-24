"""Frozen MiniLM, full-token windows; no labels opened."""
import importlib.metadata
import numpy as np
import requests
import torch
from huggingface_hub import snapshot_download
from transformers import AutoModel, AutoTokenizer
from common import *

def main():
    torch.set_num_threads(2)
    model_id='sentence-transformers/all-MiniLM-L6-v2'
    revision=requests.get('https://huggingface.co/api/models/'+model_id,timeout=30).json()['sha']
    pinned=OUT/'encoder_manifest.json'
    if pinned.exists(): revision=read(pinned)['revision']
    path=snapshot_download(model_id,revision=revision,allow_patterns=['config.json','model.safetensors','tokenizer.json','tokenizer_config.json','special_tokens_map.json','vocab.txt','modules.json','sentence_bert_config.json','1_Pooling/config.json'],cache_dir=str(PRIVATE/'hf'))
    path=Path(path)
    tokenizer=AutoTokenizer.from_pretrained(path,local_files_only=True)
    model=AutoModel.from_pretrained(path,local_files_only=True).eval()
    limit=read(path/'sentence_bert_config.json')['max_seq_length']
    pool=read(path/'1_Pooling/config.json')
    assert pool['pooling_mode_mean_tokens'] and not pool['pooling_mode_cls_token']
    budget=limit-tokenizer.num_special_tokens_to_add(pair=False)
    vectors=[]; counts=[]
    for row in read(PRIVATE/'learner.json'):
        tokens=tokenizer.encode(row['text'],add_special_tokens=False,truncation=False)
        chunks=[tokens[i:i+budget] for i in range(0,len(tokens),budget)]
        vec=[]
        for chunk in chunks:
            batch=tokenizer.prepare_for_model(chunk,return_tensors='pt',truncation=False)
            batch={k:v.unsqueeze(0) if v.ndim==1 else v for k,v in batch.items()}
            with torch.no_grad():
                h=model(**batch).last_hidden_state
                mask=batch['attention_mask'].unsqueeze(-1)
                vec.append(((h*mask).sum(1)/mask.sum(1)).numpy()[0])
        v=np.average(vec,axis=0,weights=[len(c) for c in chunks]); v/=np.linalg.norm(v)
        vectors.append(v); counts.append(dict(tokens=len(tokens),windows=len(chunks),covered=sum(map(len,chunks))))
    np.save(PRIVATE/'embeddings.npy',np.array(vectors))
    write(pinned,dict(model_id=model_id,revision=revision,tokenizer_revision=revision,dimension=len(vectors[0]),max_sequence_length=limit,content_window=budget,pooling=pool,normalization='Token-count-weighted mean of unnormalized mean-pooled windows; final L2',serialization='Context:\n{context}\n\nAssessed response:\n{response}',token_coverage=1,total_tokens=sum(c['tokens'] for c in counts),total_windows=sum(c['windows'] for c in counts),max_windows=max(c['windows'] for c in counts),files=[manifest(p) for p in path.rglob('*') if p.is_file()],embedding=manifest(PRIVATE/'embeddings.npy'),libraries={k:importlib.metadata.version(k) for k in ['torch','transformers','numpy','huggingface-hub','safetensors']}))
    print(json.dumps(read(pinned)))

if __name__=='__main__': main()
