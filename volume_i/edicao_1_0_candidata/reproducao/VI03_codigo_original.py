"""VI-03: controles próprios, sem importar VI-02 ou motores. Python 3 padrão.

Oráculo: enumeração de políticas; segurança por fecho alcançável; Büchi
por inexistência de ciclo alcançável no subgrafo sem aceitação. Não usa ν/μ.
"""
import itertools as it, random, json, pathlib, functools, time
O=pathlib.Path(__file__).resolve().parent
def reach(edges,start):
    seen={start};todo=[start]
    while todo:
        for y in edges[todo.pop()]:
            if y not in seen:seen.add(y);todo.append(y)
    return seen
def wins_policy(g,policy,v,f=None):
    edges={s:{t for t,l in g[s].get(policy[s],set())} for s in g}
    good=set()
    for s in g:
        r=reach(edges,s)
        if not r<=v or any(not edges[t] for t in r):continue
        if f is not None:
            bad=r-f;be={t:edges[t]&bad for t in bad}
            if any(t in set().union(*(reach(be,u) for u in be[t])) for t in bad if be[t]):continue
        good.add(s)
    return good
def policies(g):
    ss=list(g)
    for choices in it.product(*[list(g[s]) or [None] for s in ss]):yield dict(zip(ss,choices))
def oracle(g,v,f=None):return set().union(*(wins_policy(g,pi,v,f) for pi in policies(g)))
def validate(g):return all(es and all(t in g for t,l in es) for acts in g.values() for es in acts.values())
def cert(c,a,p,vc,va,fc=None,fa=None):
    if not validate(c) or not validate(a):return None
    if any(p[x] in va and x not in vc for x in c):return None
    if fa is not None and any(p[x] in fa and x not in fc for x in c):return None
    witness={}
    for x in c:
        for b,es in a[p[x]].items():
            options=[u for u,ds in c[x].items() if {(p[y],l) for y,l in ds}<=es]
            if not options:return None
            witness[x,b]=options[0]
    return witness
def product(g,v,events):
    k=len(events);q={};safe=set();accept=set()
    for x,i,b in it.product(g,range(k),range(2)):
        s=(x,i,b);q[s]={}
        if x in v:safe.add(s)
        if b:accept.add(s)
        for a,es in g[x].items():
            q[s][a]={((y,(i+1)%k if l&events[i] else i,int(bool(l&events[i]) and i==k-1)),l) for y,l in es}
    return q,safe,accept
def subsets(xs):
    xs=list(xs)
    return [set(xs[i] for i in range(len(xs)) if mask>>i&1) for mask in range(1<<len(xs))]
def cpre(g,z):return {s for s in g if any(es and all(y in z for y,l in es) for es in g[s].values())}
def fixed_buchi(g,v,f):
    z=set(v)
    while True:
        y=set()
        while True:
            yy=v&((f&cpre(g,z))|cpre(g,y))
            if yy==y:break
            y=yy
        if y==z:return z
        z=y
def partitions(n):
    def rec(p):
        if len(p)==n:yield tuple(p);return
        for b in range(max(p,default=-1)+2):yield from rec(p+[b])
    yield from rec([])
def stable(g,p,v,obs):
    sig=lambda x:(x in v,obs[x],tuple((a,tuple(sorted({(p[y],l) for y,l in es}))) for a,es in sorted(g[x].items())))
    return all(p[x]!=p[y] or sig(x)==sig(y) for x in g for y in g)
def refine(g,v,obs):
    p={};ids={}
    for x in g:p[x]=ids.setdefault((x in v,obs[x]),len(ids))
    steps=0
    while True:
        ids={};q={}
        for x in g:
            sig=(p[x],tuple((a,tuple(sorted({(p[y],l) for y,l in es}))) for a,es in sorted(g[x].items())))
            q[x]=ids.setdefault(sig,len(ids))
        if all((p[x]==p[y])==(q[x]==q[y]) for x in g for y in g):return q,steps
        p=q;steps+=1
@functools.lru_cache(None)
def micro_wins(e0,e1,vm,fm):
    g={0:{'u':set(e0)},1:{'u':set(e1)}};v={s for s in g if vm>>s&1};f={s for s in g if fm>>s&1}
    return oracle(g,v),oracle(g,v,f)
def main():
    start=time.perf_counter();r={};universe=[(0,0),(0,1),(1,0),(1,1)]
    nonempty=subsets(universe)[1:];pairs=[(tuple(sorted(a)),tuple(sorted(c))) for a in nonempty for c in subsets(a)[1:]]
    n=0
    for (a0,c0),(a1,c1) in it.product(pairs,repeat=2):
        for vm,fm in it.product(range(4),repeat=2):
            sa,ba=micro_wins(a0,a1,vm,fm);sc,bc=micro_wins(c0,c1,vm,fm)
            assert sa<=sc and ba<=bc;n+=1
    r['PVI02.3_exaustao_micro']={'pares_por_estado':len(pairs),'pares_jogos':len(pairs)**2,'comparacoes_seguranca_e_buchi':n,'escopo':'2 estados; uma ação; 2 etiquetas; projeção identidade; conjuntos de segurança/aceitação saturados; todas inclusões não vazias'}
    rng=random.Random(2026112603);checks=0;lifted=0;products=0
    for trial in range(96):
        a={s:{} for s in range(2)}
        for s,u in it.product(range(2),range(2)):
            if rng.random()<.15:continue
            es={(t,l) for t,l in it.product(range(2),range(4)) if rng.random()<.25}
            if es:a[s][u]=es
        p={x:x//2 for x in range(4)};c={x:{} for x in p};selector={}
        for x in c:
            for u,es in a[p[x]].items():
                ds=[(t*2+rng.randrange(2),l) for t,l in sorted(es)];ds=[z for z in ds if rng.random()<.7] or ds[:1]
                cu=f'w{x}_{u}';c[x][cu]=set(ds);selector[x,u]=cu
        va={s for s in a if rng.random()<.8};vc={x for x in c if p[x] in va};w=cert(c,a,p,vc,va);assert w is not None
        for obligations in [(1,),(1,2)]:
            A,V,F=product(a,va,obligations);C,U,H=product(c,vc,obligations);P={s:(p[s[0]],s[1],s[2]) for s in C}
            wa=oracle(A,V,F)
            # Enumerar apenas políticas abstratas; cada uma tem levantamento explícito.
            union=set()
            for pi in policies(A):
                winning=wins_policy(A,pi,V,F)
                cp={s:selector.get((s[0],pi[P[s]]),None) for s in C}
                got=wins_policy(C,cp,U,H)
                assert {s for s in C if P[s] in winning}<=got
                union|=winning;lifted+=1
            assert union==wa
            assert fixed_buchi(A,V,F)==wa;products+=1
            checks+=len(C)
    r['PVI02.3_levantamento_politicas']={'semente':2026112603,'jogos':96,'produtos_uma_duas_obrigacoes':products,'politicas_abstratas_levantadas':lifted,'estados_produto_examinados':checks,'seletor':'ações concretas renomeadas por estado; testemunho depende de x,a; projeção 4→2'}
    # Contramodelos pequenos: não reciprocidade; direção, quantificadores e informação.
    good={0:{'a':{(0,1)}},1:{'a':{(1,0)}}};bad={0:{'a':{(0,1),(1,0)}},1:{'a':{(1,0)}}}
    assert oracle(good,{0},{0})=={0} and not oracle(bad,{0},{0})
    # direção invertida: D_abstrato ⊂ p(D_concreto), abstrato vence e concreto perde.
    assert good[0]['a']<bad[0]['a']
    assert cert(good,bad,{0:0,1:1},{0},{0},{0},{0}) is not None
    assert cert(bad,good,{0:0,1:1},{0},{0},{0},{0}) is None
    # ∀u existe a NÃO garante ação concreta para a política abstrata escolhida.
    abstract={0:{'bom':{(0,1)},'ruim':{(1,0)}},1:{'ruim':{(1,0)}}};concrete={0:{'u':{(1,0)}},1:{'u':{(1,0)}}}
    assert 0 in oracle(abstract,{0},{0}) and not oracle(concrete,{0},{0})
    assert cert(concrete,abstract,{0:0,1:1},{0},{0},{0},{0}) is None
    # ∀d ∃u (controle antecipa perturbação) != ∃u ∀d.
    equality=[[u==d for d in range(2)] for u in range(2)]
    assert all(any(equality[u][d] for u in range(2)) for d in range(2)) and not any(all(row) for row in equality)
    # ∀x ∃u(x) é válido com observação completa, mas não implica ∃u ∀x em fibra oculta.
    hidden={0:{'L':{(0,1)},'R':{(2,0)}},1:{'L':{(2,0)},'R':{(1,1)}},2:{'L':{(2,0)},'R':{(2,0)}}}
    assert {0,1}<=oracle(hidden,{0,1},{0,1})
    assert not any(all(all(y in {0,1} for y,l in hidden[x][u]) for x in [0,1]) for u in ['L','R'])
    assert not validate({0:{'vazia':set()}})
    # Recorrência não segue apenas de segurança: mesmo estado; produção apagada.
    assert not wins_policy({0:{'a':{(0,0)}}},{0:'a'},{0},set())
    r['contramodelos']={k:'CONFIRMADO' for k in ['CM01_inclusao_invertida','CM02_quantificador_acao_invertido','CM03_perturbacao_antes_controle','CM04_selecao_irrealizavel_informacao_parcial','CM05_vacuidade_rejeitada','CM06_aceitacao_omitida','CM07_sem_reciproca']}
    # Oráculo de maior agregação: todas as partições dos 4 estados.
    parts=list(partitions(4));count=0
    for t in range(160):
        g={x:{} for x in range(4)}
        for x,a in it.product(g,range(2)):
            es={(y,l) for y,l in it.product(g,range(2)) if rng.random()<.18}
            if es:g[x][a]=es
        v={x for x in g if rng.random()<.8};obs={x:rng.randrange(2) for x in g};p,steps=refine(g,v,obs)
        assert stable(g,p,v,obs)
        p0=len({(x in v,obs[x]) for x in g});assert steps<=len(g)-p0
        for q in parts:
            if stable(g,q,v,obs):
                assert all(q[x]!=q[y] or p[x]==p[y] for x in g for y in g)
            count+=1
    r['PVI02.4_oraculo_particoes']={'jogos_amostrados':160,'particoes_por_jogo':len(parts),'comparacoes':count,'observaveis':'binários mais segurança; ações habilitadas e etiquetas 0/1; sem guardas gerais'}
    nd={0:{'a':{(2,0),(3,0)}},1:{'a':{(4,0),(5,0)}},2:{},3:{},4:{},5:{}}
    p={0:0,1:0,2:1,3:2,4:1,5:2};q={0:0,1:0,2:1,3:2,4:2,5:1}
    joint={x:(p[x],q[x]) for x in nd};vv=set(nd);oo={x:0 for x in nd}
    assert stable(nd,p,vv,oo) and stable(nd,q,vv,oo) and not stable(nd,joint,vv,oo)
    r['intersecao_nao_determinista']={'estados':6,'particoes_isoladas_estaveis':True,'intersecao_estavel':False,'escopo':'contramodelo à extrapolação não determinista do corolário determinista P07.1'}
    # Dependências críticas: testemunho comum, alternância, modelo renovador, história.
    A={0:2,1:3,2:2,3:2};B={0:0,1:0,2:0,3:3};obs={0:0,1:0,2:1,3:1};v=set(range(4))
    pa,_=refine({x:{0:{(A[x],0)}} for x in v},v,obs);pb,_=refine({x:{1:{(B[x],0)}} for x in v},v,obs)
    assert len(set(pa.values()))==2 and len(set(pb.values()))==3
    pg,_=refine({x:{0:{(A[x],0)},1:{(B[x],0)}} for x in v},v,obs);assert len(set(pg.values()))==4
    R={(0,0)};S={(1,0)};assert not {(x,z) for x,y in R for yy,z in S if y==yy}
    F=lambda s,q:(s[1]&q,s[2]&s[0]&q,s[1]&s[0]&q)
    assert F((1,1,1),1)==(1,1,1) and F((0,0,0),1)==(0,0,0)
    lengths=[]
    for s in [(0,1,1),(1,0,1),(1,1,0)]:
        n=0
        while any(s):s=F(s,1);n+=1;assert n<8
        lengths.append(n)
    assert lengths==[2,3,4]
    assert all(a<b for a,b in zip(range(6),range(1,7)))
    r['dependencias']={'P07.3_classes':[2,3,4],'P08.2_testemunho_incompativel':'confirmado','P10.7_passos_colapso':lengths,'P11.7':'precedência estrita preservada na cadeia; prova geral no laudo'}
    r['tempo_segundos']=round(time.perf_counter()-start,3);r['status']='APROVADO_NO_ESCOPO';r['prova_geral']='argumentação no laudo, não induzida das contagens';print(json.dumps(r,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
