# Contrato dos dados

O objeto injetado no motor. Só `tabs` é obrigatório. Nome de campo errado não dá
erro: a aba simplesmente não aparece. Confira contra esta lista.

## Abas e o que cada uma exige

Uma aba pedida em `tabs` só aparece se o campo de dados dela existir e não
estiver vazio.

| aba | exige | mostra |
|---|---|---|
| `geral` | — | tiles, onde está, o que falta, próximo passo, alertas |
| `analise` | `vagas` | fila de triagem: perseguir ou arquivar |
| `progresso` | `vagas` | as perseguidas, com posicionamento e ajustes de CV |
| `mercado` | `posicionamento` | onde ganha, onde perde, afinidade por setor |
| `cv` | `cvGeral` | checklist de ajustes que valem para todas as candidaturas |
| `cursos` | `cursos` | estudos e certificações, cada um ligado a um requisito real |
| `skills` | `skills` | nível por requisito (0–3) e as maiores lacunas |
| `projetos` | `projetos` | projetos de portfólio com etapas marcáveis |
| `aplicadas` | `vagas` | onde se candidatou de fato |
| `arquivadas` | `vagas` | descartadas, para não reavaliar duas vezes |
| `metodo` | `metodo` | como a análise foi feita e o que ela não garante |

Padrão razoável para a maioria: `["geral","analise","progresso","aplicadas","arquivadas"]`.

## Campos

```jsonc
{
  "slug": "nome-curto",        // separa o armazenamento local de outros consoles
  "regua": 80,                 // % de cobertura a partir da qual vale candidatar
  "tabs": ["geral", "analise", "aplicadas", "arquivadas"],

  "pessoa": {
    "nome": "", "cargo": "",
    "tituloConsole": "",       // vira o <title> e o cabeçalho
    "alvos": [], "locaisAceitos": []
  },

  "visaoGeral": {
    "ondeEsta": "",            // parágrafo de abertura
    "oQueFalta": "",           // a lacuna que mais aparece — o achado principal
    "proximoPasso": "",        // a única coisa a fazer se só desse para fazer uma
    "paragrafos": [],          // parágrafos extras
    "alertas": [],             // avisos em destaque
    "tiles": [{"k": "rótulo", "v": "5", "n": "nota de rodapé"}]
                               // omita e o motor calcula os tiles do funil sozinho
  },

  "vagas": [{
    "id": "v-001",             // obrigatório e único (não pode repetir com leads)
    "titulo": "", "empresa": "", "local": "", "modalidade": "",
    "url": "https://",
    "segmento": "",            // contexto curto, aparece como etiqueta
    "cob": 82,                 // 0–100
    "tem": [], "falta": [],    // requisitos, com as palavras do anúncio
    "posic": "",               // como se posicionar nesta vaga
    "ajustesCv": [],           // ajustes específicos desta vaga
    "nota": "", "alerta": false, // alerta:true destaca a nota em laranja
    "requisitos": [{"skillId": "sql", "tipo": "obrigatorio"}]  // só p/ a aba skills
  }],

  "leads": [{                  // vagas ainda não lidas: sinal, não cobertura
    "id": "l-001", "titulo": "", "empresa": "", "local": "",
    "modalidade": "", "url": "", "sinal": 88
  }],

  "posicionamento": {
    "titulo": "",              // a tese em uma frase
    "alvo": "",                // parágrafo sobre o alvo real
    "diferenciais": [], "contra": [],
    "setores": [{"setor": "", "afinidade": "Direta", "porque": ""}]
  },

  "cvGeral": [{"t": "o ajuste", "porque": "por que importa"}],

  "cursos": [{
    "nome": "", "onde": "", "link": "",
    "quando": "Agora",         // etiqueta livre: "Agora", "Depois", "Só na trilha X"
    "custo": "", "porque": ""  // "porque" deve citar a vaga que pediu isso
  }],

  "categorias": [{"id": "dados", "nome": "Dados e modelagem"}],
  "skills": [{"id": "sql", "nome": "SQL avançado", "categoria": "dados"}],

  "projetos": [{
    "id": "p-001", "nome": "", "contexto": "", "descricao": "",
    "skills": ["sql"],
    "etapas": [{"nome": "primeira etapa"}]
  }],

  "metodo": {"Varredura": "", "Cobertura": "", "Limite": ""},
                               // vira lista de definições; as chaves são os títulos
  "fonte": "",                 // linha de rodapé

  "ui": {"tab.geral": "Overview"}
                               // sobrescreve rótulos; chave ausente cai no pt-BR
}
```

## Detalhes que quebram sem avisar

- **`id` repetido entre `vagas` e `leads`** corrompe o funil: o estágio é
  guardado por `id`, então as duas viram a mesma coisa.
- **`cob` é número**, não string. `"82"` não desenha a barra.
- **`etapas`** aceita `[{"nome": "..."}]` ou `["..."]`.
- **Traduzir a interface**: sobrescreva só as chaves que quiser em `ui`. As
  chaves disponíveis estão em `UI_PADRAO`, no topo do bloco de script do motor.
