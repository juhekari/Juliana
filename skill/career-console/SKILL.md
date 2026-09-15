---
name: career-console
description: Cria um painel pessoal de transição de carreira (Career Console) — um HTML publicado como Artifact que reúne as vagas que a pessoa está perseguindo, quanto do perfil dela cada vaga cobre, e o que se repete como lacuna entre as candidaturas. Use sempre que alguém falar em procurar emprego, trocar de carreira, organizar candidaturas, acompanhar vagas, montar um painel ou dashboard de vagas, "career console", analisar se vale se candidatar a uma vaga, ou pedir ajuda para saber onde o perfil dela está forte ou fraco no mercado — mesmo que não use a palavra "console" ou "painel". Também use quando a pessoa colar um anúncio de vaga pedindo avaliação, ou quiser atualizar um console que já existe.
---

# Career Console

Um console é a fotografia honesta de uma busca de emprego: as vagas, quanto de
cada uma a pessoa cobre hoje, e o que se repete como lacuna entre as
candidaturas. O valor não está no painel bonito — está em ler os anúncios de
verdade e dizer com precisão o que falta. Um console que infla cobertura é
pior que nenhum, porque manda a pessoa gastar processo seletivo em vaga que
ela vai perder.

O motor já está pronto em `assets/console.html`, com exatamente cinco abas
fixas: análise, progresso, aplicadas, arquivadas, e posicionamento de
mercado. Não há escolha de abas a fazer — você não escreve HTML nem CSS,
nem decide o que ligar: conduz a entrevista, monta um objeto de dados e
injeta esse objeto no motor.

## Fluxo

1. **Entrevistar** — as 4 perguntas fixas de `references/entrevista.md`.
2. **Analisar** — ler cada anúncio e calcular cobertura. Regras em `references/analise.md`.
3. **Montar os dados** — o contrato dos campos está em `references/schema.md`.
4. **Gerar e publicar** — injetar no motor e publicar como Artifact.

Leia `references/entrevista.md` antes de fazer a primeira pergunta. Leia
`references/schema.md` antes de montar o objeto — inventar um nome de campo
faz o conteúdo sumir silenciosamente.

## 1. Entrevistar

`references/entrevista.md` tem o texto exato das quatro perguntas e o que
fazer quando alguma resposta faltar. Mande as quatro juntas, numa mensagem
só — não abra em mais blocos nem pergunte outra coisa antes.

## 2. Analisar

Esta é a parte que exige rigor. `references/analise.md` tem o método completo;
o essencial:

**Cobertura (`cob`) é leitura, não contagem de palavra.** Liste os requisitos
do anúncio, marque um por um se o perfil cobre, e calcule a proporção.
Requisito eliminatório que a pessoa não tem derruba a cobertura de verdade —
não arredonde para cima para agradar.

**Nunca invente experiência.** Se um requisito não aparece no histórico dela,
ele vai em `falta`. É para isso que o campo existe. A pessoa vai usar este
painel para decidir onde gastar tempo; um `tem` falso custa caro a ela, não a
você.

**A régua padrão é 80%.** Abaixo disso a vaga não está descartada — está fora
de hora: rende mais fechar a lacuna do que escrever carta de apresentação.

**Escreva `falta` com o mesmo texto quando a lacuna se repetir entre vagas.**
A aba de posicionamento de mercado cruza esses textos automaticamente; se a
mesma lacuna aparece com palavras diferentes em cada vaga, o cruzamento não
acha o padrão. `analise.md` detalha isso.

## 3. Montar os dados

Monte um objeto JSON conforme `references/schema.md`. As cinco abas são
fixas e sempre aparecem — o que muda de console para console é só o
conteúdo: `pessoa`, `vagas`, `leads`, e opcionalmente `sugestoes` (ajuste de
CV e curso associados a uma lacuna que se repete).

Escreva os textos com a voz de quem conhece a pessoa e não tem medo de dar má
notícia. "Faltam 2 pontos e os dois itens que faltam são o mesmo tema: dinheiro"
vale mais que "Boa aderência, continue se candidatando!". Concreto, específico,
sem bajulação.

## 4. Gerar e publicar

O motor tem exatamente uma linha onde os dados entram:

```js
window.__CONSOLE__ = /*__DADOS__*/ null /*__FIM__*/;
```

Leia `assets/console.html`, substitua **todo o trecho** entre `/*__DADOS__*/` e
`/*__FIM__*/` (os marcadores inclusive) pelo seu JSON, e publique o arquivo
resultante como Artifact.

Um cuidado que não é opcional: se algum texto contiver `</script>`, ele fecha o
bloco e derruba a página. Escape `</` como `<\/` dentro do JSON antes de
injetar.

Ao publicar, declare as capacidades **`db`** e **`sample`** se o ambiente
permitir:

- `db` faz as marcações da pessoa acompanharem ela em qualquer aparelho.
- `sample` libera o formulário de colar anúncio dentro do próprio painel.

As duas são opcionais e o motor degrada sozinho: sem `db` ele salva no
navegador e diz isso no rodapé; sem `sample` ele esconde o formulário em vez de
prometer uma leitura que não vai acontecer. Publique mesmo que não consiga
declarar nenhuma — o console funciona.

Depois de publicar, diga em uma ou duas frases o que o console mostrou de mais
importante. A pessoa acabou de responder muita pergunta; ela merece a conclusão,
não só o link.

## Atualizar um console que já existe

Se a pessoa já tem um console e quer mexer (vaga nova, anúncio que mudou),
**republique na mesma URL** em vez de criar outro — o link dela não pode
mudar.

As marcações que ela fez no painel (o que arquivou, o que já se candidatou)
vivem no `db`/navegador, não no JSON. Regerar os dados não apaga essas decisões,
então não há motivo para hesitar em atualizar.
