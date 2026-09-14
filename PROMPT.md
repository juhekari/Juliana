# Sem terminal: fazer tudo pelo Claude

Dois caminhos. O primeiro se você já tem o JSON pronto; o segundo se prefere não
escrever JSON nenhum.

---

## Caminho 1 — já tenho o `console.json`

Anexe `engine/console.html` e o seu `data/console.json` numa conversa com o
Claude e mande:

> Anexei o motor de um painel de carreira e o meu arquivo de dados.
>
> No HTML existe uma linha assim:
>
> `window.__CONSOLE__ = /*__DADOS__*/ null /*__FIM__*/;`
>
> Troque o trecho entre `/*__DADOS__*/` e `/*__FIM__*/` pelo conteúdo do meu
> JSON, como um objeto JavaScript literal. Escape qualquer `</` dentro dos
> textos como `<\/`, senão um `</script>` no meio do conteúdo fecha o bloco e
> derruba a página. Não mude mais nada no motor.
>
> Depois publique o resultado como Artifact, declarando as capacidades `db` e
> `sample`, e me mande o link.

A parte das capacidades importa: sem `db` as marcações não acompanham você entre
aparelhos, e sem `sample` o formulário de colar anúncio não aparece.

---

## Caminho 2 — não quero escrever JSON

Anexe `engine/console.html`, `exemplo/console.json`, o seu currículo e os links
das vagas que te interessam. Mande:

> Anexei o motor de um painel de carreira, um exemplo preenchido que serve de
> contrato dos campos, o meu currículo e algumas vagas.
>
> Leia as vagas e o meu currículo e monte o meu `console.json` seguindo
> exatamente o formato do exemplo. Para cada vaga:
>
> - `cob` é a porcentagem de requisitos do anúncio que o meu perfil cobre.
>   Calcule lendo os requisitos, não contando palavras repetidas.
> - `tem` e `falta` são os requisitos, com as palavras do anúncio.
> - `posic` é como eu me posiciono naquela vaga especificamente.
> - Não invente experiência que não está no meu currículo. Se um requisito não
>   estiver coberto, ele vai em `falta` — é para isso que o campo existe.
>
> Escolha as abas em `tabs` conforme o que os dados sustentam. Depois inline o
> JSON no motor (instruções no Caminho 1) e publique como Artifact com as
> capacidades `db` e `sample`.

---

## Depois, para atualizar

O Artifact publicado tem uma URL fixa. Para atualizar sem trocar o link, peça ao
Claude para **republicar naquela mesma URL** em vez de criar um novo.

Dá para pedir coisas como *"achei esta vaga, adiciona no meu console"* ou
*"recalcula a cobertura da vaga da Empresa X, o anúncio mudou"* — o Claude edita
o JSON e republica.
