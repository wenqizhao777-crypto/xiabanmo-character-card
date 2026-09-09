from timeline import *
from collections import Counter
import sys
lines=SRC.read_text(encoding='utf-8').splitlines()
data=json.loads((CAN/'events/records.json').read_text(encoding='utf-8'))
lo=int(sys.argv[1]);hi=int(sys.argv[2])
pack=[]
for event in data[lo-1:hi]:
 text=event['title']+event['occurrence']+event['changes']
 grams={text[i:i+n] for n in (3,4,5) for i in range(len(text)-n+1) if all('一'<=v<='龥' for v in text[i:i+n])}
 candidates=[]
 for a,b in event['source_ranges']:
  for j in range(a-1,b):
   if not lines[j].strip() or lines[j].startswith('#'):continue
   score=sum(len(g)**2 for g in grams if g in lines[j])
   candidates.append((score,j))
 candidates.sort(reverse=True)
 chosen=[]
 for score,j in candidates:
  if all(abs(j-k)>3 for k in chosen): chosen.append(j)
  if len(chosen)==2:break
 chosen=[]
 for x in event['audit_navigation']:
  v=EV[x]
  if v.get('quote_line') and v['quote_line']>v['start']+3:j=v['quote_line']-1
  else:
   f=v['finding'];g={f[i:i+n] for n in (3,4,5) for i in range(len(f)-n+1) if all('一'<=c<='龥' for c in f[i:i+n])}
   js=[j for j in range(v['start']-1,v['end']) if lines[j].strip() and not lines[j].startswith('#')]
   j=max(js,key=lambda j:sum(len(a)**2 for a in g if a in lines[j]))
  chosen.append(j)
 chosen=sorted(set(chosen))
 spans=[]
 for j in sorted(chosen):
  a=max(0,j-1);b=min(len(lines)-1,j+1)
  spans.append([a+1,b+1])
 print(event['id'],event['title'])
 for a,b in spans:
  for n in range(a,b+1): print(f'L{n} {lines[n-1]}')
 pack.append(dict(event=event['id'],ranges=spans,selection='词组匹配仅定位；由助手阅读核验，非自动事实证明'))
(CAN/'_build'/f'review_packet_{lo:03d}_{hi:03d}.json').write_text(json.dumps(pack,ensure_ascii=False,indent=2),encoding='utf-8')
