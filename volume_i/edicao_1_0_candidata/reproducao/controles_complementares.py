"""Controles sintéticos novos VI05. Não importa controles herdados ou motores."""
from pathlib import Path
from itertools import product
import json, random, time

def next_monitor(i,bit,label,k=2):
 hit=bool(label & (1<<i))
 return ((i+1)%k if hit else i, int(hit and i==k-1))

def periodic_accept(prefix,period,i):
 b=0
 for label in prefix:i,b=next_monitor(i,b,label)
 seen={};seq=[];pos=0
 while (i,b,pos) not in seen:
  seen[i,b,pos]=len(seq);seq.append((i,b,pos))
  i,b=next_monitor(i,b,period[pos]);pos=(pos+1)%len(period)
 cycle=seq[seen[i,b,pos]:]
 return any(b for i,b,pos in cycle)

def cpre(g,z):return {s for s in g if any(es and all(t in z for t,l in es) for es in g[s].values())}
def buchi(g,v,b):
 z=set(v)
 while True:
  y=set()
  while True:
   yn=(b&v&cpre(g,z)) | (v&cpre(g,y))
   if yn==y:break
   y=yn
  if y==z:return y
  z=y

def reachable(edges,s):
 seen={s};todo=[s]
 while todo:
  for t in edges[todo.pop()]:
   if t not in seen:seen.add(t);todo.append(t)
 return seen

def oracle(g,v,b):
 # Enumera políticas estacionárias no produto; elimina vértices de um DAG
 # sem aceitação por remoção de sumidouros, em vez de usar pontos fixos Büchi.
 states=list(g);winning=set();n=0
 for acts in product(*[list(g[s]) or [None] for s in states]):
  n+=1;edges={s:{t for t,l in g[s].get(a,set())} for s,a in zip(states,acts)}
  for s in states:
   if s in winning:continue
   reach=reachable(edges,s)
   if not reach<=v or any(not edges[t] for t in reach):continue
   bad=reach-b
   while True:
    remove={t for t in bad if not edges[t]&bad}
    if not remove:break
    bad-=remove
   if not bad:winning.add(s)
 return winning,n

def prod_game(g,v):
 out={};safe=set();accept=set()
 for x,i,b in product(g,range(2),range(2)):
  s=x,i,b;out[s]={}
  if x in v:safe.add(s)
  if b:accept.add(s)
  for a,es in g[x].items():out[s][a]={((y,*next_monitor(i,b,l)),l) for y,l in es}
 return out,safe,accept

def refine(xs,obs,ops):
 colors={x:obs(x) for x in xs}
 while True:
  sig={x:(colors[x],tuple(None if op(x) is None else colors[op(x)] for op in ops)) for x in xs}
  uniq={s:i for i,s in enumerate(dict.fromkeys(sig.values()))};new={x:uniq[sig[x]] for x in xs}
  if all((colors[x]==colors[y])==(new[x]==new[y]) for x in xs for y in xs):return len(set(new.values()))
  colors=new

def main():
 start=time.perf_counter();r={};n=0
 prefixes=[()] + list(product(range(4),repeat=1))+list(product(range(4),repeat=2))
 for size in range(1,5):
  for period in product(range(4),repeat=size):
   expected=all(any(l&(1<<i) for l in period) for i in range(2))
   for prefix in prefixes:
    for initial in range(2):
     assert periodic_accept(prefix,period,initial)==expected;n+=1
 r['monitor_duas_obrigacoes_palavras_eventualmente_periodicas']=dict(comparacoes=n,periodos='todos de comprimento 1–4 sobre etiquetas 0,1,2,3',prefixos='todos de comprimento 0–2',indices_iniciais=[0,1],bit_inicial=0)
 rng=random.Random(26052026);comparisons=policies=0
 for _ in range(48):
  g={x:{} for x in range(2)}
  universe=list(product(range(2),range(4)))
  for x in g:
   for a in range(2):
    if rng.random()<.15:continue
    g[x][a]=set(rng.sample(universe,rng.randint(1,3)))
  for mask in range(4):
   v={x for x in g if mask>>x&1};p,s,b=prod_game(g,v)
   actual,count=oracle(p,s,b);expected=buchi(p,s,b)
   assert actual==expected,(g,v,actual,expected)
   comparisons+=1;policies+=count
 r['buchi_produto_duas_obrigacoes']=dict(jogos_amostrados=48,segurancas_por_jogo=4,comparacoes=comparisons,politicas_enumeradas=policies,semente=26052026,estados_produto=8,oraculo='Enumeração de políticas e detecção de ciclos por remoção de sumidouros; não usa ν/μ')
 X=list(product(range(3),range(2),range(2)))
 L=lambda x:(min(x[0]+1,2),x[1],x[2])
 R=lambda x:(x[0],int(x[2]==1 and x[0]==1),x[2])
 Q=lambda x:(x[0],x[1],1)
 assert refine(X,lambda x:x[1:],[L,R])==8
 assert refine(X,lambda x:x[1:],[L,R,Q])==12
 X=list(product(range(2),repeat=3));counts=[]
 for eta in (0,1):
  ops=[lambda x,u=u,e=eta:(x[1],x[2],x[0]^u^(e&x[1])) for u in range(2)]
  counts.append(refine(X,lambda x:x[0]^x[1]^x[2],ops))
 assert counts==[2,8]
 J=lambda x:None if x[2]==0 else (x[0],x[1]^x[0],0)
 N=lambda x:(x[0],x[1],1)
 assert refine(X,lambda x:x[:2],[J,N])==8
 F=lambda x:(x[1],x[2]&x[0],x[1]&x[0])
 paths=[]
 for s,length in [((0,1,1),2),((1,0,1),3),((1,1,0),4)]:
  path=[s]
  for t in range(length):path.append(F(path[-1]))
  assert path[-1]==(0,0,0) and all(x!=(0,0,0) for x in path[:-1]);paths.append(path)
 assert F((1,1,1))==(1,1,1)
 r['modelos_recalculados']=dict(P06_2=[8,12],P06_3=counts,P08_5=8,P10_7_tracos=paths)
 # M11, alcance existencial, sem jogo adversarial acrescentado.
 recover={}
 for init in X:
  todo=[(init,0)];seen={init};dist=None
  while todo:
   x,k=todo.pop(0)
   if x==(1,1,1):dist=k;break
   b,res,v=x;succ=[]
   if b==0 and res:succ.append((1,res,v))
   if v==0 and b:succ.append((b,res,1))
   if res==0 and b and v:succ.append((b,1,v))
   for y in succ:
    if y not in seen:seen.add(y);todo.append((y,k+1))
  assert (dist is not None)==bool(init[0] or init[1]);assert dist is None or dist<=2
  recover[''.join(map(str,init))]=dist
 r['M11_distancias']=recover
 # Conjunção operacional dos cinco IO; prova de contagem, não preenchimento empírico.
 vals=list(product('SV?',repeat=5))
 evaluation=lambda x:'V' if 'V' in x else ('S' if all(i=='S' for i in x) else '?')
 io={k:sum(evaluation(x)==k for x in vals) for k in 'SV?'}
 assert io=={'S':1,'V':211,'?':31};r['avaliacoes_IO']=io
 r['status']='SEM_DIVERGENCIA_NOS_CASOS_EXECUTADOS';r['tempo_segundos']=round(time.perf_counter()-start,3)
 r['limites']='Controle sintético com duas obrigações e jogos pequenos amostrados; não prova todos os jogos, informação parcial, prazo físico, infinitude ou adequação constitutiva.'
 print(json.dumps(r,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
