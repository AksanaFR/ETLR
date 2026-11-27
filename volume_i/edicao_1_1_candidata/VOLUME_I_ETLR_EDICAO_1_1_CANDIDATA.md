# ETLR — Volume I: Constituição e transformação relacional do indivíduo

**Teoria da Constituição e Transformação Relacional · Álgebra Espaço-Temporal Lógico-Relacional**

**Proposta de identificação editorial: 1.1 CANDIDATA · revisão de enquadramento científico · 27 de novembro de 2026.** Identificação e conteúdo submetidos à avaliação da autora; sem aprovação ou publicação presumidas. A base é a edição 1.0 CANDIDATA, revisão GitHub ec3c63bc6687d1116c73d74612915fc702433090.

Esta revisão editorial delimitada explicita a finalidade investigativa da ETLR e preserva os resultados formais da edição 1.0 CANDIDATA. A revisão científica VI05 e a preparação VI06A são etapas históricas da base, datadas de 26 de novembro de 2026. As três perspectivas de revisão ali registradas são internas e não constituem avaliações externas independentes. O DOI 10.5281/zenodo.24586496 identifica a versão 1.0 depositada e seu PDF original; não identifica os bytes deste PDF revisado. Esta candidata 1.1 não possui novo DOI atribuído nesta preparação. A base científica VI04/VI05, as matrizes, os antecedentes e os limites documentais permanecem preservados. A preparação local não implica publicação, homologação autoral, execução de motores ou início do Volume II.

## Resumo

A ETLR investiga se uma estrutura organizada a partir dos fundamentos relacionais de espaço, tempo e indivíduo, mediante suas diferentes composições, funções e transformações multiescalares, é capaz de produzir conhecimento sobre princípios comuns de constituição, interação e organização em diferentes domínios da realidade. Sua finalidade não é substituir teorias particulares de domínio, mas investigar regularidades, correspondências, diferenças, limites e condições de transformação relacional. Espaço, tempo e indivíduo são investigados como candidatos a fatos relacionais fundamentais; o emprego de fundamentos relacionais na declaração de finalidade não estabelece sua necessidade, suficiência ou exclusividade ontológica. A origem histórico-filosófica inclui a matriz sefirótica autoral codificada em E/T/I e a linhagem QORELFlow; sua procedência não decide a validade dos resultados. Este volume distingue a hipótese ontológica forte, a hipótese epistemológica e o uso metodológico da tríade. Desenvolve uma linguagem contextualizada para configurações, relações, admissibilidade, ocorrências, histórias e interfaces. A formalização usa relações tipadas, execuções com testemunhos, fatoração de tarefas e jogos finitos com escolhas controláveis e ambientais. Cinquenta resultados são integrados com suas hipóteses, argumentos e limites: doze classificados na VI03 como matemática conhecida, vinte e sete como aplicações e onze como integrações internas. As demonstrações esclarecem quando representações conservam composições, trajetórias, segurança, alcance e recorrência produtiva. Contramodelos separam manifestação de constituição, composição de individuação, renovação de reparabilidade, recorrência de prazo e equivalência de identidade. A contribuição interna consiste na articulação dessas obrigações em uma arquitetura de investigação rastreável. Originalidade externa permanece não estabelecida. Não há demonstração de universalidade ontológica, autogeração forte ou validação empírica. As lacunas documentais AD-01 autônomo, G01–G20 e contratos completos ARM suspendem as afirmações que delas dependem, sem invalidar os resultados formais delimitados.

**Palavras-chave:** constituição relacional; espaço; tempo; indivíduo; representação; álgebra tipada; individuação; sustentação; jogos finitos; proveniência.

## Guia de leitura e notação

Os capítulos 1–3 distinguem origem dos problemas, hipóteses e linguagem. Os capítulos 4–6 desenvolvem composição e representação; 7–9 tratam individuação, sustentação e recorrência; 10 integra os certificados; 11–12 sintetizam contribuição e evidência. Os apêndices preservam matrizes, hipóteses e candidatos históricos, e acrescentam exame crítico e condições de avaliação externa. QOREL, ARM e ETLR-MO designam antecedentes ou instrumentos privados; nenhuma prova exige executar esses sistemas. A ausência dos contratos completos ARM impede certificar sua conformidade integral. PM e MO designam protocolos investigativos, não fundamentos da ETLR. Exemplos físicos, inclusive analogias com campos de gauge, são recursos de confronto conceitual; não são premissas da teoria nem orientam a substituição de teorias particulares.

**Convenções formais usadas desde os primeiros modelos.** Os números 0 e 1 dos modelos booleanos são valores sintéticos. Em {0,1}, a∧b é 1 somente se ambos são 1; a∨b é 1 se ao menos um é 1; a⊕b é 1 se exatamente um é 1. Uma linha de atualização usa sempre o estado anterior, salvo declaração explícita em contrário; a prima x′ indica o resultado do passo. Uma oferta/entrada u é fixada pelo contrato, não inferida da observação. min e max indicam mínimo e máximo numéricos.

Para conjuntos, ∅ é vazio; x∈X é pertinência; A⊆B é inclusão; A∪B e A∩B são união e interseção; A\B é diferença; 𝒫(J) é o conjunto dos subconjuntos de J; |X| é cardinalidade. × é produto cartesiano. ∀ significa para todo, ∃ significa existe e ⇒ significa implica. Os usos lógico e booleano de ∧/∨ serão distinguíveis pelo domínio declarado. O + de CAL-01 mantém exclusivamente seu sentido informal protegido.

Uma função p:X→Y associa a cada x um único valor; X⇀Y permite indefinição declarada. im(p)={p(x):x∈X}; a fibra de y é {x:p(x)=y}; ker(p) é a equivalência x∼x′ quando p(x)=p(x′), sem sentido de núcleo linear. Fatorar f por p significa encontrar g com f=g∘p, sendo ∘ composição de funções da direita para a esquerda. Para relações, S∘R também significa primeiro R, depois S; R⊙S, introduzido para coberturas, é explicitamente lido primeiro R, depois S. Uma projeção descarta distinções; só recebe garantia relativamente à tarefa demonstrada.

Uma definição fixa um objeto matemático ou convenção. Uma hipótese é condição a justificar ou examinar. Uma proposição afirma uma consequência sob premissas. Uma demonstração sustenta essa consequência no modelo; um contramodelo invalida uma inferência de alcance maior. As oito responsabilidades AF/AC/AT/AI e os candidatos INV/AS/AR não são anunciados como sistema independente e completo de axiomas universais. CAL-01 e os conceitos filosóficos preservam seus estatutos autorais/candidatos.


## 1. Problema, fundamento e estatutos do conhecimento

Reconhecer uma unidade, situá-la em relação a outras e acompanhá-la através de transformações envolve problemas diferentes. Pode-se reconhecer o mesmo desenho em dois registros sem demonstrar a continuidade do objeto. Pode-se descrever corretamente uma resposta sem conhecer o mecanismo que a produz. Pode-se compor duas descrições válidas e perder a correlação necessária à realização conjunta. A ETLR toma essas diferenças como problemas de constituição e conhecimento, em vez de supor que uma linguagem relacional comum já as resolva.

O objeto deste volume é a constituição e a transformação de organizações sob condições de espaço, tempo e individualidade. Sua tese formal é delimitada: uma representação só conserva uma tarefa quando preserva as distinções de que essa tarefa depende. Em sistemas com escolhas e perturbações, não basta conservar estados ou arestas; devem ser conservados a ordem das escolhas, os resultados possíveis e as condições de aceitação. Essa tese de representação não demonstra que os predicados escolhidos sejam constitutivos do fenômeno. A adequação representacional e a justificação constitutiva têm obrigações próprias.

### 1.1 A contribuição de Campbell e o limite da comparação

Campbell constitui um antecedente da pergunta, anterior ao desenvolvimento sefirótico da proposta autoral. A Joseph Campbell Foundation distingue funções mística/metafísica, cosmológica, sociológica e psicológica/pedagógica do mito: relação com o mistério da existência, imagem do universo, ordenação social e orientação da vida. Essas responsabilidades motivam, na ETLR, questões sobre limites de representação, situação, relações coletivas e continuidade individual. A correspondência é uma interpretação desta pesquisa, sem equação entre quatro funções e três objetos. A fonte distingue uma mitologia de cada mito particular e situa a formulação impressa das funções em *Occidental Mythology* (1964). [F01 — funções do mito](https://www.jcf.org/learn/joseph-campbell-four-functions-of-myth).

A jornada apresentada em *The Hero with a Thousand Faces* oferece outra motivação: separação, transformação e retorno permitem perguntar o que muda e o que permanece reconhecível. Esse uso é heurístico. A ETLR não adota o monomito como lei universal dos indivíduos nem transforma a recorrência narrativa em prova da tríade. O retorno investigativo depende de avaliar um resultado no contexto receptor, sem reproduzir uma aventura como mecanismo científico. [F02 — jornada em Campbell](https://www.jcf.org/learn/joseph-campbell-heros-journey).

Uma semelhança estrutural pode decorrer de transmissão histórica, convenções de descrição, seleção dos casos ou mecanismos distintos que produzem formas parecidas. Para que a comparação produza conhecimento discriminante, é necessário declarar o que está sendo comparado, em qual corpus e com quais alternativas. Não há neste volume uma amostra intercultural capaz de estabelecer a universalidade do esquema de Campbell ou da ETLR. Sua função é constituir uma questão histórica e filosófica com condições de confronto.

### 1.2 Semiótica comparada e origens da escrita

A comparação semiótica examina como algo é diferenciado, representado e interpretado em práticas situadas. Nesta obra, “signo/luz” e “símbolo/kli” são designações autorais dos polos interno e externo; não constituem tradução automática da terminologia de Peirce, Eco, Cassirer ou de uma tradição religiosa. Os registros editoriais de *The Essential Peirce*, volume 2, identificam um corpus filosófico pertinente, mas não autorizam atribuir aos textos uma identidade com a polaridade ETLR. A edição integral não foi relida nesta passagem. [F05 — registro editorial de Peirce](https://iupress.org/9780253211903/the-essential-peirce-volume-2/).

Um exemplo histórico concreto ajuda a precisar o problema de representação. Schmandt-Besserat analisa, no antigo Oriente Próximo, mudanças entre bens, fichas de contagem e inscrições. Diferentes suportes preservam certas correspondências enquanto transformam os procedimentos de registro e abstração. A análise apresentada pela autora situa essa reconstrução em um contexto arqueológico e histórico determinado. Ela fornece um caso de transformação representacional; não estabelece uma genealogia universal da escrita nem demonstra a necessidade de E,T,I. [F03 — texto da autora sobre fichas e escrita](https://sites.utexas.edu/dsb/tokens/tokens-and-writing-the-cognitive-development/).

Na ETLR, o problema comparativo pode ser formulado sem converter o exemplo em prova: que distinções uma manifestação conserva, quais perde e de que informação o receptor necessita para uma tarefa? A formalização de fatoração responderá a essa pergunta para funções declaradas. Ela não medirá significado humano em geral. Uma mesma inscrição pode participar de práticas diversas, e um mesmo desempenho pode ser alcançado por constituições diferentes. Comparações com tradições nórdicas, herméticas ou asiáticas continuam dependentes de corpus, período, edição e passagem. Não foram preenchidas por semelhança gráfica ou memória cultural.

### 1.3 Matriz sefirótica e genealogia QOREL/ARM

A matriz sefirótica preservada em CAL-01 pertence à formulação autoral. Sua codificação em espaço, tempo e indivíduo integra a origem estrutural da investigação, também presente na linhagem QORELFlow: investigar se suas composições, funções e transformações permitem produzir conhecimento de princípios relacionais comuns. Essa origem é apresentada com transparência, sem afirmar equivalência universal com sistemas cabalísticos, validação de uma doutrina ou ontologia demonstrada. Os resultados científicos devem poder ser examinados independentemente da adesão à tradição de origem. O estudo histórico de diagramas exige distinguir tradições, versões e usos. O registro editorial de Chajes apresenta *The Kabbalistic Tree* como estudo histórico dos diagramas e identifica a edição de 2022. Essa identificação permite situar uma referência comparativa, sem homologar a matriz ETLR como doutrina tradicional única. O livro completo não foi examinado nesta passagem; tampouco se recuperou um corpus primário delimitado de Baal HaSulam ou Michael Laitman suficiente para equiparar cada termo autoral a uma passagem tradicional. [F04 — Chajes, registro editorial](https://www.psupress.org/books/titles/978-0-271-09345-1.html).

A sequência Ω, QOREL, ARM, QORELFlow e ETLR registra uma genealogia ampla de problemas e instrumentos no acervo privado. Não é uma cadeia causal única nem uma sucessão de teorias já validadas. Os documentos recuperados atribuem a esses programas responsabilidades de referência, articulação, contexto, retorno e validação, com mudanças de vocabulário. Preservar uma responsabilidade exige confrontar seu sentido nos dois contextos; nomes iguais não provam conservação. O K de uma arquitetura histórica não é automaticamente K0 da investigação, e um procedimento chamado “retorno” não é uma inversa matemática.

PM e MO são protocolos de investigação, não fundamentos de espaço, tempo e indivíduo. No enquadramento autoral, ETLR-MO é instrumento investigativo e polo interno; a teoria ETLR é manifestação externa. Essa interpretação não prova equivalência entre código, teoria e realidade. O volume apresenta argumentos compreensíveis sem executar motores privados. A genealogia é preservada para reconhecer origem e dependências; as demonstrações formais não usam alegações físicas de Ω/QOREL como premissas ocultas. A compatibilidade com contratos completos ARM permanece sem certificação porque o conjunto documental necessário não foi recuperado inequivocamente.

### 1.4 Três hipóteses e três espécies de obrigação

A finalidade geral articula as três hipóteses seguintes sem alterar seus conteúdos ou condições de avaliação. Investigar princípios comuns entre domínios é uma questão aberta; utilidade local, correspondência entre modelos e universalidade ontológica exigem justificações distintas. A estrutura formal deste volume fornece instrumentos para essa investigação e não antecipa seu resultado.

| Hipótese preservada | Conteúdo | O que a evidência presente permite |
|---|---|---|
| H1 — ontológica forte | E,T,I são os únicos fatos relacionais fundamentais, com necessidade, suficiência e irredutibilidade a examinar | Formular e discriminar problemas; nenhum teorema do volume demonstra exclusividade universal |
| H2 — epistemológica | A tríade é fundamental à organização da experiência e do conhecimento humanos | Exige comparação histórico-cultural/cognitiva própria; êxito num modelo não basta |
| H3 — metodológica | A tríade pode funcionar como linguagem investigativa produtiva | Modelos mostram utilidade discriminante local; custo, perdas e alternativas continuam pertinentes |

As três hipóteses podem coexistir, mas a confirmação de uma versão local de H3 não implica H2 ou H1. Um modelo construído desde o começo em linguagem triádica não discrimina, por seu simples sucesso, uma ontologia triádica de uma escolha metodológica. Relação, processo, informação e modalidade permanecem alternativas a examinar: derivadas, adicionais, anteriores ou co-constitutivas conforme a hipótese. Chamá-las de aspectos de E,T,I sem critério independente eliminaria a possibilidade de confronto.

O âmbito pretendido da hipótese autoral abrange os domínios físico, mental e abstrato e preserva seu sentido filosófico espiritual/astral. O âmbito demonstrado neste volume é outro: resultados em classes explícitas de modelos. Não há observação empírica independente dos domínios espiritual/astral, nem transferência automática de um jogo finito para uma organização física ou mental.

**Adequação representacional** pergunta se a descrição conserva uma tarefa definida no modelo. **Justificação constitutiva** pergunta se estados, fronteiras, suportes e critérios representam o que constitui o objeto no domínio. **Validação empírica** pergunta se procedimentos e observações sustentam a aplicação diante de alternativas. Integridade documental permite rastrear cada obrigação, sem demonstrar sua verdade. A distinção organiza todo o volume.

## 2. Espaço, tempo, indivíduo e constituição situada

### 2.1 Caracterizações candidatas

Espaço designa, como hipótese de trabalho, a organização situada das condições de diferenciação, coexistência, relação e participação. Não se identifica automaticamente com extensão geométrica, métrica, conjunto de estados ou recorte do investigador. Uma geometria pode ser necessária a uma aplicação física, enquanto uma relação de acesso pode bastar a outra tarefa; a escolha formal precisa indicar o que deixa de representar.

Tempo designa condições de ocorrência, ordem, duração, ritmo, continuidade e transformação. Uma ordem parcial representa precedência sob hipóteses, sem esgotar duração ou experiência temporal. A sequência em que um observador registra eventos pode diferir da dependência entre eles. Relógios locais com ritmos diferentes podem compartilhar um parâmetro, sem provar tempos físicos independentes. A distinção entre ordem parcial e relógio é compatível com o antecedente técnico de Lamport [B16], cujo uso permanece localizado.

Indivíduo designa a unidade candidata cuja diferenciação, constituição, identidade, fronteira, manifestação e continuidade são investigadas. Não se exige indivisibilidade material, consciência ou autonomia. Uma unidade de análise pode ser um agregado ou uma organização sem individuação justificada. Uma estrutura matemática estática desafia a obrigação de temporalidade do próprio objeto: o tempo de sua investigação não deve ser atribuído automaticamente à estrutura.

As seis direções E→T, T→E, E→I, I→E, T→I e I→T são perguntas sobre participação recíproca. Elas não demonstram causalidade, independência, exaustividade ou ordem cosmológica. Para comparar duas respostas, é preciso manter claras a referência, a operação e as condições do domínio. Alterar o recorte de uma mesma configuração e alterar a configuração sob recorte fixo constituem diferenças discriminantes.

### Bloco protegido de CAL-01

O bloco seguinte é reprodução literal de PM-01 §2.2, conferida como substring UTF-8 no manuscrito. A aplicação editorial o inclui sem alterar palavras, composições ou comentários. A redação interpretativa fora do bloco continua candidata.

### 2.2 Calibração autoral CAL-01 — não modificar silenciosamente

E = espaço; T = tempo; I = indivíduo. A notação é provisória. O sinal + designa composição informal e não adição numérica, função, causalidade ou operador demonstrado. A ordem e os agrupamentos integram a formulação a preservar.

| Posição | Composição |
|---|---|
| Kether | E |
| Chokhmah (Hockmah) | T |
| Binah | I |
| Da’at | passagem que limita a investigação ao indivíduo |
| Chesed | E+T |
| Gevurah | E+I |
| Tiferet | I+E+T |
| Hod | I+E |
| Netzach | T+E |
| Yesod | (I+E)+(I+T) |
| Malkut | o indivíduo no espaço-tempo |

C01. A passagem Da’at delimita a investigação ao indivíduo sem eliminar E/T; distinguir Binah como objeto de Da’at como passagem. Não pressupor quarta primitiva, processo físico, fronteira material ou ordem causal.

C02. Confrontar E+T/T+E (Chesed/Netzach) e E+I/I+E (Gevurah/Hod). A ordem pode alterar referência, operação efetiva ou somente interpretação em certos domínios. Não presumir comutatividade, não comutatividade, inversibilidade, primeiro termo como emissor ou causa, ou identidade entre pares por compartilharem componentes.

C03. Conservar Tiferet, Yesod e Malkut como responsabilidades distinguíveis. Integração, articulação de relações e situação/realização são interpretações candidatas, não definições demonstradas. Preservar as duas ocorrências de I em Yesod; investigar a referência comum sem cancelar, duplicar literalmente ou impor igualdade algébrica. I+T aparece em Yesod; T+I não está isoladamente explicitado. Investigar a ausência sem inventar posição para completar simetria.

C04. Preservar a estrutura 3+3+3+1 e Da’at como passagem virtual no enquadramento histórico, sem inferir que os 22 caminhos foram formalizados, sem impor sequência linear, e sem igualar a matriz CAL-01 aos contratos QORELFlow. Distinguir o que constitui o fenômeno do como o investigador o conhece. As seis direções E↔T, E↔I, T↔I são perguntas, não leis demonstradas. Recuperar função–ação–lei–refração quando pertinente, respeitando o significado histórico e o contexto receptor.

### 2.3 Referência, polaridade e escalas

K0 é a referência investigativa persistente que permite reconhecer a questão, sua genealogia e os deltas das passagens. A referência local K pode ser revista; essa revisão deve conservar a possibilidade de dizer o que foi mudado. K0 não é estado inicial, ambiente, fronteira, orçamento ou conjunto de viabilidade. O volume usa W para regiões vencedoras e Env para ambiente, conservando E como espaço na calibração. O símbolo K_c, quando empregado como predicado constitutivo, será escrito com esse índice e não substituirá K0.

A polaridade interna, signo/luz, dirige o exame à constituição, ao potencial e às relações internas. A externa, símbolo/kli, dirige-o à manifestação, às interfaces e à participação ambiental. Não se pressupõem duas substâncias ou duas álgebras independentes. Há pelo menos três alternativas: álgebras acopladas por contrato; uma estrutura com duas vistas; uma estrutura mais ampla de relações e testemunhos que contenha os dois casos. A arquitetura formal adotada aqui explora a terceira possibilidade, sem decidir entre ontologias concorrentes. Refração pode envolver perda, transformação e reconstrução parcial; projeção funcional é apenas um caso matemático delimitado.

Fronteira, interface, campo, dimensão e escala possuem responsabilidades distintas. Fronteira classifica pertencimento e participação relativamente à referência; interface especifica portas e condições de intercâmbio; campo reúne condições relacionais pertinentes; dimensão é um eixo ou aspecto declarado; escala indica nível de organização ou resolução. Nenhuma dessas expressões ganha suficiência ontológica pelo uso em um tipo formal. Uma relação externa a A pode ser interna a G que contém A e B, permanecendo externa a A. A mudança de classificação não produz G como indivíduo.

As famílias constitutivas, externas, de fronteira, temporais, coletivas e multiescalares organizam perguntas históricas. Não se confundem com as seis direções entre E,T,I, nem precisam formar classes disjuntas. Uma mesma ocorrência pode participar de várias famílias e escalas, inclusive em organizações sobrepostas. Duplicar seu registro sem conservar a referência comum produziria erro de proveniência ou de contagem.

### 2.4 Dois confrontos constitutivos básicos

<a id="r-VI00-U00"></a>

### VI00-U00 — U/C: observação e constituição

**Hipóteses preservadas:** Modelos binários estipulados na seção-fonte.

**Conclusão do registro:** Manifestação inicial igual não decide dependência ou condição futura.

Considere dois participantes binários, entrada u e observação do par (a,b). No modelo U, (a',b')=(u,u); no modelo C, (a',b')=(u,a). Com u=0 constante e estado inicial (0,0), ambos permanecem em (0,0).

<a id="prova-VI00-U00"></a>

**Demonstração e contramodelo.** A substituição nas duas regras dá (0,0), e a indução repete o cálculo em qualquer horizonte. Entretanto, a intervenção que fixa (a,b)=(1,0), conservando u=0, produz (0,0) em U e (0,1) em C. Portanto a trajetória inicialmente igual não determina a dependência funcional estipulada. Alterar somente a referência de A para G={A,B} reclassifica o vínculo como interno a G sem mudar nenhuma regra. Trocar U por C, sob a mesma referência, altera a dependência. São operações diferentes.

A intervenção discrimina dois mecanismos formais, mas não preenche identidade, continuidade ou participação coletiva. Acoplamento e individuação não se identificam. Este ID indexa o confronto U/C de §00.6 do rev14; não cria um teorema histórico retroativo.

**Limite herdado:** ID de índice novo, não renumeração de resultado antigo.

**Rastreabilidade:** Integração interna; referências B09 B13. Fonte, linha 292: Caderno Científico ETLR(f1), rev14, linha 292 (fonte histórica em acervo privado); [ficha completa](MATRIZ_RASTREABILIDADE_50_RESULTADOS.html#r-VI00-U00); [auditoria VI05](../edicao_1_0_candidata/AUDITORIA_50_RESULTADOS.html#r-VI00-U00). Originalidade externa não estabelecida.


<a id="r-VI00-U01"></a>

### VI00-U01 — F/D: condições futuras de passagem

**Hipóteses preservadas:** Modelos binários estipulados na seção-fonte.

**Conclusão do registro:** Manifestação inicial igual não decide dependência ou condição futura.

O estado é (x,g) em {0,1}² e a oferta é u. Defina y=u se g=1 e y=x se g=0. F(x,g;u)=(y,g), enquanto D(x,g;u)=(y,x), usando o x anterior.

<a id="prova-VI00-U01"></a>

**Demonstração e contramodelo.** Para toda tripla (x,g,u), o primeiro resultado observado x'=y e a admissão inicial g coincidem nos dois modelos. Em (1,0), com oferta 0, F dá (1,0) e D dá (1,1). Na oferta seguinte 0, F mantém (1,0), enquanto D dá (0,1). Assim, coincidência presente de manifestação e admissão não implica coincidência das condições de passagem futuras. A afirmação resulta de duas substituições, sem supor mudança do recorte.

A dependência g'=x foi estipulada. Ela representa transformação de uma condição operacional; não demonstra produção material de fronteira, origem das regras ou autogeração forte.

**Limite herdado:** ID de índice novo, não renumeração de resultado antigo.

**Rastreabilidade:** Integração interna; referências B09 B17. Fonte, linha 394: Caderno Científico ETLR(f1), rev14, linha 394 (fonte histórica em acervo privado); [ficha completa](MATRIZ_RASTREABILIDADE_50_RESULTADOS.html#r-VI00-U01); [auditoria VI05](../edicao_1_0_candidata/AUDITORIA_50_RESULTADOS.html#r-VI00-U01). Originalidade externa não estabelecida.


Esses confrontos distinguem observação, dependência estipulada e evolução das condições de passagem. O passo constitutivo adicional — justificar por que uma dependência ou condição é indispensável ao indivíduo no domínio — continua distinto da capacidade de representá-la. Essa separação permitirá conservar resultados matemáticos sem converter o nome de um estado em certificado ontológico.

## 3. Linguagem, assinatura tipada e transformação

### 3.1 Objetos de uma descrição situada

Fixe contexto c=(d,δ,s,F,Env,K): domínio d, aspecto ou dimensão δ, escala s, campo F, ambiente Env e referência local K. Os índices são responsabilidades de interpretação; não uma decomposição necessária de toda realidade. Uma configuração Q_c=(V_ref,X,R,∂,H,L) reúne referências participantes, estados pertinentes, relações, condições de fronteira, história e regras/versionamento. O conjunto de configurações será Conf(c). Para evitar colisão, V sem índice será reservado à segurança nos jogos.

| Tipo | Objeto e responsabilidade |
|---|---|
| Ctx, Ref | Contexto e unidade candidata referida; nome não demonstra individualidade |
| Conf(c) | Configuração contextualizada, com distinções suficientes à tarefa |
| Rel(c) | Relação situada de aridade declarada, participantes, papéis e condições |
| Adm | Avaliação {P,N,?}: permitido, negado, indeterminado |
| Trans(c,c') | Relação entre configurações de origem e destino compatíveis |
| Ev, Hist | Ocorrência com testemunho e história com precedência/proveniência pertinentes |
| Port | Entrada/saída tipada e condições de compartilhamento |
| Rep | Função ou correspondência de representação explicitamente declarada |
| Game | Estados, ações, resultados ambientais, etiquetas e objetivo |

Uma relação n-ária pode ser descrita como subconjunto de um produto de tipos de papéis. Sua redução a arestas binárias só é adequada se conservar requisitos conjuntos e correlações. Duas condições isoladamente satisfeitas podem não ter testemunho comum, como mostrará a composição de interfaces. A opção por conjuntos e relações neste fragmento é um instrumento matemático, sem declarar que toda relação real seja extensionalmente esgotada por ele.

Formação, admissibilidade e ocorrência são julgamentos diferentes. Escrever Γ;c⊢e:τ significa que a expressão possui tipo sob declarações Γ. Avaliar g(c,x,e)=P significa permissão no contrato. Executar exige ainda um testemunho de transição e uma ocorrência. Uma ocorrência pode conservar o estado observado; a diagonal de uma relação não é, sozinha, um acontecimento. O valor ? registra insuficiência de informação e não uma terceira verdade ontológica. Suspender execução sob ? não o converte em N.

O contrato histórico de passagem Ω_e conserva origem/destino, referência K0, regra e versão, obrigações, testemunho e proveniência pertinentes. O índice e distingue esse contrato do projeto Ω. Se uma guarda consulta história, a próxima junção precisa receber a história ou um resumo provadamente suficiente. Memória seletiva é compatível com conservação; apagar distinções sem verificar a tarefa não é.

### 3.2 Oito responsabilidades axiomáticas candidatas

Os nomes AF, AC, AT e AI são preservados como responsabilidades históricas. Algumas leis decorrem das definições matemáticas; outras são obrigações de interpretação. Não se afirma independência ou completude de um sistema axiomático único.

Na tabela seguinte, β é apenas o nome de um classificador contextual de uma relação em interior, exterior, passagem ou indeterminação, relativamente à referência declarada; não é guarda de execução nem constitui por si uma fronteira efetiva.

| ID | Formulação integrada candidata | Tratamento formal e limite |
|---|---|---|
| <a id="cand-AF-01"></a>AF-01 | Classificação de relações depende de contexto e referência | β pode classificar interior, exterior, passagem ou indeterminação; não determina admissibilidade |
| <a id="cand-AF-02"></a>AF-02 | Manifestação não determina em geral constituição ou identidade | Fatoração de cada diagnóstico precisa ser examinada |
| <a id="cand-AC-01"></a>AC-01 | Formação, permissão, realização e mudança observável são distintas | Guarda trivalente e ocorrência possuem contratos separados |
| <a id="cand-AC-02"></a>AC-02 | Composição exige tipos e condições intermediárias compatíveis | Associatividade é demonstrável para relações fixas; não se estende por decreto a CAL-01 |
| <a id="cand-AT-01"></a>AT-01 | Ocorrência, transformação, precedência e duração não se identificam | Mesmos extremos podem conter evento ou execução vazia |
| <a id="cand-AT-02"></a>AT-02 | A história pertinente deve ser conservada ou resumida com suficiência | Preservar cobertura não preserva ordem, multiplicidade ou genealogia |
| <a id="cand-AI-01"></a>AI-01 | Continuidade e identidade exigem critérios e história declarados | Igualdade de tokens, papéis ou comportamento pode divergir |
| <a id="cand-AI-02"></a>AI-02 | Compor organizações não demonstra individuação coletiva | IO01–05 são obrigações candidatas, com justificação própria |

Uma definição formal pode absorver parte de uma responsabilidade, como a associatividade de AC-02 no fragmento relacional. Isso não prova redundância global do compromisso conceitual. AF-02, AC-01 e AT-02 compartilham o lema de fatoração, mas avaliam tarefas diferentes. AI-01 e AI-02 não decorrem da associatividade. Contramodelos a inferências excessivas não são, sem trabalho adicional, modelos de sete axiomas e negação do oitavo.

### 3.3 Invariantes e efeitos de transformação

Há invariantes estruturais da linguagem, propriedades condicionais de uma organização e grandezas próprias de um domínio. Tipagem preservada é diferente de energia conservada; constância de uma observação é diferente de continuidade histórica. A lista histórica INV-01–08 inclui obrigações de integridade, preservação e revisão, sem constituir oito grandezas constantes. Aplicar uma transformação exige declarar qual dessas responsabilidades está em questão.

Operações de expansão, contração e revisão podem afetar o conjunto de interpretações admissíveis, o campo, a interface ou a própria regra. A antitonia de restrições fixas só vale na primeira classe. Alterar regra/versionamento exige novo contrato de transferência. Uma mudança de representação pode dispensar a revisão de resultados independentes, mas precisa reabrir as conclusões cujas premissas efetivamente mudaram.

## 4. Álgebra das relações, execuções e interfaces

Uma operação formal precisa de domínio, tipos e regra de composição. Essa exigência permite usar matemática estabelecida sem atribuir-lhe uma ontologia maior que suas hipóteses. A álgebra relacional conhecida fornece composição existencial, união, vazio e diagonais. Em um tipo único X, essas operações formam o exemplo relacional de álgebra idempotente com distributividade. Com tipos variados, a composição é parcial por compatibilidade de origem e destino. O antecedente de tipagem em Kozen [B01] evita tratar toda expressão como multiplicação global; não se usa seu metateorema para inferir leis do + autoral de CAL-01.

<a id="r-P02-1"></a>

### P02.1 — Associatividade condicionada

**Hipóteses preservadas:** Três relações fixas com tipos intermediários compatíveis.

**Conclusão do registro:** Composição associativa e diagonais como identidades.

Se R⊆X×Y, S⊆Y×Z e T⊆Z×W são relações fixas, define-se (x,z)∈S∘R quando existe y com xRy e ySz.

<a id="prova-P02-1"></a>

**Demonstração.** (x,w) pertence a T∘(S∘R) precisamente quando existem z,y tais que xRy, ySz e zTw. A mesma fórmula caracteriza (T∘S)∘R. Logo os dois conjuntos são iguais. Para a diagonal Id_X={(x,x):x∈X}, o testemunho intermediário é necessariamente x; por isso R∘Id_X=R e Id_Y∘R=R. A existência de pares não foi pressuposta: a prova também vale para relações vazias.

Não há comutatividade geral: uma relação X→Y não pode sequer ser composta na ordem inversa sem tipos compatíveis. A prova não cobre uma política que modifica as próprias relações ao reagrupar fatores, nem define o sinal + de CAL-01.

**Limite herdado:** Álgebra conhecida; não vale automaticamente para políticas com efeitos de agrupamento nem para CAL-01.

**Rastreabilidade:** Matemática conhecida; referências B01 B02. Fonte, linha 505: Caderno Científico ETLR(f1), rev14, linha 505 (fonte histórica em acervo privado); [ficha completa](MATRIZ_RASTREABILIDADE_50_RESULTADOS.html#r-P02-1); [auditoria VI05](../edicao_1_0_candidata/AUDITORIA_50_RESULTADOS.html#r-P02-1). Originalidade externa não estabelecida.


### 4.1 Projeção e o testemunho intermediário

<a id="r-P02-2"></a>

### P02.2 — Imagem da composição

**Hipóteses preservadas:** Mapas de projeção funcionais e relações fixas.

**Conclusão do registro:** Imagem da composição contida na composição das imagens.

Fixe projeções p_X,p_Y,p_Z e escreva p_*(R)={(p_X(x),p_Y(y)):xRy}. Então p_*(S∘R)⊆p_*(S)∘p_*(R).

<a id="prova-P02-2"></a>

**Demonstração.** Todo par do primeiro conjunto tem um único testemunho concreto y usado nos dois fatores. Sua classe p_Y(y) testemunha a composição abstrata. No sentido inverso, os fatores podem ter testemunhos y e y' diferentes na mesma fibra, impedindo a junção concreta.

**Contramodelo.** R={(a,b₀)}, S={(b₁,c)}, b₀≠b₁ e p_Y(b₀)=p_Y(b₁). A composição concreta é vazia, mas a abstrata contém (p_X(a),p_Z(c)). Se p_Y for injetiva, a igualdade de classes força y=y' e assegura igualdade; a injetividade é suficiente, sem ser necessária. Quando ambos os fatores usam b₀, a igualdade pode valer embora p_Y continue não injetiva.

**Limite herdado:** Injetividade intermediária é suficiente, não necessária; igualdade é por extremos.

**Rastreabilidade:** Matemática conhecida; referências B03 B17. Fonte, linha 513: Caderno Científico ETLR(f1), rev14, linha 513 (fonte histórica em acervo privado); [ficha completa](MATRIZ_RASTREABILIDADE_50_RESULTADOS.html#r-P02-2); [auditoria VI05](../edicao_1_0_candidata/AUDITORIA_50_RESULTADOS.html#r-P02-2). Originalidade externa não estabelecida.


<a id="r-P03-1"></a>

### P03.1 — Levantamento por extremos

**Hipóteses preservadas:** Relações e projeções dos extremos; composição particular.

**Conclusão do registro:** Igualdade se e somente se cada par abstrato de extremos tem algum caminho concreto.

Para a composição particular R,S de P02.2, a igualdade das duas relações projetadas equivale à seguinte condição: cada par abstrato de extremos obtido compondo as imagens admite algum xRySz com as mesmas imagens de x e z.

<a id="prova-P03-1"></a>

**Demonstração.** A condição é exatamente a inclusão da composição das imagens na imagem da composição: cada par à direita recebe o testemunho exigido para estar à esquerda. A inclusão contrária já foi provada em P02.2. As duas inclusões equivalem à igualdade.

Os quantificadores são por par de extremos. Não se exige levantar todo intermediário abstrato escolhido nem iniciar no representante concreto previamente fixado. A condição mais forte de P04.1 resolve outra tarefa. Pode haver uma rota concreta por um intermediário e, simultaneamente, outra rota abstrata espúria com os mesmos extremos; isso não viola a igualdade por extremos.

**Limite herdado:** Critério mais fraco que levantamento a partir de cada representante.

**Rastreabilidade:** Matemática conhecida; referências B03 B17. Fonte, linha 642: Caderno Científico ETLR(f1), rev14, linha 642 (fonte histórica em acervo privado); [ficha completa](MATRIZ_RASTREABILIDADE_50_RESULTADOS.html#r-P03-1); [auditoria VI05](../edicao_1_0_candidata/AUDITORIA_50_RESULTADOS.html#r-P03-1). Originalidade externa não estabelecida.


O contraste central está nos quantificadores. A igualdade por extremos pode admitir apenas um caminho concreto por par de extremos; o levantamento forte exigirá cada representante inicial. Essa diferença já impede confundir uma composição bem tipada e não vazia com a realização de toda trajetória abstrata descrita.

### 4.2 Execuções com palavras e cobertura

<a id="r-P02-3"></a>

### P02.3 — Trajetórias rotuladas

**Hipóteses preservadas:** Palavras finitas, estados de junção completos, concatenação sem restrição histórica adicional.

**Conclusão do registro:** Associatividade e projeção de rótulos preserva composição.

Uma execução finita enriquecida é uma tripla (x,w,y), onde w é uma palavra de eventos de um alfabeto fixo. Para relações de execuções R:X→Y e S:Y→Z, a composição reúne (x,wv,z) quando existem y com (x,w,y)∈R e (y,v,z)∈S. O estado intermediário conserva toda condição da próxima junção.

<a id="prova-P02-3"></a>

**Demonstração.** Três fatores compõem, em qualquer agrupamento, exatamente quando existem os mesmos dois estados intermediários e três palavras w,v,t. As etiquetas finais são (wv)t e w(vt), iguais pela associatividade da concatenação. As triplas (x,ε,x), com palavra vazia ε, são unidades. Apagar somente a palavra preserva a composição: os testemunhos y permanecem os mesmos e qualquer par composto possui suas palavras testemunhas. Apagar também distinções de y volta ao problema de P02.2.

Palavra vazia não é acontecimento consumado. Duas palavras diferentes com os mesmos extremos não se tornam a mesma história por sua projeção; uma história pode ainda conter dependências parciais que uma palavra linear não registra.

**Limite herdado:** Esquecimento de rótulos não apaga estado de junção; não conserva história individual.

**Rastreabilidade:** Aplicação; referências B01 B02. Fonte, linha 529: Caderno Científico ETLR(f1), rev14, linha 529 (fonte histórica em acervo privado); [ficha completa](MATRIZ_RASTREABILIDADE_50_RESULTADOS.html#r-P02-3); [auditoria VI05](../edicao_1_0_candidata/AUDITORIA_50_RESULTADOS.html#r-P02-3). Originalidade externa não estabelecida.


<a id="r-P11-2"></a>

### P11.2 — Álgebra de execuções

**Hipóteses preservadas:** Relações em X×P(J)×X com estados de junção suficientes; eventos certificados.

**Conclusão do registro:** Composição associativa com unidade, distributividade e estrela de execuções finitas.

Fixe estados X e conjunto finito J de obrigações. Uma relação de execuções cobertas é R⊆X×𝒫(J)×X. Defina R⊙S por (x,A∪B,z) quando existem y,(x,A,y)∈R e (y,B,z)∈S. Aqui a escrita R⊙S significa primeiro R, depois S. A unidade é 1={(x,∅,x)} e o zero é a relação vazia.

<a id="prova-P11-2"></a>

**Demonstração.** Em três fatores, ambos os agrupamentos exigem os mesmos estados y,z e produzem A∪B∪C. A união de conjuntos é associativa, dando a igualdade. A unidade usa o mesmo estado e acrescenta ∅ à cobertura. Não há testemunho para composição com 0. Distribuir a composição sobre união consiste em separar a alternativa de pertencer ao primeiro ou ao segundo fator; os testemunhos são os mesmos. Por indução, Rⁿ representa exatamente n passos, com cobertura igual à união de suas etiquetas. Logo R*=⋃_{n≥0}Rⁿ representa todas e somente as execuções finitas, incluindo a execução vazia.

A construção pode ter até |X|²·2^|J| triplas. Isso só é uma cota finita se X for finito. Cobertura não conserva ordem, multiplicidade, genealogia nem periodicidade. Não fornece uma execução infinita por simplesmente escrever estrela.

**Limite herdado:** Cobertura esquece ordem/multiplicidade; não substitui log ou CAL-01.

**Rastreabilidade:** Aplicação; referências B01 B02. Fonte, linha 2326: Caderno Científico ETLR(f1), rev14, linha 2326 (fonte histórica em acervo privado); [ficha completa](MATRIZ_RASTREABILIDADE_50_RESULTADOS.html#r-P11-2); [auditoria VI05](../edicao_1_0_candidata/AUDITORIA_50_RESULTADOS.html#r-P11-2). Originalidade externa não estabelecida.


A compactação entre esses resultados usa uma mesma construção: triplas com estado inicial, testemunho em um monoide e estado final. Palavras usam concatenação; cobertura usa união de subconjuntos de J. A prova de associatividade usa, em ambos, os mesmos estados intermediários e a lei do monoide. A diferença de testemunho é substantiva: cobertura responde “quais obrigações ocorreram?”, enquanto uma palavra conserva ordem e multiplicidade. Nenhuma das duas representa automaticamente toda proveniência de ocorrências.

### 4.3 Composição aberta e ambiente compartilhado

<a id="r-P08-1"></a>

### P08.1 — Composição de interfaces

**Hipóteses preservadas:** Mesma conexão global, tipos e variáveis compartilhadas; ocultação só após todos os fatores.

**Conclusão do registro:** Agrupamentos seriais dão a mesma relação.

Uma unidade A possui estado interno x_A, entrada u_A, saída v_A e relação aberta R_A(x_A,u_A,x'_A,v_A,e), podendo consultar o ambiente comum e. Para três unidades, fixe conexões W_AB(v_A,u_B) e W_BC(v_B,u_C). A relação global é a conjunção R_A∧W_AB∧R_B∧W_BC∧R_C, quantificando existencialmente apenas os valores de interface internos após seu último uso.

<a id="prova-P08-1"></a>

**Demonstração.** Expandir (AB)C e A(BC) produz os mesmos cinco fatores e as mesmas variáveis internas. Associatividade da conjunção e renomeação sem captura dos quantificadores fornecem a mesma fórmula. Uma variável ainda consultada por outro fator não pode ser eliminada como se possuísse um testemunho independente.

**Contramodelo.** Em booleanos, ∃e[(a=e)∧(b=e)] permite apenas a=b. Já (∃e a=e)∧(∃e b=e), com testemunhos independentes, permite todos os pares. Igualmente, exigir e=0 e e=1 no mesmo ambiente é insatisfatível; duplicar o ambiente muda o contrato. A associatividade demonstrada é de uma conexão global fixa, sem afirmar que ordens temporais diferentes comutem.

**Limite herdado:** Associatividade lógica não é comutação temporal.

**Rastreabilidade:** Aplicação; referências B09. Fonte, linha 1226: Caderno Científico ETLR(f1), rev14, linha 1226 (fonte histórica em acervo privado); [ficha completa](MATRIZ_RASTREABILIDADE_50_RESULTADOS.html#r-P08-1); [auditoria VI05](../edicao_1_0_candidata/AUDITORIA_50_RESULTADOS.html#r-P08-1). Originalidade externa não estabelecida.


<a id="r-P08-2"></a>

### P08.2 — Abstração versus composição

**Hipóteses preservadas:** Projeções funcionais; relações R,S; homogeneidade das saídas de S na interface.

**Conclusão do registro:** Inclusão geral; igualdade para toda R se interface homogênea, necessária com X não vazio.

Além da inclusão de P02.2, defina D_S(y)={p_Z(z):ySz}. Se D_S é constante em cada fibra de p_Y, a composição das imagens coincide com a imagem da composição para toda relação anterior R e toda projeção p_X.

<a id="prova-P08-2"></a>

**Demonstração da suficiência.** Um par da composição abstrata tem testemunhos xRy e y'Sz com p_Y(y)=p_Y(y'). Pela homogeneidade, p_Z(z)∈D_S(y), logo existe z' com ySz' e p_Z(z')=p_Z(z). O mesmo y agora testemunha uma composição concreta com as imagens externas requeridas. Isso dá a inclusão inversa.

**Necessidade para toda R, com X≠∅.** Se D_S(y)≠D_S(y') na mesma fibra, escolha uma classe c presente num lado e ausente no outro e um x₀∈X. Tome R={(x₀,y)}, usando como y o lado sem c. A composição abstrata alcança c pelo outro representante; a concreta não. Contradição à igualdade universal. Para uma R fixa, homogeneidade não é necessária: R=∅ já produz igualdade. O contramodelo de dois intermediários em P02.2 basta para a falha irrestrita; o exemplo histórico de três estados não recebe alegação de minimalidade universal.

**Limite herdado:** Homogeneidade não necessária para cada R particular; exemplo de três estados não mínimo irrestrito.

**Rastreabilidade:** Integração interna; referências B03 B09. Fonte, linha 1253: Caderno Científico ETLR(f1), rev14, linha 1253 (fonte histórica em acervo privado); [ficha completa](MATRIZ_RASTREABILIDADE_50_RESULTADOS.html#r-P08-2); [auditoria VI05](../edicao_1_0_candidata/AUDITORIA_50_RESULTADOS.html#r-P08-2). Originalidade externa não estabelecida.


Determinismo de regras locais tampouco garante solução global única para uma restrição instantânea de feedback. Em booleanos, p=f(q), q=h(p) equivale a um ponto fixo de f∘h. Com f identidade e h negação, não há solução; com ambas identidades, há duas. Uma evolução com atraso, como p(t+1)=1−p(t), é outro modelo e pode alternar. A satisfatibilidade de uma conexão lógica não determina uma cronologia física.

A composição multiescalar deve declarar se o ambiente é comum, se recursos são compartilhados, quais variáveis ainda serão usadas e quais contratos já foram integrados. Provas locais não autorizam duplicar recursos ou perturbações correlacionadas. Uma relação que é externa aos módulos pode ser interna ao conjunto composto, sem que essa mudança de referência prove unidade constitutiva do conjunto.

## 5. Representação suficiente e conservação de trajetórias

Uma representação é suficiente relativamente a uma tarefa e a uma classe de operações. Igualdade da manifestação presente não garante igualdade de futuros, admissibilidade ou diagnóstico histórico. O problema matemático básico é determinar se a tarefa pode ser definida sem consultar as distinções apagadas.

<a id="r-P08-3"></a>

### P08.3 — Fatoração de tarefas

**Hipóteses preservadas:** Manifestação m e característica f deterministas.

**Conclusão do registro:** f=g∘m se e somente se ker(m) contido em ker(f).

Se m:X→M é uma manifestação determinista e f:X→F é uma tarefa, existe g:im(m)→F com f=g∘m se e somente se m(x)=m(y) implica f(x)=f(y). Equivalentemente, ker(m)⊆ker(f).

<a id="prova-P08-3"></a>

**Demonstração.** Se g existe, substituir m(x)=m(y) na igualdade f=g∘m dá f(x)=f(y). Reciprocamente, defina g(m(x))=f(x). Qualquer outro representante y da mesma manifestação fornece o mesmo f pela hipótese; portanto a definição é independente do representante, e g∘m=f em todo X. A função g é única na imagem de m. Não há exigência de sobrejetividade sobre um contradomínio maior.

**Contramodelo e alcance.** Se m(a)=m(b), mas f(a)≠f(b), nenhum pós-processamento da manifestação isolada resolve f. Acrescentar informação k(x) muda a representação para (m(x),k(x)) e exige novo teste. Recuperar integralmente x requer m injetiva; resolver apenas f pode exigir menos. Para uma manifestação multivalorada, esta formulação funcional precisa ser substituída por outro contrato.

**Limite herdado:** Informação adicional e nova observação mudam a representação; não há métrica semântica universal.

**Rastreabilidade:** Matemática conhecida; referências B17. Fonte, linha 1293: Caderno Científico ETLR(f1), rev14, linha 1293 (fonte histórica em acervo privado); [ficha completa](MATRIZ_RASTREABILIDADE_50_RESULTADOS.html#r-P08-3); [auditoria VI05](../edicao_1_0_candidata/AUDITORIA_50_RESULTADOS.html#r-P08-3). Originalidade externa não estabelecida.


<a id="r-P03-2"></a>

### P03.2 — Guarda e história ocultada

**Hipóteses preservadas:** Duas histórias admitidas identificadas por p, com guardas distintas.

**Conclusão do registro:** Guarda não fatora por p.

Se duas histórias admitidas h,h' do mesmo estado local x são apagadas pela projeção p(x,h)=x e uma guarda g distingue essas histórias, g não fatora por p.

<a id="prova-P03-2"></a>

**Demonstração.** A suposta fatoração exigiria g(x,h)=ĝ(x)=g(x,h'), contradizendo a hipótese. É a direção necessária de P08.3 aplicada à guarda, mesmo que os valores sejam P,N,?. Um resumo histórico menor que a história integral pode bastar quando torna a guarda constante nas fibras. A impossibilidade é relativa à projeção e à tarefa escolhidas, não uma inacessibilidade absoluta de toda informação interna.

**Limite herdado:** Impossibilidade relativa à projeção e guarda, não inacessibilidade universal.

**Rastreabilidade:** Aplicação; referências B17. Fonte, linha 644: Caderno Científico ETLR(f1), rev14, linha 644 (fonte histórica em acervo privado); [ficha completa](MATRIZ_RASTREABILIDADE_50_RESULTADOS.html#r-P03-2); [auditoria VI05](../edicao_1_0_candidata/AUDITORIA_50_RESULTADOS.html#r-P03-2). Originalidade externa não estabelecida.


<a id="r-P04-2"></a>

### P04.2 — Preservação da guarda

**Hipóteses preservadas:** Guarda trivalente definida em X; p sobre sua imagem.

**Conclusão do registro:** Guarda fatora se e somente se constante nas fibras.

Dada uma guarda g:X→{P,N,?}, há ĝ:im(p)→{P,N,?} com g=ĝ∘p exatamente quando g é constante por fibra.

<a id="prova-P04-2"></a>

**Demonstração.** P08.3 vale para qualquer conjunto de valores, incluindo os três valores da avaliação. Se constante, defina ĝ(p(x))=g(x); se não, dois representantes exigem valores diferentes da mesma função.

**Contramodelo de independência.** Dois estados podem ter relações de sucessores vazias e avaliações N e ?. A dinâmica projetada é igual, mas não fornece uma única avaliação correta. P também pode ser uma avaliação anterior à execução sem testemunho realizado; tal registro não deve ser confundido com uma ação habilitada do jogo que obrigatoriamente possui resultados. Preservar a dinâmica não substitui preservar a guarda.

**Limite herdado:** Condição independente da uniformidade dinâmica.

**Rastreabilidade:** Matemática conhecida; referências B17. Fonte, linha 746: Caderno Científico ETLR(f1), rev14, linha 746 (fonte histórica em acervo privado); [ficha completa](MATRIZ_RASTREABILIDADE_50_RESULTADOS.html#r-P04-2); [auditoria VI05](../edicao_1_0_candidata/AUDITORIA_50_RESULTADOS.html#r-P04-2). Originalidade externa não estabelecida.


### 5.1 Quocientes de transições

<a id="r-P04-1"></a>

### P04.1 — Levantamento por cada representante

**Hipóteses preservadas:** Relações rotuladas fixas; p sobre sua imagem.

**Conclusão do registro:** Uniformidade dos conjuntos de sucessores projetados equivale ao levantamento de todo caminho finito desde cada representante.

Para cada rótulo a, seja R_a⊆X×X. O quociente contém a aresta p(x) —a→ p(y) sempre que xR_a y. Defina S_a(x)={p(y):xR_a y}. A condição S_a(x)=S_a(x') para todos os x,x' da mesma fibra equivale a levantar todo caminho abstrato finito desde qualquer representante inicial fixado.

<a id="prova-P04-1"></a>

**Suficiência.** No comprimento zero use o representante inicial. Dado um levantamento até x_i e a próxima aresta abstrata a_i para a classe c, algum representante da classe atual tem sucessor em c. A igualdade de S_a entre representantes fornece um sucessor de x_i na mesma classe c. Isso estende o caminho. Indução conclui qualquer comprimento finito.

**Necessidade.** Se as assinaturas diferem, existe uma aresta de comprimento um disponível por um representante e indisponível por outro. O caminho abstrato de uma aresta não pode ser levantado desde este último, contrariando a propriedade. Observações saturadas se conservam independentemente pela constância nas fibras. A prova não transporta durações, probabilidades ou proveniência que não foram incluídas nos rótulos/estado.

**Limite herdado:** Não preserva probabilidades, duração nem história ausente do estado.

**Rastreabilidade:** Matemática conhecida; referências B17. Fonte, linha 738: Caderno Científico ETLR(f1), rev14, linha 738 (fonte histórica em acervo privado); [ficha completa](MATRIZ_RASTREABILIDADE_50_RESULTADOS.html#r-P04-1); [auditoria VI05](../edicao_1_0_candidata/AUDITORIA_50_RESULTADOS.html#r-P04-1). Originalidade externa não estabelecida.


<a id="r-P08-4"></a>

### P08.4 — Quociente relacional exato

**Hipóteses preservadas:** Observação constante por fibra e conjuntos de sucessores projetados iguais por rótulo.

**Conclusão do registro:** Levantamento de toda trajetória finita a partir de cada representante.

Suponha a observação O constante por fibra e os conjuntos S_a de P04.1 iguais para cada rótulo. Então toda trajetória finita do quociente levanta-se desde qualquer representante e conserva a sequência de observações.

<a id="prova-P08-4"></a>

**Demonstração.** A construção indutiva de P04.1 escolhe, a cada passo, um sucessor do representante corrente na classe exigida. Constância de O fornece a mesma observação em cada posição. O vazio de sucessores participa da assinatura e impede inventar uma aresta habilitada. A necessidade para o levantamento forte já pertence a P04.1; este resultado conserva a aplicação suficiente às interfaces, sem enfraquecer o antecedente. Guardas, duração e identidade são tarefas adicionais, não consequências da observação.

**Limite herdado:** Não enfraquece P04.1, que também tem necessidade; não conserva guarda por si.

**Rastreabilidade:** Aplicação; referências B17. Fonte, linha 1314: Caderno Científico ETLR(f1), rev14, linha 1314 (fonte histórica em acervo privado); [ficha completa](MATRIZ_RASTREABILIDADE_50_RESULTADOS.html#r-P08-4); [auditoria VI05](../edicao_1_0_candidata/AUDITORIA_50_RESULTADOS.html#r-P08-4). Originalidade externa não estabelecida.


<a id="r-P07-2"></a>

### P07.2 — Sobreaproximação segura

**Hipóteses preservadas:** Imagem relacional e mesmos rótulos; relação abstrata contém essa imagem.

**Conclusão do registro:** Trajetórias concretas se projetam; recíproca pode falhar.

Se ĤR_a contém a imagem de R_a por p, toda trajetória concreta rotulada projeta-se em trajetória de ĤR. A imagem é a menor relação com essa obrigação de inclusão.

<a id="prova-P07-2"></a>

**Demonstração.** Cada passo concreto tem sua imagem em ĤR_a pela hipótese. Repetir o argumento ao longo da trajetória prova a projeção. Qualquer relação que contenha todos os passos projetados contém sua imagem por definição, provando a minimalidade por inclusão. Duas inclusões compatíveis podem ser compostas pela transitividade da inclusão.

**Contramodelo à recíproca.** O intermediário b₀ de uma chegada e o b₁ de uma saída em P02.2 geram um caminho abstrato sem caminho concreto. Assim, ausência no sobreaproximado exclui um comportamento concreto cuja descrição seria conservada, mas presença no sobreaproximado não o realiza. A distribuição de escolhas controláveis e ambientais também não se recupera de arestas unidas.

**Limite herdado:** Presença abstrata não prova realização; ausência pode excluir comportamento compatível com a projeção.

**Rastreabilidade:** Aplicação; referências B03. Fonte, linha 1099: Caderno Científico ETLR(f1), rev14, linha 1099 (fonte histórica em acervo privado); [ficha completa](MATRIZ_RASTREABILIDADE_50_RESULTADOS.html#r-P07-2); [auditoria VI05](../edicao_1_0_candidata/AUDITORIA_50_RESULTADOS.html#r-P07-2). Originalidade externa não estabelecida.


Esses resultados usam estruturas conhecidas de congruência, homomorfismo e equivalência comportamental [B17], além do antecedente de aproximação semântica de Cousot e Cousot [B03]. A terminologia “segura” de uma sobreaproximação significa inclusão de comportamentos concretos projetados. A segurança estratégica de um controlador é outra propriedade, dependente das escolhas e do objetivo. Uma abstração pode conservar todas as arestas e perder quem escolhe cada uma delas.

### 5.2 Fatoração determinista e regimes alternados

<a id="r-P06-4"></a>

### P06.4 — Quociente exato mínimo

**Hipóteses preservadas:** Sistema finito determinista parcial com observação e alfabeto fixos.

**Conclusão do registro:** Única partição mais grosseira conserva observações, definição das operações e futuros.

Considere X finito, alfabeto fixo A, observação O e funções parciais T_a:X⇀X. Uma partição admissível conserva O, definição das operações e bloco sucessor por ação. P₀ agrupa observações iguais; P_{n+1} conserva o bloco anterior e subdivide segundo o vetor de assinaturas: indefinida ou bloco de T_a(x) em P_n. Para executar o procedimento por inspeção de todas as ações, toma-se A finito e suas operações disponíveis. A caracterização abstrata por estabilidade não reivindica um algoritmo efetivo para um alfabeto infinito não apresentado.

<a id="prova-P06-4"></a>

**Demonstração.** Cada passo refina; cada refinamento estrito aumenta o número de blocos, limitado por |X|. A sequência estabiliza em P*. A estabilidade torna as operações parciais bem definidas no quociente e conserva os futuros por indução no comprimento da palavra. Se Q é outra partição admissível, Q refina P₀. Supondo Q refinar P_n, dois estados do mesmo bloco Q têm a mesma habilitação e sucessores no mesmo bloco Q; portanto têm a mesma assinatura por blocos P_n e ficam juntos em P_{n+1}. Assim Q refina cada P_n e P*. Logo P* é a única partição mais grosseira admissível, como equivalência, não como numeração de blocos. Guardas trivalentes, tempo e genealogia ausentes de O não se conservam automaticamente.

**Limite herdado:** Não inclui automaticamente guardas trivalentes, tempo, identidade ou proveniência.

**Rastreabilidade:** Matemática conhecida; referências B06 B17. Fonte, linha 1027: Caderno Científico ETLR(f1), rev14, linha 1027 (fonte histórica em acervo privado); [ficha completa](MATRIZ_RASTREABILIDADE_50_RESULTADOS.html#r-P06-4); [auditoria VI05](../edicao_1_0_candidata/AUDITORIA_50_RESULTADOS.html#r-P06-4). Originalidade externa não estabelecida.


<a id="r-P07-1"></a>

### P07.1 — Fatoração dinâmica e composição

**Hipóteses preservadas:** Operações parciais; projeção sobrejetiva; igualdade de habilitação e classe sucessora por fibra.

**Conclusão do registro:** Quociente único; correspondências exatas compõem; projeção conjunta exata para mesmas ações.

Para funções parciais T_a e p:X→im(p), existe uma única família U_a de operações parciais no quociente que preserva e reflete definição e satisfaz pT_a=U_ap se e somente se cada fibra tem habilitação igual e classe sucessora igual por ação.

<a id="prova-P07-1"></a>

**Demonstração.** Necessidade: a operação U_a não pode atribuir duas definições ou destinos à mesma classe. Suficiência: declare U_a(p(x)) definida exatamente quando T_a(x) está definida e tome seu valor p(T_a(x)); as duas condições garantem independência do representante. A sobrejetividade sobre a imagem dá unicidade. Se q também é exata para a dinâmica obtida, definição se conserva em cadeia e qpT_a=qU_ap=V_aqp, dando composição exata. Se p e q são exatas sobre X para as mesmas ações, j(x)=(p(x),q(x)) é exata: igualdade do par garante ambas as condições e os dois destinos coordenados. A imagem de j é o contradomínio pertinente.

**Precisão EVI03-04.** Este último corolário é determinista. Para relações não deterministas, a igualdade dos conjuntos de cada coordenada pode perder a correlação entre destinos conjuntos; é indispensável verificar nova estabilidade. Nenhum argumento acima conserva história ou identidade não incluídas no contrato.

**Limite herdado:** Não misturar ações distintas nem concluir história ou identidade preservadas.

**Rastreabilidade:** Matemática conhecida; referências B17. Fonte, linha 1091: Caderno Científico ETLR(f1), rev14, linha 1091 (fonte histórica em acervo privado); [ficha completa](MATRIZ_RASTREABILIDADE_50_RESULTADOS.html#r-P07-1); [auditoria VI05](../edicao_1_0_candidata/AUDITORIA_50_RESULTADOS.html#r-P07-1). Originalidade externa não estabelecida.


<a id="r-P07-3"></a>

### P07.3 — Alternância de regimes

**Hipóteses preservadas:** X finito, O fixo, ações A1 e A2, partições mínimas respectivas.

**Conclusão do registro:** Partição mínima da união refina a interseção; igualdade exatamente se interseção estável.

Fixe o mesmo X finito e O. Se P₁,P₂ são os mínimos deterministas para alfabetos A₁,A₂ e P* o mínimo para A₁∪A₂, então P* refina a interseção J das equivalências P₁,P₂. Há igualdade exatamente quando J é estável para a união.

<a id="prova-P07-3"></a>

**Demonstração.** Toda partição admissível para a união é admissível para cada alfabeto, logo refina ambos os mínimos, por P06.4. Em particular P* refina J. Se J é estável, conserva O e todas as ações, sendo admissível; a minimalidade de P* implica que J refina P*. As inclusões das equivalências dão igualdade. A recíproca segue da estabilidade de P*.

**Contramodelo.** X={a,b,c,d}, O=(0,0,1,1). A envia a,b,c,d a c,d,c,c; B envia-os a a,a,a,d. Para A, o mínimo é {{a,b},{c,d}}. Para B é {{a,b},{c},{d}}. A interseção é a segunda partição, mas A leva a e b a blocos distintos. A palavra A;B distingue a de b, e o mínimo da união tem quatro classes. As contagens 2,3,4 resultam desses testes de estabilidade. A união permite alternância arbitrária rotulada; proibir certas mudanças exige um monitor de regime.

**Limite herdado:** Alternância livre rotulada; restrições de regime exigem monitor próprio.

**Rastreabilidade:** Integração interna; referências B06 B17. Fonte, linha 1105: Caderno Científico ETLR(f1), rev14, linha 1105 (fonte histórica em acervo privado); [ficha completa](MATRIZ_RASTREABILIDADE_50_RESULTADOS.html#r-P07-3); [auditoria VI05](../edicao_1_0_candidata/AUDITORIA_50_RESULTADOS.html#r-P07-3). Originalidade externa não estabelecida.


Refinar observações, guardas ou alfabetos sob as mesmas regras adiciona obrigações e pode exigir mais classes. Mudar a dinâmica não tem uma monotonicidade geral comparável. A representação conjunta de duas vistas só recebe o corolário de P07.1 quando ambas conservam as mesmas ações deterministas. No caso não determinista, a precisão EVI03-04, demonstrada em PVI02.4, exige estabilidade adicional das correlações entre destinos.

## 6. Campos, memória e transformação das condições de passagem

O campo de possíveis, o conjunto admissível e as relações ativas não se identificam. Pode haver uma oferta não admitida; uma permissão sem ocorrência; uma ocorrência sem alteração da manifestação. Um campo pode ser descrito como parte do estado enriquecido ou como regime que altera regras, desde que o contrato esclareça a escolha. A informação necessária à próxima operação é relativa ao objetivo: nem toda revisão requer história integral, mas a proveniência pode requerer mais que um estado suficiente à previsão.

<a id="r-P05-1"></a>

### P05.1 — Contração conjuntiva

**Hipóteses preservadas:** Universo e restrições fixos; A contido em B.

**Conclusão do registro:** J(B) contido em J(A).

Seja I₀ um universo fixo e C_i⊆I₀ restrições fixas. Para índices ativos A, defina J(A)=⋂_{i∈A}C_i, entendendo J(∅)=I₀. Se A⊆B, então J(B)⊆J(A).

<a id="prova-P05-1"></a>

**Demonstração.** Cada candidato de J(B) satisfaz todas as restrições de B e, em particular, todas as de A. Pertence, portanto, a J(A). A inclusão pode ser igualdade se as novas restrições forem redundantes. O argumento depende de universo e conteúdo fixos; não descreve automaticamente uma revisão que também modifica as próprias regras.

**Limite herdado:** Não exige contração estrita; mudança de universo ou conteúdo invalida inferência automática.

**Rastreabilidade:** Matemática conhecida; referências B03. Fonte, linha 873: Caderno Científico ETLR(f1), rev14, linha 873 (fonte histórica em acervo privado); [ficha completa](MATRIZ_RASTREABILIDADE_50_RESULTADOS.html#r-P05-1); [auditoria VI05](../edicao_1_0_candidata/AUDITORIA_50_RESULTADOS.html#r-P05-1). Originalidade externa não estabelecida.


<a id="r-P05-2"></a>

### P05.2 — Reabertura exata

**Hipóteses preservadas:** Restrições conjuntivas fixas; D subconjunto dos índices ativos A.

**Conclusão do registro:** Retornam exatamente candidatos com conjunto não vazio de bloqueadores contido em D.

Mantenha as condições de P05.1. Para x∈I₀, defina os bloqueadores ativos B_A(x)={i∈A:x∉C_i}. Retirando D⊆A, os candidatos que retornam são exatamente aqueles com ∅≠B_A(x)⊆D.

<a id="prova-P05-2"></a>

**Demonstração.** Estar fora de J(A) equivale a ter ao menos um bloqueador em A. Estar em J(A\D) equivale a não possuir bloqueador fora de D. As duas condições juntas equivalem a ter conjunto não vazio de bloqueadores, todo ele removido por D. Isso caracteriza precisamente J(A\D)\J(A). Restrições iguais em conteúdo podem ter origens e IDs distintos: retirar uma delas não retira a outra. Não se trata de uma teoria de revisão geral com regras interdependentes.

**Limite herdado:** Não é revisão geral de crenças ou regras interdependentes.

**Rastreabilidade:** Aplicação; referências B03. Fonte, linha 875: Caderno Científico ETLR(f1), rev14, linha 875 (fonte histórica em acervo privado); [ficha completa](MATRIZ_RASTREABILIDADE_50_RESULTADOS.html#r-P05-2); [auditoria VI05](../edicao_1_0_candidata/AUDITORIA_50_RESULTADOS.html#r-P05-2). Originalidade externa não estabelecida.


<a id="r-P06-1"></a>

### P06.1 — Insuficiência de J para revisão

**Hipóteses preservadas:** M1; p(A)=J(A); retirar C2 admitido em {2} e {1,2}.

**Conclusão do registro:** Não há atualização determinista da observação para essa retirada.

No M1, I₀={a,b,c}, C₁={a,b}, C₂={a}. Os quatro estados são os subconjuntos ativos de {1,2}. A observação é J(A). Ativar regra já ativa e retirar regra inativa são operações indefinidas neste fragmento.

<a id="prova-P06-1"></a>

**Demonstração.** A={2} e B={1,2} têm a mesma observação {a}. Retirar 2 é definido em ambos; depois da retirada, suas observações são I₀ e {a,b}, respectivamente. Uma atualização determinista baseada só em J teria de atribuir duas respostas diferentes à mesma entrada. Portanto não existe tal atualização. Os demais pares de estados já têm observações diferentes; separar A e B produz quatro classes e torna todas as operações bem definidas. Quatro classes são necessárias e suficientes nesse contrato. A sequência ∅,{1},{1,2},{1} produz cardinalidades 3,2,1,2. O resumo de bloqueadores pertinentes pode resolver a revisão; proveniência integral continua outra obrigação.

**Limite herdado:** Exige memória de bloqueadores pertinente; não necessariamente história integral.

**Rastreabilidade:** Aplicação; referências B06 B17. Fonte, linha 994: Caderno Científico ETLR(f1), rev14, linha 994 (fonte histórica em acervo privado); [ficha completa](MATRIZ_RASTREABILIDADE_50_RESULTADOS.html#r-P06-1); [auditoria VI05](../edicao_1_0_candidata/AUDITORIA_50_RESULTADOS.html#r-P06-1). Originalidade externa não estabelecida.


<a id="r-P05-3"></a>

### P05.3 — Campo omitido

**Hipóteses preservadas:** Mesma projeção local e sucessores projetados distintos sob sonda comum.

**Conclusão do registro:** Projeção local viola P04.1; guardas distintas violam P04.2.

Enriqueça o estado como (x,F), com estado local x e campo pertinente F. Se uma mesma sonda a, admitida no contrato comparado, produz conjuntos distintos de sucessores locais projetados em (x,F₀) e (x,F₁), apagar F viola a uniformidade de P04.1. Se as guardas diferem, viola P04.2.

<a id="prova-P05-3"></a>

**Demonstração.** Os dois estados enriquecidos estão na mesma fibra local, mas têm assinaturas diferentes; a necessidade de P04.1 dá a primeira conclusão. Valores distintos da guarda na mesma fibra dão a segunda por P04.2. Representar a alteração de campo como mudança de estado enriquecido pode recuperar informação suficiente. Isso não transforma toda alteração de campo em individuação nem prova que o campo representado esgote a espacialidade do fenômeno.

**Limite herdado:** Mudança de campo no estado enriquecido não prova individuação.

**Rastreabilidade:** Aplicação; referências B17. Fonte, linha 894: Caderno Científico ETLR(f1), rev14, linha 894 (fonte histórica em acervo privado); [ficha completa](MATRIZ_RASTREABILIDADE_50_RESULTADOS.html#r-P05-3); [auditoria VI05](../edicao_1_0_candidata/AUDITORIA_50_RESULTADOS.html#r-P05-3). Originalidade externa não estabelecida.


### 6.1 Sondas, regimes e limites da redução

<a id="r-P06-2"></a>

### P06.2 — Observabilidade relativa

**Hipóteses preservadas:** M2 finito; O=(b,q); ações L,R fixas.

**Conclusão do registro:** 8 classes; com ação Q1, 12 classes.

No M2, x=(m,b,q), m∈{0,1,2}, b,q∈{0,1}. L(x)=(min(m+1,2),b,q). R(x)=(m,1 se q=1 e m=1, senão 0,q). A observação é O=(b,q); as operações são L,R.

<a id="prova-P06-2"></a>

**Demonstração.** Em q=0, L não muda b e R fixa b=0, independentemente de m. Indução sobre palavras mostra que todos os m com o mesmo b são indistinguíveis: duas classes nesse regime. Em q=1, R distingue m=1 dos outros. L;R distingue m=0 de m=2, pois leva o primeiro a m=1 com resposta 1 e o segundo permanece em 2 com resposta 0. Valores diferentes de b ou q já diferem em O. Logo há seis classes em q=1 e duas em q=0: oito ao todo. Acrescentando Q1(m,b,q)=(m,b,1), qualquer diferença em m antes oculta pode ser exposta a R ou L;R; todas as doze configurações tornam-se distinguíveis. A inacessibilidade depende das sondas e do ambiente, não de uma impossibilidade ontológica geral.

**Limite herdado:** Classes dependem do alfabeto e ambiente; não são indivíduos.

**Rastreabilidade:** Aplicação; referências B06. Fonte, linha 1004: Caderno Científico ETLR(f1), rev14, linha 1004 (fonte histórica em acervo privado); [ficha completa](MATRIZ_RASTREABILIDADE_50_RESULTADOS.html#r-P06-2); [auditoria VI05](../edicao_1_0_candidata/AUDITORIA_50_RESULTADOS.html#r-P06-2). Originalidade externa não estabelecida.


<a id="r-P06-3"></a>

### P06.3 — Limite de redução em M3

**Hipóteses preservadas:** Regime η=1 fixo, entradas conhecidas, paridade preservada, previsão determinista de todos os futuros.

**Conclusão do registro:** Oito estados precisam ser distinguidos; η=0 admite duas classes.

No M3, x=(a,b,c)∈{0,1}³, entrada conhecida u∈{0,1}, T_η(x,u)=(b,c,a⊕u⊕(η∧b)) e z=a⊕b⊕c. O regime η é fixo durante a previsão.

<a id="prova-P06-3"></a>

**Demonstração.** Para η=0, z'=z⊕u. Duas classes, uma para cada paridade, bastam e são necessárias para conservar z. Para η=1, z₁=z₀⊕u₀⊕b e z₂=z₁⊕u₁⊕c. Portanto b=z₀⊕z₁⊕u₀, c=z₁⊕z₂⊕u₁ e a=z₀⊕b⊕c. A trajetória das três paridades com entradas conhecidas recupera univocamente o estado inicial. Se dois estados distintos tivessem a mesma representação determinista suficiente para todos esses futuros, ela produziria as mesmas paridades, contradizendo essa recuperação. Oito classes são necessárias; a identidade é suficiente.

Variar η ocultamente ou omitir as entradas altera as premissas. O resultado é de cardinalidade de representação, sem inferência de dimensão física ou número de indivíduos.

**Limite herdado:** Cardinalidade de representação, não dimensão física ou emergência.

**Rastreabilidade:** Aplicação; referências B06. Fonte, linha 1014: Caderno Científico ETLR(f1), rev14, linha 1014 (fonte histórica em acervo privado); [ficha completa](MATRIZ_RASTREABILIDADE_50_RESULTADOS.html#r-P06-3); [auditoria VI05](../edicao_1_0_candidata/AUDITORIA_50_RESULTADOS.html#r-P06-3). Originalidade externa não estabelecida.


<a id="r-P08-5"></a>

### P08.5 — Habilitação dinâmica

**Hipóteses preservadas:** Modelo J/N; preservar O=(a,b) e definição de J.

**Conclusão do registro:** Oito classes necessárias e suficientes; p=(a,b) insuficiente.

No modelo J/N, (a,b,g)∈{0,1}³, O=(a,b). J(a,b,1)=(a,b⊕a,0) e J é indefinida em g=0; N(a,b,g)=(a,b,1).

<a id="prova-P08-5"></a>

**Demonstração.** Para cada par (a,b), os estados com g=0 e g=1 têm a mesma observação e habilitações diferentes de J. Precisam ser separados. Pares (a,b) distintos já diferem na observação. Todas as oito configurações precisam, portanto, de classes distintas; a identidade as representa exatamente, provando suficiência. J(0,0,1)=(0,0,0) mostra mudança da habilitação sem mudança local observada. Em g=0, J após N é definida e N após J não é. Isso distingue ordem temporal e reagrupamento lógico, sem provar criação material de portas ou individuação.

**Limite herdado:** Portas fixas; não prova criação material de fronteira.

**Rastreabilidade:** Aplicação; referências B06 B17. Fonte, linha 1344: Caderno Científico ETLR(f1), rev14, linha 1344 (fonte histórica em acervo privado); [ficha completa](MATRIZ_RASTREABILIDADE_50_RESULTADOS.html#r-P08-5); [auditoria VI05](../edicao_1_0_candidata/AUDITORIA_50_RESULTADOS.html#r-P08-5). Originalidade externa não estabelecida.


M1, M2 e M3 compartilham o critério de suficiência dinâmica, sem compartilhar a mesma lei de domínio. M1 preserva origem de restrições para revisar interpretações; M2 explicita o papel das sondas e do ambiente na observabilidade; M3 mostra que o regime relacional pode exigir todas as distinções do estado. Os números de classes são resultados dessas tarefas sintéticas. Não medem emergência, número de indivíduos ou dimensão física.

Uma mudança de habilitação, como a de J/N, representa transformação das condições da próxima participação. A porta já estava prevista na assinatura; não se demonstrou criação de uma nova interface material. Em CAL-01, a distinção entre E+T e T+E, ou E+I e I+E, permanece uma pergunta de referência e operação. A não comutatividade de L e R num modelo não decide a semântica do + protegido.

## 7. Individuação, participação e identidade

A organização candidata G_c=(M_G,R_G,∂_cG,P_G,H_G,ι_G) reúne participantes, relações, fronteira, participação, história e política de identidade. Essa descrição dá um lugar para registrar critérios, sem demonstrar que o conjunto descrito constitua um indivíduo. Reconhecer organização exige uma referência; justificar individuação exige algo além da nomeação.

| Critério candidato | Conteúdo que deve ser especificado | Limite preservado |
|---|---|---|
| IO-01 / IO01 — constituição | Predicado K_c, dependências, ambiente e intervenções admissíveis | Conectividade ou dependência cruzada sozinha não prova necessidade constitutiva |
| IO-02 / IO02 — fronteira | Portas, tipos, acesso, intercâmbio e alterações possíveis | Contorno ou lista de membros não prova produção da fronteira |
| IO-03 / IO03 — identidade | Política ι_c, correspondência, duplicação, fusão e exclusividade | Mesmo estado, nome ou função não decide identidade histórica |
| IO-04 / IO04 — continuidade | Horizonte, acontecimentos, tolerâncias e interrupções | Fotografias inicial/final podem omitir ruptura |
| IO-05 / IO05 — participação externa | Entradas, respostas, guardas, durações e classe ambiental | Capacidade admissível difere de participação realizada |

Uma avaliação operacional pode usar satisfeito, violado e indeterminado. A conjunção é violada se algum critério é violado, satisfeita se todos o são, e indeterminada nos demais casos. São 243 combinações: uma satisfeita, 211 violadas e 31 indeterminadas. A tabela é uma regra de avaliação; não fornece evidência para preencher os critérios. Sua suficiência para o predicado Ind_op é definicional, enquanto sua adequação ao fenômeno permanece uma obrigação independente.

### 7.1 Sincronização e mudanças invisíveis

<a id="r-P09-1"></a>

### P09.1 — Invisibilidade de mudança constitutiva

**Hipóteses preservadas:** Modelos C/I com paridade; trocas arbitrárias e entradas conhecidas.

**Conclusão do registro:** Toda história de regimes dá z_n=z_0 XOR entradas; trocas invisíveis.

Sejam T_C(a,b;u)=(b,a⊕u), T_I(a,b;u)=(a⊕u,b) e α(a,b)=a⊕b. Escolha qualquer sequência de regimes m_t∈{C,I}, entradas conhecidas u_t e atualize x_{t+1}=T_{m_t}(x_t;u_t). Então z_n=α(x_n)=z₀⊕u₀⊕…⊕u_{n−1}, qualquer que seja a história dos regimes.

<a id="prova-P09-1"></a>

**Demonstração.** Substituir as duas regras dá α(T_C(x;u))=α(T_I(x;u))=α(x)⊕u. A fórmula vale para n=0. Se vale em n, a próxima regra, qualquer que seja, acrescenta somente u_n por XOR; a indução conclui. Assim uma história sempre C e outra com mudança C→I são indistinguíveis em z,u em todos os horizontes, embora as dependências das coordenadas sejam diferentes. A observação micro ou outra intervenção pode discriminar os regimes. Não se conclui que toda secção seja invisível nem que toda mudança de regime encerre identidade.

**Limite herdado:** Não diz que toda secção é invisível nem que não há intervenção informativa.

**Rastreabilidade:** Integração interna; referências B03 B17. Fonte, linha 1629: Caderno Científico ETLR(f1), rev14, linha 1629 (fonte histórica em acervo privado); [ficha completa](MATRIZ_RASTREABILIDADE_50_RESULTADOS.html#r-P09-1); [auditoria VI05](../edicao_1_0_candidata/AUDITORIA_50_RESULTADOS.html#r-P09-1). Originalidade externa não estabelecida.


Sincronia não é sinônimo de atração, estabilidade ou dependência cruzada. Em U(a,b;u)=(a⊕u,b⊕u), a diferença a⊕b é invariante: estados iguais permanecem iguais, mas estados diferentes não convergem. Em D(a,b;u)=(u,u), todos chegam à diagonal em um passo sem dependência cruzada direta nas coordenadas anteriores. Um mediador ambiental pode, por outro lado, realizar uma via A_t→e_{t+1}→B_{t+2} sem aresta direta A_t→B_{t+1}. Classificar o mediador como externo não elimina a dependência. Interpretar uma intervenção como causal exige admissibilidade e modularidade próprias, além das equações estipuladas.

### 7.2 Transporte, genealogia e continuidade

<a id="r-P09-2"></a>

### P09.2 — Transporte por papéis

**Hipóteses preservadas:** Mapas q_t e transferências comutam; contratos, K e eventos conservados.

**Conclusão do registro:** Trajetória de papéis preservada sob evoluções/substituições, mesmo sem tokens originais.

Em cada realização t, sejam S_t o conjunto de estados, q_t:S_t→Z uma projeção de papéis, F_t a evolução, F̄ a evolução comum e r_t:S_t→S_{t+1} a transferência durante substituição. Exija q_tF_t(x,u)=F̄(q_t(x),u), quando permitido, e q_{t+1}r_t(x)=q_t(x). Guardas, respostas e durações fatoram com o mesmo contrato; o predicado constitutivo K_t é K̄∘q_t inclusive nas transferências; os eventos são registrados.

<a id="prova-P09-2"></a>

**Demonstração.** Um evento de evolução conserva a trajetória abstrata pela primeira igualdade e os dados de interface pelas fatorações. Um evento de substituição conserva o estado de papéis pela segunda igualdade e K pela hipótese específica de transferência. Indução sobre a sequência finita de eventos conserva todo o contrato. A prova não usa a interseção dos conjuntos de componentes inicial e final. Portanto substituição total é compatível com conservação operacional, desde que valores, conexões e obrigações sejam efetivamente transportados.

Mapas q_t constantes só preservam contratos triviais e não justificam sua pertinência. O certificado não demonstra realizabilidade física de r_t nem decide identidade ontológica; esta continua dependente da política e de evidência histórica.

**Limite herdado:** Suficiente para contrato; realizabilidade da transferência e identidade ontológica não provadas.

**Rastreabilidade:** Aplicação; referências B09 B17. Fonte, linha 1680: Caderno Científico ETLR(f1), rev14, linha 1680 (fonte histórica em acervo privado); [ficha completa](MATRIZ_RASTREABILIDADE_50_RESULTADOS.html#r-P09-2); [auditoria VI05](../edicao_1_0_candidata/AUDITORIA_50_RESULTADOS.html#r-P09-2). Originalidade externa não estabelecida.


<a id="r-P09-3"></a>

### P09.3 — Identidade exclusiva e rastreamento

**Hipóteses preservadas:** Identidade como equivalência; para rastreamento, populações finitas de igual tamanho sem nascimentos/mortes.

**Conclusão do registro:** Duas filhas distintas não ambas idênticas à mãe; rastreamento completo/único equivale a emparelhamento perfeito/único.

Suponha que a identidade numérica ≡ seja uma equivalência. Se G≡B e G≡C, então B≡C. Logo duas filhas numericamente distintas não podem ambas ser idênticas à mesma mãe sob esse critério.

<a id="prova-P09-3"></a>

**Demonstração.** Simetria fornece B≡G; transitividade com G≡C fornece B≡C. Uma genealogia pode, porém, registrar G→B e G→C sem atribuir identidade a nenhuma das filhas. Continuidade ramificada requer uma relação diferente dessa equivalência exclusiva.

Para populações consecutivas finitas do mesmo tamanho, sem nascimentos ou mortes, forme o grafo bipartido de correspondências elegíveis. Se rastreamento completo significa bijeção elegível entre populações, existe rastreamento completo exatamente quando existe emparelhamento perfeito; é único exatamente quando esse emparelhamento é único. **Demonstração:** as arestas da bijeção cobrem cada vértice uma vez, que é a definição de emparelhamento perfeito; o argumento inverso e a unicidade seguem da mesma correspondência. No grafo completo 2×2 há dois emparelhamentos. A elegibilidade exige evidência anterior; o algoritmo não a produz. Fusões, fissões, mortes e nascimentos precisam de eventos adicionais.

**Limite herdado:** Elegibilidade requer evidência prévia; não resolve política universal de identidade.

**Rastreabilidade:** Matemática conhecida; prova elementar autônoma por equivalência e pela definição de emparelhamento. B17 é mantido no histórico da matriz, mas não localiza este argumento de identidade ou emparelhamento e não é apoio bibliográfico específico. Fonte, linha 1718: Caderno Científico ETLR(f1), rev14, linha 1718 (fonte histórica em acervo privado); [ficha completa](MATRIZ_RASTREABILIDADE_50_RESULTADOS.html#r-P09-3); [auditoria VI05](../edicao_1_0_candidata/AUDITORIA_50_RESULTADOS.html#r-P09-3). Originalidade externa não estabelecida.


Semelhança local pode falhar em transitividade. Os conjuntos {a,b}, {b,c} e {c,d} têm sobreposição de Jaccard 1/3 entre vizinhos e zero entre extremos. O limiar 1/3 não define identidade como equivalência. Tomar seu fecho transitivo modifica o critério e passa a unir extremos antes rejeitados. Uma política histórica pode permitir deriva; isso precisa ser declarado em vez de ser confundido com semelhança instantânea.

### 7.3 Contratos temporizados e detectabilidade

<a id="r-P09-4"></a>

### P09.4 — Contrato temporizado exato

**Hipóteses preservadas:** Sistema determinista com guarda P/N/?; resposta e duração positiva consultadas sob P; interface restrita.

**Conclusão do registro:** Contrato abstrato existe exatamente se guarda, resposta, duração e classe sucessora constantes nas fibras; histórias finitas adaptativas conservadas.

Considere entradas u, guarda g(x,u)∈{P,N,?}, e, somente sob g=P, sucessor determinista F(x,u), resposta O(x,u) e duração positiva τ(x,u). Seja p sobrejetiva sobre sua imagem. Um contrato abstrato exato existe se e somente se, para todo u e x,y da mesma fibra, g(x,u)=g(y,u) e, quando P, O(x,u)=O(y,u), τ(x,u)=τ(y,u), pF(x,u)=pF(y,u).

<a id="prova-P09-4"></a>

**Demonstração.** Se o contrato existe, cada grandeza é função da classe e da entrada; as igualdades seguem por substituição. Reciprocamente, escolha um representante de cada classe. A igualdade das guardas determina o domínio das funções executáveis; as demais igualdades tornam seus valores independentes do representante. Isso define o contrato em toda a imagem de p.

Para o mesmo interlocutor determinista inicial, escolhendo entradas apenas da história visível, prove por indução: histórias iguais levam à mesma próxima entrada; o contrato dá a mesma guarda e, sob P, resposta, duração e próxima classe. Portanto toda interação finita é conservada. Recusas temporizadas, espera e relógio absoluto só estão cobertos se fazem parte dos observáveis. Duração positiva por passo não exclui Zeno na classe geral: a soma de 2^{-n} é finita. Esse exemplo pressupõe permitir durações variáveis ao longo de infinitos passos; não afirma Zeno em um sistema de estados e entradas finitos com função de duração fixa e estritamente positiva, onde o conjunto finito de durações executáveis tem mínimo positivo. O teorema não afirma preservação de concorrência, informação oculta adicional ou dinâmica probabilística.

**Limite herdado:** Não vale automaticamente para observação oculta adicional, informação parcial, concorrência ou Zeno.

**Rastreabilidade:** Integração interna; referências B15 B17. Fonte, linha 1748: Caderno Científico ETLR(f1), rev14, linha 1748 (fonte histórica em acervo privado); [ficha completa](MATRIZ_RASTREABILIDADE_50_RESULTADOS.html#r-P09-4); [auditoria VI05](../edicao_1_0_candidata/AUDITORIA_50_RESULTADOS.html#r-P09-4). Originalidade externa não estabelecida.


<a id="r-P09-5"></a>

### P09.5 — Detectabilidade de secção

**Hipóteses preservadas:** Projeção de histórias p_H e diagnóstico σ definido.

**Conclusão do registro:** Detector exato existe se e somente se σ constante nas fibras.

Para histórias h, observação p_H(h) e diagnóstico definido σ(h), há detector exato d com σ=d∘p_H se e somente se σ é constante nas fibras de p_H.

<a id="prova-P09-5"></a>

**Demonstração.** Aplicar P08.3 ao conjunto de histórias fornece as duas direções: substituir observações iguais prova necessidade; definir d pelo valor comum de σ prova suficiência. Vale também para diagnósticos com três valores definidos, preservando ?. Isso não revela uma verdade binária subjacente ao desconhecimento.

**Contramodelo.** Nas histórias C/I de P09.1, tome σ como ocorrência de C→I sob uma política que distingue tal alteração. Uma história sempre C e outra com troca têm a mesma observação de paridades e entradas e diagnósticos diferentes. Não há detector exato com esse acesso. Maior horizonte não resolve essa perda estrutural, embora nova observação possa resolvê-la.

**Limite herdado:** Predicado de secção é estipulado; ? não descobre verdade subjacente.

**Rastreabilidade:** Aplicação; referências B17. Fonte, linha 1805: Caderno Científico ETLR(f1), rev14, linha 1805 (fonte histórica em acervo privado); [ficha completa](MATRIZ_RASTREABILIDADE_50_RESULTADOS.html#r-P09-5); [auditoria VI05](../edicao_1_0_candidata/AUDITORIA_50_RESULTADOS.html#r-P09-5). Originalidade externa não estabelecida.


<a id="r-P09-6"></a>

### P09.6 — Limite de horizonte

**Hipóteses preservadas:** Classe de máquinas finitas sem limite superior conhecido de estados.

**Conclusão do registro:** Para todo H há máquinas iguais nos H primeiros passos e distintas no seguinte.

Na classe das máquinas deterministas finitas sem teto conhecido para o número de estados, para todo H natural existem M_H,N_H cujas primeiras H saídas coincidem e cuja saída H+1 difere.

<a id="prova-P09-6"></a>

**Demonstração construtiva.** M_H emite sempre zero. N_H tem contador k∈{0,…,H+1}, inicialmente zero, atualiza k'=min(k+1,H+1) e emite 1 exatamente quando k'>H. Ignorando entradas, as primeiras H saídas são zero e a seguinte é um. As máquinas são finitas para cada H, inclusive H=0. O quantificador é ∀H∃M_H,N_H, e não um mesmo par que permanece indistinguível em todos os horizontes finitos e depois diverge. Para um par finito conhecido com regras e estados acessíveis, análise completa pode decidir equivalência. O resultado limita certificação por um teste de horizonte fixo numa classe sem limite conhecido.

**Limite herdado:** Não impede equivalência decidível numa classe finita conhecida.

**Rastreabilidade:** Aplicação; referências B06. Fonte, linha 1825: Caderno Científico ETLR(f1), rev14, linha 1825 (fonte histórica em acervo privado); [ficha completa](MATRIZ_RASTREABILIDADE_50_RESULTADOS.html#r-P09-6); [auditoria VI05](../edicao_1_0_candidata/AUDITORIA_50_RESULTADOS.html#r-P09-6). Originalidade externa não estabelecida.


Uma secção é investigada como evento situado capaz de alterar constituição, fronteira ou continuidade sob política declarada. Dividir um desenho, trocar uma partição ou perder exatidão de uma projeção não constitui, sozinho, tal evento. Mudança de regime, ruptura, reorganização com identidade e produção de descendentes são alternativas que podem coexistir conforme critérios e domínio. Um resultado indeterminado preserva a pergunta; não autoriza inventar a história faltante.

## 8. Sustentação, recursos e recuperação

Persistência passiva, manutenção externa, automanutenção, autorregulação, reparação e autogeração são propriedades distinguíveis. Uma organização pode manter estado porque as condições pouco se degradam, porque o ambiente as repõe ou porque processos atribuídos a ela as renovam. Feedback pode regular um desvio sem renovar sensor ou atuador. Reparação pode restituir função após violação de uma condição constitutiva, sem conservar continuidade ininterrupta.

A autogeração organizacional candidata designa produção ou renovação de condições que habilitam processos, fronteira e organização, com origem e continuidade examináveis. Convém distinguir reposição parcial, renovação de um inventário declarado e a tese forte de suficiência desse inventário para individuação ou autonomia. Os dois primeiros níveis são representáveis nos modelos; não demonstram o terceiro. Autorreprodução, que produz outra organização candidata com genealogia própria, é outra questão.

As responsabilidades históricas AS-01–08 e AR-01–10 permanecem candidatas: contexto, inventário constitutivo, dependência efetiva, perda e reposição, participação ambiental, proveniência, identidade, continuidade, recuperabilidade e distinção entre regras e suportes. Este volume não as transforma em leis necessárias de toda organização. Sua função é exigir que cada aplicação diga o que perde, o que produz e de que condições depende.

### 8.1 Segurança robusta e reposição

<a id="r-P10-1"></a>

### P10.1 — Núcleo robusto de viabilidade

**Hipóteses preservadas:** Jogo finito totalmente observado; controle antes de distúrbio; ações e sucessores não vazios.

**Conclusão do registro:** Predecessor iterado caracteriza segurança em n passos; maior ponto fixo permite política estacionária segura.

Em um jogo finito, o controlador observa x, escolhe u∈A(x) e o ambiente escolhe (x',ℓ)∈D(x,u). Toda ação habilitada tem D não vazio. Defina CPre(Z)={x:∃u∈A(x), D(x,u)≠∅ e todo resultado tem x'∈Z}. Para segurança V, W₀=V e W_{n+1}=V∩CPre(W_n).

<a id="prova-P10-1"></a>

**Demonstração.** Para zero passos, basta estar em V. Para n+1, a primeira ação deve levar todos os resultados a estados dos quais uma continuação garante n passos. Isso prova suficiência concatenando as políticas, e necessidade examinando o primeiro movimento de qualquer política garantidora. A monotonicidade de CPre dá uma sequência decrescente. No finito, há no máximo |V| remoções estritas. No ponto fixo W*, escolha uma ação testemunha em cada estado; indução mantém toda execução em W*, dando uma política estacionária. Qualquer conjunto preservável C⊆V fica contido em cada W_n por indução e, portanto, em W*. Isso prova maximalidade e caracterização.

**Contramodelo de ordem.** Se u,d∈{0,1} e o resultado é seguro exatamente quando u=d, ∀d∃u é verdadeiro e ∃u∀d é falso. Observar d antes de escolher u muda o jogo. Remover resultados inseguros antes de calcular CPre também muda a garantia. Estados ocultos que exigem ações opostas impedem transferir automaticamente a prova à informação parcial.

**Limite herdado:** Ordem ∃u∀d indispensável; não transfere a controle por interface parcial.

**Rastreabilidade:** Matemática conhecida; referências B05 B07. Fonte, linha 1995: Caderno Científico ETLR(f1), rev14, linha 1995 (fonte histórica em acervo privado); [ficha completa](MATRIZ_RASTREABILIDADE_50_RESULTADOS.html#r-P10-1); [auditoria VI05](../edicao_1_0_candidata/AUDITORIA_50_RESULTADOS.html#r-P10-1). Originalidade externa não estabelecida.


<a id="r-P10-2"></a>

### P10.2 — Reposição entre danos em S

**Hipóteses preservadas:** M10/S inicial 11; regras booleanas originais.

**Conclusão do registro:** Permanência b=1 em todos os prefixos se e somente se há reposição entre danos sucessivos.

No modelo S, b,r,q,d∈{0,1}, S(b,r;q,1)=(r,0), S(b,r;q,0)=(b,r∨(b∧q)), inicialmente (b,r)=(1,1). O evento de reposição é (q,d)=(1,0). A palavra ambiental conserva b=1 em todos os prefixos exatamente quando há reposição entre quaisquer dois danos sucessivos.

<a id="prova-P10-2"></a>

**Suficiência.** A reserva inicial protege o primeiro dano, que consome r. Enquanto não há dano, b é preservado; uma reposição com b=1 restaura r. A hipótese assegura reserva antes de cada próximo dano. Indução sobre os danos mantém b.

**Necessidade.** Se um par de danos sucessivos não possui reposição intermediária e b já caiu, a propriedade falhou. Caso contrário, o primeiro dano zera r; nenhum evento intermediário a repõe e o segundo força b'=0. Portanto tal par é incompatível com segurança de todos os prefixos. O argumento cobre palavras finitas e infinitas, pois cada dano tem posição finita. A regra não usa q no mesmo passo do dano. Outras reservas ou reposição externa mudam a necessidade; a conclusão não é universal.

**Limite herdado:** Necessidade específica para uma reserva e condição inicial; dano não usa q no mesmo passo.

**Rastreabilidade:** Aplicação; referências B11 B12. Fonte, linha 2019: Caderno Científico ETLR(f1), rev14, linha 2019 (fonte histórica em acervo privado); [ficha completa](MATRIZ_RASTREABILIDADE_50_RESULTADOS.html#r-P10-2); [auditoria VI05](../edicao_1_0_candidata/AUDITORIA_50_RESULTADOS.html#r-P10-2). Originalidade externa não estabelecida.


<a id="r-P10-3"></a>

### P10.3 — Balanços e renovação necessária

**Hipóteses preservadas:** Reserva sem teto e ingresso antes da demanda; para parte b, perda líquida obrigatória ε>0, estoque finito.

**Conclusão do registro:** Sobrevivência equivale a todos os balanços prefixais não negativos; produção interna necessária sob déficit externo persistente.

Para reserva sem teto, r₀≥0, ingresso q_t≥0 antes da demanda d_t≥0 e falha na primeira reserva negativa, r_{t+1}=r_t+q_t−d_t enquanto viável. A sobrevivência até n equivale a Σ_{t<k}d_t≤r₀+Σ_{t<k}q_t para todo k≤n.

<a id="prova-P10-3"></a>

**Demonstração.** Somar as recorrências até k dá r_k=r₀+Σq−Σd. Se todos os prefixos são não negativos, não há primeira falha. Se algum é negativo, o primeiro deles foi calculado após prefixos executáveis e constitui falha. Saldo final ou média não substituem o critério. Com reserva zero, demanda 1 antes de ingresso 2 no passo seguinte, o saldo final positivo chega tarde demais. Com teto R, a recorrência passa a min(R,r+q)−d e perdas por saturação exigem outra contabilidade.

Para uma condição v com v_{t+1}=v_t+p_int(t)+p_ext(t)−ℓ(t), suponha v(t₀) finito e perda líquida ℓ−p_ext≥ε>0 após t₀. Se p_int é zero daí em diante, somar dá v(t₀+n)≤v(t₀)−nε, negativo para n>v(t₀)/ε. Continuidade ilimitada exige reposição interna suficiente para cobrir déficits em todos os prefixos. Perda nula ou reposição externa suficiente são contramodelos à necessidade irrestrita de produção interna. Produção necessária sob essas premissas ainda não prova autogeração forte.

**Limite herdado:** Saldo final/média não bastam; teto e saturação exigem outra recorrência.

**Rastreabilidade:** Aplicação; referências B12 B15. Fonte, linha 2041: Caderno Científico ETLR(f1), rev14, linha 2041 (fonte histórica em acervo privado); [ficha completa](MATRIZ_RASTREABILIDADE_50_RESULTADOS.html#r-P10-3); [auditoria VI05](../edicao_1_0_candidata/AUDITORIA_50_RESULTADOS.html#r-P10-3). Originalidade externa não estabelecida.


### 8.2 Ablação, feedback e origem

<a id="r-P10-4"></a>

### P10.4 — Ablação e indispensabilidade

**Hipóteses preservadas:** Retirar ações sem mudar estados, distúrbios, V ou introduzir reparos.

**Conclusão do registro:** Núcleo só diminui; contribuição local não implica indispensabilidade robusta.

Uma ablação retira ações mantendo estados, distúrbios das ações remanescentes e segurança V; não acrescenta reparos. Seu núcleo robusto é subconjunto do original.

<a id="prova-P10-4"></a>

**Demonstração.** Para qualquer Z, o predecessor após ablação está contido no predecessor original, pois cada ação restante já existia. Indução nas aproximações W_n de P10.1 conserva essa inclusão até estabilizar. Se x₀ era viável e deixa de sê-lo ao retirar p, nenhuma política remanescente vence; p era indispensável para aquela garantia, a partir de x₀ e sob o regime dado.

**Contramodelo à necessidade individual.** Duas rotas A,B repõem o mesmo suporte a cada perda. Usar cada uma altera a produção quando a outra não é usada, mostrando contribuição local. Retirar somente A ou somente B deixa uma estratégia; retirar ambas elimina a reposição. Portanto contribuição local não implica indispensabilidade robusta. Retirar perturbações junto com a ação seria outra comparação, sem a inclusão garantida.

**Limite herdado:** Necessidade relativa ao estado/regime; retirada simultânea de distúrbios altera pergunta.

**Rastreabilidade:** Aplicação; referências B05 B12. Fonte, linha 2063: Caderno Científico ETLR(f1), rev14, linha 2063 (fonte histórica em acervo privado); [ficha completa](MATRIZ_RASTREABILIDADE_50_RESULTADOS.html#r-P10-4); [auditoria VI05](../edicao_1_0_candidata/AUDITORIA_50_RESULTADOS.html#r-P10-4). Originalidade externa não estabelecida.


<a id="r-P10-5"></a>

### P10.5 — Insuficiência do grafo/feedback

**Hipóteses preservadas:** Mesmas arestas de dependência funcional em funções AND/OR; atuador com duração declarada.

**Conclusão do registro:** Grafo e ciclos não determinam recuperação nem renovação.

O grafo de dependência funcional possui i→j quando variar somente a coordenada i altera a saída j em algum estado. Ele não determina recuperação nem renovação.

<a id="prova-P10-5"></a>

**Demonstração por contramodelos.** F_∧(a,b,c)=(b∧c,a∧c,a∧b) e F_∨(a,b,c)=(b∨c,a∨c,a∨b) têm exatamente as seis arestas entre coordenadas distintas e fixam 111. De 100, F_∧ produz 000, enquanto F_∨ produz 011 e depois 111. O mesmo grafo omite requisitos conjuntos versus alternativos e não decide recuperação. Um recurso q que suspende produções pode manter o grafo potencial e impedir realizações.

Para separar regulação de renovação, seja desvio e, atuador de capacidade h, u=e se h>0 e u=0 caso contrário, e'=e⊕u, h'=max(0,h−1). Há feedback corretor enquanto o atuador funciona, mas nenhum produtor de h. Um atuador ideal sem desgaste também regula sem ser produzido. Logo feedback não implica renovação, com ou sem falha futura. Esses casos refutam inferências baseadas apenas no grafo, sem refutar teorias que já incluem recursos, produção e duração.

**Limite herdado:** Contramodelos a inferências excessivas; não refutam teorias mais ricas de fechamento.

**Rastreabilidade:** Integração interna; referências B10 B11 B12. Fonte, linha 2073: Caderno Científico ETLR(f1), rev14, linha 2073 (fonte histórica em acervo privado); [ficha completa](MATRIZ_RASTREABILIDADE_50_RESULTADOS.html#r-P10-5); [auditoria VI05](../edicao_1_0_candidata/AUDITORIA_50_RESULTADOS.html#r-P10-5). Originalidade externa não estabelecida.


<a id="r-P10-6"></a>

### P10.6 — Origem produtiva não identificável

**Hipóteses preservadas:** Histórias com mesmo registro e diagnósticos de origem distintos.

**Conclusão do registro:** Não existe decisor exato só do registro; existe se diagnóstico constante na fibra.

Se histórias h_int,h_ext têm a mesma observação q(h), mas diagnósticos de origem produtiva diferentes, não existe decisor exato da origem a partir somente dessa observação. Existe tal decisor precisamente quando o diagnóstico é constante nas fibras de q.

<a id="prova-P10-6"></a>

**Demonstração.** Se d fosse exato, D(h_int)=d(q(h_int))=d(q(h_ext))=D(h_ext), contradição. A recíproca define d pelo valor comum na fibra, como em P08.3. A nova responsabilidade é origem das condições de sustentação, sem novo lema de fatoração. Etiquetas sintéticas “interno” ou “externo” fazem parte da estipulação do modelo; não autenticam causalidade real. Seria preciso justificar quais processos geraram as ocorrências e distinguir ingresso de recurso genérico de ingresso de suporte já organizado.

**Limite herdado:** Etiquetas sintéticas não são evidência causal real.

**Rastreabilidade:** Aplicação; referências B17 B12. Fonte, linha 2083: Caderno Científico ETLR(f1), rev14, linha 2083 (fonte histórica em acervo privado); [ficha completa](MATRIZ_RASTREABILIDADE_50_RESULTADOS.html#r-P10-6); [auditoria VI05](../edicao_1_0_candidata/AUDITORIA_50_RESULTADOS.html#r-P10-6). Originalidade externa não estabelecida.


### 8.3 Renovação e recuperação têm semânticas distintas

<a id="r-P10-7"></a>

### P10.7 — Renovação de fronteira/habilitação

**Hipóteses preservadas:** Três suportes expiram por passo; atualização síncrona; q=1; inicial 111.

**Conclusão do registro:** Renovação nominal de todos os papéis; sem origem em 000 nem recuperação de perda de um papel.

Há três suportes: b de fronteira funcional, m de capacidade produtiva e a de habilitação. Cada ocorrência expira após um passo. Todas as produções são calculadas a partir do estado anterior e disponibilizadas juntas: b'=m∧q, m'=a∧b∧q, a'=m∧b∧q. O conjunto seguro é V={111}.

<a id="prova-P10-7"></a>

**Demonstração.** F(111,1)=111; a expiração obriga cada 1 seguinte a ter uma ocorrência nova com testemunho produtor. Indução dá renovação de todos os papéis sob q=1. F(000,1)=000 e F(x,0)=000 impedem origem sem semente e sobrevivência à privação nesse modelo. Perda de b dá 011→100→000; perda de m dá 101→010→100→000; perda de a dá 110→101→010→100→000. Portanto a renovação nominal não garante reparação das perdas isoladas, com colapsos em dois, três e quatro passos, respectivamente.

O inventário, as durações, o sincronismo, a fronteira funcional e as regras são estipulados. O resultado demonstra renovação do inventário declarado, sem demonstrar membrana material, produção das metaleis ou suficiência constitutiva. Não se identifica o recurso genérico q com um suporte pronto, nem se presume que a interface empírica respeite essa distinção.

**Limite herdado:** Inventário, leis, sincronismo e fronteira são estipulados; não autogeração forte.

**Rastreabilidade:** Integração interna; referências B10 B11 B12. Fonte, linha 2104: Caderno Científico ETLR(f1), rev14, linha 2104 (fonte histórica em acervo privado); [ficha completa](MATRIZ_RASTREABILIDADE_50_RESULTADOS.html#r-P10-7); [auditoria VI05](../edicao_1_0_candidata/AUDITORIA_50_RESULTADOS.html#r-P10-7). Originalidade externa não estabelecida.


<a id="r-P10-8"></a>

### P10.8 — Alcance versus continuidade

**Hipóteses preservadas:** Mesmo jogo de P10.1; alvo W*; recuperação tolerada em Q.

**Conclusão do registro:** Atrator caracteriza chegar ao núcleo em até n passos; não implica permanência prévia nem identidade.

Seja W* o núcleo de continuidade de P10.1 e Q o conjunto tolerado antes da chegada. Defina A₀=W* e A_{n+1}=A_n∪(Q∩CPre(A_n)). Então A_n é exatamente a região de recuperação garantida em até n passos, permanecendo em Q antes de alcançar W*.

<a id="prova-P10-8"></a>

**Demonstração.** No alvo, zero passos bastam. Fora de A_n, chegar em até n+1 exige uma primeira ação com todos os sucessores em A_n e origem tolerada em Q. Isso é necessário pelo primeiro movimento e suficiente concatenando as continuações de horizonte n. A indução conclui. O posto de primeira entrada fornece uma política de alcance em tempo finito.

Um estado de A_n pode estar fora de V. Logo recuperabilidade não implica ter permanecido seguro antes. Histórias 111→111→111 e 111→011→111 têm o mesmo terminal, mas a segunda viola V={111}. Uma política de identidade pode distinguir perda e reconstituição com novos tokens. O atrator de estados não decide essa política e um alvo não vazio não torna todos os estados recuperáveis.

**Limite herdado:** Alvo não vazio não garante recuperabilidade de todos os estados.

**Rastreabilidade:** Aplicação; referências B05 B07. Fonte, linha 2116: Caderno Científico ETLR(f1), rev14, linha 2116 (fonte histórica em acervo privado); [ficha completa](MATRIZ_RASTREABILIDADE_50_RESULTADOS.html#r-P10-8); [auditoria VI05](../edicao_1_0_candidata/AUDITORIA_50_RESULTADOS.html#r-P10-8). Originalidade externa não estabelecida.


<a id="r-P11-1"></a>

### P11.1 — Recuperabilidade de M11

**Hipóteses preservadas:** Regras assíncronas históricas, persistência dos suportes, q fixo, sem novos danos.

**Conclusão do registro:** Com q=1 recupera 111 exatamente se b OU r; máximo dois passos; q=0 só alvo inicial.

No M11 assíncrono, x=(b,r,v) é binário e suportes não alterados persistem. Com q=1, as regras são: ρ_B, se b=0 e r=1, faz b:=1; ρ_V, se v=0 e b=1, faz v:=1; ρ_R, se r=0 e b=v=1, faz r:=1. Apenas uma regra é executada por transição, sem novos danos durante a recuperação. Rec_q significa alcançar 111, admitindo caminho vazio.

<a id="prova-P11-1"></a>

**Demonstração.** Se b=1, repor v por ρ_V quando necessário permite repor r por ρ_R: no máximo dois passos. Se r=1 e b=0, executar ρ_B e, se necessário, ρ_V também leva ao alvo em até dois. Se b=r=0, nenhuma regra pode fornecer b ou r, nem ρ_V pode operar; não há recuperação, qualquer que seja v. Assim Rec₁ equivale a b∨r=1. Com q=0 nenhuma regra opera e apenas o alvo inicial já está recuperado. As menores rotas são: 100→101→111, 010→110→111, 011→111, 101→111, 110→111, e a rota vazia de 111; 000 e 001 não recuperam.

M11 conserva suportes e pode permanecer no alvo sem produzir. P10.7 impõe expiração e renovação, com outras guardas e sincronismo. A diferença de reparabilidade não é contradição entre os resultados.

**Limite herdado:** Recuperação difere de renovação; alvo 111 pode persistir sem produção.

**Rastreabilidade:** Aplicação; referências B10 B11. Fonte, linha 2265: Caderno Científico ETLR(f1), rev14, linha 2265 (fonte histórica em acervo privado); [ficha completa](MATRIZ_RASTREABILIDADE_50_RESULTADOS.html#r-P11-1); [auditoria VI05](../edicao_1_0_candidata/AUDITORIA_50_RESULTADOS.html#r-P11-1). Originalidade externa não estabelecida.


A reserva booleana de S, o balanço sem teto, a renovação síncrona e a reparação assíncrona de M11 representam contratos diferentes. Usar a mesma palavra “suporte” não permite misturar suas provas. É preciso conservar ordem de ingresso e demanda, expiração, capacidade de produção, paralelismo, danos durante a recuperação e recurso ambiental. Um regime que garante q=1 não certifica resistência à privação ilimitada. O recorte não fornece energia gratuita ou criação de matéria e leis a partir do nada.

## 9. Fechamento produtivo, recorrência e proveniência

Quatro sentidos de fechamento devem ser separados. Fechamento de uma representação significa suficiência para atualizar uma descrição; fechamento de um inventário produtivo exige eventos e suportes declarados; fechamento robusto exige uma política contra todos os resultados admitidos; fechamento organizacional constitutivo acrescenta justificação de fronteira, integração, identidade e participação. Nenhum desses sentidos se infere apenas de um circuito desenhado.

O grafo expandido incorpora configurações pertinentes: validade dos suportes, recursos, fase de inicialização, restrições ambientais e memória necessária. Um inventário finito de tipos não torna esse grafo finito se quantidades, histórias ou relógios não forem limitados. Proibir importações estruturadas após uma semente é uma condição de recorte, diferente de proibir todo ingresso de recurso. A atribuição de produção interna precisa alcançar as ocorrências efetivamente usadas, em vez de apenas uma ocorrência interna irrelevante coexistindo com sustentação externa.

<a id="r-P11-3"></a>

**Terminologia de grafos e recorrência.** Um caminho dirigido segue arestas na sua orientação; um passeio pode repetir vértices e arestas. Uma componente fortemente conexa (SCC, sigla inglesa) é uma classe maximal de vértices mutuamente alcançáveis; um vértice isolado satisfaz alcançabilidade por caminho vazio, mas precisa de laço para sustentar execução infinita sozinho. Um objetivo de Büchi exige visitar um conjunto de aceitação infinitamente; várias obrigações são de Büchi generalizado. O monitor de P11.5 converte essas obrigações em um objetivo único no produto.

### P11.3 — Fechamento produtivo recorrente

**Hipóteses preservadas:** Grafo expandido finito exato; x0; segurança V; J finito não vazio; evidência nas arestas.

**Conclusão do registro:** FPR equivale a SCC segura alcançável com aresta interna e cobertura conjunta de J; testemunho eventualmente periódico.

Fixe grafo expandido finito exato de transições, estado inicial x₀, segurança V e conjunto finito não vazio J de obrigações nas arestas. FPR significa existir trajetória infinita desde x₀ inteiramente em V com cada j∈J ocorrendo infinitamente. Então FPR equivale à existência de componente fortemente conexa C do grafo em V, alcançável por caminho seguro, com uma aresta interna e cobertura conjunta de J por suas arestas internas.

<a id="prova-P11-3"></a>

**Necessidade.** Numa trajetória infinita em grafo finito, após algum índice nenhum vértice visitado apenas finitamente reaparece. Quaisquer dois vértices recorrentes se ligam em ambos os sentidos por trechos da trajetória e pertencem à mesma componente C. Há aresta interna usada infinitamente. Como J e as arestas são finitos, cada j que ocorre infinitamente aparece numa aresta interna recorrente. O prefixo dá alcance seguro de C.

**Suficiência.** Escolha em C uma aresta para cada obrigação. Conectividade forte permite ligar o destino de cada uma à origem da próxima, e a última à primeira. Concatenar gera um passeio fechado positivo cobrindo J. Um prefixo seguro desde x₀ até seu início e a repetição infinita do passeio dão FPR. Caminhos conectores podem ter comprimento ≤|C|−1; com uma aresta por obrigação, o período é ≤|J|·|C|. O prefixo total pode ser simplificado, com comprimento ≤|V|−1. São cotas suficientes, sem otimalidade reivindicada.

Um singleton sem laço não admite execução infinita. Um estado com dois laços, um para A e outro para B, pode exigir um passeio que alterna ambos; procurar só um ciclo simples seria insuficiente. O grafo de tipos não substitui o grafo expandido com recursos e expiração. Dois módulos independentes podem cumprir FPR sem integração justificada. Uma trajetória possível também não é garantia contra todos os resultados do ambiente.

**Limite herdado:** SCC de tipos não basta; não prova integração de módulos, identidade nem autogeração forte.

**Rastreabilidade:** Aplicação; B07 e B15 são antecedentes de aceitação infinita e temporalização, não localizadores da prova SCC nem de suas cotas. O argumento acima é autônomo. Fonte, linha 2338: Caderno Científico ETLR(f1), rev14, linha 2338 (fonte histórica em acervo privado); [ficha completa](MATRIZ_RASTREABILIDADE_50_RESULTADOS.html#r-P11-3); [auditoria VI05](../edicao_1_0_candidata/AUDITORIA_50_RESULTADOS.html#r-P11-3). Originalidade externa não estabelecida.


<a id="r-P11-4"></a>

### P11.4 — Expiração e recorrência necessária

**Hipóteses preservadas:** V exige suportes sempre; validade máxima uniforme L; sem importação; só produção interna cria ocorrência.

**Conclusão do registro:** Toda continuidade infinita produz cada tipo infinitamente e em toda janela L; recíproca isolada falsa.

Suponha tempo discreto com a seguinte convenção: suportes presentes no início de um passo perdem uma unidade de validade, e produtos novos tornam-se disponíveis ao final. Cada ocorrência tem duração máxima uniforme L≥1. V exige ao menos uma ocorrência válida de cada tipo de um inventário J_S em todo estado; sem importações, apenas produção interna declarada cria novas ocorrências.

<a id="prova-P11-4"></a>

**Demonstração.** Ao final de qualquer janela de L transições, todas as ocorrências presentes no início expiraram. Se não houve produção de um tipo exigido nessa janela, esse tipo está ausente no estado final, contrariando V. Logo toda janela contém produção de cada tipo, e não pode haver última produção numa trajetória infinita segura. A recíproca isolada é falsa: produzir um suporte a cada L+1 passos dá infinitas produções, com intervalos sem suporte. Produzir apenas um dos tipos também não conserva os demais.

Finitude de tipos não implica prazo uniforme ou finitude do espaço de estados. Suportes estáveis, importação permitida e dormência com ausência tolerada alteram a obrigação. Na variante sequencial com três tipos e uma produção por passo, L<3 não permite cobrir três tipos em toda janela de L. Para L=3, a agenda B,M,A a partir de (3,3,3) dá (3,2,2),(2,3,1),(1,2,3) e se repete com validade positiva. Paralelismo e estoques mudam esse resultado particular.

**Limite herdado:** Finitos tipos não implicam estado finito ou TTL uniforme; suporte estável e dormência alteram tese.

**Rastreabilidade:** Integração interna; referências B12 B15. Fonte, linha 2358: Caderno Científico ETLR(f1), rev14, linha 2358 (fonte histórica em acervo privado); [ficha completa](MATRIZ_RASTREABILIDADE_50_RESULTADOS.html#r-P11-4); [auditoria VI05](../edicao_1_0_candidata/AUDITORIA_50_RESULTADOS.html#r-P11-4). Originalidade externa não estabelecida.


### 9.1 Recorrência garantida e prazos

<a id="r-P11-5"></a>

### P11.5 — Garantia robusta recorrente

**Hipóteses preservadas:** Jogo finito de informação completa, controle antes do distúrbio, sucessores não vazios; monitor de obrigações.

**Conclusão do registro:** Pontos fixos ν/μ caracterizam segurança e Büchi; política estacionária no produto, memória finita na origem.

Considere o jogo finito de P10.1 e J={j₀,…,j_{k−1}}, k>0. O monitor tem índice i da obrigação aguardada e bit b inicialmente 0. Numa transição com etiqueta ℓ⊆J, se j_i∈ℓ avance i uma posição módulo k e faça b'=1 somente se esse avanço completa a volta; nos demais casos b'=0. Avance no máximo uma posição por passo. B é o conjunto do produto com b=1. A segurança do produto é V. Para um operador monótono em subconjuntos, μ denota o menor ponto fixo e ν o maior. No fragmento finito, obtêm-se por iteração a partir de ∅ e do universo pertinente, respectivamente; as fórmulas abaixo restringem o universo seguro a V. Defina

`H(Z)=μY.[(B∩V∩CPre(Z)) ∪ (V∩CPre(Y))]`,

`Wrec=νZ.H(Z)`, iniciando Z em V e cada iteração interna Y em ∅.

**Monitor.** Infinitas voltas exigem ter encontrado cada obrigação infinitamente. Reciprocamente, se cada obrigação aparece infinitamente, a atualmente aguardada aparecerá de novo; indução nos avanços completa qualquer número de voltas. Eventos simultâneos não invalidam essa construção. O bit é recalculado, sem ficar travado em 1.

<a id="prova-P11-5"></a>

**Suficiência do ponto fixo.** Em Z=Wrec, as iterações crescentes internas atribuem a cada estado um posto finito. No posto base há estado em B com uma ação que leva todos os resultados novamente a Z. Nos demais postos escolha ação que leve a postos menores. Toda execução atinge a base em tempo finito, conserva V e retorna a Z; repetir dá infinitas visitas a B. As ações escolhidas dependem só do estado do produto, fornecendo política estacionária nele e memória finita no sistema original.

**Necessidade.** Seja Q o conjunto de estados com alguma política vencedora. A continuação após qualquer história compatível permanece vencedora, logo cada resultado da ação prescrita fica em Q. De cada estado de Q há garantia de uma visita futura a B, seguida de uma ação que mantém sucessores em Q. Sob a política escolhida, se não houvesse limite finito para esse primeiro retorno, a árvore finitamente ramificada dos prefixos sem a visita conteria um ramo infinito sem B. Para explicitar esse argumento, escolha recursivamente um filho com extensões de comprimentos arbitrariamente grandes; algum existe porque há finitos filhos. A sequência de escolhas seria uma execução adversarial que contradiz a vitória. Há, portanto, um limite finito. Indução retroativa nesse limite coloca o estado na aproximação interna de H(Q). Assim Q⊆H(Q). A monotonicidade de H e indução nas aproximações decrescentes exteriores dão Q⊆Wrec. Com a suficiência, isso prova igualdade.

**Precisão EVI03-03.** Büchi não impõe um prazo escolhido previamente. Contudo, sob uma política estacionária vencedora no produto finito, o subgrafo alcançável fora de B não pode conter ciclo: o ambiente poderia repeti-lo para sempre. Trechos sem B têm, então, comprimento limitado pelo número de estados; |Wrec|+1 é uma estimativa conservadora de retorno. Uma política histórica vencedora pode escolher esperas crescentes, e a palavra com produções em 2^n continua tendo lacunas ilimitadas. Sem teto físico por duração de passo, a cota discreta não fornece prazo físico.

**Contramodelos.** Um único estado com ações separadas que produzem A ou B exige memória para alternar; nenhuma escolha estacionária determinista no estado original realiza ambas. Uma rota produtiva com um resultado ambiental adicional que destrói habilitação pode satisfazer FPR cooperativo e falhar na garantia robusta. CPre considera todos os resultados originais: não se retiram os ruins antes do teste.

**Limite da evidência:** A limitação histórica de controles de um alvo é preservada na matriz. A VI05 acrescentou 14.280 comparações do monitor de duas obrigações em palavras eventualmente periódicas e 192 comparações de regiões vencedoras em produtos de oito estados, com 33.612 políticas enumeradas. A prova geral continua textual; esses universos não cobrem todos os monitores/jogos ou informação parcial.

**Rastreabilidade:** Aplicação; referências B07 B08. Fonte, linha 2383: Caderno Científico ETLR(f1), rev14, linha 2383 (fonte histórica em acervo privado); [ficha completa](MATRIZ_RASTREABILIDADE_50_RESULTADOS.html#r-P11-5); [auditoria VI05](../edicao_1_0_candidata/AUDITORIA_50_RESULTADOS.html#r-P11-5). Originalidade externa não estabelecida.


<a id="r-P11-6"></a>

### P11.6 — Rotas e cortes recorrentes

**Hipóteses preservadas:** Mesmos estados, segurança, eventos e semântica; ablação ou mais distúrbios.

**Conclusão do registro:** Garantia não aumenta; arestas removidas não criam trajetórias; cortes minimais podem não ser unitários.

Mantendo estados, segurança e eventos, retirar ações controláveis não amplia a região vencedora recorrente; acrescentar resultados ambientais às ações existentes também não a amplia. Retirar arestas de um grafo cooperativo não cria trajetórias.

<a id="prova-P11-6"></a>

**Demonstração.** Uma política disponível após ablação já existia antes. Se ela vence contra mais resultados ambientais, vence contra qualquer subconjunto dos mesmos resultados. Assim toda testemunha de vitória do jogo mais exigente também é testemunha no original. No grafo cooperativo, cada caminho restante já era caminho original. Isso prova as inclusões sem depender de implementação de pontos fixos.

**Cortes.** Em um estado seguro, rotas r₀,r₁ produzem A e r₂ produz B. Os conjuntos mínimos por inclusão que permitem recorrência de ambos são {r₀,r₂} e {r₁,r₂}. Os cortes minimais são {r₂} e {r₀,r₁}. Retirar uma das duas rotas de A é dispensável isoladamente, mas retirar ambas impede A. Minimalidade por inclusão difere de menor cardinalidade. Custos e estoques devem ser checados em todos os prefixos; balanço total de um ciclo não garante que ele possa começar desde a reserva disponível.

**Limite herdado:** Minimal por inclusão não significa menor cardinalidade.

**Rastreabilidade:** Aplicação; referências B05 B07. Fonte, linha 2397: Caderno Científico ETLR(f1), rev14, linha 2397 (fonte histórica em acervo privado); [ficha completa](MATRIZ_RASTREABILIDADE_50_RESULTADOS.html#r-P11-6); [auditoria VI05](../edicao_1_0_candidata/AUDITORIA_50_RESULTADOS.html#r-P11-6). Originalidade externa não estabelecida.


A formulação por pontos fixos é uma aplicação de métodos clássicos de jogos de Büchi [B07, B08]. A contribuição interna está em conservar obrigações produtivas justificadas e segurança no mesmo produto. O método não descobre quais etiquetas são constitutivas. A distinção entre recorrência e prazo protege duas afirmações verdadeiras em alcances diferentes: uma palavra Büchi arbitrária pode ter lacunas ilimitadas; uma política estacionária vencedora num produto finito fornece uma cota discreta própria desse produto. Prazo requerido pela aplicação precisa ser especificado e monitorado, com unidades e limites físicos de duração quando pertinentes.

### 9.2 Ocorrências, ciclos e identidade

<a id="r-P11-7"></a>

### P11.7 — DAG de ocorrências e ciclos de tipos

**Hipóteses preservadas:** Pais estritamente anteriores ao produto.

**Conclusão do registro:** Proveniência de ocorrências acíclica pode projetar ciclo entre tipos.

Cada ocorrência possui identificação própria e cada aresta de proveniência vai de um pai estritamente anterior ao produto numa relação de precedência transitiva e irreflexiva. O grafo dessas ocorrências é acíclico, mesmo quando sua projeção aos tipos tem ciclos.

<a id="prova-P11-7"></a>

**Demonstração.** Um ciclo de ocorrências e₀≺e₁≺…≺e_n=e₀ implicaria e₀≺e₀ pela transitividade, contrariando irreflexividade. A cadeia A(t)→B(t+1)→A(t+2) é acíclica nas ocorrências, mas a projeção dos rótulos gera A→B→A. A projeção perdeu os identificadores e a precedência. Portanto ciclo de tipos não implica causalidade retroativa, nem a aciclicidade de um log prova que suas atribuições causais sejam empiricamente corretas. A ausência de ciclos finitos tampouco afirma, em uma ordem infinita arbitrária, ausência de cadeias descendentes infinitas; bem-fundação seria outra hipótese.

**Limite herdado:** Ciclo tipado não dá causalidade retroativa.

**Rastreabilidade:** Matemática conhecida; referências B16. Fonte, linha 2407: Caderno Científico ETLR(f1), rev14, linha 2407 (fonte histórica em acervo privado); [ficha completa](MATRIZ_RASTREABILIDADE_50_RESULTADOS.html#r-P11-7); [auditoria VI05](../edicao_1_0_candidata/AUDITORIA_50_RESULTADOS.html#r-P11-7). Originalidade externa não estabelecida.


<a id="r-P11-8"></a>

### P11.8 — Disponibilidade, origem e identidade

**Hipóteses preservadas:** Projeção só da disponibilidade ou estado terminal.

**Conclusão do registro:** Não determina origem produtiva, permanência anterior ou identidade.

Uma observação só da disponibilidade atual não determina origem produtiva nem continuidade anterior. Igualdade de estado terminal não determina identidade.

<a id="prova-P11-8"></a>

**Demonstração.** Duas execuções podem registrar disponibilidade 1 em todo passo, com cada reposição interna numa e externa na outra. A observação é a mesma e o diagnóstico de origem difere, impedindo fatoração por P08.3. Para continuidade, 111→111→111 e 111→011→111 terminam iguais, mas somente a primeira permanece em V={111}. Uma política de identidade pode distinguir ruptura e reconstituição sem alterar o terminal. Como a política e a história não são funções desse terminal em geral, ele não as decide. As duas construções são contramodelos de suficiência observacional, sem escolher uma política universal de identidade.

**Limite herdado:** Atribuição de identidade ainda exige política e evidência; aplicação de resultados anteriores.

**Rastreabilidade:** Integração interna; referências B16 B17. Fonte, linha 2411: Caderno Científico ETLR(f1), rev14, linha 2411 (fonte histórica em acervo privado); [ficha completa](MATRIZ_RASTREABILIDADE_50_RESULTADOS.html#r-P11-8); [auditoria VI05](../edicao_1_0_candidata/AUDITORIA_50_RESULTADOS.html#r-P11-8). Originalidade externa não estabelecida.


Autopoiese, fechamento de restrições e sistemas abertos oferecem antecedentes conceituais localizados no catálogo B09–B12. As comparações preservadas na VI03 reconhecem que essas teorias trazem critérios próprios. Os contramodelos aqui demonstrados não as refutam por reduzir seu conteúdo a um grafo; mostram precisamente por que essa redução seria inadequada. Recorrência de eventos num inventário estipulado continua insuficiente para concluir individuação ou autogeração forte.

## 10. Certificado integrado de conservação dinâmica e estratégica

O problema integrador pode agora ser formulado. Uma abstração útil à sustentação deve conservar não só manifestações e passos possíveis, mas também quem escolhe, quando escolhe, quais resultados permanecem possíveis e quais eventos satisfazem o objetivo. A projeção conjunta dessas responsabilidades é mais exigente que a igualdade por extremos. Em contrapartida, pode ser suficiente um refinamento unilateral quando a tarefa consiste em implementar uma garantia abstrata, sem exigir equivalência total.

### 10.1 Contrato do jogo e certificado C

Fixe X finito; em cada x, A(x) é o conjunto de ações identificadas habilitadas e D(x,a) um conjunto finito não vazio de resultados (x',ℓ). O controlador observa x e escolhe a; o ambiente escolhe o resultado depois. Estados sem ação são bloqueios, que perdem objetivos infinitos. Políticas podem consultar a história completa disponível; política estacionária depende apenas do estado atual. No produto, o estado inclui a memória finita do monitor. Não se acrescenta transição de espera a um bloqueio sem declará-la no jogo. As etiquetas reúnem exatamente os dados consultados pelo objetivo, inclusive produção, duração ou origem quando pertinentes. Não há medida probabilística ou simultaneidade oculta nessa semântica.

**EVI03-01 incorporada.** Na representação dos geradores históricos VI02, adota-se explicitamente A_hab(x)={a:D(x,a)≠∅}: entradas vazias são tratadas como desabilitadas. No contrato formal, uma ação declarada habilitada com D vazio é entrada malformada e deve ser rejeitada. Normalizar o gerador não é admitir vitória por universalidade vazia. O original VI02 não foi alterado.

Seja p:X→Y sobrejetiva. O certificado exige:

1. **C1 — diagnósticos:** O, pertença a V e todas as guardas/avaliações consultadas são constantes por fibra. Outros predicados só estão cobertos quando expressamente incluídos.
2. **C2 — escolhas:** p(x)=p(y) implica A(x)=A(y), como conjuntos de ações identificadas. Renomeações precisam de contrato anterior explícito.
3. **C3 — resultados:** para cada a habilitada, {(p(x'),ℓ):(x',ℓ)∈D(x,a)} é igual para todos os representantes da fibra. A igualdade é de pares classe/etiqueta por ação, sem apagar suas correlações.
4. **C4 — memória e semântica:** condições pertinentes à segurança, expiração, recursos, identidade operacional e regime ambiental já estão em X ou monitor. A semântica dos eventos foi justificada no modelo. C4 é uma premissa de modelagem, sem certificação automática pelo algoritmo.

<a id="r-PVI02-1"></a>

### PVI02.1 — Quociente exato rotulado com escolhas

**Hipóteses preservadas:** C1–C4; X finito, p sobrejetiva; ações identificadas; resultados não vazios; informação completa.

**Conclusão do registro:** Projeção e levantamento desde cada representante com ações e etiquetas; segurança saturada conservada.

O certificado C1–C4 é definido no capítulo de conservação: observações, segurança e guardas saturadas; mesmas ações identificadas por fibra; mesmos conjuntos de pares (classe sucessora,etiqueta) para cada ação; memória pertinente incluída no estado ou monitor. X é finito, p:X→Y sobrejetiva e cada ação habilitada possui resultados não vazios.

<a id="prova-PVI02-1"></a>

**Demonstração.** Um passo concreto fornece, por definição, a aresta com mesma ação e etiqueta no quociente. Isso projeta toda execução. Para levantar uma execução abstrata, fixe primeiro seu representante inicial x₀. Dada a ação e o par (classe,etiqueta) do próximo passo, C3 assegura esse mesmo par entre os resultados de x₀, não apenas de outro representante. Escolha um sucessor testemunha e repita a partir dele. Indução levanta todo prefixo. No finito, fixe uma ordem total de X e escolha o primeiro sucessor testemunha em cada passo; a recursão constrói um levantamento infinito sem trocar arbitrariamente o representante corrente. C1 conserva segurança e os diagnósticos incluídos. C2 preserva a identidade da ação, não só a união das arestas.

O levantamento conserva traço de ações e etiquetas, sem reproduzir cada estado de outra realização concreta. C4 é hipótese de suficiência da modelagem, não consequência da estabilização de uma partição. Recursos ilimitados, história ilimitada ou relógios reais podem tornar X infinito.

**Limite herdado:** C4 é hipótese de modelagem; não valida constituição nem informação parcial.

**Rastreabilidade:** Aplicação; referências B04 B17. Fonte, linha 70: ETLR-VI-02, linha 70 (fonte histórica em acervo privado); [ficha completa](MATRIZ_RASTREABILIDADE_50_RESULTADOS.html#r-PVI02-1); [auditoria VI05](../edicao_1_0_candidata/AUDITORIA_50_RESULTADOS.html#r-PVI02-1). Originalidade externa não estabelecida.


<a id="r-PVI02-2"></a>

### PVI02.2 — Transporte exato de viabilidade e recorrência robusta

**Hipóteses preservadas:** Certificado C; monitor finito determinista compatível; segurança/aceitação saturadas; J não vazio.

**Conclusão do registro:** Igualdade CPre e transporte de segurança, alcance e Büchi; política abstrata levantável.

Se C vale e M é monitor finito determinista atualizado apenas por classes/observações e etiquetas preservadas, P(x,m)=(p(x),m) é o mapa no produto. Exija o mesmo estado inicial do monitor e segurança/aceitação saturadas. Para todo Z abstrato, `CPre_X(P⁻¹Z)=P⁻¹(CPre_Y(Z))`.

<a id="prova-PVI02-2"></a>

**Demonstração do predecessor.** Se x tem ação com todos os resultados em P⁻¹Z, C2 fornece a mesma ação abstrata. C3 identifica exatamente os pares classe/etiqueta, e a atualização igual do monitor põe todos os resultados abstratos em Z. Reciprocamente, uma ação abstrata testemunha está habilitada concretamente por C2; C3 e a atualização do monitor levam todos os resultados concretos a P⁻¹Z. O não vazio impede vitória vacuamente universal. Isso prova a equivalência bilateral de pertinência.

**Transporte dos pontos fixos.** A imagem inversa conserva ∅, universo, uniões e interseções. Para segurança, as bases V e os passos V∩CPre coincidem por imagem inversa; indução conserva cada aproximação decrescente de P10.1. Para alcance, o mesmo vale para a base alvo saturada e passos A∪(Q∩CPre), com Q saturado. Para Büchi, fixe uma aproximação externa; indução nas aproximações internas conserva H; depois indução nas externas conserva Wrec de P11.5. No finito, todas estabilizam, dando W_X=P⁻¹W_Y nas três tarefas. Uma política estacionária abstrata pode ser levantada com as mesmas ações. A igualdade das regiões não exige que toda política concreta seja constante por fibra.

As etiquetas produtivas precisam de justificação semântica anterior. Segurança e recorrência são conservadas no modelo, sem provar prazo físico ou suficiência do inventário constitutivo. Monitor que consulta informação descartada invalida a premissa de compatibilidade.

**Limite herdado:** Não certifica prazo físico, regime infinito ou adequação produtiva dos rótulos.

**Rastreabilidade:** Integração interna; referências B05 B07. Fonte, linha 83: ETLR-VI-02, linha 83 (fonte histórica em acervo privado); [ficha completa](MATRIZ_RASTREABILIDADE_50_RESULTADOS.html#r-PVI02-2); [auditoria VI05](../edicao_1_0_candidata/AUDITORIA_50_RESULTADOS.html#r-PVI02-2). Originalidade externa não estabelecida.


### 10.2 Refinamento suficiente e construção canônica relativa

<a id="r-PVI02-3"></a>

### PVI02.3 — Certificado suficiente de conservação unilateral

**Hipóteses preservadas:** Para toda ação abstrata, controle concreto escolhido antes da perturbação com resultados projetados não vazios contidos; predicados/monitor compatíveis.

**Conclusão do registro:** Toda política vencedora abstrata induz vencedora concreta para segurança e recorrência.

**Precisão incorporada EVI03-02.** Para todo estado concreto x e toda ação abstrata a∈Ā(p(x)), existe controle concreto u=κ(x,a)∈A(x), escolhido antes do resultado ambiental, tal que

`∅ ≠ {(p(x'),ℓ):(x',ℓ)∈D_X(x,u)} ⊆ D_Y(p(x),a)`.

A ordem é ∀x∀a∃u∀resultado. No produto, exija atualização compatível do monitor, mesmo estado inicial e implicações P(s)∈V_Y⇒s∈V_X e P(s)∈B_Y⇒s∈B_X. Aceitação definida pelas mesmas etiquetas e monitor satisfaz a segunda implicação por construção.

<a id="prova-PVI02-3"></a>

**Demonstração.** Dada política abstrata π, a política concreta registra a projeção da história h, consulta a=π(P(h)) e executa κ(x,a). Todo resultado concreto permitido projeta-se, pela inclusão, num resultado abstrato dessa ação. Indução em cada prefixo mostra que toda execução concreta projeta-se em execução sob π. Não vazio assegura continuidade quando a política é vencedora. Se todas as execuções abstratas conservam V_Y e visitam B_Y infinitamente, as implicações dos predicados transferem segurança e recorrência a todas as execuções concretas. κ nunca é escolhido após a perturbação.

**Contramodelos.** Inverter a inclusão permite ao concreto acrescentar um resultado inseguro que a vitória abstrata não considerou. Exigir só ∀u∃a pode deixar a ação abstrata boa sem implementação. Sem recíproca: o abstrato pode ter um resultado ruim adicional e perder enquanto o concreto vence. Com observação apenas da fibra {x₀,x₁}, controles L e R podem preservar, respectivamente, apenas x₀ e apenas x₁. O seletor por estado completo existe, mas nenhuma primeira escolha comum vence. Portanto ∀x∃u não implica escolha realizável pela observação parcial; é necessária obrigação observacional adicional. O contrato não se identifica sem ressalvas com refinamento por quantizador estático e mesmas entradas.

**Limite herdado:** Sem recíproca; seletor deve ser realizável com informação disponível; ver EVI03-02.

**Rastreabilidade:** Aplicação; referências B04 B05. Fonte, linha 97: ETLR-VI-02, linha 97 (fonte histórica em acervo privado); [ficha completa](MATRIZ_RASTREABILIDADE_50_RESULTADOS.html#r-PVI02-3); [auditoria VI05](../edicao_1_0_candidata/AUDITORIA_50_RESULTADOS.html#r-PVI02-3). Originalidade externa não estabelecida.


<a id="r-PVI02-4"></a>

### PVI02.4 — Refinamento canônico relativo ao contrato finito

**Hipóteses preservadas:** X e contrato finitos fixados; P0 por observáveis, segurança e guardas; ações/eventos distinguidos.

**Conclusão delimitada nesta edição:** O refinamento termina e dá a mais grosseira partição que refina P₀ e satisfaz C1–C3 no contrato fixado. C4 permanece premissa de modelagem e não é certificada pelo refinamento. A formulação-resumo VI03/VI04 é preservada no histórico da matriz e na errata E05-07.

Fixe contrato finito: X, ações identificadas, resultados, etiquetas, observáveis, segurança e guardas. P₀ distingue todas as avaliações pertinentes. P_{n+1} conserva o bloco anterior e distingue, para cada ação, habilitação e conjunto de pares (bloco sucessor em P_n,etiqueta).

<a id="prova-PVI02-4"></a>

**Demonstração.** O número de blocos cresce em todo passo estrito e é limitado por |X|. Há no máximo |X|−|P₀| refinamentos estritos. No limite P*, as assinaturas são constantes, satisfazendo C1–C3. Seja Q qualquer partição estável admissível que refine P₀. Suponha que Q refine P_n. Estados no mesmo bloco Q têm conjuntos iguais de pares (bloco Q,etiqueta) por ação e mesma habilitação; substituir cada bloco Q por seu bloco P_n conserva a igualdade. Assim a assinatura por P_n é igual, e Q refina P_{n+1}. Indução dá Q refinando P*. Logo P* é a partição mais grosseira admissível no contrato fixado. A canonicidade é da equivalência, não dos nomes dos blocos. C4 não é produzido pelo algoritmo.

**Precisão EVI03-04.** A interseção de equivalências fortes não deterministas pode ser instável. Tome s com sucessores a,b e t com sucessores c,d, destinos sem sucessores. Q₁={{s,t},{a,c},{b,d}} e Q₂={{s,t},{a,d},{b,c}} são estáveis com observação constante. Sua interseção mantém s,t juntos e separa a,b,c,d; as assinaturas dos sucessores agora diferem. Portanto exige novo refinamento. A identidade pode ser o único resultado admissível, sem compressão. Permitir renomear ações, descartar observações ou enfraquecer objetivos é outro problema de minimização.

**Limite herdado:** Pode ser identidade; não é mínimo ontológico ou mínimo estratégico irrestrito.

**Rastreabilidade:** Aplicação; referências B06 B17. Fonte, linha 101: ETLR-VI-02, linha 101 (fonte histórica em acervo privado); [ficha completa](MATRIZ_RASTREABILIDADE_50_RESULTADOS.html#r-PVI02-4); [auditoria VI05](../edicao_1_0_candidata/AUDITORIA_50_RESULTADOS.html#r-PVI02-4). Originalidade externa não estabelecida.


### 10.3 Contramodelos integradores

| Caso | Construção | Inferência impedida |
|---|---|---|
| CI01 — escolhas apagadas | Em x=0 seguro, um jogo oferece ação que fica em 0 e outra que vai a 1 inseguro; outro oferece uma ação com ambos os resultados | Mesma união de arestas não determina a garantia do controlador |
| CI02 — produção apagada | Mesmo laço seguro com etiqueta produtiva em um modelo e vazia no outro | Segurança e extremos iguais não conservam recorrência produtiva |
| CI03 — guarda apagada | Mesma ausência de execução, avaliações N e ? distintas | Vazio de transições não determina avaliação epistêmica |
| CI04 — história apagada | [1,1,1] e [1,0,1] com amostragem apenas nas pontas | Terminal recuperado não prova continuidade |
| CI05 — prazo omitido | Produções nos instantes 2^n | Büchi numa trajetória não impõe uma lacuna máxima prévia |
| CI06 — testemunhos distintos | Chegada por b₀ e saída por b₁ na mesma classe | Composição abstrata não garante junção concreta |
| CI07 — escolha oculta | Dois estados indistinguíveis exigem L e R incompatíveis | Seletor dependente de x pode ser irrealizável na interface parcial |
| CI08 — individuação trivial | Ind_op é declarado sempre verdadeiro | Preservar o avaliador não demonstra adequação constitutiva |

As quatro precisões VI03 estão, portanto, incorporadas como decisões editoriais e formais rastreáveis: EVI03-01 neste contrato; EVI03-02 no enunciado de PVI02.3; EVI03-03 na prova de P11.5 e na interpretação de prazos; EVI03-04 em P07.1 e no contramodelo de PVI02.4. Não são mudanças silenciosas do rev14. Nenhuma é apresentada como refutação das proposições em seus domínios corretos.

## 11. Síntese científica, contribuição e limites

A ETLR investiga se uma estrutura organizada a partir dos fundamentos relacionais de espaço, tempo e indivíduo, mediante suas diferentes composições, funções e transformações multiescalares, é capaz de produzir conhecimento sobre princípios comuns de constituição, interação e organização em diferentes domínios da realidade. Os resultados deste volume constituem instrumentos formais e confrontos delimitados desse programa. Sua articulação permite examinar tarefas relacionais comuns em modelos declarados, mas não demonstra que todos os domínios compartilhem uma única constituição. A ETLR não pretende substituir teorias particulares de domínio; analogias físicas ou de gauge não integram suas premissas.

O volume estabelece uma arquitetura de obrigações que começa com referência e descrição, passa por composição e representação suficiente e termina com conservação de garantias em jogos declarados. Seu resultado integrador é o transporte exato de segurança, alcance e recorrência mediante um quociente que conserva escolhas e resultados rotulados. Quando equivalência é excessiva, o refinamento unilateral oferece uma condição suficiente de implementação. Esses resultados compartilham matemática estabelecida; seu uso articulado na investigação ETLR é a contribuição interna candidata.

Os cinquenta registros não correspondem a cinquenta teoremas independentes ou descobertas novas. Há provas básicas e aplicações de uma mesma estrutura: fatoração por fibras, junção existencial, refinamento de partições e pontos fixos. A compactação conserva a diferença entre as tarefas e seus quantificadores, em vez de repetir o mesmo argumento como novidade. A classificação herdada — 12 matemática conhecida, 27 aplicações, 11 integrações internas — é preservada individualmente. Originalidade externa não foi estabelecida por essa classificação nem pela ausência de um antecedente localizado.

A fundamentação filosófica permanece positiva como formulação de problemas: espaço, tempo e indivíduo têm caracterizações candidatas que exigem confronto; a polaridade organiza perguntas sobre constituição e manifestação; CAL-01 fixa uma referência autoral sem impor um operador. O formalismo mostra que algumas distinções são necessárias a tarefas específicas. Não prova que essas três categorias sejam as únicas primitivas de toda organização ou que tenham o mesmo estatuto em todos os domínios.

Os modelos também produzem resultados negativos determinados. Observação coincidente não identifica mecanismo; composição não individua; renovação não implica reparabilidade; grafo de dependências não determina executabilidade; saldo final não garante prefixos viáveis; existência de trajetória não equivale a política robusta; tipo recorrente não é ocorrência retrocausal; estado terminal não decide identidade. Cada negação tem um contramodelo ou argumento de impossibilidade localizado, preservando os resultados independentes.

O limite de aplicação é constitutivo. É necessário justificar que o estado conserva memória pertinente, que o inventário inclui os suportes exigidos, que as ações são realizáveis com a informação disponível e que os eventos registrados possuem a origem declarada. Informação parcial, regimes contínuos, recursos sem teto e história ilimitada não recebem teoremas gerais de redução finita neste volume. Um certificado calculado sobre uma descrição inadequada pode estar matematicamente correto e ser insuficiente para o domínio.

AD-01 autônomo, a identificação integral das lacunas G01–G20 e os contratos completos ARM permanecem pendências documentais. Não se inventam cláusulas ou uma lista substituta de vinte lacunas. A compatibilidade integral com esses documentos fica suspensa. As demonstrações de relações e jogos aqui explicitadas não dependem de recuperar tais cláusulas como premissas; por isso permanecem disponíveis em seus escopos. A anterioridade específica de aplicações e integrações internas continua aberta a confronto bibliográfico adicional.

Nenhuma conclusão deste volume afirma universalidade ontológica, autogeração forte, produção das metaleis ou validação empírica. A obra se encerra como manuscrito científico candidato completo no recorte documentado: contém definições operacionais, hipóteses, demonstrações e contramodelos suficientes para examinar os resultados apresentados. A completude expositiva não resolve a incompletude da investigação ontológica, documental ou empírica.

## 12. Rastreabilidade, decisões editoriais e evidência

### 12.1 Base exata e cadeia documental

A presente candidata de revisão editorial parte dos bytes da edição 1.0 CANDIDATA no commit ec3c63bc6687d1116c73d74612915fc702433090. A identificação 1.1 CANDIDATA é proposta para avaliação autoral. A edição 1.0 e o DOI 10.5281/zenodo.24586496 permanecem referências históricas distintas deste PDF revisado. As descrições de auditoria e execução a seguir registram as etapas históricas; não anunciam sua repetição nesta revisão editorial.

A base documental da revisão VI05 foi a edição VI04, com as matrizes e os antecedentes VI00–VI03. A conferência histórica de tamanho, checksums e membros do acervo privado não identificou divergências. Integridade documental não equivale a validação científica. Esta seleção pública conserva identificadores, localizadores bibliográficos e condições dos argumentos; os documentos internos completos permanecem separados.

A cadeia de continuidade investigativa e suas autorizações são conservadas integralmente no acervo privado. Protocolos, conversas e pacotes de continuidade não integram esta seleção pública. Essa separação editorial não modifica a origem dos problemas nem as premissas científicas expostas.

### 12.2 Auditoria individual e dependências

Os cinquenta IDs foram mantidos, com auditoria das provas integradas, enunciados, domínios, quantificadores, contramodelos e referências. A matriz nova preserva todos os campos recebidos, inclusive os que descrevem somente o estado histórico de auditoria VI03/VI04, e acrescenta campos VI05. As provas históricas completas de todas as etapas 00–11 não recebem certificação retroativa por essa leitura do manuscrito integrado.

O campo de dependências do argumento VI05 distingue apoios efetivamente usados dos antecedentes expositivos antes agrupados no campo VI04. O grafo desse novo campo foi verificado quanto a IDs e ciclos. A ausência de ciclo nesse grafo não prova adequação ontológica. As fichas permitem verificar cada uso, em vez de inferir aprovação da contagem de cinquenta registros.

### 12.3 Execução real, prova e revisão documental

VI02 e VI03 foram copiados byte a byte para diretórios temporários e executados com Python 3.12.14. Ambos retornaram código zero, stderr vazio e igualdade semântica com as saídas históricas, excluindo apenas tempo_segundos na comparação VI03. Os programas e saídas selecionados estão em reproducao/, acompanhados de instruções e verificação própria. Não foram executados motores, repositórios ou todas as suítes históricas.

O controle complementar VI05, de implementação própria, enumera palavras sobre as quatro etiquetas de duas obrigações, períodos de comprimento 1–4, prefixos de 0–2 e os dois índices iniciais: 14.280 comparações sem divergência. Em 48 jogos de dois estados amostrados com semente 26052026 e quatro conjuntos seguros por jogo, compara a fórmula Büchi no produto de oito estados com enumeração de políticas e detecção de ciclos sem aceitação: 192 comparações, 33.612 políticas enumeradas. Recalcula também P06.2/3, P08.5, P10.7, as oito distâncias de M11 e a contagem trivalente dos IO. Não se somam esses universos como amostra empírica ou prova universal.

Uma execução computacional confirma o resultado dos casos realizados; uma demonstração textual sustenta a conclusão geral sob premissas. Revisão documental confirma o que os documentos dizem e sua integridade; nenhuma dessas operações autentica por si um fenômeno físico, mental ou espiritual/astral. Não houve prova mecanizada ou parecer humano externo independente.

### 12.4 CHECAR_RAMIFICAÇÕES, PM-01 e HIP-CIC

PM-01 foi reaberto como fonte de proteção e continuidade, com R01–R04 e distinções de evidência. Seu trecho CAL-01 está literal. Os dezoito registros VI01 e sete VI02-A–G permanecem abertos no Apêndice B. Suas perguntas, alternativas, relações, testes e condições de retorno não foram encerrados por revisão editorial. As ramificações ancestrais FUND/CAL/QF continuam preservadas no acervo histórico privado; não são declaradas resolvidas por esta seleção. CHECAR_RAMIFICAÇÕES é convenção investigativa, não software executado nem substituto do AD-01 autônomo ausente.

### 12.5 Artefatos, apresentação e preservação

A base 1.0 possui Markdown e HTML integrais, estilos locais, sumário, âncoras, glossário, índices, matriz, auditoria individual, erratas, registro bibliográfico e questões abertas. Nesta revisão editorial, o PDF candidato deriva do HTML local correspondente; o diff focal, os hashes e as verificações da candidata são entregues separadamente. Os registros CHANGELOG e VERIFICACAO_FORMATOS.json da base descrevem a edição 1.0 e não certificam este PDF revisado. A atualização pública dos derivados indispensáveis depende de autorização específica, preservando os resultados, os campos científicos da matriz e a identidade da versão depositada. Nenhuma aprovação científica é inferida das verificações de apresentação.

Os 870 arquivos históricos anteriores à VI05 permanecem preservados no acervo privado. Esta edição pública candidata é uma seleção editorial separada, com manifesto próprio. Integridade não é homologação científica. A preparação não implica publicação, modificação de motores ou repositórios, nem início de Volume II.

## Apêndice A. Matriz compacta dos cinquenta resultados

| ID | Resultado | Capítulo | Classificação VI03 |
|---|---|---|---|
| [P02.1](#r-P02-1) | Associatividade condicionada | 4 | Matemática conhecida |
| [P02.2](#r-P02-2) | Imagem da composição | 4 | Matemática conhecida |
| [P02.3](#r-P02-3) | Trajetórias rotuladas | 4 | Aplicação |
| [P03.1](#r-P03-1) | Levantamento por extremos | 4 | Matemática conhecida |
| [P03.2](#r-P03-2) | Guarda e história ocultada | 5 | Aplicação |
| [P04.1](#r-P04-1) | Levantamento por cada representante | 5 | Matemática conhecida |
| [P04.2](#r-P04-2) | Preservação da guarda | 5 | Matemática conhecida |
| [P05.1](#r-P05-1) | Contração conjuntiva | 6 | Matemática conhecida |
| [P05.2](#r-P05-2) | Reabertura exata | 6 | Aplicação |
| [P05.3](#r-P05-3) | Campo omitido | 6 | Aplicação |
| [P06.1](#r-P06-1) | Insuficiência de J para revisão | 6 | Aplicação |
| [P06.2](#r-P06-2) | Observabilidade relativa | 6 | Aplicação |
| [P06.3](#r-P06-3) | Limite de redução em M3 | 6 | Aplicação |
| [P06.4](#r-P06-4) | Quociente exato mínimo | 5 | Matemática conhecida |
| [P07.1](#r-P07-1) | Fatoração dinâmica e composição | 5 | Matemática conhecida |
| [P07.2](#r-P07-2) | Sobreaproximação segura | 5 | Aplicação |
| [P07.3](#r-P07-3) | Alternância de regimes | 5 | Integração interna |
| [P08.1](#r-P08-1) | Composição de interfaces | 4 | Aplicação |
| [P08.2](#r-P08-2) | Abstração versus composição | 4 | Integração interna |
| [P08.3](#r-P08-3) | Fatoração de tarefas | 5 | Matemática conhecida |
| [P08.4](#r-P08-4) | Quociente relacional exato | 5 | Aplicação |
| [P08.5](#r-P08-5) | Habilitação dinâmica | 6 | Aplicação |
| [P09.1](#r-P09-1) | Invisibilidade de mudança constitutiva | 7 | Integração interna |
| [P09.2](#r-P09-2) | Transporte por papéis | 7 | Aplicação |
| [P09.3](#r-P09-3) | Identidade exclusiva e rastreamento | 7 | Matemática conhecida |
| [P09.4](#r-P09-4) | Contrato temporizado exato | 7 | Integração interna |
| [P09.5](#r-P09-5) | Detectabilidade de secção | 7 | Aplicação |
| [P09.6](#r-P09-6) | Limite de horizonte | 7 | Aplicação |
| [P10.1](#r-P10-1) | Núcleo robusto de viabilidade | 8 | Matemática conhecida |
| [P10.2](#r-P10-2) | Reposição entre danos em S | 8 | Aplicação |
| [P10.3](#r-P10-3) | Balanços e renovação necessária | 8 | Aplicação |
| [P10.4](#r-P10-4) | Ablação e indispensabilidade | 8 | Aplicação |
| [P10.5](#r-P10-5) | Insuficiência do grafo/feedback | 8 | Integração interna |
| [P10.6](#r-P10-6) | Origem produtiva não identificável | 8 | Aplicação |
| [P10.7](#r-P10-7) | Renovação de fronteira/habilitação | 8 | Integração interna |
| [P10.8](#r-P10-8) | Alcance versus continuidade | 8 | Aplicação |
| [P11.1](#r-P11-1) | Recuperabilidade de M11 | 8 | Aplicação |
| [P11.2](#r-P11-2) | Álgebra de execuções | 4 | Aplicação |
| [P11.3](#r-P11-3) | Fechamento produtivo recorrente | 9 | Aplicação |
| [P11.4](#r-P11-4) | Expiração e recorrência necessária | 9 | Integração interna |
| [P11.5](#r-P11-5) | Garantia robusta recorrente | 9 | Aplicação |
| [P11.6](#r-P11-6) | Rotas e cortes recorrentes | 9 | Aplicação |
| [P11.7](#r-P11-7) | DAG de ocorrências e ciclos de tipos | 9 | Matemática conhecida |
| [P11.8](#r-P11-8) | Disponibilidade, origem e identidade | 9 | Integração interna |
| [VI00-U00](#r-VI00-U00) | U/C: observação e constituição | 2 | Integração interna |
| [VI00-U01](#r-VI00-U01) | F/D: condições futuras de passagem | 2 | Integração interna |
| [PVI02.1](#r-PVI02-1) | Quociente exato rotulado com escolhas | 10 | Aplicação |
| [PVI02.2](#r-PVI02-2) | Transporte exato de viabilidade e recorrência robusta | 10 | Integração interna |
| [PVI02.3](#r-PVI02-3) | Certificado suficiente de conservação unilateral | 10 | Aplicação |
| [PVI02.4](#r-PVI02-4) | Refinamento canônico relativo ao contrato finito | 10 | Aplicação |


## Apêndice B. Hipóteses preservadas e efeitos locais

### HIP-CIC-VI01-01

**Pergunta:** Em que sentido a tríade é necessária, suficiente, irredutível e exclusiva?

**Alternativas preservadas:** Tríade necessária/suficiente/irredutível/exclusiva; redução parcial; insuficiência; restrição de domínio.

**Relação:** Compromissos separáveis; alternativas podem valer em domínios distintos.

**Teste discriminante herdado:** Fixar sentidos antes dos casos e buscar distinção constitutiva que o vocabulário não determine.. Este campo registra a proposta/evidência da fonte; não afirma nova execução nesta passagem.

**Condição de retorno:** Critério adverso estável e fontes fundamentais reconciliadas..

**Efeito VI04:** Formalização não prova exclusividade ou suficiência da tríade. **Estado:** aberto.

### HIP-CIC-VI01-02

**Pergunta:** A espacialidade é condição irredutível, relacionalmente reconstruível ou co-constituída?

**Alternativas preservadas:** Condição irredutível; reconstrução por relações; co-constituição por organização/processos.

**Relação:** Concorrentes quanto à prioridade; podem coincidir descritivamente.

**Teste discriminante herdado:** Mesma métrica e recorte com condições de acesso distintas; redução sem termos espaciais tácitos.. Este campo registra a proposta/evidência da fonte; não afirma nova execução nesta passagem.

**Condição de retorno:** Reconstrução com consequências e perdas explícitas..

**Efeito VI04:** Espaço e representação permanecem distintos; prioridade ontológica aberta. **Estado:** aberto.

### HIP-CIC-VI01-03

**Pergunta:** A temporalidade pertence ao objeto, à realização ou ao domínio de investigação?

**Alternativas preservadas:** Condição de todo objeto; condição das realizações; regime dependente do domínio.

**Relação:** Incompatíveis quanto a objeto abstrato atemporal no mesmo alcance de H1.

**Teste discriminante herdado:** Separar estrutura estática do ato temporal de investigá-la; comparar informação perdida sem T.. Este campo registra a proposta/evidência da fonte; não afirma nova execução nesta passagem.

**Condição de retorno:** Argumento sobre temporalidade do objeto ou decisão explícita de alcance..

**Efeito VI04:** Precedência e duração separadas; objeto abstrato atemporal permanece questão. **Estado:** aberto.

### HIP-CIC-VI01-04

**Pergunta:** Há processos cuja descrição constitutiva dispensa unidade individual privilegiada?

**Alternativas preservadas:** Unidade fundamental; pluralidade situada de individuações; processos sem unidade privilegiada.

**Relação:** Não excluir pluralidade por nomear o processo inteiro indivíduo.

**Teste discriminante herdado:** Rede distribuída com padrões sobrepostos; testar critérios que selecionam unidade sem arbitrariedade.. Este campo registra a proposta/evidência da fonte; não afirma nova execução nesta passagem.

**Condição de retorno:** Critério de unidade com poder de discriminação independente de nomeação..

**Efeito VI04:** Recorrência de módulos não seleciona unidade privilegiada. **Estado:** aberto.

### HIP-CIC-VI01-05

**Pergunta:** A relação deriva da tríade, é fundamental, co-constitutiva ou depende do domínio?

**Alternativas preservadas:** A derivada; B fundamental anterior/adicional; C co-constitutiva; D dependente de domínio/nível.

**Relação:** Podem coexistir entre níveis; rivalidade exige mesmo caso e mesmos recursos.

**Teste discriminante herdado:** Fixar conteúdo de E/T/I e mostrar relações diferentes sob esse conteúdo; examinar traduções conservativas.. Este campo registra a proposta/evidência da fonte; não afirma nova execução nesta passagem.

**Condição de retorno:** Consequência diferente ou equivalência descritiva demonstrável..

**Efeito VI04:** Relação permanece questão fundamental; nenhuma redução ontológica nova. **Estado:** aberto.

### HIP-CIC-VI01-06

**Pergunta:** Qual a diferença entre disposição, possibilidade sob regra e atribuição inferencial de potencial?

**Alternativas preservadas:** Disposição constitutiva; possibilidade sob regra; atribuição inferencial provisória.

**Relação:** Podem ser complementares; nenhuma implica ocorrência.

**Teste discriminante herdado:** Mesmo potencial com admissão/seleção diferentes; ocorrência discrepante confronta regra e evidência.. Este campo registra a proposta/evidência da fonte; não afirma nova execução nesta passagem.

**Condição de retorno:** Mecanismo/regra e condições de atualização explicitados..

**Efeito VI04:** Disposição, possibilidade e potencial inferido permanecem distintos; execução não decorre da permissão. **Estado:** aberto.

### HIP-CIC-VI01-07

**Pergunta:** Qual a origem e o estatuto da fronteira na referência e no regime declarados?

**Alternativas preservadas:** Externa; produzida internamente; co-constituída; apenas recorte; indeterminada.

**Relação:** Mistas conforme relação e horizonte; recorte não equivale a produção.

**Teste discriminante herdado:** Mudar referência sem mudar vínculo; intervir na condição de passagem mantendo referência.. Este campo registra a proposta/evidência da fonte; não afirma nova execução nesta passagem.

**Condição de retorno:** Origem e efeito confrontáveis sem mover fronteira após resultado..

**Efeito VI04:** Fronteira pode ser externa, interna ou co-constituída; representação não determina sua origem. **Estado:** aberto.

### HIP-CIC-VI01-08

**Pergunta:** Duas álgebras, projeções de uma estrutura ou estrutura mais ampla conservam as responsabilidades polares?

**Alternativas preservadas:** Duas álgebras acopladas; estrutura com projeções; estrutura relacional mais ampla.

**Relação:** Alternativas de formalização; dualidade conceitual não prova independência algébrica.

**Teste discriminante herdado:** Comparar tarefas conservadas, composição, perdas e operadores realmente necessários.. Este campo registra a proposta/evidência da fonte; não afirma nova execução nesta passagem.

**Condição de retorno:** Comparação adequada sem transformar + em operador..

**Efeito VI04:** Três arquiteturas polares preservadas, sem escolha ontológica. **Estado:** aberto.

### HIP-CIC-VI01-09

**Pergunta:** Quais critérios justificam identidade sob substituição, transformação e bifurcação?

**Alternativas preservadas:** Conservação de componentes; de papéis; história/continuidade; políticas mistas.

**Relação:** Podem concordar em alguns casos e divergir em substituição e bifurcação.

**Teste discriminante herdado:** Substituição total, membros iguais com regra distinta, duplicação e rastreamento ambíguo.. Este campo registra a proposta/evidência da fonte; não afirma nova execução nesta passagem.

**Condição de retorno:** Justificação de elegibilidade e identidade além do contrato exato..

**Efeito VI04:** Transporte por papéis e rastreamento conservam contratos declarados; identidade ontológica aberta. **Estado:** aberto.

### HIP-CIC-VI01-10

**Pergunta:** A mudança de escala é mudança de resolução, de organização ou de individuação?

**Alternativas preservadas:** Resolução; organização de nível distinto; organizações sobrepostas; unidade apenas analítica.

**Relação:** Não são etapas obrigatórias; resolução e organização podem variar independentemente.

**Teste discriminante herdado:** Mesmo vínculo interno/externo por recorte versus mudança constitutiva sob referência fixa.. Este campo registra a proposta/evidência da fonte; não afirma nova execução nesta passagem.

**Condição de retorno:** Evidência de IO no nível candidato e compartilhamento preservado..

**Efeito VI04:** Reescala exige referência e contrato; mudança de representação não demonstra individuação. **Estado:** aberto.

### HIP-CIC-VI01-11

**Pergunta:** Que distinções uma refração conserva para a tarefa e o contexto receptor?

**Alternativas preservadas:** Perda/conservação de tarefa; transformação semântica; transformação efetiva da participação.

**Relação:** Responsabilidades relacionadas, sem equivalência automática.

**Teste discriminante herdado:** Mesma manifestação com f diferente; acrescentar contexto e testar novamente a base conjunta.. Este campo registra a proposta/evidência da fonte; não afirma nova execução nesta passagem.

**Condição de retorno:** Contrato de interpretação e tarefa, sem inversibilidade universal..

**Efeito VI04:** Fatoração conserva tarefas funcionais; refração permanece mais ampla e CAL-01 não recebe operador. **Estado:** aberto.

### HIP-CIC-VI01-12

**Pergunta:** Os critérios IO são adequados e suficientes no domínio ou exigem condições adicionais?

**Alternativas preservadas:** Critérios suficientes em domínio; condições adicionais; unidade somente representacional.

**Relação:** V no contrato não decide entre adequação e conveniência descritiva.

**Teste discriminante herdado:** Contrato constante/trivial e organizações com mesmo comportamento mas constituição diversa.. Este campo registra a proposta/evidência da fonte; não afirma nova execução nesta passagem.

**Condição de retorno:** Predicados justificados e evidência própria para cada IO..

**Efeito VI04:** IO01–05 permanecem critérios candidatos; preservação do avaliador não prova adequação. **Estado:** aberto.

### HIP-CIC-VI01-13

**Pergunta:** Que parcelas de sustentação são internas, externas, mistas ou indeterminadas?

**Alternativas preservadas:** Interna; externa; mista; origem indeterminada.

**Relação:** Podem coexistir; indispensabilidade interna contradiz suficiência exclusivamente externa apenas no mesmo regime.

**Teste discriminante herdado:** Ablação mantendo recursos/distúrbios; discriminar ingresso genérico e suporte organizado.. Este campo registra a proposta/evidência da fonte; não afirma nova execução nesta passagem.

**Condição de retorno:** Proveniência e contrafactuais pertinentes ao domínio..

**Efeito VI04:** Origem produtiva exige diagnóstico e informação suficientes; contribuições mistas preservadas. **Estado:** aberto.

### HIP-CIC-VI01-14

**Pergunta:** Autonomia refere-se a regulação, indispensabilidade, produção, fronteira ou integração?

**Alternativas preservadas:** Regulação; indispensabilidade interna; produção de suportes; fronteira/habilitação sustentada; integração forte.

**Relação:** Eixos não equivalentes; possível coexistência sem cadeia universal.

**Teste discriminante herdado:** Regulador com atuador externo, rotas redundantes e módulos que renovam sem integrar.. Este campo registra a proposta/evidência da fonte; não afirma nova execução nesta passagem.

**Condição de retorno:** Declarar autonomia de quê, perante quais variações e em qual horizonte..

**Efeito VI04:** Regulação, indispensabilidade, produção e integração permanecem propriedades distintas. **Estado:** aberto.

### HIP-CIC-VI01-15

**Pergunta:** Como distinguir renovação, persistência, recuperação e autogeração forte?

**Alternativas preservadas:** Reposição parcial; renovação de inventário; autogeração forte; persistência; recuperação.

**Relação:** Propriedades independentes conforme expiração, agenda e regime.

**Teste discriminante herdado:** M11 versus P10.7; perdas líquidas, suporte estável, privação e produção com lacunas.. Este campo registra a proposta/evidência da fonte; não afirma nova execução nesta passagem.

**Condição de retorno:** Completude constitutiva e continuidade justificadas..

**Efeito VI04:** M11, renovação síncrona e atratores distinguem recuperação, persistência e renovação; tese forte aberta. **Estado:** aberto.

### HIP-CIC-VI01-16

**Pergunta:** Quais informações devem ser conservadas para o diagnóstico de sustentação escolhido?

**Alternativas preservadas:** Estados/transições; guardas/tempo; origem/eventos; estrutura controle/distúrbio; evidência adicional.

**Relação:** Requisitos dependem da tarefa; segurança de imagem não é garantia recorrente.

**Teste discriminante herdado:** VI00-C01/C02: mesmo grafo com garantia diferente; mesmo laço com produção diferente.. Este campo registra a proposta/evidência da fonte; não afirma nova execução nesta passagem.

**Condição de retorno:** Certificado específico da representação e da pergunta..

**Efeito VI04:** Fatoração identifica informação necessária ao diagnóstico; monitor e proveniência não se substituem. **Estado:** aberto.

### HIP-CIC-VI01-17

**Pergunta:** Que diferença de referência ou operação sustentaria as direções das composições CAL-01?

**Alternativas preservadas:** Direção de referência; operações distintas; ambas; insuficiência; T+I distribuído ou questão ainda aberta.

**Relação:** Inversão escrita não decide comutação; não preencher simetria por conveniência.

**Teste discriminante herdado:** Definir domínio e operação antes de comparar ordem; distinguir Tiferet, Yesod e Malkut.. Este campo registra a proposta/evidência da fonte; não afirma nova execução nesta passagem.

**Condição de retorno:** Nova decisão autoral somente se houver proposta concreta de mudança da calibração..

**Efeito VI04:** CAL-01 literal; direção de referência e operação continuam questões sem operador novo. **Estado:** aberto.

### HIP-CIC-VI01-18

**Pergunta:** Quais fontes estão integralmente lidas, copiadas em bytes, parcialmente recuperadas ou apenas relatadas?

**Alternativas preservadas:** Originais recuperados; trechos/regras recuperados; relato de acesso anterior; lacuna atual.

**Relação:** Estatutos de acesso diferentes, sem contradição automática entre sessões.

**Teste discriminante herdado:** Confrontar bytes de PM/f2 e redação autônoma AD-01 quando acessíveis.. Este campo registra a proposta/evidência da fonte; não afirma nova execução nesta passagem.

**Condição de retorno:** Originais identificados e comparação cláusula a cláusula, sem reconstrução disfarçada..

**Efeito VI04:** PM/f2 e base local conferidos; AD/G/ARM continuam pendentes. **Estado:** aberto.

### HIP-CIC-VI02-A

**Pergunta:** Nomes fixos ou menus estratégicos de ações

**Alternativas preservadas:** Nomes fixos ou menus estratégicos de ações

**Relação:** Concorrentes conforme o contrato; exatidão forte e minimização estratégica têm tarefas diferentes

**Teste discriminante herdado:** Exibir jogos equivalentes por menus, mas distintos por nomes; não executado nesta passagem. Este campo registra a proposta/evidência da fonte; não afirma nova execução nesta passagem.

**Condição de retorno:** Fixar equivalência antes de agregar.

**Efeito VI04:** Ações identificadas mantidas; menus estratégicos sem teorema novo. **Estado:** aberto.

### HIP-CIC-VI02-B

**Pergunta:** Simulação unilateral ou exatidão bilateral

**Alternativas preservadas:** Simulação unilateral ou exatidão bilateral

**Relação:** Complementares por finalidade; recíproca contradita em geral

**Teste discriminante herdado:** PVI02.3 testada e contramodelos CM01–07; exatidão VI02 reproduzida. Este campo registra a proposta/evidência da fonte; não afirma nova execução nesta passagem.

**Condição de retorno:** Declarar direção e realizabilidade do seletor.

**Efeito VI04:** PVI02.3 incorpora quantificadores e predicados; sem recíproca geral. **Estado:** aberto.

### HIP-CIC-VI02-C

**Pergunta:** Ambiente comum ou fatores independentes

**Alternativas preservadas:** Ambiente comum ou fatores independentes

**Relação:** Modelos concorrentes; cópias independentes mudam a semântica

**Teste discriminante herdado:** Testemunho e=0/e=1 e composição espúria; sem teorema geral composicional. Este campo registra a proposta/evidência da fonte; não afirma nova execução nesta passagem.

**Condição de retorno:** Provar contrato global com correlações e recursos.

**Efeito VI04:** Testemunho ambiental comum preservado; sem teorema geral composicional. **Estado:** aberto.

### HIP-CIC-VI02-D

**Pergunta:** Informação completa ou parcial

**Alternativas preservadas:** Informação completa ou parcial

**Relação:** Regimes diferentes; seletor observacional é condição adicional

**Teste discriminante herdado:** CM04; leitura de B08; não executado algoritmo geral de crenças. Este campo registra a proposta/evidência da fonte; não afirma nova execução nesta passagem.

**Condição de retorno:** Especificar observações e construir política realizável.

**Efeito VI04:** Seletor observacional adicional requerido; sem algoritmo geral de crenças. **Estado:** aberto.

### HIP-CIC-VI02-E

**Pergunta:** Büchi, prazo e espaço finito/infinito

**Alternativas preservadas:** Büchi, prazo e espaço finito/infinito

**Relação:** Objetivos/regimes distintos e por vezes complementares

**Teste discriminante herdado:** Auditoria de posto e contramodelo de lacunas; sem controle contínuo geral. Este campo registra a proposta/evidência da fonte; não afirma nova execução nesta passagem.

**Condição de retorno:** Monitor de prazo e prova da abstração finita pertinente.

**Efeito VI04:** EVI03-03 incorporada; finitude e prazo físico distintos. **Estado:** aberto.

### HIP-CIC-VI02-F

**Pergunta:** Conservação de diagnóstico ou adequação constitutiva

**Alternativas preservadas:** Conservação de diagnóstico ou adequação constitutiva

**Relação:** Obrigações complementares; uma não implica outra

**Teste discriminante herdado:** Avaliador constante e módulos independentes; confronto com fechamento estrito B12. Este campo registra a proposta/evidência da fonte; não afirma nova execução nesta passagem.

**Condição de retorno:** Predicado independente com mecanismo/evidência por domínio.

**Efeito VI04:** Avaliador conservado não demonstra pertinência constitutiva. **Estado:** aberto.

### HIP-CIC-VI02-G

**Pergunta:** Duas álgebras, vistas ou estrutura mais ampla

**Alternativas preservadas:** Duas álgebras, vistas ou estrutura mais ampla

**Relação:** Alternativas preservadas; podem coincidir em fragmentos

**Teste discriminante herdado:** Leitura de relações tipadas; sem comparação completa de expressividade. Este campo registra a proposta/evidência da fonte; não afirma nova execução nesta passagem.

**Condição de retorno:** Construir tradução e caso discriminante sem impor ontologia.

**Efeito VI04:** Alternativas de álgebras, vistas e estrutura mais ampla preservadas. **Estado:** aberto.



## Apêndice C. Vocabulário e fontes de continuidade

| ID | Termo | Conteúdo candidato e limite |
|---|---|---|
| <a id="def-VI00-D01"></a>VI00-D01 | Espaço | Organização situada das condições de diferenciação, coexistência, relação e participação. **Limite:** Não é definição necessária e suficiente, métrica ou conjunto universal. |
| <a id="def-VI00-D02"></a>VI00-D02 | Tempo | Condições de ocorrência, ordem, duração, ritmo, continuidade e transformação. **Limite:** Ordem de registro e contador não esgotam tempo. |
| <a id="def-VI00-D03"></a>VI00-D03 | Indivíduo | Unidade cuja constituição, identidade, fronteira e continuidade são investigadas. **Limite:** Seleção não prova individuação; sem exigência universal de partes materiais. |
| <a id="def-VI00-D04"></a>VI00-D04 | Relação | Questão transversal: derivada, co-constitutiva, anterior ou adicional à tríade. **Limite:** Não foi escolhida posição ontológica definitiva. |
| <a id="def-VI00-D05"></a>VI00-D05 | Unidade/agregado/organização/indivíduo | Quatro responsabilidades distintas de análise, coleção, configuração e individuação. **Limite:** Não são estágios obrigatórios de uma ontologia. |
| <a id="def-VI00-D06"></a>VI00-D06 | Polaridade signo/luz e símbolo/kli | Perspectivas interna e externa da mesma referência individual. **Limite:** Não equivale automaticamente a Peirce, Cabala ou duas substâncias. |
| <a id="def-VI00-D07"></a>VI00-D07 | Domínio | Fenômenos e interpretações com regras e critérios declarados. **Limite:** Não simples etiqueta. |
| <a id="def-VI00-D08"></a>VI00-D08 | Dimensão | Aspecto ou variável de diferenciação. **Limite:** Não necessariamente dimensão geométrica ou independente. |
| <a id="def-VI00-D09"></a>VI00-D09 | Campo | Organização de condições de participação e transformação. **Limite:** Não necessariamente campo físico. |
| <a id="def-VI00-D10"></a>VI00-D10 | Ambiente | Entidades e condições externas pertinentes à referência. **Limite:** Exterioridade precisa de recorte justificado. |
| <a id="def-VI00-D11"></a>VI00-D11 | Fronteira | Distingue classificação relativa e condições efetivas de passagem. **Limite:** Uma lista ou contorno não prova produção de fronteira. |
| <a id="def-VI00-D12"></a>VI00-D12 | Interface/manifestação | Condições de relação através da fronteira e resultado distinguível da ocorrência. **Limite:** Não são o indivíduo completo. |
| <a id="def-VI00-D13"></a>VI00-D13 | Escala | Nível de organização ou resolução da pergunta. **Limite:** Resolução nova não produz indivíduo. |
| <a id="def-VI00-D14"></a>VI00-D14 | K0 e contexto local | K0 é referência persistente; c=(d,δ,s,F,Env,K) declara condições locais nesta edição (𝒜 é a grafia histórica de ambiente). **Limite:** K0 não é espaço, ambiente ou conjunto viável. |
| <a id="def-VI00-D15"></a>VI00-D15 | Ocorrência/relação/estado/história | O(c), Rel(c), St(c), evento e história com proveniência. **Limite:** Ocorrência identificada não é indivíduo; história não é só estado. |
| <a id="def-VI00-D16"></a>VI00-D16 | Admissibilidade | Permitido, negado ou indeterminado conforme informação e condições. **Limite:** Indeterminado não é falsidade; formação não é ocorrência. |
| <a id="def-VI00-D17"></a>VI00-D17 | Composição relacional | Junção por um mesmo estado intermediário bem tipado. **Limite:** Estados devem conter informação pertinente às guardas. |
| <a id="def-VI00-D18"></a>VI00-D18 | Trajetória rotulada | Registro (x,ℓ,y), concatenação de palavras com junção em y. **Limite:** Palavra vazia não é evento ocorrido. |
| <a id="def-VI00-D19"></a>VI00-D19 | Continuidade e identidade | Predicado contextual de continuidade e equivalência formal quando exigida. **Limite:** Tolerância local pode não ser transitiva. |
| <a id="def-VI00-D20"></a>VI00-D20 | Gramática e julgamentos | AST, tipos, Γ;c⊢e:τ e obrigações de admissão/registro. **Limite:** Sem parser ou interpretador geral demonstrado. |
| <a id="def-VI00-D21"></a>VI00-D21 | Configuração Q_c e semânticas | (V_ref,X,R,∂,H,L); V_ref corresponde ao V histórico de participantes; interpretação, operação e história distintas. **Limite:** Conf_c não é universo de todas as organizações reais. |
| <a id="def-VI00-D22"></a>VI00-D22 | Contrato de passagem Ω_e | Contextos, K0, regra/versionamento, obrigações/testemunhos e proveniência. **Limite:** Transportar obrigação não a demonstra; Ω_e não é projeto Ω. |
| <a id="def-VI00-D23"></a>VI00-D23 | Invariante | Igualdade preservada, propriedade preservada, extensão rastreável e revisão declarada são distintas. **Limite:** INV não são todos leis de conservação de grandezas. |
| <a id="def-VI00-D24"></a>VI00-D24 | Campo dinâmico | Possíveis, admissíveis, ativas, restrições e atributos W_attr (W histórico nessa entrada; W sem índice designa regiões vencedoras nos jogos). **Limite:** Inclusão é condição do modelo coerente, não licença para apagar observação discrepante. |
| <a id="def-VI00-D25"></a>VI00-D25 | Sensibilidade/Resp | Conjuntos de respostas a sondas e comparação por inclusão. **Limite:** Inclusão não mede intensidade ou probabilidade. |
| <a id="def-VI00-D26"></a>VI00-D26 | Restrição e bloqueadores | J(A)=J0∩interseção C_i; bloqueadores por candidato e origem. **Limite:** Mesmo conteúdo não elimina proveniências distintas. |
| <a id="def-VI00-D27"></a>VI00-D27 | Sistema e quociente exato | (X,A,T,O), ações parciais; partição conserva observação, habilitação e futuros. **Limite:** Mínimo operacional não é indivíduo ontológico. |
| <a id="def-VI00-D28"></a>VI00-D28 | Correspondência segura/exata | Inclusão de passos concretos versus conservação e levantamento exigidos. **Limite:** Segurança sobreaproximada não é equivalência. |
| <a id="def-VI00-D29"></a>VI00-D29 | Sistema aberto e ligação W_link (W histórico) | R_A em X_A×U_A×X_A×V_A, com ambiente comum quando declarado; contrato W_link entre valores de interfaces. **Limite:** Assinaturas fixas; variável ambiental comum não duplicável. |
| <a id="def-VI00-D30"></a>VI00-D30 | Refração por tarefa | Conservação de f por manifestação m via fatoração. **Limite:** Não esgota sentidos histórico, semântico ou físico de refração. |
| <a id="def-VI00-D31"></a>VI00-D31 | Ind_op e IO | Conjunção de cinco avaliações satisfeito/violado/? (V/F/? na entrada histórica) em contexto e horizonte; não confundir com conjunto seguro V. **Limite:** V no contrato não é prova de suficiência ontológica. |
| <a id="def-VI00-D32"></a>VI00-D32 | Transporte/identidade/genealogia | Preservação de papéis, descendência histórica e equivalência de identidade são distintas. **Limite:** Rastreamento único exige evidência de elegibilidade. |
| <a id="def-VI00-D33"></a>VI00-D33 | Contrato temporizado | Guarda, resposta, duração e próxima classe sob interface declarada. **Limite:** Requer incluir todo observável usado pelo interlocutor. |
| <a id="def-VI00-D34"></a>VI00-D34 | Secção | Evento situado com política de mudança constitutiva e origem/destino. **Limite:** Não é mera divisão descritiva ou falha de projeção. |
| <a id="def-VI00-D35"></a>VI00-D35 | Formas de sustentação | Persistência, manutenção, regulação, reparação, reconstituição, autogeração candidata e reprodução. **Limite:** Não constituem hierarquia universal de implicações. |
| <a id="def-VI00-D36"></a>VI00-D36 | Viabilidade/recuperação | Núcleo de segurança robusta e atrator de recuperação são conjuntos distintos. **Limite:** Recuperação não demonstra identidade anterior. |
| <a id="def-VI00-D37"></a>VI00-D37 | Ablação/corte minimal | Remoção de ações e família minimal por inclusão cuja retirada impede a propriedade. **Limite:** Minimal não é necessariamente menor cardinalidade. |
| <a id="def-VI00-D38"></a>VI00-D38 | Suportes/processos/ocorrências | Tipos, produtores, pais, validade, custos e identidades novas. **Limite:** Finitos tipos não implicam estado finito. |
| <a id="def-VI00-D39"></a>VI00-D39 | Álgebra de cobertura | Relações X×P(J)×X com união de eventos, soma, composição e estrela. **Limite:** Não conserva a ordem ou a multiplicidade do log. |
| <a id="def-VI00-D40"></a>VI00-D40 | FPR | Trajetória infinita segura desde x0 com cada evento de J infinitamente frequente. **Limite:** Não inclui integração ontológica, produção de leis ou origem sem semente. |
| <a id="def-VI00-D41"></a>VI00-D41 | Fechamentos | Topológico, operacional, produtivo e organizacional candidatos. **Limite:** Não há cadeia universal entre os quatro; FC-02 não é FPR. |
| <a id="def-VI00-D42"></a>VI00-D42 | Monitor de obrigações | Índice da próxima obrigação e bit de volta completa para objetivo Büchi. **Limite:** Memória pode ser necessária; não autoriza apagar perturbações. |

O glossário conserva as 42 entradas de origem como referência de localização e responsabilidade. As notações operacionais do corpo explicitam as convenções desta redação. Definições candidatas não são promovidas a verdades ontológicas pela inclusão no glossário. As 56 dependências VI00, divergências VI01 e índices históricos completos permanecem no acervo privado; os resultados, as hipóteses e seus limites estão expostos nesta edição e no material suplementar selecionado.

## Bibliografia verificável e alcance da consulta

Os IDs B01–B17 preservam o catálogo VI03 e seus localizadores, com dezesseis fontes substantivas lidas em trechos naquela passagem. Os campos VI04 descrevem o acesso anterior; os campos VI05 e o registro bibliográfico separado informam o acesso atual. F01–F02 são páginas institucionais sobre Campbell, F03 é texto primário da autora e F04–F05 são metadados editoriais; esses estatutos não se confundem. Nesta VI04 foram reabertos o catálogo, o laudo e os argumentos pertinentes, e consultadas online as fontes marcadas como reconferidas. Não se afirma nova leitura integral de todos os artigos. B14 permanece acesso parcial. A listagem distingue o alcance herdado de consulta da verificação desta redação.

### B01 — Kozen, Dexter (1998)

[Typed Kleene Algebra](https://www.cs.cornell.edu/~kozen/Papers/typed.pdf).

**Localizador herdado:** TR98-1669, §§1,2.1 e 3; PDF pp.1–5 e 9–10. **Alcance VI03:** Texto: introdução, axiomas e tipagem; sem auditoria do metateorema completo. **Alcance VI04:** Página/PDF primário reaberto online nesta VI04; leitura localizada.

**Alcance VI05:** PDF primário online e extração do PDF local. **Localizador atual:** Introdução, tipagem; PDF pp.1–5; metateorema não usado como premissa. **Função/limite:** Antecedente técnico pertinente; extração de fórmulas antigas tem artefatos, cotejo pelo enunciado e pelas provas próprias.

### B02 — Kozen, Dexter (1994)

[A Completeness Theorem for Kleene Algebras and the Algebra of Regular Events](https://www.cs.cornell.edu/kozen/Papers/ka.pdf). DOI: [10.1006/inco.1994.1037](https://doi.org/10.1006/inco.1994.1037).

**Localizador herdado:** §1.1, PDF p.3; introdução PDF pp.1–3. **Alcance VI03:** Introdução e exemplo relacional; não relida toda a prova de completude. **Alcance VI04:** Catálogo/localizador e confronto VI03 reutilizados; sem nova leitura integral.

**Alcance VI05:** PDF primário online e extração local. **Localizador atual:** §1.1, PDF p.3, exemplo relacional. **Função/limite:** Operações relacionais conhecidas; não reivindicar uma nova álgebra geral pela mudança de vocabulário.

### B03 — Cousot, Patrick; Cousot, Radhia (1977)

[Abstract Interpretation: A Unified Lattice Model for Static Analysis of Programs by Construction or Approximation of Fixpoints](https://www.di.ens.fr/~cousot/COUSOTpapers/publications.www/CousotCousot-POPL-77-ACM-p238--252-1977.pdf). DOI: [10.1145/512950.512973](https://doi.org/10.1145/512950.512973).

**Localizador herdado:** §§6–8, pp.242–244; PDF pp.6–8. **Alcance VI03:** Páginas digitalizadas efetivamente inspecionadas visualmente. **Alcance VI04:** Catálogo/localizador e confronto VI03 reutilizados; sem nova leitura integral.

**Alcance VI05:** PDF online sem texto extraível; imagem local reaberta. **Localizador atual:** PDF pp.6–8 / artigo pp.242–244. **Função/limite:** Contexto de aproximação por ordem e pontos fixos; não atribuir automaticamente as pequenas identidades conjuntivas ETLR a esse artigo.

### B04 — Alur, Rajeev; Henzinger, Thomas A.; Kupferman, Orna; Vardi, Moshe Y. (1998)

[Alternating Refinement Relations](https://www.cs.huji.ac.il/~ornak/publications/concur98.pdf). DOI: [10.1007/BFb0055622](https://doi.org/10.1007/BFb0055622).

**Localizador herdado:** §3, definição de A-simulation e Lemma 1; PDF pp.6–7. **Alcance VI03:** Texto e conferência visual da definição com quatro quantificadores. **Alcance VI04:** Catálogo/localizador e confronto VI03 reutilizados; sem nova leitura integral.

**Alcance VI05:** Duas aberturas online falharam por timeout; PDF local conferido e definição extraída. **Localizador atual:** §3, definição de A-simulation e Lemma 1; PDF pp.6–7. **Função/limite:** Ordem alternada de quantificadores pertinente; fonte não é idêntica ao certificado forte bilateral por nomes fixos de ações.

### B05 — Reissig, Gunther; Weber, Alexander; Rungger, Matthias (2017)

[Feedback Refinement Relations for the Synthesis of Symbolic Controllers](https://arxiv.org/pdf/1503.03715). DOI: [10.1109/TAC.2016.2593947](https://doi.org/10.1109/TAC.2016.2593947).

**Localizador herdado:** arXiv v3, Def.V.2, Thm.V.4, Def.VI.2 e Thm.VI.3; PDF pp.9–10,13. **Alcance VI03:** Definições e teoremas indicados; limites de implementação em pp.8–10. **Alcance VI04:** Catálogo/localizador e confronto VI03 reutilizados; sem nova leitura integral.

**Alcance VI05:** PDF arXiv primário online e extração local. **Localizador atual:** v3 de 02/01/2017; §V, Def.V.2/Thm.V.4 e §VI; PDF pp.9–10,13. **Função/limite:** Refinamento por realimentação tem hipóteses próprias de implementação e quantização; não equivale sem ressalvas a PVI02.3.

### B06 — Hopcroft, John (1971)

[An n log n Algorithm for Minimizing States in a Finite Automaton](https://www.cs.cmu.edu/~cdm/resources/Hopcroft1971.pdf).

**Localizador herdado:** STAN-CS-71-190, Introduction; Formal description; Correctness, PDF pp.5–7. **Alcance VI03:** Texto primário via leitor web, seções indicadas; bytes locais não obtidos. **Alcance VI04:** Catálogo/localizador e confronto VI03 reutilizados; sem nova leitura integral.

**Alcance VI05:** PDF primário online. **Localizador atual:** STAN-CS-71-190, Introdução, descrição formal e correção; PDF pp.5–7. **Função/limite:** Antecedente de minimização determinista; prova simples de refinamento não herda automaticamente sua complexidade n log n.

### B07 — Emerson, E. Allen; Jutla, Charanjit S. (1991)

[Tree Automata, Mu-Calculus and Determinacy](https://www.cs.cornell.edu/courses/cs6860/2010fa/Handouts/EmersonJutla91.pdf). DOI: [10.1109/SFCS.1991.185392](https://doi.org/10.1109/SFCS.1991.185392).

**Localizador herdado:** §§4.1–4.2, Def.4.1, Thm.4.1–4.4; PDF pp.8–9. **Alcance VI03:** Fórmulas e argumento de estratégias sem história; p.8 conferida visualmente. **Alcance VI04:** Catálogo/localizador e confronto VI03 reutilizados; sem nova leitura integral.

**Alcance VI05:** PDF primário online e extração local. **Localizador atual:** §§4.1–4.2; Def.4.1/Thms.4.1–4.4; PDF pp.8–9. **Função/limite:** Antecedente de jogos, paridade e pontos fixos. A fórmula Büchi e o critério SCC do volume têm provas próprias, sem atribuição literal.

### B08 — Chatterjee, Krishnendu; Doyen, Laurent; Henzinger, Thomas A.; Raskin, Jean-François (2007)

[Algorithms for Omega-Regular Games with Imperfect Information](https://lsv.ens-paris-saclay.fr/~doyen/papers/Algorithms_for_Omega-regular_Games_of_Imperfect_Information.pdf). DOI: [10.2168/LMCS-3(3:4)2007](https://doi.org/10.2168/LMCS-3(3:4)2007).

**Localizador herdado:** §2, PDF pp.4–5, definição observation-based; Lemma 2.1. **Alcance VI03:** Introdução pp.1,3 e definições p.4; sem revalidar algoritmos completos. **Alcance VI04:** Catálogo/localizador e confronto VI03 reutilizados; sem nova leitura integral.

**Alcance VI05:** PDF primário online e extração local. **Localizador atual:** §2, PDF pp.4–5, estratégias baseadas em observação. **Função/limite:** Delimita o regime de informação parcial; não autoriza aplicar o seletor por estado completo a uma interface parcial.

### B09 — Willems, Jan C. (2007)

[The Behavioral Approach to Open and Interconnected Systems](https://homes.esat.kuleuven.be/~sistawww/smc/jwillems/Articles/JournalArticles/2007.1.pdf). DOI: [10.1109/MCS.2007.906923](https://doi.org/10.1109/MCS.2007.906923).

**Localizador herdado:** pp.46–47,59–62; PDF pp.1–2,14–17; Tearing, Zooming, and Linking. **Alcance VI03:** Variáveis compartilhadas, terminais tipados e interconexão; não artigo integral. **Alcance VI04:** Catálogo/localizador e confronto VI03 reutilizados; sem nova leitura integral.

**Alcance VI05:** PDF autoral online e extração local. **Localizador atual:** Artigo pp.46–47,59–62; PDF pp.1–2,14–17. **Função/limite:** Interconexão por variáveis compartilhadas é comparação pertinente; não demonstra individuação ou causalidade dos modelos booleanos ETLR.

### B10 — Hordijk, Wim; Steel, Mike (2004)

[Detecting Autocatalytic, Self-Sustaining Sets in Chemical Reaction Systems](https://ir.canterbury.ac.nz/server/api/core/bitstreams/74a31f99-dbd0-456c-a427-4fbe7a647d86/content). DOI: [10.1016/j.jtbi.2003.11.020](https://doi.org/10.1016/j.jtbi.2003.11.020).

**Localizador herdado:** Preprint UCDMS2003/14, §§2–4, pp.3–5; PDF pp.4–6. **Alcance VI03:** Definições CRS/RAF, fecho e Lemma 4.1 via leitor web; download local HTTP403. **Alcance VI04:** Catálogo/localizador e confronto VI03 reutilizados; sem nova leitura integral.

**Alcance VI05:** Preprint primário online. **Localizador atual:** UCDMS2003/14, §§2–4; PDF pp.4–6, definições CRS/RAF e fecho. **Função/limite:** RAF usa condições químicas/catalíticas próprias; não reduzi-lo ao grafo potencial nem tratá-lo como refutado pelos contramodelos ETLR.

### B11 — Varela, Francisco G.; Maturana, Humberto R.; Uribe, R. (1974)

[Autopoiesis: The Organization of Living Systems, Its Characterization and a Model](https://monoskop.org/images/d/dd/Varela_Maturana_Uribe_1974_Autopoiesis.pdf). DOI: [10.1016/0303-2647(74)90031-8](https://doi.org/10.1016/0303-2647(74)90031-8).

**Localizador herdado:** §§2–6, pp.188–189; PDF pp.2–3. **Alcance VI03:** Digitalização lida visualmente, centro das páginas legível; sem reprodução da simulação original. **Alcance VI04:** Catálogo/localizador e confronto VI03 reutilizados; sem nova leitura integral.

**Alcance VI05:** Digitalização online sem texto extraível; imagem local inspecionada. **Localizador atual:** Artigo p.188, §3 e início de §4; imagem B11_p2.png. **Função/limite:** Definição enfatiza rede produtiva e realização da unidade. A margem direita da cópia tem perdas; não alegada leitura integral da definição em todos os detalhes ou do artigo.

### B12 — Montévil, Maël; Mossio, Matteo (2015)

[Biological Organisation as Closure of Constraints](https://montevil.org/publications/articles/2015-mm-organisation-closure-constraints/). DOI: [10.1016/j.jtbi.2015.02.029](https://doi.org/10.1016/j.jtbi.2015.02.029).

**Localizador herdado:** §§3–5, Defs.2–4; manuscrito 2016 PDF pp.8–10; HTML §5. **Alcance VI03:** Texto autoral §§3–5, dependência e fechamento estrito; sem estudo empírico. **Alcance VI04:** Catálogo/localizador e confronto VI03 reutilizados; sem nova leitura integral.

**Alcance VI05:** Texto autoral online e extração local. **Localizador atual:** §§3–5, Defs.2–4; HTML §5 Closure; manuscrito PDF pp.8–10. **Função/limite:** Fechamento estrito acrescenta condição de integração; recorrência de etiquetas não é equivalência com esse conceito.

### B13 — Rovelli, Carlo (1996)

[Relational Quantum Mechanics](https://arxiv.org/pdf/quant-ph/9609002). DOI: [10.1007/BF02302261](https://doi.org/10.1007/BF02302261).

**Localizador herdado:** arXiv v2, introdução e §II.A; PDF pp.2–3. **Alcance VI03:** Programa de reconstrução e exemplo dos dois observadores; não artigo integral. **Alcance VI04:** Catálogo/localizador e confronto VI03 reutilizados; sem nova leitura integral.

**Alcance VI05:** PDF primário arXiv online. **Localizador atual:** v2; introdução e §II.A, PDF pp.2–3. **Função/limite:** Comparação histórica delimitada à mecânica quântica relacional; não fundamenta a validade do U/C clássico, H1 ou IO suficientes.

### B14 — Ladyman, James (1998)

[What Is Structural Realism?](https://www.sciencedirect.com/science/article/abs/pii/S0039368198801295). DOI: [10.1016/S0039-3681(98)80129-5](https://doi.org/10.1016/S0039-3681(98)80129-5).

**Localizador herdado:** Introdução disponível na página editorial; corpo §§2–3 não recuperado. **Alcance VI03:** ACESSO PARCIAL: metadados e início da introdução; excluído da base de confronto substantivo. **Alcance VI04:** Catálogo/localizador e confronto VI03 reutilizados; sem nova leitura integral.

**Alcance VI05:** Abertura atual recusada por HTTP403. **Localizador atual:** Localizador herdado: introdução editorial parcial. **Função/limite:** Metadados herdados, sem novo corpo acessível e sem apoio substantivo a conclusões. Lacuna preservada.

### B15 — Alur, Rajeev; Dill, David L. (1994)

[A Theory of Timed Automata](https://www.cmi.ac.in/~madhavan/courses/verification-2011/alur-dill-tcs-94.pdf). DOI: [10.1016/0304-3975(94)90010-8](https://doi.org/10.1016/0304-3975(94)90010-8).

**Localizador herdado:** §1.1–1.2, §3.3–3.4, Defs.3.6–3.8; pp.185–186,193–194. **Alcance VI03:** Modelagem temporal e relógios, PDF pp.3–4,11–12. **Alcance VI04:** Catálogo/localizador e confronto VI03 reutilizados; sem nova leitura integral.

**Alcance VI05:** PDF primário online e extração local. **Localizador atual:** §§1.1–1.2 e 3.3–3.4; PDF pp.3–4,11–12. **Função/limite:** Tempo quantitativo e relógios têm semântica própria. Não atribuir a fonte os balanços elementares ou o critério SCC do volume.

### B16 — Lamport, Leslie (1978)

[Time, Clocks, and the Ordering of Events in a Distributed System](https://lamport.azurewebsites.net/pubs/time-clocks.pdf). DOI: [10.1145/359545.359563](https://doi.org/10.1145/359545.359563).

**Localizador herdado:** The Partial Ordering e Logical Clocks; pp.558–559, PDF pp.1–2. **Alcance VI03:** Definição de precedência e distinção de relógios lógicos e físicos. **Alcance VI04:** Catálogo/localizador e confronto VI03 reutilizados; sem nova leitura integral.

**Alcance VI05:** PDF do autor online e extração local. **Localizador atual:** The Partial Ordering e Logical Clocks; pp.558–559 / PDF pp.1–2. **Função/limite:** Precedência e relógios distintos; ciclo de tipos não é causalidade retroativa e ordem de registro não autentica causa.

### B17 — Rutten, J. J. M. M. (2000)

[Universal Coalgebra: A Theory of Systems](https://fldit-www.cs.tu-dortmund.de/~peter/Rutten/UniversalCoalgebra.pdf). DOI: [10.1016/S0304-3975(00)00056-6](https://doi.org/10.1016/S0304-3975(00)00056-6).

**Localizador herdado:** §2 Example 2.1; Cor.5.6, Props.5.7–5.8 e Thm.7.2; pp.9,33–34,38. **Alcance VI03:** PDF pp.6–7,31–32,36; não a monografia inteira. **Alcance VI04:** Página/PDF primário reaberto online nesta VI04; leitura localizada.

**Alcance VI05:** PDF primário online e extração local. **Localizador atual:** §2 Example 2.1; Cor.5.6 e Props.5.7–5.8, PDF pp.31–32 / artigo pp.33–34; Thm.7.2 PDF p.36 / artigo p.38. **Função/limite:** Pertinente a sistemas, homomorfismos e quocientes; não localiza emparelhamento perfeito nem identidade filosófica em P09.3.

### Fundamentação histórico-filosófica: consultas VI04 e reconferência VI05

**F01 — Joseph Campbell Foundation (s.d.).** [Joseph Campbell’s Four Functions of Myth](https://www.jcf.org/learn/joseph-campbell-four-functions-of-myth). Página, apresentação e quatro funções; linhas web 46–61. **Alcance:** Conteúdo institucional consultado nesta VI04; livros integrais de Campbell não relidos. Consulta VI04 e reconferência VI05: 26/11/2026.

**F02 — Joseph Campbell Foundation (s.d.).** [Joseph Campbell and the Hero’s Journey](https://www.jcf.org/learn/joseph-campbell-heros-journey). Apresentação e seção What is the Hero’s Journey. **Alcance:** Página institucional consultada; uso heurístico, sem homologação de universalidade. Consulta: 26/11/2026.

**F03 — Schmandt-Besserat, Denise (2013).** [Tokens and Writing: the Cognitive Development](https://sites.utexas.edu/dsb/tokens/tokens-and-writing-the-cognitive-development/). Texto da autora; publicado em Symbols at ‘Ain Ghazal, Berlin: Ex Oriente, p.56–62; resumo e introdução. **Alcance:** Página do texto primário consultada; recorte do antigo Oriente Próximo, sem genealogia universal da escrita. Consulta: 26/11/2026.

**F04 — Chajes, J. H. (2022).** [The Kabbalistic Tree / האילן הקבלי](https://www.psupress.org/books/titles/978-0-271-09345-1.html). Penn State University Press; ISBN 978-0-271-09345-1, registro editorial. **Alcance:** Metadados e apresentação editorial consultados; livro integral não lido nesta passagem. Consulta: 26/11/2026.

**F05 — Peirce, Charles Sanders; Peirce Edition Project (ed.) (1998).** [The Essential Peirce, Volume 2: Selected Philosophical Writings (1893–1913)](https://iupress.org/9780253211903/the-essential-peirce-volume-2/). Indiana University Press; ISBN 9780253211903, registro editorial. **Alcance:** Registro editorial; sem atribuição de equivalência substantiva à polaridade ETLR; endereço alternativo do Peirce Edition Project inacessível. Consulta: 26/11/2026.

### Corpus bibliográfico herdado, sem nova leitura integral

Campbell, Joseph. *The Hero with a Thousand Faces*. New York: Pantheon Books, 1949; *The Masks of God*. New York: Viking Press, 1959–1968, quatro volumes; Campbell e Bill Moyers, *The Power of Myth*, ed. Betty Sue Flowers, New York: Doubleday, 1988. Os livros identificam o corpus de partida; as afirmações localizadas desta redação usam F01–F02, sem inventar páginas. Cassirer, Eco, Lévi-Strauss e demais referências propostas na abertura do rev14 permanecem corpus comparativo a examinar, sem alegação de leitura substantiva nova.


### Fontes autorais e documentais

PM-01, versão 1.0 de 24/11/2026, §2.2, §§2.3–4; ETLR-00-f2, §§I–VI; Caderno Científico ETLR(f1), rev14, abertura e capítulos 00–11; ETLR-VI-00, §§3–10 e inventários; ETLR-VI-01, definições, matriz de 46 resultados, divergências e hipóteses; ETLR-VI-02, §§3–7 e PVI02.1–4; laudo, matriz individual e bibliografia VI03. Essas fontes autorais e documentais integram o acervo histórico privado, não distribuído integralmente neste pacote. Os localizadores textuais permitem reconhecer a proveniência sem expor caminhos internos. A R4 é fonte genealógica candidata, não substituição da cadeia científica. Os projetos privados e os 44 capítulos históricos referenciados não recebem certificação integral por essa remissão.

**Registro histórico do encerramento do primeiro ciclo (edição 1.0):** ETLR-VI-05 constituída como primeira edição científica 1.0 CANDIDATA, revista internamente nas perspectivas matemática, epistemológica/ontológica e científica/editorial/bibliográfica. Permanecem apreciação autoral e avaliação externa, sem homologação presumida. A preparação editorial VI06A não implica publicação externa, execução de motores ou início de Volume II. A revisão editorial candidata 1.1 explicita a finalidade investigativa sem reabrir esse ciclo matemático.

## Apêndice D. Candidatos históricos de integridade e sustentação

As tabelas seguintes são extraídas literalmente do rev14, com seus enunciados e pendências. Os rótulos históricos não são axiomas ontológicos homologados. Sua inclusão permite ao leitor identificar as responsabilidades mencionadas no corpo sem pressupor o acervo privado.

### D.INV — tabela preservada do rev14

Fonte: rev14, linha 723: Caderno Científico ETLR(f1), rev14, linha 723 (fonte histórica em acervo privado). O estatuto “nesta passagem” nas tabelas é histórico do rev14.

| ID histórico | Responsabilidade preservada | Pode mudar / condição |
|---|---|---|
| <a id="cand-INV-01"></a>INV-01 Gramática | Formação e composição conforme a versão de linguagem declarada | Expressões; revisão da gramática requer tradução/registro, não invariância de toda versão. |
| <a id="cand-INV-02"></a>INV-02 Identificação | Distinção das ocorrências e vínculos entre referências | Nomes, representações, identidades individuais sob critérios próprios. |
| <a id="cand-INV-03"></a>INV-03 Referência | K0 ou reenquadramento explícito | K local, domínio, escala. |
| <a id="cand-INV-04"></a>INV-04 Proveniência | Origem, dependências, regra e revisões recuperáveis | Conclusões e estados; corrigir sem apagar ocorrência histórica. |
| <a id="cand-INV-05"></a>INV-05 Fronteira relativa | Referente e condições da classificação explícitos | Fronteira efetiva, classificação e interfaces. |
| <a id="cand-INV-06"></a>INV-06 Composição | Compatibilidade de tipos, testemunho comum e obrigações | Ordem e resultados; associatividade das relações fixas, não de toda política de execução. |
| <a id="cand-INV-07"></a>INV-07 Continuidade condicional | Critério de continuidade declarado quando satisfeito | Identidade pode romper-se; estado e componentes podem mudar. |
| <a id="cand-INV-08"></a>INV-08 Reescala | Vínculo rastreável entre origem e representação resultante | Resolução, representação, propriedades acessíveis; não demonstra individuação. |

### D.AS — tabela preservada do rev14

Fonte: rev14, linha 2128: Caderno Científico ETLR(f1), rev14, linha 2128 (fonte histórica em acervo privado). O estatuto “nesta passagem” nas tabelas é histórico do rev14.

| Candidato histórico | Estatuto nesta passagem | Obrigação que permanece |
| --- | --- | --- |
| <a id="cand-AS-01"></a>AS-01 Constituição | Predicado V explicitado e distinguido do núcleo W* | Justificar inventário e critérios por domínio; V não é K0 |
| <a id="cand-AS-02"></a>AS-02 Dependência efetiva | Testemunhos locais, ablações e cortes separados em P10.4 | Intervenções admissíveis e evidência causal própria do domínio |
| <a id="cand-AS-03"></a>AS-03 Abertura ambiental | Recursos e substituição externa aparecem no balanço P10.3 | Caracterizar o que entra como recurso e o que entra como suporte organizado |
| <a id="cand-AS-04"></a>AS-04 Temporalidade | Prefixos, horizonte, ordem de atualização e monitor ambiental explicitados | Uma sequência discreta não demonstra a ontologia do tempo |
| <a id="cand-AS-05"></a>AS-05 Distinção de identidade | Função, identidade e genealogia permanecem distintas | IO-03/04 e rastreamento não ambíguo; não basta estado final |
| <a id="cand-AS-06"></a>AS-06 Fechamento condicionado | Ciclos potenciais insuficientes; viabilidade depende de produção, recursos e regime | Não converter um grafo em certificado autônomo de fechamento constitutivo |
| <a id="cand-AS-07"></a>AS-07 Reconstituição | Recuperação por alcance separada de permanência e identidade | Critérios de ruptura, suspensão e novo indivíduo |
| <a id="cand-AS-08"></a>AS-08 Multiescalaridade | Nenhuma passagem automática da manutenção de partes à autonomia do coletivo | Contratos integrados, condições coletivas e IO na escala considerada |

### D.AR — tabela preservada do rev14

Fonte: rev14, linha 2455: Caderno Científico ETLR(f1), rev14, linha 2455 (fonte histórica em acervo privado). O estatuto “nesta passagem” nas tabelas é histórico do rev14.

| Candidato histórico | Estatuto após esta passagem | Obrigação discriminante |
| --- | --- | --- |
| <a id="cand-AR-01"></a>AR-01 Distinção constitutiva | Tipos formais separados em S,P,X e eventos | Justificar interpretação no domínio |
| <a id="cand-AR-02"></a>AR-02 Dependência contextual | Guardas, efeito e orçamento explícitos | Intervenção admissível e rotas concorrentes |
| <a id="cand-AR-03"></a>AR-03 Sustentação efetiva | Circuito insuficiente, contramodelos reproduzidos | Observar produção e uso causal, não só rótulos |
| <a id="cand-AR-04"></a>AR-04 Fechamento condicionado | Regime e quantificadores incorporados | Não mudar ambiente após observar o resultado |
| <a id="cand-AR-05"></a>AR-05 Recuperabilidade | P11.1 caracteriza M11; perdas arbitrárias não seguem | Declarar classe e intervalo dos danos |
| <a id="cand-AR-06"></a>AR-06 Constituição inicial | Semente separada da manutenção recorrente | Testar iniciação sem suporte e rotas lentas |
| <a id="cand-AR-07"></a>AR-07 Historicidade | Log de ocorrências e pais exemplificado | Dados auditáveis do domínio; não apenas identificadores |
| <a id="cand-AR-08"></a>AR-08 Identidade contextual | P11.8 separa retorno e reconhecimento | Política IO-03/04 e genealogia independente |
| <a id="cand-AR-09"></a>AR-09 Polaridade | Projeção externa não determina produção/recuperação | Suficiência das observações e contratos |
| <a id="cand-AR-10"></a>AR-10 Composição multiescalar | FPR de módulos não basta para unidade coletiva | Suportes, fronteira e IO na escala integrada |


## Apêndice E. Revisão crítica interna e estatuto histórico da edição 1.0

### E.1 Perspectiva matemática

A unidade de auditoria é cada um dos cinquenta registros, não a contagem de parágrafos intitulados demonstração. Foram examinados enunciado, domínio, quantificadores, prova integrada, exemplo ou contramodelo, dependências e alcance das referências. A auditoria individual encontra-se em **AUDITORIA_50_RESULTADOS**. “Sustentado condicionalmente” significa que o argumento textual foi considerado válido sob suas premissas explícitas nesta revisão interna. Não equivale a certificação por assistente de provas, parecer externo ou validação do modelo no domínio de aplicação.

O núcleo matemático tem quatro estruturas recorrentes: composição por testemunho comum, fatoração de funções por fibras, estabilidade de partições e predecessores estratégicos com pontos fixos. Reutilizar essas estruturas é legítimo e reduz a dependência de terminologia privada. Também limita a reivindicação matemática: aplicar o lema de fatoração a guarda, origem e secção não produz três lemas novos independentes. A classificação de doze registros como matemática conhecida, vinte e sete como aplicações e onze como integrações internas é mantida após confronto individual. Ela descreve o papel do registro no corpus; não mede originalidade externa, dificuldade ou independência lógica.

Os resultados de composição e fatoração não requerem genericamente finitude de todos os conjuntos. As construções algorítmicas de refinamento e as caracterizações de jogos aqui verificadas declaram o regime finito pertinente. Não se transfere a parada do algoritmo a um sistema com história ilimitada, recursos sem teto ou relógios reais apenas porque há poucos tipos de suporte. Um argumento de levantamento de todo prefixo finito não deve, fora das hipóteses dadas, ser anunciado como algoritmo efetivo de realização de toda história infinita.

PVI02.4 recebeu uma delimitação no próprio enunciado: a partição final satisfaz C1–C3 e é a mais grosseira relativa a esses dados fixos. C4 não é decidida pelo refinamento. A prova já continha essa ressalva, mas a conclusão abreviada anterior dizia “satisfaz o certificado”, permitindo uma leitura mais ampla. A alteração fecha essa diferença entre título-resumo e prova; não demonstra a suficiência constitutiva da memória, nem altera o resultado histórico original.

O certificado exato conserva pares de **classe sucessora e etiqueta por ação**. Igualdade das classes marginais e igualdade das etiquetas marginais, separadamente, não bastam quando a correlação entre elas importa. Em PVI02.3 a inclusão é do conjunto concreto projetado no conjunto abstrato, com controle escolhido antes do resultado ambiental. A conservação é unilateral, inclusive quando o abstrato perde por admitir uma perturbação extra. Um seletor que distingue estados ocultos não é implementável automaticamente por quem só observa sua fibra.

P11.3 trata existência de trajetória; P11.5 trata uma política contra todos os resultados ambientais permitidos. A primeira prova usa uma componente fortemente conexa no grafo expandido seguro. A segunda usa um produto com monitor e a ordem de escolhas do jogo. A revisão das dependências distingue esses argumentos: o critério cooperativo não é premissa lógica necessária da caracterização robusta. Em ambos, as etiquetas produtivas são dados semanticamente justificados no modelo, e não inferências produzidas pela teoria de grafos.

Para políticas estacionárias vencedoras no produto finito, um ciclo alcançável inteiramente fora da aceitação permitiria ao ambiente impedir a próxima volta. Sua ausência dá um limite discreto próprio da política. Isso não estabelece um prazo escolhido pela aplicação nem uma duração física sem limite superior por passo. Uma execução Büchi arbitrária pode continuar produzindo nos tempos 2^n. Em P11.4 a janela uniforme L decorre de outra premissa, a validade máxima dos suportes, e não do simples uso de Büchi.

Não foi encontrado, nesta leitura, contramodelo aos cinquenta argumentos integrados quando todas as respectivas premissas são mantidas. Essa conclusão é um parecer interno delimitado, sujeito a erro de revisão e a novos contraexemplos; não é “aprovação automática” de cinquenta teoremas. Algumas conclusões são identidades elementares ou contramodelos existenciais. Outras exigem hipóteses de modelagem fortes e não resolvidas para aplicações reais. Essas diferenças permanecem nas fichas individuais.

### E.2 Perspectiva epistemológica e ontológica

A arquitetura formal exige uma tarefa antes de avaliar a suficiência de uma representação. Se o diagnóstico constitutivo for estipulado e preservado, demonstrou-se conservação daquele diagnóstico. Para concluir que ele reconhece indivíduos no domínio seria preciso justificar seu conteúdo por critérios independentes da facilidade de preservá-lo. Declarar Ind_op sempre satisfeito produziria um avaliador perfeitamente conservado e cientificamente não discriminante. Esse caso impede converter sucesso representacional em prova de individuação.

H1, H2 e H3 têm obrigações distintas. H1 contém ao menos necessidade, suficiência, irredutibilidade e exclusividade da tríade. Uma resposta favorável a uma dessas exigências não encerra as demais. H2 requer evidência sobre organização da experiência e do conhecimento humanos; o corpus comparativo presente não a fornece. H3 pode obter sustentação local pela explicitação de diferenças que outros recortes omitem, mas tal ganho deve ser comparado ao custo da descrição e a linguagens alternativas. O êxito dos modelos booleanos construídos no próprio vocabulário não discrimina H1 de uma convenção metodológica.

O estatuto da relação permanece aberto: derivada de E,T,I; anterior ou adicional; co-constitutiva; ou dependente de domínio e nível. Uma tradução que sempre rebatize relação como espaço, tempo ou indivíduo, sem fixar previamente o que cada termo conserva, não é teste de redução. O confronto exige declarar vocabulário de partida, tradução, tarefa, perdas e possibilidade de resultado adverso. O mesmo vale para processo, informação e modalidade, sem impor que sejam novas primitivas.

Definir espaço por condições relacionais é uma caracterização candidata compatível com algumas alternativas, não uma demonstração de prioridade do espaço sobre a relação. Definir o indivíduo como unidade investigada permite formular a pergunta, mas não selecionar por si uma unidade privilegiada. A definição de tempo inclui ordem e duração sem decidir se todo objeto abstrato possui temporalidade própria. O tempo de investigar uma estrutura não fornece essa propriedade à estrutura. Essas são tensões filosóficas efetivas, mantidas como questões e não eliminadas por normalização terminológica.

A prova matemática utiliza conceitos de relação, função e conjunto como instrumentos explícitos. Portanto este volume não deriva uma ontologia relacional a partir de premissas inteiramente livres de relações. Isso seria circular se fosse apresentado como demonstração de H1. Como a pretensão demonstrada é condicional e representacional, a dependência é uma escolha de formalização que deve permanecer visível. A ausência de ciclos no grafo de dependências das provas também não decide, por si, circularidade ou suficiência de uma fundamentação filosófica.

CAL-01 é referência autoral protegida, reproduzida literalmente. O + informal, Da’at como passagem, os dois I em Yesod e a ausência de T+I isolado não recebem interpretação algébrica por analogia. K0 conserva a referência da investigação, sem tornar-se estado inicial ou região vencedora. Signo/luz e símbolo/kli mantêm os polos interno e externo do vocabulário autoral. Uma mudança de observação não é, por definição, transformação do fenômeno; uma mudança de referência não é individuação do conjunto; proveniência registrada não equivale a causalidade empiricamente autenticada.

As tradições filosóficas e históricas ajudam a constituir problemas e alternativas. A comparação pode ser produtiva sem provar transmissão histórica, universalidade intercultural ou uma ontologia. As páginas institucionais sobre Campbell têm estatuto distinto de um texto primário do próprio Campbell. Os registros editoriais de Chajes e Peirce identificam obras, sem fornecer exame integral de seus argumentos. Essas diferenças de fonte impedem usar convergência de nomes, diagramas ou narrativas como premissa tácita de um teorema.

### E.3 Perspectiva científica, editorial e bibliográfica

A autonomia obtida é a do fragmento formal e dos confrontos explicitamente apresentados. O leitor pode reconstruir as equações e os argumentos sem executar QOREL, ARM ou ETLR-MO. Uma folha de notação, definições de termos técnicos antes do uso essencial, índices e tabelas completas dos candidatos históricos reduzem obstáculos expositivos. A fundamentação genealógica continua dependente das fontes identificadas, e a conformidade integral com contratos ARM ausentes não foi certificada. Não se declara que a recuperação editorial tornou completo o programa científico.

As referências foram revistas por função: antecedente técnico, comparação conceitual, registro de metadados ou acesso parcial. P09.3 conserva uma prova autônoma por equivalência e pela definição de emparelhamento perfeito; B17 não foi localizado como fonte específica desses argumentos e deixa de aparecer como apoio direto. Em P11.3, B07 e B15 são contexto de aceitação e tempo, não localizadores da prova SCC e de suas cotas. A matemática conhecida continua conhecida quando o manuscrito oferece sua demonstração elementar; retirar uma atribuição inadequada não cria novidade.

O registro bibliográfico informa o que foi realmente reaberto nesta passagem. B04 foi recuperado pela cópia local após falhas da abertura online. B14 permanece sem corpo acessível e sem uso substantivo. As digitalizações B03 e B11 exigem leitura visual; a margem da cópia B11 apresenta perdas. As demais fontes possuem localizadores por seção, definição, teorema e página da versão consultada. Não se alega releitura integral de todos os artigos ou livros, revisão sistemática exaustiva de anterioridade ou originalidade externa estabelecida.

Os controles reproduzidos são execuções reais de programas sintéticos em cópias temporárias. O controle novo de duas obrigações amplia a evidência sobre monitor e produto em universos pequenos explicitados. Uma prova textual, uma comparação computacional e uma aplicação empírica são evidências de tipos diferentes. As contagens não são somadas para criar uma impressão de população científica ampliada; jogos amostrados e palavras enumeradas são relatados separadamente. Não houve avaliação externa independente por matemático, filósofo ou editor humano.

O primeiro ciclo editorial-científico encerrou-se com a edição 1.0 **CANDIDATA**, seus pareceres internos, erratas e perguntas abertas. A autorização da autora para executá-lo está registrada; aprovação autoral do conteúdo final, homologação externa, publicação e abertura de outro volume não são inferidas desse encerramento. Esse registro histórico não constitui aprovação da revisão editorial candidata 1.1.

## Apêndice F. Questões abertas e condições para avaliação externa

O inventário seguinte organiza pendências efetivas sem substituir os IDs HIP-CIC preservados, nem reconstruir uma lista G01–G20 inexistente na base. A designação Q05 identifica questões desta entrega, e não novas conclusões.

| Questão | Vínculo preservado | Estado e consequência | Condição de avanço |
|---|---|---|---|
| Q05-01 Estatuto de E,T,I | H1–H3; HIP-CIC-VI01-01–05 | Necessidade, suficiência, irredutibilidade e exclusividade universais não demonstradas | Fixar sentidos e domínio antes de confrontar alternativas e casos adversos |
| Q05-02 Relação e demais alternativas | HIP-CIC-VI01-05; FUND ancestral | Prioridade/derivação/co-constituição continuam concorrentes em alcances declarados | Traduções conservativas e diferença verificável, sem rebatismo por conveniência |
| Q05-03 Adequação de IO | HIP-CIC-VI01-12; VI02-F | IO01–05 são candidatos; Ind_op é avaliador definido | Evidência independente por critério, unidade e domínio; testar casos triviais e sobrepostos |
| Q05-04 Memória e etiquetas | C4; VI01-16 e VI02-F | Algoritmo não certifica suficiência da modelagem ou origem produtiva real | Inventário, observáveis, proveniência e regra de atualização justificáveis no domínio |
| Q05-05 Observação parcial | VI02-D; PVI02.3 | Seletor por estado pode ser irrealizável na interface | Definir observação, memória disponível e seletor uniforme/realizável com prova própria |
| Q05-06 Prazo e infinitude | VI02-E; P11.4/5 | Finitude e validade máxima são premissas; sem garantia contínua geral | Monitor de prazo, unidades, duração máxima e prova da abstração pertinente |
| Q05-07 Composição e escala | VI01-10, VI02-C | Ambiente comum e correlações não podem ser duplicados; FPR de partes não individua coletivo | Contrato integrado de recursos, eventos, fronteira, informação e IO coletivos |
| Q05-08 Identidade e origem | VI01-09/13; P09.3/5, P10.6 | Elegibilidade e política históricas exigem evidência própria | Registros e intervenções admissíveis que discriminem continuidade, descendência e reconstituição |
| Q05-09 Autogeração forte | VI01-14/15; P10.7/P11.3 | Renovação de inventário estipulado não prova sua completude constitutiva | Justificar suportes, fronteira, sementes, integração e dependência ambiental sem circularidade |
| Q05-10 Anterioridade | Matriz VI03/VI05; B01–B17 | Originalidade externa não estabelecida | Busca e comparação técnica mais ampla, inclusive contra reformulações conhecidas |
| Q05-11 Fontes documentais ausentes | HIP-CIC-VI01-18; PM-01 | AD-01 autônomo, G01–G20 e contratos ARM completos não identificados inequivocamente | Recuperar originais/versionamento e confrontar cláusulas sem reconstrução disfarçada |
| Q05-12 Avaliação externa e dados | H2/H3; todos os modelos aplicados | Sem revisão independente e sem validação empírica | Selecionar domínio, métodos e medidas, registrar previsões e comparar alternativas |

Para uma futura avaliação matemática externa, a unidade de trabalho deve ser o enunciado completo com suas premissas, prova e contramodelos, acompanhado da matriz de dependências. O avaliador deverá poder reformular o argumento em notação usual, contestar a minimalidade ou suficiência de uma premissa e relatar um contraexemplo que mantenha todas as condições. Códigos, versões, sementes e saídas disponíveis permitem reproduzir os controles; não substituem a avaliação das demonstrações gerais.

Para avaliação filosófica, é necessário preservar o conteúdo forte de H1 e explicitar o que contaria contra cada uma de suas partes. A avaliação deverá distinguir definição operacional de tese constitutiva e perguntar se as traduções preservam diferenças ou apenas as renomeiam. Não se solicita que o avaliador aceite QOREL/ARM como pressuposto. A genealogia pode ser examinada como fonte histórica, separadamente dos argumentos de validade.

Para avaliação científica aplicada, o protocolo deverá selecionar um domínio, identificar como se medem estados, suportes, ações, tempos e fronteiras, justificar a atribuição de origem e registrar as informações indisponíveis. Deve declarar previsões ou discriminações antes dos resultados e comparar ao menos uma alternativa pertinente. Evidência favorável a uma aplicação não encerra universalidade ontológica. A pesquisa sobre domínios mental ou abstrato requer critérios próprios; o sentido filosófico espiritual/astral preservado não é anunciado como observação empírica.

A apreciação autoral das formulações candidatas e a decisão específica sobre publicação permanecem necessárias. A preparação desta seleção não envia documentos a terceiros nem inicia o Volume II. Os originais e a continuidade investigativa permanecem preservados separadamente.

## Apêndice G. Índice científico consolidado

### Resultados e demonstrações

| ID | Enunciado | Demonstração | Dependências do argumento |
|---|---|---|---|
| P02.1 | [Associatividade condicionada](#r-P02-1) | [Prova](#prova-P02-1) | Definições locais |
| P02.2 | [Imagem da composição](#r-P02-2) | [Prova](#prova-P02-2) | Definições locais |
| P02.3 | [Trajetórias rotuladas](#r-P02-3) | [Prova](#prova-P02-3) | Definições locais |
| P03.1 | [Levantamento por extremos](#r-P03-1) | [Prova](#prova-P03-1) | P02.2 |
| P03.2 | [Guarda e história ocultada](#r-P03-2) | [Prova](#prova-P03-2) | P08.3 |
| P04.1 | [Levantamento por cada representante](#r-P04-1) | [Prova](#prova-P04-1) | Definições locais |
| P04.2 | [Preservação da guarda](#r-P04-2) | [Prova](#prova-P04-2) | P08.3 |
| P05.1 | [Contração conjuntiva](#r-P05-1) | [Prova](#prova-P05-1) | Definições locais |
| P05.2 | [Reabertura exata](#r-P05-2) | [Prova](#prova-P05-2) | P05.1 |
| P05.3 | [Campo omitido](#r-P05-3) | [Prova](#prova-P05-3) | P04.1 P04.2 |
| P06.1 | [Insuficiência de J para revisão](#r-P06-1) | [Prova](#prova-P06-1) | P05.2 P08.3 |
| P06.2 | [Observabilidade relativa](#r-P06-2) | [Prova](#prova-P06-2) | P08.3 |
| P06.3 | [Limite de redução em M3](#r-P06-3) | [Prova](#prova-P06-3) | P08.3 |
| P06.4 | [Quociente exato mínimo](#r-P06-4) | [Prova](#prova-P06-4) | Definições locais |
| P07.1 | [Fatoração dinâmica e composição](#r-P07-1) | [Prova](#prova-P07-1) | Definições locais |
| P07.2 | [Sobreaproximação segura](#r-P07-2) | [Prova](#prova-P07-2) | P02.2 |
| P07.3 | [Alternância de regimes](#r-P07-3) | [Prova](#prova-P07-3) | P06.4 |
| P08.1 | [Composição de interfaces](#r-P08-1) | [Prova](#prova-P08-1) | Definições locais |
| P08.2 | [Abstração versus composição](#r-P08-2) | [Prova](#prova-P08-2) | P02.2 |
| P08.3 | [Fatoração de tarefas](#r-P08-3) | [Prova](#prova-P08-3) | Definições locais |
| P08.4 | [Quociente relacional exato](#r-P08-4) | [Prova](#prova-P08-4) | P04.1 |
| P08.5 | [Habilitação dinâmica](#r-P08-5) | [Prova](#prova-P08-5) | P07.1 P04.2 |
| P09.1 | [Invisibilidade de mudança constitutiva](#r-P09-1) | [Prova](#prova-P09-1) | Definições locais |
| P09.2 | [Transporte por papéis](#r-P09-2) | [Prova](#prova-P09-2) | P07.1 P08.3 |
| P09.3 | [Identidade exclusiva e rastreamento](#r-P09-3) | [Prova](#prova-P09-3) | Definições locais |
| P09.4 | [Contrato temporizado exato](#r-P09-4) | [Prova](#prova-P09-4) | P04.2 P08.3 |
| P09.5 | [Detectabilidade de secção](#r-P09-5) | [Prova](#prova-P09-5) | P08.3 P09.1 |
| P09.6 | [Limite de horizonte](#r-P09-6) | [Prova](#prova-P09-6) | Definições locais |
| P10.1 | [Núcleo robusto de viabilidade](#r-P10-1) | [Prova](#prova-P10-1) | Definições locais |
| P10.2 | [Reposição entre danos em S](#r-P10-2) | [Prova](#prova-P10-2) | Definições locais |
| P10.3 | [Balanços e renovação necessária](#r-P10-3) | [Prova](#prova-P10-3) | Definições locais |
| P10.4 | [Ablação e indispensabilidade](#r-P10-4) | [Prova](#prova-P10-4) | P10.1 |
| P10.5 | [Insuficiência do grafo/feedback](#r-P10-5) | [Prova](#prova-P10-5) | Definições locais |
| P10.6 | [Origem produtiva não identificável](#r-P10-6) | [Prova](#prova-P10-6) | P08.3 |
| P10.7 | [Renovação de fronteira/habilitação](#r-P10-7) | [Prova](#prova-P10-7) | Definições locais |
| P10.8 | [Alcance versus continuidade](#r-P10-8) | [Prova](#prova-P10-8) | P10.1 |
| P11.1 | [Recuperabilidade de M11](#r-P11-1) | [Prova](#prova-P11-1) | Definições locais |
| P11.2 | [Álgebra de execuções](#r-P11-2) | [Prova](#prova-P11-2) | Definições locais |
| P11.3 | [Fechamento produtivo recorrente](#r-P11-3) | [Prova](#prova-P11-3) | Definições locais |
| P11.4 | [Expiração e recorrência necessária](#r-P11-4) | [Prova](#prova-P11-4) | Definições locais |
| P11.5 | [Garantia robusta recorrente](#r-P11-5) | [Prova](#prova-P11-5) | P10.1 |
| P11.6 | [Rotas e cortes recorrentes](#r-P11-6) | [Prova](#prova-P11-6) | P11.5 P10.4 |
| P11.7 | [DAG de ocorrências e ciclos de tipos](#r-P11-7) | [Prova](#prova-P11-7) | Definições locais |
| P11.8 | [Disponibilidade, origem e identidade](#r-P11-8) | [Prova](#prova-P11-8) | P08.3 P10.6 P10.8 |
| VI00-U00 | [U/C: observação e constituição](#r-VI00-U00) | [Prova](#prova-VI00-U00) | Definições locais |
| VI00-U01 | [F/D: condições futuras de passagem](#r-VI00-U01) | [Prova](#prova-VI00-U01) | Definições locais |
| PVI02.1 | [Quociente exato rotulado com escolhas](#r-PVI02-1) | [Prova](#prova-PVI02-1) | P04.1 P04.2 |
| PVI02.2 | [Transporte exato de viabilidade e recorrência robusta](#r-PVI02-2) | [Prova](#prova-PVI02-2) | PVI02.1 P10.1 P10.8 P11.5 |
| PVI02.3 | [Certificado suficiente de conservação unilateral](#r-PVI02-3) | [Prova](#prova-PVI02-3) | Definições locais |
| PVI02.4 | [Refinamento canônico relativo ao contrato finito](#r-PVI02-4) | [Prova](#prova-PVI02-4) | PVI02.1 |

### Definições conceituais candidatas

| ID | Entrada |
|---|---|
| VI00-D01 | [Espaço](#def-VI00-D01) |
| VI00-D02 | [Tempo](#def-VI00-D02) |
| VI00-D03 | [Indivíduo](#def-VI00-D03) |
| VI00-D04 | [Relação](#def-VI00-D04) |
| VI00-D05 | [Unidade/agregado/organização/indivíduo](#def-VI00-D05) |
| VI00-D06 | [Polaridade signo/luz e símbolo/kli](#def-VI00-D06) |
| VI00-D07 | [Domínio](#def-VI00-D07) |
| VI00-D08 | [Dimensão](#def-VI00-D08) |
| VI00-D09 | [Campo](#def-VI00-D09) |
| VI00-D10 | [Ambiente](#def-VI00-D10) |
| VI00-D11 | [Fronteira](#def-VI00-D11) |
| VI00-D12 | [Interface/manifestação](#def-VI00-D12) |
| VI00-D13 | [Escala](#def-VI00-D13) |
| VI00-D14 | [K0 e contexto local](#def-VI00-D14) |
| VI00-D15 | [Ocorrência/relação/estado/história](#def-VI00-D15) |
| VI00-D16 | [Admissibilidade](#def-VI00-D16) |
| VI00-D17 | [Composição relacional](#def-VI00-D17) |
| VI00-D18 | [Trajetória rotulada](#def-VI00-D18) |
| VI00-D19 | [Continuidade e identidade](#def-VI00-D19) |
| VI00-D20 | [Gramática e julgamentos](#def-VI00-D20) |
| VI00-D21 | [Configuração Q_c e semânticas](#def-VI00-D21) |
| VI00-D22 | [Contrato de passagem Ω_e](#def-VI00-D22) |
| VI00-D23 | [Invariante](#def-VI00-D23) |
| VI00-D24 | [Campo dinâmico](#def-VI00-D24) |
| VI00-D25 | [Sensibilidade/Resp](#def-VI00-D25) |
| VI00-D26 | [Restrição e bloqueadores](#def-VI00-D26) |
| VI00-D27 | [Sistema e quociente exato](#def-VI00-D27) |
| VI00-D28 | [Correspondência segura/exata](#def-VI00-D28) |
| VI00-D29 | [Sistema aberto e ligação W_link (W histórico)](#def-VI00-D29) |
| VI00-D30 | [Refração por tarefa](#def-VI00-D30) |
| VI00-D31 | [Ind_op e IO](#def-VI00-D31) |
| VI00-D32 | [Transporte/identidade/genealogia](#def-VI00-D32) |
| VI00-D33 | [Contrato temporizado](#def-VI00-D33) |
| VI00-D34 | [Secção](#def-VI00-D34) |
| VI00-D35 | [Formas de sustentação](#def-VI00-D35) |
| VI00-D36 | [Viabilidade/recuperação](#def-VI00-D36) |
| VI00-D37 | [Ablação/corte minimal](#def-VI00-D37) |
| VI00-D38 | [Suportes/processos/ocorrências](#def-VI00-D38) |
| VI00-D39 | [Álgebra de cobertura](#def-VI00-D39) |
| VI00-D40 | [FPR](#def-VI00-D40) |
| VI00-D41 | [Fechamentos](#def-VI00-D41) |
| VI00-D42 | [Monitor de obrigações](#def-VI00-D42) |

### Responsabilidades axiomáticas e candidatos históricos

Não se declara um sistema axiomático independente/completo. AF/AC/AT/AI são oito responsabilidades; INV, AS e AR são 26 candidatos históricos com obrigações abertas. As definições operacionais de composição, jogos, predecessores, monitor e refinamento estão nos capítulos correspondentes.

| ID candidato | Localização |
|---|---|
| AF-01 | [Texto e estatuto](#cand-AF-01) |
| AF-02 | [Texto e estatuto](#cand-AF-02) |
| AC-01 | [Texto e estatuto](#cand-AC-01) |
| AC-02 | [Texto e estatuto](#cand-AC-02) |
| AT-01 | [Texto e estatuto](#cand-AT-01) |
| AT-02 | [Texto e estatuto](#cand-AT-02) |
| AI-01 | [Texto e estatuto](#cand-AI-01) |
| AI-02 | [Texto e estatuto](#cand-AI-02) |
| INV-01 | [Texto e estatuto](#cand-INV-01) |
| INV-02 | [Texto e estatuto](#cand-INV-02) |
| INV-03 | [Texto e estatuto](#cand-INV-03) |
| INV-04 | [Texto e estatuto](#cand-INV-04) |
| INV-05 | [Texto e estatuto](#cand-INV-05) |
| INV-06 | [Texto e estatuto](#cand-INV-06) |
| INV-07 | [Texto e estatuto](#cand-INV-07) |
| INV-08 | [Texto e estatuto](#cand-INV-08) |
| AS-01 | [Texto e estatuto](#cand-AS-01) |
| AS-02 | [Texto e estatuto](#cand-AS-02) |
| AS-03 | [Texto e estatuto](#cand-AS-03) |
| AS-04 | [Texto e estatuto](#cand-AS-04) |
| AS-05 | [Texto e estatuto](#cand-AS-05) |
| AS-06 | [Texto e estatuto](#cand-AS-06) |
| AS-07 | [Texto e estatuto](#cand-AS-07) |
| AS-08 | [Texto e estatuto](#cand-AS-08) |
| AR-01 | [Texto e estatuto](#cand-AR-01) |
| AR-02 | [Texto e estatuto](#cand-AR-02) |
| AR-03 | [Texto e estatuto](#cand-AR-03) |
| AR-04 | [Texto e estatuto](#cand-AR-04) |
| AR-05 | [Texto e estatuto](#cand-AR-05) |
| AR-06 | [Texto e estatuto](#cand-AR-06) |
| AR-07 | [Texto e estatuto](#cand-AR-07) |
| AR-08 | [Texto e estatuto](#cand-AR-08) |
| AR-09 | [Texto e estatuto](#cand-AR-09) |
| AR-10 | [Texto e estatuto](#cand-AR-10) |

### Definições operacionais por seção

| Objeto | Localização no manuscrito |
|---|---|
| Contexto, configuração e assinatura | §3.1 |
| Composição de relações, diagonais | P02.1 |
| Execuções, palavras e cobertura | P02.3 e P11.2 |
| Fatoração, fibra e núcleo | Guia e P08.3 |
| Quociente e levantamento forte | P04.1/2 |
| Campos, restrições e bloqueadores | P05.1/2 |
| IO e Ind_op | Capítulo 7 |
| Identidade e rastreamento | P09.3 |
| Contrato temporizado | P09.4 |
| Jogo, CPre e núcleo seguro | P10.1 e §10.1 |
| Atrator de recuperação | P10.8 |
| SCC e FPR | P11.3 |
| Monitor e Büchi, μ e ν | P11.5 |
| Certificado C1–C4 | §10.1 |
| Refinamento e canonicidade relativa | PVI02.4 |
