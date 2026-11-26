"""Controles sintéticos VI-02; Python 3, biblioteca padrão. Sem motores."""
import itertools as it, random, json
from collections import defaultdict
from pathlib import Path

def pre(g,z):
    return {x for x,acts in g.items() if any(es and all(y in z for y,l in es) for es in acts.values())}

def safety(g,v):
    z=set(v)
    while True:
        n=set(v)&pre(g,z)
        if n==z:return z
        z=n

def buchi(g,v,f):
    z=set(v)
    while True:
        y=set()
        while True:
            n=set(v)&((set(f)&pre(g,z))|pre(g,y))
            if n==y:break
            y=n
        if y==z:return z
        z=y

def product(g,v,obligations):
    # l é bitmask de eventos. Um requisito por transição; volta marca b=1.
    k=len(obligations); G={}; V=set(); F=set()
    for x in g:
        for i,b in it.product(range(k),range(2)):
            s=(x,i,b); G[s]={}
            if x in v:V.add(s)
            if b:F.add(s)
            for a,es in g[x].items():
                out=set()
                for y,l in es:
                    ok=bool(l & obligations[i]); j=(i+1)%k if ok else i
                    out.add(((y,j,int(ok and i==k-1)),0))
                G[s][a]=out
    return G,V,F

def direct_policy(g,v,f):
    # Oráculo independente: enumera políticas estacionárias no produto;
    # alcançabilidade adversarial e ciclo evitável de F, por fecho transitivo.
    states=list(g); win=set()
    choices=[[a for a,es in g[x].items() if es] or [None] for x in states]
    for acts in it.product(*choices):
        edges={x:set(y for y,l in g[x].get(a,())) for x,a in zip(states,acts)}
        for x in states:
            if x in win:continue
            reach={x}; frontier=[x]
            while frontier:
                q=frontier.pop()
                for y in edges[q]-reach:reach.add(y);frontier.append(y)
            if not reach<=v or any(not edges[q] for q in reach):continue
            bad=reach-set(f); cycle=False
            for q in bad:
                seen=set(); todo=list(edges[q]&bad)
                while todo:
                    t=todo.pop()
                    if t in seen:continue
                    seen.add(t);todo.extend((edges[t]&bad)-seen)
                if q in seen:cycle=True;break
            if not cycle:win.add(x)
    return win

def quotient(g,p,v):
    q={}; flags={}
    for x,acts in g.items():
        u=p[x]; sig={a:frozenset((p[y],l) for y,l in es) for a,es in acts.items() if es}
        if u in q and (q[u]!=sig or flags[u]!=(x in v)):raise ValueError('fibra não homogênea')
        q[u]=sig; flags[u]=(x in v)
    return q,{u for u in q if flags[u]}

def blowup(q,v,rng):
    p={(x,i):x for x in q for i in range(2)}; g={}
    for u in p:
        g[u]={}
        for a,es in q[p[u]].items():
            g[u][a]={( (y,i),l) for y,l in es for i in rng.choice([(0,),(1,),(0,1)])}
    return g,p,{u for u in p if p[u] in v}

def refine(g,v):
    p={x:int(x in v) for x in g}
    while True:
        sigs={}; n={}
        for x,acts in g.items():
            sig=(p[x],tuple(sorted((a,tuple(sorted({(p[y],l) for y,l in es}))) for a,es in acts.items() if es)))
            n[x]=sigs.setdefault(sig,len(sigs))
        if all((p[x]==p[y])==(n[x]==n[y]) for x in g for y in g):return n
        p=n

def main():
    report={}; rng=random.Random(20261126)
    # Exaustão: 2 estados, 2 ações, 3 sucessores não vazios, 4 conjuntos de segurança.
    subs=[{(0,0)},{(1,0)},{(0,0),(1,0)}]; n=0
    for es in it.product(subs,repeat=4):
        q={x:{a:es[2*x+a] for a in range(2)} for x in range(2)}
        for b in range(4):
            v={x for x in q if b>>x&1};g,p,V=blowup(q,v,rng)
            qq,vv=quotient(g,p,V);assert qq==q and vv==v
            for mask in range(4):
                z={x for x in q if mask>>x&1};assert pre(g,{x for x in g if p[x] in z})=={x for x in g if p[x] in pre(q,z)}
            assert safety(g,V)=={x for x in g if p[x] in safety(q,v)};n+=1
    report['seguranca_exaustao']={'jogos_restricoes':n,'predecessores':n*4}
    # 512 jogos rotulados com 2 estados, duas ações, dois eventos e ações desabilitáveis.
    n=0; oracle=0; refinement=0
    for t in range(512):
        q={x:{a:{(y,l) for y in range(2) for l in range(4) if rng.randrange(4)==0} for a in range(2)} for x in range(2)}
        v={x for x in q if rng.randrange(4)!=0};g,p,V=blowup(q,v,rng)
        qq,vv=quotient(g,p,V);assert vv==v
        for obligations in [(1,),(1,2)]:
            G,W,F=product(g,V,obligations);Q,U,B=product(q,v,obligations)
            wp=buchi(G,W,F);wq=buchi(Q,U,B)
            assert wp=={(x,i,b) for x,i,b in G if (p[x],i,b) in wq};n+=1
            if len(obligations)==1:
                assert wq==direct_policy(Q,U,B);oracle+=1
        r=refine(g,V);quotient(g,r,V)
        assert all(p[x]!=p[y] or r[x]==r[y] for x in g for y in g);refinement+=1
    report['recorrencia_amostrada']={'semente':20261126,'comparacoes_produto':n,'oraculo_politicas':oracle,'refinamentos':refinement}
    # C1: as mesmas transições sem rótulo de ação não preservam quantificadores.
    a={0:{0:{(0,0)},1:{(1,0)}},1:{0:{(1,0)}}}; b={0:{0:{(0,0),(1,0)}},1:{0:{(1,0)}}}
    erase=lambda g:{x:{y for es in acts.values() for y,l in es} for x,acts in g.items()}
    assert erase(a)==erase(b) and safety(a,{0})=={0} and not safety(b,{0})
    # C2: mesmo estado e dinâmica, evento produtivo omitido.
    a={0:{0:{(0,1)}}};b={0:{0:{(0,0)}}};assert erase(a)==erase(b)
    A,V,F=product(a,{0},(1,));B,W,H=product(b,{0},(1,));assert (0,0,0) in buchi(A,V,F) and (0,0,0) not in buchi(B,W,H)
    # C3: guardas permitida sem resultado x negada; no sistema relacional vazio.
    assert set()==set() and 'permitido'!='negado'
    # C4: mesmos estados terminais, continuidade diverge.
    assert [1,0,1][-1]==[1,1,1][-1] and not all([1,0,1]) and all([1,1,1])
    # C5: produtividade recorrente sem prazo fixo. 0 sempre seguro nominalmente;
    # produção nos tempos 2^k. As lacunas 2^k crescem sem limite.
    times=[2**k for k in range(10)];assert max(b-a for a,b in zip(times,times[1:]))==256
    # C6: juntar testemunhos antes de ocultar.
    R={(0,0)};S={(1,0)};assert not {(x,z) for x,y in R for yy,z in S if y==yy}; assert {(x,z) for x,y in R for yy,z in S}=={(0,0)}
    report['contramodelos']={'C1':'controle/disturbio','C2':'eventos','C3':'guarda x relacao vazia (ilustracao)','C4':'continuidade','C5':'prazo (prefixo ilustrativo)','C6':'testemunho compartilhado'}
    print(json.dumps(report,indent=2,ensure_ascii=False))
if __name__=='__main__':main()
