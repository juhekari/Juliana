#!/usr/bin/env python3
"""Harness de teste: injeta um JSON no motor da skill e gera a página.

Only the standard library — whoever unpacks this may have nothing installed.

Na prática quem gera o console é o Claude, seguindo skill/career-console.
Este script existe para validar o motor sem passar por uma conversa.

    python3 build.py                              # exemplo/console.json -> dist/index.html
"""

import argparse
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
MARCADOR = re.compile(r"/\*__DADOS__\*/.*?/\*__FIM__\*/", re.S)

# Precisa espelhar TABS no motor. Um id fora desta lista é erro de digitação,
# e um erro de digitação silencioso custa uma aba que a pessoa acha que pediu.
ABAS = {
    "geral": None,
    "analise": "vagas",
    "progresso": "vagas",
    "mercado": "posicionamento",
    "cv": "cvGeral",
    "cursos": "cursos",
    "skills": "skills",
    "projetos": "projetos",
    "aplicadas": "vagas",
    "arquivadas": "vagas",
    "metodo": "metodo",
}


def tem_dados(dados, chave):
    if not chave:
        return True
    v = dados.get(chave)
    return bool(v)


def validar(dados):
    """Devolve (abas_boas, erros, avisos)."""
    erros, avisos = [], []

    tabs = dados.get("tabs")
    if not tabs:
        avisos.append('sem "tabs" — usando o padrão geral/analise/aplicadas/arquivadas')
        tabs = ["geral", "analise", "aplicadas", "arquivadas"]
    if not isinstance(tabs, list):
        erros.append('"tabs" precisa ser uma lista')
        return [], erros, avisos

    boas = []
    for t in tabs:
        if t not in ABAS:
            erros.append('aba desconhecida: "%s" (conhecidas: %s)' % (t, ", ".join(sorted(ABAS))))
            continue
        if not tem_dados(dados, ABAS[t]):
            avisos.append('aba "%s" pedida, mas "%s" está vazio — não vai aparecer' % (t, ABAS[t]))
            continue
        boas.append(t)

    # ids repetidos entre vagas e leads quebram o funil: o estágio é por id.
    ids = [v.get("id") for v in dados.get("vagas", [])] + [l.get("id") for l in dados.get("leads", [])]
    vistos, repetidos = set(), set()
    for i in ids:
        if i in vistos:
            repetidos.add(i)
        vistos.add(i)
    if repetidos:
        erros.append("ids repetidos entre vagas/leads: %s" % ", ".join(str(r) for r in sorted(repetidos)))
    if any(not i for i in ids):
        erros.append("toda vaga e todo lead precisa de um \"id\"")

    return boas, erros, avisos


def main():
    ap = argparse.ArgumentParser(description="Gera o console a partir do motor + dados.")
    ap.add_argument("--data", default="exemplo/console.json")
    ap.add_argument("--engine", default="skill/career-console/assets/console.html")
    ap.add_argument("--out", default="dist/index.html")
    ap.add_argument("--force", action="store_true", help="gera mesmo com erros de validação")
    args = ap.parse_args()

    dados_p = (RAIZ / args.data).resolve()
    motor_p = (RAIZ / args.engine).resolve()
    saida_p = (RAIZ / args.out).resolve()

    for p in (dados_p, motor_p):
        if not p.exists():
            sys.exit("não encontrei %s" % p)

    try:
        dados = json.loads(dados_p.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        sys.exit("%s não é JSON válido: linha %d, coluna %d — %s" % (dados_p.name, e.lineno, e.colno, e.msg))

    boas, erros, avisos = validar(dados)
    for a in avisos:
        print("  aviso: %s" % a)
    for e in erros:
        print("  ERRO:  %s" % e)
    if erros and not args.force:
        sys.exit("\nnada foi gerado. Corrija os erros acima, ou rode com --force.")

    motor = motor_p.read_text(encoding="utf-8")
    if not MARCADOR.search(motor):
        sys.exit("o motor não tem o marcador /*__DADOS__*/ … /*__FIM__*/")

    bruto = json.dumps(dados, ensure_ascii=False, separators=(",", ":"))
    # Um "</script>" dentro de qualquer texto fecharia o bloco e derrubaria a
    # página. O escape é obrigatório, não defensivo.
    bruto = bruto.replace("</", "<\\/")

    html = MARCADOR.sub(lambda _: bruto, motor, count=1)
    saida_p.parent.mkdir(parents=True, exist_ok=True)
    saida_p.write_text(html, encoding="utf-8")

    try:
        mostrar = saida_p.relative_to(RAIZ)
    except ValueError:
        mostrar = saida_p          # --out fora do repositório: mostra o caminho inteiro
    print("\n%s — %.1f KB" % (mostrar, len(html.encode("utf-8")) / 1024))
    print("abas: %s" % (", ".join(boas) if boas else "nenhuma"))


if __name__ == "__main__":
    main()
