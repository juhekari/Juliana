# Contrato dos dados

O objeto injetado no motor. Nome de campo errado não dá erro: o conteúdo
simplesmente não aparece em lugar nenhum. Confira contra esta lista.

## As 5 abas — fixas, não configuráveis

Todo console tem exatamente estas cinco, sempre nesta ordem. Não existe campo
para escolher ou tirar aba — é assim por construção, porque as quatro
primeiras são o destino dos botões "Vou perseguir" / "Me inscrevi" / "Arquivar":
tirar uma delas faria uma vaga movida para lá desaparecer sem aviso.

| aba | fonte | mostra |
|---|---|---|
| `analise` | `vagas`, `leads` | fila de triagem: perseguir ou arquivar |
| `progresso` | `vagas` | as perseguidas, com posicionamento e ajustes de CV |
| `aplicadas` | `vagas` | onde se candidatou de fato |
| `arquivadas` | `vagas` | descartadas, para não reavaliar duas vezes |
| `mercado` | `vagas[].falta` + `sugestoes` | cruzamento das lacunas repetidas entre as vagas aplicadas |

## Campos

```jsonc
{
  "slug": "nome-curto",        // separa o armazenamento local de outros consoles
  "regua": 80,                 // % de cobertura a partir da qual vale candidatar

  "pessoa": {
    "nome": "", "cargo": "",
    "tituloConsole": ""        // vira o <title> e o cabeçalho
  },

  "vagas": [{
    "id": "v-001",             // obrigatório e único (não pode repetir com leads)
    "titulo": "", "empresa": "", "local": "", "modalidade": "",
    "url": "https://",
    "segmento": "",            // contexto curto, aparece como etiqueta
    "cob": 82,                 // 0–100, número — "82" em string não desenha a barra
    "tem": [], "falta": [],    // requisitos, com as palavras do anúncio
    "posic": "",               // como se posicionar nesta vaga
    "ajustesCv": [],           // ajustes específicos desta vaga
    "nota": "", "alerta": false // alerta:true destaca a nota em laranja
  }],

  "leads": [{                  // vagas ainda não lidas: sinal, não cobertura
    "id": "l-001", "titulo": "", "empresa": "", "local": "",
    "modalidade": "", "url": "", "sinal": 88
  }],

  "sugestoes": {
    // a chave é o texto EXATO de um "falta" que se repete entre vagas —
    // é assim que a aba mercado liga o padrão à recomendação
    "Airflow como dono do orquestrador": {
      "cv": "Frase pronta para o CV/LinkedIn atacando esse item",
      "curso": {"nome": "", "link": ""}   // ou uma string simples, sem link
    }
  },

  "fonte": "",                 // linha de rodapé

  "ui": {"tab.analise": "Jobs to review"}
                               // sobrescreve rótulos; chave ausente cai no pt-BR
}
```

## Como `mercado` calcula o cruzamento

Não é texto escrito uma vez — é calculado toda vez que a aba abre:

1. Pega as vagas em estágio `aplicada`. Se não houver nenhuma ainda, usa
   `analise` + `progresso` como aproximação e avisa que é preliminar.
2. Junta os `falta[]` dessas vagas e conta quantas vezes cada texto se repete
   **exatamente** — por isso é essencial escrever a mesma lacuna com as
   mesmas palavras em vagas diferentes (`analise.md` cobre isso).
3. O que aparece 2+ vezes vira "o que se repete", com a contagem
   ("faltou em N de T vagas") e a sugestão de `sugestoes[aquele texto]`, se
   existir.
4. O que aparece 1 vez só vai para uma lista secundária, sem sugestão.

## Detalhes que quebram sem avisar

- **`id` repetido entre `vagas` e `leads`** corrompe o funil: o estágio é
  guardado por `id`, então as duas viram a mesma coisa.
- **Texto de `falta` inconsistente entre vagas** (mesma lacuna, palavras
  diferentes) impede o cruzamento de achar o padrão — ele conta strings
  exatas, não sinônimos.
- **Chave de `sugestoes` que não bate com nenhum `falta`** nunca aparece;
  `build.py` avisa sobre isso.
- **Traduzir a interface**: sobrescreva só as chaves que quiser em `ui`. As
  chaves disponíveis estão em `UI_PADRAO`, no topo do bloco de script do motor.
