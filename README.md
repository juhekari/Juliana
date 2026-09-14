# Career Console — template

Um painel de acompanhamento de transição de carreira: as vagas que interessam, a
cobertura de cada uma contra o seu perfil, o que ajustar no CV e o que estudar.

O conteúdo é **seu** e vive num arquivo JSON. O motor é o mesmo para todo mundo.

```
engine/console.html     o motor: CSS, abas e lógica. Você não precisa mexer aqui.
data/console.json       o seu conteúdo. É aqui que você escreve.
exemplo/console.json     exemplo completo, pessoa fictícia, todas as abas ligadas.
build.py                junta os dois -> dist/index.html
PROMPT.md               o caminho sem terminal: peça ao Claude fazer o build
```

## Começando

```bash
python3 build.py --data exemplo/console.json   # veja o exemplo primeiro
open dist/index.html

cp exemplo/console.json data/console.json      # comece do exemplo, não do zero
# edite data/console.json
python3 build.py
```

Sem Python à mão? Veja **PROMPT.md** — dá para fazer tudo dentro de uma conversa
com o Claude.

## Escolhendo as abas

O campo `tabs` decide quais abas existem e em que ordem. Ligar uma aba depois é
editar uma linha e rodar o build de novo.

| aba | precisa de | o que mostra |
|---|---|---|
| `geral` | — | tiles, onde você está, o que falta, próximo passo |
| `analise` | `vagas` | fila de triagem: decidir perseguir ou arquivar |
| `progresso` | `vagas` | as que você persegue, com posicionamento e ajustes de CV |
| `mercado` | `posicionamento` | onde você ganha, onde perde, afinidade por setor |
| `cv` | `cvGeral` | checklist de ajustes que valem para todas as candidaturas |
| `cursos` | `cursos` | estudos e certificações, cada um ligado a um requisito real |
| `skills` | `skills` | seu nível por requisito (0–3) e as maiores lacunas |
| `projetos` | `projetos` | projetos de portfólio, com etapas marcáveis |
| `aplicadas` | `vagas` | onde você de fato se inscreveu |
| `arquivadas` | `vagas` | descartadas, para não reavaliar duas vezes |
| `metodo` | `metodo` | como a análise foi feita e o que ela não garante |

Pedir uma aba sem os dados dela não quebra nada: o build avisa e a aba não
aparece. Todo campo fora de `tabs` é opcional.

## Os campos

`regua` (padrão 80) é a porcentagem de cobertura a partir da qual vale se
candidatar. É o traço vertical nas barras.

Cada item de `vagas` aceita: `id` (obrigatório e único), `titulo`, `empresa`,
`local`, `modalidade`, `url`, `segmento`, `cob` (0–100), `tem[]`, `falta[]`,
`posic`, `ajustesCv[]`, `nota`, `alerta`, e `requisitos[]` no formato
`{"skillId": "...", "tipo": "obrigatorio"|"desejavel"}` se você usar a aba
`skills`.

`leads` é a fila ainda não lida — só sinal de palavra-chave, sem cobertura:
`id`, `titulo`, `empresa`, `local`, `modalidade`, `url`, `sinal`.

Veja `exemplo/console.json` para todos os outros: é o contrato completo.

## Trocar os textos da interface

Todo rótulo visível sai de `ui`. Sobrescreva só o que quiser mudar — chave
ausente cai no português padrão, então dá para traduzir aos poucos e nunca
sobra buraco na tela.

```json
"ui": { "tab.geral": "Overview", "acao.perseguir": "Pursue this" }
```

As chaves estão todas em `UI_PADRAO`, no topo do bloco de script do motor.

## Publicar como Artifact

O arquivo gerado é autocontido — abre com duplo clique, sem servidor.

Para publicar no seu Claude, peça: *"publique este arquivo como Artifact,
declarando as capacidades `db` e `sample`"*.

As duas capacidades são opcionais e detectadas em separado:

- **`db`** — suas marcações acompanham você em qualquer aparelho. Sem ela, tudo
  fica no `localStorage` daquele navegador e o rodapé diz isso com todas as
  letras.
- **`sample`** — libera o formulário de colar o anúncio, que lê a descrição e
  cadastra a vaga sozinho. Sem ela o formulário simplesmente não aparece:
  prometer uma leitura que não acontece é pior que não ter o botão.

> **As capacidades são declaradas na hora de publicar, não dentro do HTML.** Se
> quem publicar esquecer, o console cai no `localStorage` em silêncio e parece
> quebrado. É o erro mais comum.

O mesmo arquivo também funciona como página estática (GitHub Pages, por
exemplo), aí sempre no modo `localStorage`.

## O que o console não faz

Não abre URLs sozinho — o navegador não deixa. Por isso o formulário de colar
anúncio pede o texto junto com o link.

Cobertura é julgamento sobre texto de anúncio, não promessa de resultado. Vaga
sai do ar, requisito muda e recrutador pesa o que quer.
