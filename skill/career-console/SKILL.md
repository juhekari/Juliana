---
name: career-console
description: Cria um painel pessoal de transição de carreira (Career Console) — um HTML publicado como Artifact que reúne as vagas que a pessoa está perseguindo, quanto do perfil dela cada vaga cobre, o que ajustar no CV e o que estudar. Use sempre que alguém falar em procurar emprego, trocar de carreira, organizar candidaturas, acompanhar vagas, montar um painel ou dashboard de vagas, "career console", analisar se vale se candidatar a uma vaga, ou pedir ajuda para saber onde o perfil dela está forte ou fraco no mercado — mesmo que não use a palavra "console" ou "painel". Também use quando a pessoa colar um anúncio de vaga pedindo avaliação, ou quiser atualizar um console que já existe.
---

# Career Console

Um console é a fotografia honesta de uma busca de emprego: as vagas, quanto de
cada uma a pessoa cobre hoje, e o que fazer a respeito. O valor não está no
painel bonito — está em ler os anúncios de verdade e dizer com precisão o que
falta. Um console que infla cobertura é pior que nenhum, porque manda a pessoa
gastar processo seletivo em vaga que ela vai perder.

O motor já está pronto em `assets/console.html`. Você não escreve HTML nem CSS:
conduz a entrevista, monta um objeto de dados e injeta esse objeto no motor.

## Fluxo

1. **Entrevistar** — conversa, não formulário. Detalhes em `references/entrevista.md`.
2. **Analisar** — ler cada anúncio e calcular cobertura. Regras em `references/analise.md`.
3. **Montar os dados** — o contrato dos campos está em `references/schema.md`.
4. **Gerar e publicar** — injetar no motor e publicar como Artifact.

Leia `references/entrevista.md` antes de fazer a primeira pergunta. Leia
`references/schema.md` antes de montar o objeto — inventar um nome de campo
faz a aba sumir silenciosamente.

## 1. Entrevistar

Não despeje um questionário. Pergunte em blocos curtos, reagindo ao que a
pessoa responde, do jeito que um amigo que entende de recrutamento perguntaria.

O mínimo para um console útil:

- **Quem ela é hoje**: cargo, há quanto tempo, e qual o domínio (o assunto que
  ela conhece de verdade). O domínio costuma ser o ativo mais raro e o mais
  esquecido pela própria pessoa.
- **O que ela quer**: os títulos de cargo alvo, e onde aceita trabalhar.
- **As vagas**: peça que cole os anúncios. **Link sozinho não serve** — você
  não consegue abrir URLs. Peça o texto do anúncio junto: responsabilidades e
  requisitos. Este é o insumo mais importante de todos.
- **A experiência dela**: currículo, LinkedIn colado, ou a conversa mesmo. Sem
  isso não há como calcular cobertura sem chutar.

Se a pessoa não tiver vagas em mãos, tudo bem: monte o console com o perfil e
as abas que os dados sustentam. Ela adiciona vagas depois, pelo próprio painel
ou pedindo a você.

Não pergunte quais abas ela quer. Deduza das respostas, mostre a lista que você
pretende ligar e deixe ela ajustar. Perguntar "quer a aba de posicionamento de
mercado?" no começo é pedir que ela decida sobre algo que ainda não viu.

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

**Procure o padrão entre as vagas.** O requisito que aparece em mais anúncios e
que ela não cobre é o `oQueFalta` da visão geral. Esse é o achado mais valioso
do console inteiro, e só aparece olhando o conjunto.

## 3. Montar os dados

Monte um objeto JSON conforme `references/schema.md`. Só `tabs` é obrigatório;
todo o resto é opcional, e cada aba aparece quando os dados dela existem.

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

Se a pessoa já tem um console e quer mexer (vaga nova, anúncio que mudou, mais
uma aba), **republique na mesma URL** em vez de criar outro — o link dela não
pode mudar.

As marcações que ela fez no painel (o que arquivou, o que já se candidatou)
vivem no `db`/navegador, não no JSON. Regerar os dados não apaga essas decisões,
então não há motivo para hesitar em atualizar.
