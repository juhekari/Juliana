# Como calcular cobertura

A cobertura é o número que a pessoa vai usar para decidir onde gastar as
próximas semanas. Ela precisa ser defensável.

## O método

Para cada vaga:

1. **Extraia os requisitos do anúncio**, um por um, com as palavras do próprio
   anúncio. Requisitos que a empresa lista como obrigatórios e os que lista como
   desejáveis vão para listas diferentes na sua cabeça.
2. **Marque cada um** contra o histórico real da pessoa: cobre, não cobre.
3. **Calcule a proporção**, dando peso menor aos desejáveis. Um requisito
   listado como diferencial não pode derrubar a cobertura como se fosse
   obrigatório.
4. **Ajuste para baixo se houver eliminatório faltando.** Uma vaga que exige
   5 anos de um cargo que a pessoa nunca teve não é 85% só porque o resto
   casa — esse item sozinho derruba a candidatura na triagem automática.

O que cobre vai em `tem`, o que não cobre vai em `falta`, ambos com as palavras
do anúncio — é assim que a pessoa reconhece o termo quando reescrever o CV.

## O que não fazer

**Não conte palavras-chave.** Casamento de vocabulário dá resultados absurdos:
um anúncio em outro idioma pode "bater" 100% por compartilhar termos técnicos.
Cobertura é leitura de requisito.

**Não infle para animar.** A pessoa não precisa de ânimo, precisa de um mapa. Se
a vaga está em 55%, diga 55% e explique o que falta. Ela decide.

**Não invente.** Se você não sabe se ela tem um requisito, pergunte ou coloque
em `falta`. Nunca preencha `tem` com suposição.

## A régua

O padrão é 80% (`regua`), e ele aparece como um traço nas barras do painel. A
ideia: abaixo da régua a vaga não está descartada, está **fora de hora** — o
esforço rende mais fechando a lacuna do que escrevendo carta.

Ajuste a régua se o caso pedir, e diga por quê.

## O achado que importa mais — e por que o texto de `falta` precisa ser igual

Olhe o conjunto, não só cada vaga. **Qual requisito aparece em mais anúncios e a
pessoa não cobre?** Costuma ser o achado mais útil do console inteiro — uma
lacuna só, que destrava várias vagas de uma vez. É por isso que a aba
`mercado` existe: ela cruza o `falta[]` das vagas aplicadas e mostra o que se
repete.

Esse cruzamento é literal, string contra string — não é uma segunda IA lendo
o significado. Se a mesma lacuna aparece como "Airflow como dono do
orquestrador" numa vaga e "experiência com orquestração de pipeline" noutra,
o motor as trata como duas coisas diferentes e o padrão não aparece.
**Escreva a mesma lacuna com o mesmo texto, exatamente, em toda vaga onde ela
aparecer.** Antes de finalizar os dados, releia os `falta[]` de todas as
vagas e unifique a redação de qualquer lacuna repetida.

Quando um padrão for claro, preencha `sugestoes` (ver `schema.md`) com a
chave sendo esse texto exato — é o que liga o padrão à recomendação de CV e
de curso na aba `mercado`.

Nos consoles que funcionaram, esse achado era sempre específico e um pouco
desconfortável: "faltou responsabilidade financeira em 3 das 4 vagas
aplicadas" fala mais alto que "melhore suas habilidades técnicas".

Repare também no que **não** é lacuna de competência, mas de vocabulário: a
pessoa faz a coisa, só não chama pelo nome que o mercado usa. Isso é ajuste de
CV, rápido e de alto retorno — e vale dizer com essa clareza em `sugestoes`.

## O posicionamento

`posic` (por vaga) responde: nesta vaga específica, por onde ela entra? Qual é o
argumento? O que ela precisa atacar de frente porque o recrutador vai notar de
qualquer jeito?

Posicionamento honesto reconhece a lacuna em vez de torcer para ninguém
perceber. "A vaga pede que você responda por margem da conta, e isso é lacuna
real: não tente fingir. O caminho é mostrar planejamento de capacidade como
decisão de recurso com consequência financeira."
