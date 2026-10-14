import json
from pathlib import Path
puzzles=json.loads(Path(__file__).with_name('puzzles.js').read_text().split('=',1)[1].rstrip(';\n'))
units=[[r*9+c for c in range(9)] for r in range(9)]+[[r*9+c for r in range(9)] for c in range(9)]+[[r*9+c for r in range(br,br+3) for c in range(bc,bc+3)] for br in range(0,9,3) for bc in range(0,9,3)]
peers=[set().union(*(set(u) for u in units if i in u))-{i} for i in range(81)]
def solutions(b):
 b=b[:];found=[]
 def search():
  options=[(set(range(1,10))-{b[j] for j in peers[i]},i) for i,v in enumerate(b) if not v]
  if not options:found.append(b[:]);return
  cs,i=min(options,key=lambda x:len(x[0]))
  for v in sorted(cs):
   b[i]=v;search()
   if len(found)>1:break
  b[i]=0
 search();return found
assert len(puzzles)==10
assert len({tuple(p['givens']) for p in puzzles})==10
for p in puzzles:
 assert all(set(p['solution'][i] for i in u)==set(range(1,10)) for u in units)
 assert all(not v or v==p['solution'][i] for i,v in enumerate(p['givens']))
 assert solutions(p['givens'])==[p['solution']]
 b=p['givens'][:]
 while True:
  cs={i:set(range(1,10))-{b[j] for j in peers[i]} for i,v in enumerate(b) if not v}
  moves={i:next(iter(c)) for i,c in cs.items() if len(c)==1}
  for u in units:
   for v in range(1,10):
    spots=[i for i in u if i in cs and v in cs[i]]
    if len(spots)==1:moves[spots[0]]=v
  if not moves:break
  for i,v in moves.items():b[i]=v
 assert sum(v==0 for v in b)==p['singlesRemaining']>=45
 assert p['searchNodes']>=5000
 print(f"Puzzle {p['id']:02}: unique, valid; {p['clues']} clues, {p['searchNodes']} search nodes")
print('PASS: 10 distinct puzzles')
