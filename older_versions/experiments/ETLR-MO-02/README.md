# ETLR-MO-02 — Motor contextual lógico-relacional

**Versão pública experimental 0.1 · 21/11/2026 · pesquisa independente**

Este diretório apresenta uma implementação finita e reproduzível de um **ciclo de investigação contextual** vinculado à [Álgebra Espaço-Temporal Lógico-Relacional (ETLR), Volume I](../../ETLR_Volume_I_EDIT02_R4_AUTONOMA_CANDIDATA.html). Não é uma reconstrução da monografia, um sistema cognitivo geral, uma prova de autogeração universal ou uma descrição de processos físicos.

O ponto de partida não é atribuir uma identidade ao que observamos. É delimitar o espaço relacional, o regime temporal e os indivíduos candidatos; distinguir **constituição interna, manifestação externa e limite contextual**; confrontar uma diferença e conservar o resultado para nova investigação.

## Entenda o procedimento

**Constituir → Confrontar → Reconstituir → Retornar**.

1. **Constituir:** identificar um espaço relacional, um campo e a unidade participante, com tipos, fontes e condições de admissibilidade.
2. **Confrontar:** examinar a menor diferença pertinente: limite, observação, hipótese rival ou insuficiência. Evitar inferir uma estrutura interna única a partir de uma única manifestação externa.
3. **Reconstituir:** atualizar apenas o que é justificável; conservar questões indeterminadas, limites de validade e proveniência.
4. **Retornar:** reaplicar o mesmo ciclo, quando uma ocorrência ou novo contexto justificar a continuidade, sem exigir uma nova gramática a cada escala.

O **limite é uma operação contextual**, não uma fronteira fixa nem um veto genérico. Pode vir do próprio indivíduo, do ambiente, de outro participante ou da relação; pode restringir uma representação sem demonstrar que a constituição interna mudou. O resultado pode levar à revisão do próprio limite. A análise detalhada dessas distinções, de sua dinâmica temporal e das formas de individuação está em [`ARQUITETURA_RELACIONAL.md`](ARQUITETURA_RELACIONAL.md).

## Executar em Python

Recomendado: **Python 3.13** (versão efetivamente utilizada nos testes; código escrito para sintaxe Python 3.10+, ainda sem validação em todas as versões).

Na raiz do repositório:

```bash
cd experiments/ETLR-MO-02
python -m etlr_contextual exemplos/01_simples.etlr
python -m etlr_contextual exemplos/02_ramificacao.etlr
python -m exemplos.03_reparo_reproducao
python run_tests.py
```

Nenhum pacote externo é necessário para executar a linguagem e os testes. O comando `run_tests.py` gera `RESULTADOS.json` e `TESTES_EXECUCAO.txt` localmente (não versionados por padrão).

## Linguagem declarativa ETLR-L0

```text
ESPACO canal
CAMPO regime_de_turnos
INDIVIDUO A
LIMITE 12
OBSERVADO 7
PERGUNTA CHECK
RECURSO 12
```

Este programa pergunta se a medida observada 7 satisfaz o limite 12 no contexto declarado. Saída esperada: `LOCAL_CLOSED`, `ADMISSIBLE@rev0`, uma passagem de confronto.

Se `LIMITE DESCONHECIDO`, a admissibilidade será `INDETERMINATE`. Com `PERGUNTA WHY_SHORT`, o protótipo abre somente três alternativas configuradas: limitação ambiental, autolimitação e limitação relacional; elas permanecem **hipóteses indeterminadas**, não diagnósticos causais.

O parser não executa código externo ou Python arbitrário: interpreta sete instruções textuais fixas. Isso limita deliberadamente a linguagem a um domínio piloto.

## Qual é a reprodução funcional investigada?

O núcleo sintético contém três capacidades: `CONSTITUTE`, `CONFRONT` e `RECONSTITUTE`. Há receitas de projeto para restaurar qualquer uma delas usando as outras duas e um recurso. A operação `replicate()` pode produzir uma instância com **o mesmo conjunto declarado de capacidades e receitas**, desde que o pai esteja operacional, os recursos sejam suficientes e sejam fornecidos critérios de individuação.

- **R0:** a operação admite reentrada sobre estado de mesmo tipo.
- **R1:** repara uma perda de componente sob receita e recurso disponíveis.
- **R2:** reproduz a configuração funcional em um estado descendente sob condições.
- **R3:** autogeração constitutiva integral — **não demonstrada**.

O interpretador Python, as receitas de recuperação e os critérios para nova escala **não são produzidos pelo motor**. Duas gerações sucessivas verificadas no modelo não implicam reprodução autônoma do sistema real.

## Evidências e limites

A suíte disponibilizada contém **31 testes unitários**; um deles examina **80 configurações finitas sintéticas** (8 conjuntos de componentes × 5 orçamentos × 2 regimes de receitas). Testes finitos sobre condições estipuladas verificam comportamentos do protótipo, não a validade universal da ETLR.

Os casos negativos incluem perda de dois componentes, ausência de receita, recurso insuficiente, contexto inválido, quebra de proveniência e ausência de testemunho de individuação.

Uma cadeia SHA-256 relaciona registros locais, mas **não autentica fatos nem protege contra reescrita coordenada de toda a cadeia**. A passagem para uma nova escala depende de cinco marcadores externos (constituição, fronteira, identidade, continuidade, participação), que não constituem certificação ontológica.

## Documentação

- [`ARQUITETURA_RELACIONAL.md`](ARQUITETURA_RELACIONAL.md) — explicação completa das funções contextuais, limites, temporalidades, representações, composição, realização e reentrada.
- [`ARTIGO_EXPERIMENTAL_v0_1.md`](ARTIGO_EXPERIMENTAL_v0_1.md) — formalização, proposições, demonstrações internas, controles e discussão científica.
- [`REFERENCIAS.bib`](REFERENCIAS.bib) — bibliografia científica dos conceitos antecedentes.
- [`LICENSE`](LICENSE) — licença PolyForm Noncommercial 1.0.0 do código, testes e exemplos.
- [`NOTICE`](NOTICE) — aviso obrigatório de direitos autorais.
- [`NOTA_DE_DIREITOS.md`](NOTA_DE_DIREITOS.md) — delimitação precisa dos direitos de software e de texto.
- `tests/test_motor.py` — testes que permitem reproduzir e contestar os resultados.

**Atribuições intelectuais.** A discussão faz referência à individuação em Gilbert Simondon; autopoiese em Varela, Maturana e Uribe; fechamento de restrições em Montévil e Mossio; conjuntos autocatalíticos em Hordijk e Steel; controle e adaptação em Ashby; teoria de sistemas de transição em Rutten e Clarke et al.; composicionalidade em Fong e Spivak; ordem causal parcial em Lamport; proveniência no W3C PROV-DM; e parcimônia em Rissanen e Simon. A contribuição candidata consiste na **articulação operacional específica** dessas preocupações para o protocolo ETLR, não na reivindicação de sua invenção isolada. Referências completas e natureza de cada crédito constam do artigo.

**Licenciamento da revisão atual:** o **código-fonte, os testes e os exemplos executáveis** estão sob **[PolyForm Noncommercial 1.0.0](LICENSE)**, com o [aviso obrigatório](NOTICE). São permitidos os usos previstos no texto integral da licença; não há autorização comercial geral. As versões publicadas anteriormente sob MIT conservam as permissões então concedidas. O Volume I mantém CC BY-NC-ND 4.0, e o artigo experimental e a análise filosófica não são relicenciados como software. Consulte [`NOTA_DE_DIREITOS.md`](NOTA_DE_DIREITOS.md). Este material é experimental, não revisado por pares e sem DOI.