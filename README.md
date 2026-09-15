# Career Console — skill

Um painel pessoal de transição de carreira: as vagas que interessam, quanto de
cada uma o perfil da pessoa cobre, e o que se repete como lacuna entre as
candidaturas.

Ninguém edita JSON nem roda build. A pessoa **instala a skill no próprio
Claude**, conversa, e recebe o painel publicado.

```
skill/career-console/          ← o produto
├── SKILL.md                   instruções: entrevistar, analisar, gerar, publicar
├── assets/console.html        o motor (5 abas fixas, CSS e JS, ~43KB)
└── references/
    ├── entrevista.md          as 4 perguntas fixas, texto literal
    ├── analise.md             como calcular cobertura sem inflar
    └── schema.md              o contrato dos dados

exemplo/console.json           exemplo completo (referência e fixture)
build.py                       harness de teste: valida o motor sem passar por uma conversa
```

## Como a pessoa usa

1. Instala `career-console.skill` no Claude dela.
2. Diz algo como *"me ajuda a organizar minha busca de emprego"*.
3. O Claude manda as 4 perguntas fixas de uma vez (currículo/LinkedIn, cargos
   alvo, localização, e **3 a 5 anúncios de vaga colados** — o texto, não só
   o link, porque a página não consegue abrir URLs sozinha).
4. O Claude lê cada anúncio, calcula a cobertura, monta os dados e publica o
   console como Artifact.

Depois é conversa: *"achei esta vaga, adiciona"*, *"o anúncio da Empresa X
mudou, recalcula"*. O Claude republica na mesma URL.

## O que o painel faz sozinho

O HTML publicado é autocontido — sem script externo, sem `fetch`. O que a pessoa
marca nele (perseguir, me inscrevi, arquivar) fica no `db` do Claude,
sincronizando entre aparelhos, ou no navegador quando não houver `db`.

Essa separação é proposital: o JSON é a análise de mercado, o estado é o que a
pessoa decidiu. Regerar a análise com vagas novas não apaga as decisões dela.

As duas capacidades são opcionais e degradam sozinhas:

- **`db`** — marcações acompanham a pessoa em qualquer aparelho. Sem ela, o
  painel salva no navegador e diz isso no rodapé.
- **`sample`** — libera o formulário de colar anúncio dentro do painel. Sem ela,
  o formulário não aparece, em vez de prometer uma leitura que não acontece.

## As abas

Cinco, fixas, sempre nesta ordem, sem seleção: `analise`, `progresso`,
`aplicadas`, `arquivadas`, `mercado`.

As quatro primeiras são o funil: uma vaga entra em análise, quando a pessoa
decide persegui-la vai para progresso, ao se candidatar vira aplicada, e o
que é descartado vai para arquivadas. A quinta, `mercado`, não é conteúdo
escrito uma vez — é calculada toda vez que abre: cruza o `falta[]` das vagas
aplicadas e mostra o que se repete entre elas, com sugestão de ajuste de CV e
de curso quando houver uma cadastrada em `sugestoes`.

Não há campo para escolher outras abas. É assim de propósito: as quatro do
funil são o destino dos botões do painel, e um teste real mostrou que tirar
uma delas faz uma vaga movida para lá desaparecer sem aviso — o motor força
as cinco por construção, então esse bug deixou de ser possível.

## Testar o motor sem conversar

```bash
python3 build.py                 # exemplo/console.json -> dist/index.html
open dist/index.html
```

## O que o console não promete

Cobertura é julgamento sobre texto de anúncio, não previsão de resultado. Vaga
sai do ar, requisito muda, e recrutador pesa o que quer.
