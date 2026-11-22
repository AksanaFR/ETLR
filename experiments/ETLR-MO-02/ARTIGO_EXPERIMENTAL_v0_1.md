# ETLR-MO-02 — Motor contextual lógico-relacional

## Sistema algébrico-filosófico experimental, linguagem ETLR-L0 e ensaio de reprodução funcional

**Data:** 21 de novembro de 2026  
**Estado:** preprint técnico-experimental, versão 0.1; sem avaliação por pares.  
**Base teórica:** *Álgebra Espaço-Temporal Lógico-Relacional*, Volume I, ETLR-00 a ETLR-11, edição de trabalho EDIT02 R4 (2026), repositório da obra: <https://github.com/AksanaFR/ETLR>.  
**Nota de escopo:** o trabalho apresenta apenas o motor contextual, sem reproduzir a formulação integral do Volume I.
**Objetivo:** investigar se uma mesma regra de análise situada pode continuar, recuperar partes de sua capacidade operacional e gerar uma instância funcionalmente equivalente, sempre especificando condições de aplicação e de fracasso.

> **Veredicto delimitado:** o protótipo fornece uma **reprodução funcional condicionada de componentes declarativos** e uma **reparação de perda isolada** quando há componentes auxiliares, receitas e recursos preexistentes. **Não demonstra autogeração integral, autopoiese biológica ou autorreprodução do interpretador Python.** O testemunho de individuação entre escalas foi fornecido como hipótese externa, não inferido pelo motor.

## 1. Problema científico: o que precisa se reproduzir?

A afirmação “um sistema se reproduz” admite pelo menos quatro interpretações distintas.

| Nível | Propriedade | Critério no ensaio |
|---|---|---|
| R0 | **Iteração** | A mesma regra transforma um estado situado em outro estado tratável. |
| R1 | **Recuperação funcional** | Após perda delimitada, processos ainda disponíveis recompõem uma condição operacional necessária. |
| R2 | **Reprodução funcional** | Uma organização produz uma segunda instância com o mesmo conjunto de capacidades especificadas; ambas podem operar separadamente. |
| R3 | **Autogeração constitutiva** | A rede participa da produção e reconstrução das condições constitutivas que a tornam possível, com fechamento funcional verificado sob perturbações e regimes de recursos definidos. |

R0 não implica R1; R1 não implica R2; R2 não implica R3. Uma cópia de software pode funcionar porque um processador, um sistema operacional, um interpretador e recursos são providos de fora. Nesse caso, há replicação de um programa, não autogeração dos meios de sua existência. Essa separação é exigida pelos problemas da ETLR-10 e ETLR-11 e dialoga com a autopoiese (Varela, Maturana e Uribe), o fechamento de restrições (Montévil e Mossio) e as redes autocatalíticas (Hordijk e Steel) [R2–R4].

### 1.1 A pergunta própria da ETLR

A proposta da ETLR não é reivindicar a descoberta da recursão, da individuação ou da autopoiese. Sua pergunta operacional específica é:

**É possível definir uma operação de confronto relacional suficientemente pequena para permanecer tipada e auditável quando os participantes, as fronteiras, os campos, as escalas e as condições de continuidade se alteram?**

**Hipótese MO02/H1.** Uma passagem que preserve (i) referência relacional situada; (ii) regras e condições de admissibilidade; (iii) diferenciações justificadas; e (iv) proveniência pode ser reaplicada a um estado resultante sem substituir sua semântica central.

**Hipótese MO02/H2.** Uma rede de três capacidades operacionais com dependências cruzadas e receitas explícitas pode recuperar a perda isolada de uma delas, enquanto falha diante de determinadas perdas múltiplas. Isto é uma propriedade do modelo, não uma lei universal.

**Hipótese MO02/H3.** Uma organização funcionalmente íntegra pode produzir um segundo estado que conserva sua regra contextual, seu núcleo e suas receitas. A existência de um segundo estado não atesta, sozinha, individuação ontológica ou autonomia constitutiva.

## 2. Estratos: ontologia, linguagem, modelo e teste

Estas camadas não devem ser confundidas:

1. **Ontologia investigativa:** indivíduos, fronteiras, ambientes, campos, história, individuação e constituição, na formulação da ETLR [R1].
2. **Semântica interpretativa:** o que designamos como “indivíduo”, “espaço”, “limite”, “manifestação” e “evidência” em um domínio específico. Duas descrições iguais não comprovam identidade interna, conforme o problema de não identificabilidade explicitado na ETLR-09.
3. **Álgebra candidata:** conjuntos de estados, relações de admissibilidade, transformação parcial, projeções e condições de fechamento.
4. **Linguagem executável:** subconjunto estrito ETLR-L0, com sintaxe controlada e regras de confronto explicitamente programadas para um domínio textual.
5. **Ensaio computacional:** testes finitos, resultados repetíveis e controles negativos. São verificações de código sob hipóteses estipuladas, não observações independentes da natureza.

### 2.1 O mínimo espaço–campo–indivíduo

Para um domínio interpretativo `D`, sejam:

- `K_D`: conjunto dos contextos espaciais-relacionais delimitáveis (sem pressupor distância euclidiana);
- `H_D`: conjunto dos regimes temporais e condições de campo pertinentes;
- `B_D`: conjunto de indivíduos ou organizações *candidatos*, identificados em determinada escala;
- `R_D`: relações situadas entre um ou vários participantes (`n >= 1`), fronteiras e ambientes.

A referência mínima de uma investigação é `c = (k, h, b)`, com `k in K_D`, `h in H_D`, `b in B_D`. A prioridade de selecionar `k` é metodológica; **não impõe uma origem cosmológica na qual espaço antecede tempo ou indivíduos**.

Uma relação `r in R_D` só é tratável quando sua formação e suas condições de admissibilidade são declaradas. Este critério coincide com a preocupação da ETLR-00/02/04 de não confundir notação bem formada com ocorrência efetiva.

### 2.2 Fronteira e limite relacional

Definimos, apenas como notação investigativa:

`F_D(b,c)`: fronteira relativa de `b` em `c`.  
`L_D(b,r,c)`: condição limitante que incide sobre `b`, uma relação ou manifestação `r`, no contexto `c`.  
`O_D(b,c)`: manifestação/observação externa situada.

As três funções são distintas. É possível que `O_D(b1,c1) = O_D(b2,c2)` apesar de organizações internas não equivalentes. Também é possível que `O_D(b,c1) != O_D(b,c2)` sem prova de que a constituição interna de `b` tenha sido alterada. Logo, **não existe inversão geral garantida da observação para a constituição**.

A limitação não se reduz a um operador de negação. Pode selecionar, permitir, impedir, redirecionar, reorganizar ou permanecer indeterminada. O teste distingue `ADMISSIBLE`, `INCOMPATIBLE` e `INDETERMINATE`, estados de admissibilidade contextual, **não valores de verdade para toda e qualquer proposição**.

## 3. Álgebra operacional mínima

### 3.1 Estado situado

O estado computacional é uma tupla tipada:

`S = (c, o, Q, G, P, F, A, V)`

- `c = (k,h,b)`: referência espaço–campo–indivíduo com revisão contextual;
- `o`: observação delimitada;
- `Q`: agenda finita de questões, cada uma com tipo declarado;
- `G = (C, N)`: componentes funcionais `C` e receitas de reconstituição `N`;
- `P`: cadeia de proveniência;
- `F`: quantidade não negativa de recurso disponível;
- `A`: alternativas e hipóteses com seu estatuto;
- `V`: conclusões e situação de continuidade.

Dizemos que `S` é **bem formado** quando todos os campos de referência são identificáveis, os tipos são válidos e a proveniência é íntegra segundo o esquema local. Isso não significa que todos os seus enunciados sejam empiricamente verdadeiros.

### 3.2 Transição parcial

Definimos `C_D : S_D ⇀ S_D`: operador **parcial** de evolução contextual. O resultado depende de condições de entrada; não é uma transformação física universal.

```text
C_D(S):
  verificar formação de S e proveniência declarada
  se falta componente funcional:
      tentar UMA reconstrução com componentes, receita e recurso disponíveis
      caso contrário: BLOQUEAR sem inventar funcionamento
  senão, se existe uma pergunta pertinente:
      confrontar UMA pergunta conforme as regras do domínio
      registrar conclusão, insuficiência ou alternativas sem elevar hipótese a fato
  senão:
      conservar ponto fixo local ou suspender por evidência
  retornar S' com a mesma estrutura de estado e história verificável
```

**Reentrada:** quando `C_D(S)` é definido e devolve um estado do mesmo tipo, `C_D` pode ser reexecutado. Isso é uma propriedade de **fechamento por tipagem sob condições**, não prova de fechamento constitutivo do sistema inteiro.

`S_(n+1) = C_D(S_n)` para passagens admissíveis.  
`C_D(S*) = S*` para um estado localmente fechado sem nova agenda ou perturbação.

A agenda de questões é finita e há orçamento de passos. O sistema suspende a investigação em vez de criar ramos infinitos sem novas condições discriminantes.

### 3.3 Composição e mudança de escala

Se `alpha` é uma projeção da escala micro para a macro, a conservação dinâmica exigiria verificar uma condição do tipo:

`alpha(T_micro(x)) = T_macro(alpha(x))`, para os estados/acontecimentos admissíveis do ensaio.

Essa equação é uma condição clássica de compatibilidade de projeções dinâmicas, aqui remetida à investigação ETLR-07; não é criação de uma operação matemática inteiramente nova. A composição de sistemas abertos e a semântica composicional têm antecedentes em Fong e Spivak [R7].

O protótipo não demonstra essa equação entre todos os domínios. No teste de reentrada, usa um **testemunho externo de cinco critérios candidatos da ETLR-09** (`constitution`, `boundary`, `identity`, `continuity`, `participation`) para permitir uma nova escala. Um dicionário com cinco valores `true` serve como *marcador sintático de pré-condição*, não como prova de que os critérios foram cientificamente satisfeitos.

## 4. Autorreparo: três componentes com dependências recíprocas

O núcleo do exemplo contém exatamente três capacidades **declarativas**:

- `CONSTITUTE`: situar e formar a referência da investigação;
- `CONFRONT`: examinar uma diferença admissível;
- `RECONSTITUTE`: preservar resultado e preparar continuidade.

A regra de **reparação localizada** usa duas funções ainda presentes para reconstituir a terceira, consumindo uma unidade de recurso. Suas três receitas são:

```text
{CONFRONT, RECONSTITUTE} + recurso  -> CONSTITUTE
{CONSTITUTE, RECONSTITUTE} + recurso -> CONFRONT
{CONSTITUTE, CONFRONT} + recurso -> RECONSTITUTE
```

São receitas **de projeto**, não consequências deduzidas da ontologia ETLR. Sua inspiração conceitual é o estudo de redes mutuamente sustentadas e sistemas autocatalíticos [R3–R4]; os nomes e a construção concreta pertencem ao protótipo desta pesquisa.

**Proposição P1 — recuperação de perda unitária.** Se o estado tem exatamente dois dos três componentes, a receita do terceiro permanece disponível e o orçamento é no mínimo uma unidade, uma passagem de reparação restaura o conjunto de três componentes e reduz o orçamento em uma unidade.

**Demonstração no modelo.** A única função faltante é alvo da receita correspondente. Seus dois requisitos pertencem ao conjunto presente. Como o recurso é positivo, o interpretador escolhe a receita, insere o alvo e desconta uma unidade. O estado resultante volta a possuir o núcleo completo. **QED — para as receitas e hipóteses deste modelo.**

**Contraexemplo C1.** Com somente um componente presente, nenhuma receita possui seus dois requisitos satisfeitos; o reparo não ocorre. **Contraexemplo C2.** Se a receita pertinente é apagada, nem dois componentes e nem combustível bastam para recuperar o terceiro. **Contraexemplo C3.** Sem combustível, não há reparo, ainda que a dependência circular seja visualmente reconhecível.

Esses contraexemplos são importantes porque **fechamento estrutural de um grafo não implica processos efetivos de recuperação**, distinção explicitada na ETLR-11.

## 5. Reprodução funcional com contabilidade de recursos

Uma segunda operação, `Rep`, é definida apenas sobre estados com núcleo íntegro, todas as receitas, testemunho externo de individuação, estado localmente resolvido e recurso suficiente.

`Rep(S, c', W, f_transfer) -> (S_pai', S_filho)`

O custo de reproduzir três componentes é fixado no **modelo** em três unidades. A unidade adicional transferida ao filho é `f_transfer >= 0`.

`F_pai' = F_pai - 3 - f_transfer`  
`F_filho = f_transfer`  
`F_pai' + F_filho + 3 = F_pai`.

**Proposição P2 — conservação contábil local.** Dadas as regras do modelo, a reprodução não aumenta o orçamento total dos dois estados: exatamente três unidades são cobradas para construir a cópia. A igualdade vale por substituição algébrica.

**Proposição P3 — cópia funcional contextual.** Se a operação é admissível, o novo estado contém o mesmo conjunto de três capacidades e as mesmas receitas declarativas; sob um contexto próprio bem formado, pode executar o mesmo `C_D` sem consultar o estado mutável de seu predecessor. Isso **não é** prova de que um novo indivíduo ontológico surgiu, nem de que o programa Python foi reproduzido.

**Limite decisivo:** o interpretador em Python é fornecido por fora da entidade modelada e continua necessário para todas as gerações. Também não são criados de nada os recursos, as receitas nem as condições iniciais. Uma reprodução de **configuração funcional** não é uma produção integral do sistema de suporte.

## 6. ETLR-L0 — a linguagem mínima de execução

A linguagem executável ETLR-L0 formaliza um subconjunto explícito das operações de investigação em sete campos:

```text
ESPACO canal
CAMPO regime_de_turnos
INDIVIDUO A
LIMITE 12
OBSERVADO 7
PERGUNTA CHECK
RECURSO 12
```

As palavras-chave definem a situação, não uma teoria completa do mundo. `LIMITE DESCONHECIDO` mantém a admissibilidade indeterminada. `PERGUNTA WHY_SHORT` ativa, apenas neste domínio sintético, três hipóteses de origem de uma manifestação breve.

**Interpretação por linha:**

1. `ESPACO`: nomeia o domínio relacional que autoriza a análise.
2. `CAMPO`: indica o regime em que acontecimentos e regras ganham validade.
3. `INDIVIDUO`: identifica o participante candidato, sem pressupor acesso ao seu interior.
4. `LIMITE`: explicita a restrição contextual observável.
5. `OBSERVADO`: valor externo, que não reconstrói automaticamente o estado interno.
6. `PERGUNTA`: obriga uma confrontação local, sempre tipada.
7. `RECURSO`: orçamento materializado no modelo, necessário para reparação e reprodução.

**Saída esperada:** `LOCAL_CLOSED` e `ADMISSIBLE@rev0: observado=7, limite=12`; nenhuma hipótese extra é aberta. Como controle, substitua `LIMITE 12` por `LIMITE DESCONHECIDO`: o resultado deverá tornar-se `INDETERMINATE`, não `ADMISSIBLE`.

### 6.1 Executar

O pacote usa somente a biblioteca padrão Python; a suíte foi executada com Python 3.13.5. Sintaxe preparada para Python 3.10+, embora essas versões anteriores não tenham sido verificadas nesta entrega:

```bash
cd experiments/ETLR-MO-02
python -m etlr_contextual exemplos/01_simples.etlr
python -m etlr_contextual exemplos/02_ramificacao.etlr
python -m exemplos.03_reparo_reproducao
python run_tests.py
```

O comando `python run_tests.py` produz `RESULTADOS.json` com as contagens e os hashes SHA-256 do motor e da suíte, além de `TESTES_EXECUCAO.txt` com o log dos ensaios. Os hashes verificam identidade de arquivos nesta execução, mas não constituem assinatura independente de autoria nem prova de veracidade das interpretações.

### 6.2 Aprofundamento: a diferença entre observação e constituição

Imagine dois indivíduos que enviam mensagens com sete caracteres. Mesmo meio, mesmo comprimento e mesma regra de limite. A observação é idêntica, mas pode haver constituições, decisões e contextos internos diferentes. Se a manifestação não distingue as duas possibilidades, a conclusão sobre constituição permanece **não identificável** sob aquela projeção. Essa obrigação de não inferir univocamente o interior a partir do exterior deriva dos problemas de projeção e não identificabilidade enfrentados no Volume I (ETLR-07 e ETLR-09), com paralelos formais em teoria de sistemas [R1, R6].

Agora altere somente a regra do meio: o limite passa de sete para doze. A manifestação aumenta de sete para nove. O motor registra o evento e reconsidera a admissibilidade. **Não** conclui que a pessoa mudou internamente, nem que a mudança da regra foi sua causa exclusiva. Observamos transição contextual; causalidade requer outro experimento.

## 7. Laudo de ensaio — execução do protótipo

**Ambiente de teste:** interpretador Python local, biblioteca padrão `unittest`, dados sintéticos inteiramente declarados, sem modelo de linguagem, rede externa, inferência empírica ou agentes autônomos.

**Suíte MO02:** **31 testes aprovados, 0 falhas e 0 erros**. Um desses testes percorre exaustivamente **80 configurações finitas**: 8 subconjuntos possíveis de funções × 5 quantidades de recurso × 2 condições de presença/ausência do conjunto completo de receitas. Não são 80 experimentos independentes do mundo real.

| Família de teste | Resultado observado | Alcance permitido |
|---|---|---|
| Relação simples | 1 passagem; ponto fixo sem expansão indevida | Economia operacional local. |
| Ramificação | 3 alternativas explicitamente indeterminadas; 4 passagens | O método pode abrir questões sem inventar evidência. |
| Evento contextual | Revisão de limite e observação com histórico conservado | Reutilização do motor com proveniência. |
| Reparo unitário | Reconstitui a função ausente quando duas outras, receita e recurso estão presentes | Recuperação funcional localizada. |
| Perda dupla | Bloqueio | Não há reparação universal. |
| Perda de receita ou recurso | Bloqueio | Dependência de condições constitutivas preexistentes. |
| Reprodução | Pai produz filho com o mesmo núcleo e receitas; filho opera em contexto distinto | Cópia funcional condicionada. |
| Segunda geração | Filho pode produzir neto, usando o recurso que recebeu | Continuidade funcional por duas gerações no modelo. |
| Reescala sem testemunho | Operação rejeitada | Não identificar automaticamente agregação com individuação. |
| Proveniência adulterada | Cadeia SHA-256 local inválida é detectada | Detecta alteração de registros sem recomputação coordenada. |
| Varredura finita | 80 casos cobertos em um teste parametrizado | Cobertura exaustiva **apenas** do conjunto parametrizado. |

**Declaração de resultado:** R0 (reentrada) demonstrado no domínio simulado; R1 (recuperação localizada) demonstrado sob hipóteses; R2 (reprodução de configuração funcional) demonstrado sob hipóteses; R3 (autogeração constitutiva ampla) **não demonstrado**.

### 7.1 Limites do teste

- O algoritmo que executa as regras é escrito externamente em Python e não se reproduz.
- A capacidade de reparação é especificada por receitas predeterminadas. A produção das receitas não é modelada.
- As cinco obrigações de individuação entram como marcadores booleanos **externos**; sua suficiência não foi estabelecida.
- O combustível vem de uma reserva declarada; não há metabolismo ou aquisição autônoma de recursos.
- A memória de proveniência é registrada, mas não há autorreparação integral da memória, do armazenamento ou do interpretador.
- O conjunto `WHY_SHORT` conhece somente três alternativas previamente previstas. Não infere todas as relações possíveis de qualquer domínio.
- A equação de reescala não foi provada para os domínios físico, social e mental em geral.
- Os testes demonstram propriedades da implementação e dos casos desenhados; não validam uma teoria científica universal.

## 8. Creditação das ideias e operadores

A atribuição precisa separar **antecedente histórico**, **construção matemática conhecida**, **hipótese autoral da ETLR** e **escolha de implementação desta experiência**.

| Elemento empregado | Crédito intelectual pertinente | O que a ETLR acrescenta neste ensaio |
|---|---|---|
| Individuação como processo e problema filosófico | Gilbert Simondon, trabalho de 1958 reunido em edição de 2005 [R8]. | Perguntas situadas sobre constituição, escalas e continuidade. Não reivindica inventar a individuação. |
| Autopoiese e redes de produção de componentes | Varela, Maturana e Uribe (1974) [R2]. | Teste explícito que diferencia repetição funcional de produção constitutiva. Não reivindica equivalência à autopoiese. |
| Fechamento organizacional de restrições | Montévil e Mossio (2015) [R3]. | Distinção operacional entre limites, manutenção, recuperação e reentrada em contextos. |
| Conjuntos autocatalíticos e disponibilidade de recursos | Hordijk e Steel (2004) [R4]. | Rede sintética de 3 receitas com controles de perda; não é um modelo de química. |
| Autorregulação e adaptação sob perturbações | W. Ross Ashby (1952) [R9]. | Experimentos de falha/reparo em condições declaradas. |
| Sistemas de transição, invariantes e teste automatizado | Clarke, Grumberg e Peled (1999) [R5]; Rutten (2000) [R6]. | Operador `C_D`, estados tipados e verificações finitas no domínio piloto. |
| Composição de estruturas e interfaces | Fong e Spivak (2019) [R7]. | Reentrada condicionada a nova escala; nenhum novo teorema categorial alegado. |
| Ordem parcial de acontecimentos | Leslie Lamport (1978) [R10]. | Não impor ordem temporal total como condição geral da ETLR. |
| Proveniência de dados e atividades | W3C PROV-DM (2013) [R11]. | Cadeia de registros verificáveis por hash; ainda não equivale à conformidade PROV. |
| Parcimônia de modelos, sem eliminar informação relevante | Jorma Rissanen (1978) [R12]; Herbert Simon (1962) [R13]. | Regra de confrontar a menor diferença que possa alterar resultado; sem alegar derivação do princípio físico da mínima ação. |
| Signo e símbolo | Charles S. Peirce, tradição semiótica [R14]. | **A definição autoral da ETLR não é idêntica à de Peirce.** A semelhança vocabular não autoriza atribuir a ele a polaridade interna/externa do Volume I. |
| Núcleo `Constituir–Confrontar–Reconstituir` | Hipótese operacional da ETLR, formulada nesta pesquisa a partir do Volume I [R1]. | Integração específica de referência, admissibilidade, limite, manifestação, continuidade, ramificação e economia relacional. |
| Três componentes e receitas cruzadas, custos de cópia | **Escolha de engenharia do protótipo ETLR-MO-02**, sem precedência científica alegada. | Caso de prova delimitado; a demonstração de suas propriedades é interna ao modelo. |

### Referências bibliográficas verificadas

**[R1] ETLR, Volume I.** *Álgebra Espaço-Temporal Lógico-Relacional: Constituição, fronteira e continuidade do indivíduo*, ETLR-00–11, edição de trabalho EDIT02 R4, 2026. <https://github.com/AksanaFR/ETLR>. O presente texto dialoga diretamente com os capítulos ETLR-02, 04, 07, 09, 10 e 11. Os testes deste artigo pertencem ao protótipo independente aqui documentado.

**[R2] Varela, F. G.; Maturana, H. R.; Uribe, R. (1974).** “Autopoiesis: The organization of living systems, its characterization and a model.” *BioSystems*, 5(4), 187–196. DOI: <https://doi.org/10.1016/0303-2647(74)90031-8>.

**[R3] Montévil, M.; Mossio, M. (2015).** “Biological organisation as closure of constraints.” *Journal of Theoretical Biology*, 372, 179–191. DOI: <https://doi.org/10.1016/j.jtbi.2015.02.029>.

**[R4] Hordijk, W.; Steel, M. (2004).** “Detecting autocatalytic, self-sustaining sets in chemical reaction systems.” *Journal of Theoretical Biology*, 227(4), 451–461. <https://pubmed.ncbi.nlm.nih.gov/15038982/>.

**[R5] Clarke, E. M.; Grumberg, O.; Peled, D. A. (1999).** *Model Checking*. MIT Press. <https://mitpress.mit.edu/9780262032704/model-checking/>.

**[R6] Rutten, J. J. M. M. (2000).** “Universal coalgebra: a theory of systems.” *Theoretical Computer Science*, 249(1), 3–80. DOI: <https://doi.org/10.1016/S0304-3975(00)00056-6>.

**[R7] Fong, B.; Spivak, D. I. (2019).** *An Invitation to Applied Category Theory: Seven Sketches in Compositionality*. Cambridge University Press. DOI: <https://doi.org/10.1017/9781108668804>.

**[R8] Simondon, G. (2005; pesquisa original de 1958).** *L'individuation à la lumière des notions de forme et d'information*. Jérôme Millon. Fonte bibliográfica: <https://simondon.fr/site/content/publications-et-%C5%93uvres>.

**[R9] Ashby, W. R. (1952).** *Design for a Brain: The Origin of Adaptive Behaviour*. Chapman & Hall. <https://www.ashby.info/Ashby%20-%20Design%20for%20a%20Brain%20-%20The%20Origin%20of%20Adaptive%20Behavior.pdf>.

**[R10] Lamport, L. (1978).** “Time, Clocks, and the Ordering of Events in a Distributed System.” *Communications of the ACM*, 21(7), 558–565. DOI: <https://doi.org/10.1145/359545.359563>.

**[R11] Moreau, L.; Missier, P. (eds.) (2013).** *PROV-DM: The PROV Data Model*. W3C Recommendation. <https://www.w3.org/TR/prov-dm/>.

**[R12] Rissanen, J. (1978).** “Modeling by shortest data description.” *Automatica*, 14(5), 465–471. DOI: <https://doi.org/10.1016/0005-1098(78)90005-5>.

**[R13] Simon, H. A. (1962).** “The Architecture of Complexity.” *Proceedings of the American Philosophical Society*, 106(6), 467–482. Apresentação editorial: <https://www.sfipress.org/21-simon-1962>.

**[R14] Peirce, C. S.** Fundamentação semiótica sobre signos, símbolos e interpretantes; apresentação acadêmica: *Stanford Encyclopedia of Philosophy*, “Peirce’s Theory of Signs.” <https://plato.stanford.edu/entries/peirce-semiotics/>.

## 9. O que seria uma contribuição científica nova?

A novidade possível não deve ser procurada em reivindicar o primeiro uso de autopoiese, recursão, fronteira, limite, escala, composição ou formalismos relacionais. Essas ideias possuem histórias documentadas e literatura extensa.

Uma contribuição verificável da ETLR poderá surgir de um **teorema novo**, de um **contraexemplo discriminante**, de um **protocolo reproduzível que resolva um problema de classificação não resolvido pelos métodos anteriores**, de **previsões testáveis** ou de **conservações formais entre domínios sob hipóteses explícitas**.

O trabalho presente oferece um candidato à integração dessas questões em um protocolo conciso, acompanhado de código e de falhas deliberadas. A prioridade histórica, superioridade científica e generalidade da formulação **não estão estabelecidas**. A revisão bibliográfica realizada é seletiva, não uma revisão sistemática de toda a literatura.

## 10. Caminho para a próxima falsificação

**F1 — Autorreconstrução de regras.** Apagar uma receita, mantendo seus componentes. Especificar um mecanismo *interno* para regenerar a receita, sem acesso externo ao catálogo da receita ausente; se não recuperar, a hipótese de fechamento mais forte falha.

**F2 — Dependência do interpretador.** Interromper ou substituir o interpretador Python. Se a organização não puder reproduzir a execução sem ele, a autogeração integral não foi alcançada (limitação arquitetural esperada neste protótipo).

**F3 — Testemunho de individuação.** Substituir marcadores `true` por evidências geradas a partir de critérios independentes, com contraexemplos de agregados não individuados.

**F4 — Conservação multiescalar.** Definir projeção `alpha`, dinâmica microscópica e dinâmica coletiva; construir exemplos que satisfaçam e violem `alpha ∘ T_micro = T_macro ∘ alpha`.

**F5 — Investigadores independentes.** Fornecer os mesmos fatos e a gramática ETLR-L0 a duas pessoas sem apresentação do modelo esperado; comparar justificativas, ambiguidade e resultados.

**F6 — Transferência real de domínio.** Substituir a mensagem curta por um pequeno sistema físico, social e formal, com critérios de teste específicos. Se o ciclo só funcionar porque o programador antecipou todas as respostas, a alegação de generalidade deve ser reduzida.

### Parecer final

> O motor contextual ETLR-MO-02 reproduz sua **configuração funcional** e repara uma **perda unitária delimitada** em uma rede artificial de três capacidades, sob receitas e recursos fornecidos. Esse resultado é compatível, de modo condicionado, com os problemas de constituição, admissibilidade, transformação, continuidade e fechamento examinados no Volume I. O modelo **não** demonstra, por si, autogeração constitutiva da organização inteira, individuação ontológica entre escalas, universalidade da álgebra, nem exclusividade histórica da formulação.

**Disponibilização:** versão experimental pública do motor, acompanhada por código e testes. O código-fonte, os testes e os exemplos executáveis do ETLR-MO-02 estão, na revisão atual, licenciados sob **PolyForm Noncommercial 1.0.0**, conforme [`LICENSE`](LICENSE), [`NOTICE`](NOTICE) e [`NOTA_DE_DIREITOS.md`](NOTA_DE_DIREITOS.md). A mudança não revoga as permissões das versões já distribuídas sob MIT. A licença CC BY-NC-ND 4.0 do Volume I permanece específica ao conteúdo da obra; este artigo e a análise filosófica não são relicenciados como software. Nenhuma conclusão deste trabalho constitui comprovação de autogeração universal.


**Implementação e ensaios:** consulte [`README.md`](README.md), [`ARQUITETURA_RELACIONAL.md`](ARQUITETURA_RELACIONAL.md), a linguagem em `etlr_contextual/` e os testes em `tests/`.