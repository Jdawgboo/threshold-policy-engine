"""Choose binary thresholds under transparent constraints."""
from __future__ import annotations

def metrics(scores:list[float], actual:list[int], threshold:float)->dict:
 predicted=[int(score>=threshold) for score in scores]; tp=sum(p==1 and a==1 for p,a in zip(predicted,actual)); fp=sum(p==1 and a==0 for p,a in zip(predicted,actual)); fn=sum(p==0 and a==1 for p,a in zip(predicted,actual));
 precision=tp/(tp+fp) if tp+fp else 0.; recall=tp/(tp+fn) if tp+fn else 0.; return {'threshold':threshold,'precision':precision,'recall':recall,'cost':fp+fn}
def choose(scores:list[float],actual:list[int],min_precision:float=0.,min_recall:float=0.)->dict|None:
 candidates=[metrics(scores,actual,t) for t in sorted(set(scores))]; valid=[c for c in candidates if c['precision']>=min_precision and c['recall']>=min_recall]; return min(valid,key=lambda c:(c['cost'],-c['threshold'])) if valid else None
if __name__=='__main__':
 import json,sys; p=json.load(sys.stdin); print(json.dumps(choose(p['scores'],p['actual'],p.get('min_precision',0),p.get('min_recall',0)),indent=2))
