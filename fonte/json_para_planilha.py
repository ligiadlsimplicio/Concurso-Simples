"""Faz o caminho inverso: transforma um JSON da pasta dados/ em planilhas CSV editáveis.

Uso, dentro da pasta fonte:
    python3 json_para_planilha.py patrocinio-fiscal-2026
"""
import csv, json, sys, pathlib

RAIZ = pathlib.Path(__file__).resolve().parent.parent


def gravar(arquivo, cabecalho, linhas):
    with open(arquivo, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(cabecalho)
        w.writerows(linhas)


def exportar(nome):
    c = json.loads((RAIZ / "dados" / f"{nome}.json").read_text(encoding="utf-8"))
    pasta = RAIZ / "planilhas" / nome
    pasta.mkdir(parents=True, exist_ok=True)
    geral = [[k, c[k]] for k in ("id", "nome", "orgao", "banca", "dataProva", "horaProva", "duracaoMin", "notaMinima")]
    geral += [[k, c[k]] for k in ("aviso", "notaExtra") if c.get(k)]
    if c.get("maisQuestoes"):
        geral += [["maisQuestoes_" + k, c["maisQuestoes"].get(k, "")] for k in ("antes", "nome", "url", "depois")]
    if c.get("carimboAulas"):
        geral += [["carimbo_" + k, c["carimboAulas"][k]] for k in ("assunto", "nome", "desc")]
    gravar(pasta / "concurso.csv", ["campo", "valor"], geral)
    gravar(pasta / "materias.csv", ["id", "nome", "curto", "qtd", "valor"],
           [[m["id"], m["nome"], m["curto"], m["qtd"], m["valor"]] for m in c["materias"]])
    gravar(pasta / "aulas.csv", ["id_aula", "materia", "assunto", "titulo_aula", "titulo_pagina", "texto_pagina"],
           [[a["id"], a["materia"], a["assunto"], a["titulo"], p["t"], p["b"]] for a in c["aulas"] for p in a["cards"]])
    linhas = []
    for q in c["questoes"]:
        alts = q["alternativas"] + [""] * (5 - len(q["alternativas"]))
        linhas.append([q["id"], q["materia"], q["assunto"], q["enunciado"], *alts, "ABCDE"[q["correta"]],
                       q["explicacao"], q["origem"], q["fonte"], "sim" if q.get("extra") else "", q.get("texto", "")])
    gravar(pasta / "questoes.csv", ["id", "materia", "assunto", "enunciado", "alternativa_A", "alternativa_B",
                                    "alternativa_C", "alternativa_D", "alternativa_E", "correta", "explicacao",
                                    "origem", "fonte", "fora_do_edital", "texto"], linhas)
    print(f"Planilhas criadas em planilhas/{nome}/")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    exportar(sys.argv[1])
