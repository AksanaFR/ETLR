# Reprodução dos controles científicos selecionados

Requisitos: Python 3, biblioteca padrão. Nenhuma instalação de bibliotecas, acesso à rede, chave, motor ou repositório é necessária. A versão efetivamente testada consta de RESULTADO_VI06A.json.

A partir da raiz do pacote, execute:

```text
python reproducao/verificar_integridade.py
python reproducao/reproduzir.py DIRETORIO_NOVO_DE_SAIDA
```

Escolha um diretório de saída fora do pacote editorial. Sem argumento, o programa cria um diretório temporário. São gravados stdout, stderr e REPRODUCAO.json. Cada controle é executado em cópia temporária com limite de cinco minutos; nenhum código de entrada é alterado. O sucesso exige saída zero, stderr vazio e igualdade semântica com a referência. Somente tempo_segundos é excluído da comparação VI03/VI05; a comparação VI02 não exclui campos.

| Controle | Código original | Referência | Alcance |
|---|---|---|---|
| VI02 | VI02_codigo_original.py | VI02_expected_original.json | Jogos finitos e transporte de garantias; certificado e refinamento no universo executado |
| VI03 | VI03_codigo_original.py | VI03_expected_original.json | Oráculos por enumeração de políticas, contramodelos e partições; 67.600 combinações micro, 192 produtos, 9.066 políticas, sete contramodelos e 2.400 comparações de partições no registro histórico |
| VI05 | controles_complementares.py | CONTROLES_COMPLEMENTARES.json | 14.280 comparações de palavras; 192 comparações em 48 jogos amostrados, 33.612 políticas; modelos booleanos e contagem trivalente dos IO |

As saídas de referência são as preservadas na VI05. Os três códigos selecionados são integrais em bytes; os hashes constam do manifesto. O programa de execução e o verificador de integridade foram preparados para esta seleção pública. A VI06A registra uma nova execução dos controles em RESULTADO_VI06A.json e nas saídas VI02/VI03/VI05.stdout.json.

Esses controles são sintéticos, de escopo finito e declarado. Não validam empiricamente a ontologia, não constituem prova mecanizada das cinquenta conclusões, não estabelecem originalidade externa e não executam todas as suítes históricas. As condições formais e a prova textual continuam no volume, na auditoria e na matriz. Os motores QOREL/ARM e os documentos internos não são necessários para executar esta seleção.
