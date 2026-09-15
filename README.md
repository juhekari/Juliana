# Career Console — skill

Um painel pessoal de transição de carreira: as vagas que interessam, quanto de
cada uma o perfil da pessoa cobre, o que ajustar no CV e o que estudar.

Ninguém edita JSON nem roda build. A pessoa **instala a skill no próprio
Claude**, conversa, e recebe o painel publicado.

```
skill/career-console/          ← o produto
├── SKILL.md                   instruções: entrevistar, analisar, gerar, publicar
├── assets/console.html        o motor (11 abas, CSS e JS, ~50KB)
└── references/
    ├── entrevista.md          o roteiro de perguntas
    ├── analise.md             como calcular cobertura sem inflar
    └── schema.md              o contrato dos dados

exemplo/console.json           exemplo completo, todas as abas (referência e fixture)
build.py                       harness de teste: valida o motor sem passar por uma conversa
```

## Como a pessoa usa

1. Instala `career-console.skill` no Claude dela.
2. Diz algo como *"me ajuda a organizar minha busca de emprego"*.
3. O Claude entrevista: quem ela é, o que quer, e pede que **cole os anúncios**
   das vagas (o texto, não só o link — a página não consegue abrir URLs).
4. O Claude lê cada anúncio, calcula a cobertura, monta os dados e publica o
   console como Artifact.

Depois é conversa: *"achei esta vaga, adiciona"*, *"o anúncio da Empresa X
mudou, recalcula"*. O Claude republica na mesma URL.

## O que o painel faz sozinho

O HTML publicado é autocontido — sem script externo, sem `fetch`. O que a pessoa
marca nele (perseguir, me inscrevi, arquivar, nível numa skill) fica no `db` do
Claude, sincronizando entre aparelhos, ou no navegador quando não houver `db`.

Essa separação é proposital: o JSON é a análise de mercado, o estado é o que a
pessoa decidiu. Regerar a análise com vagas novas não apaga as decisões dela.

As duas capacidades são opcionais e degradam sozinhas:

- **`db`** — marcações acompanham a pessoa em qualquer aparelho. Sem ela, o
  painel salva no navegador e diz isso no rodapé.
- **`sample`** — libera o formulário de colar anúncio dentro do painel. Sem ela,
  o formulário não aparece, em vez de prometer uma leitura que não acontece.

## As abas

`geral`, `analise`, `progresso`, `mercado`, `cv`, `cursos`, `skills`,
`projetos`, `aplicadas`, `arquivadas`, `metodo`.

O Claude deduz quais ligar a partir do que a entrevista rendeu e confirma antes
de publicar. Uma aba só aparece se os dados dela existirem.

## Testar o motor sem conversar

```bash
python3 build.py                 # exemplo/console.json -> dist/index.html
open dist/index.html
```

## O que o console não promete

Cobertura é julgamento sobre texto de anúncio, não previsão de resultado. Vaga
sai do ar, requisito muda, e recrutador pesa o que quer.
