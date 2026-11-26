"""Converte as planilhas (CSV) de um concurso no arquivo JSON que o app usa.

Cada concurso fica numa pasta dentro de planilhas/, com 4 arquivos CSV:
    concurso.csv   dados gerais (campo, valor)
    materias.csv   uma linha por matéria
    aulas.csv      uma linha por PÁGINA de aula
    questoes.csv   uma linha por questão (a coluna "texto" é opcional: texto de apoio da questão)

Os CSV podem ser editados no Excel, LibreOffice ou Google Planilhas
(salve como CSV, separado por vírgula, codificação UTF-8).

Uso, dentro da pasta fonte:
    python3 planilha_para_json.py patrocinio-fiscal-2026
O resultado vai para dados/<nome-da-pasta>.json
"""
import csv, json, sys, pathlib

RAIZ = pathlib.Path(__file__).resolve().parent.parent
LETRAS = "ABCDE"


def ler(arquivo):
    with open(arquivo, encoding="utf-8-sig", newline="") as f:
        return [{k.strip(): (v or "").strip() for k, v in linha.items()} for linha in csv.DictReader(f)]


def converter(nome):
    pasta = RAIZ / "planilhas" / nome
    erros = []

    geral = {l["campo"]: l["valor"] for l in ler(pasta / "concurso.csv")}
    concurso = {
        "id": geral["id"], "nome": geral["nome"], "orgao": geral["orgao"], "banca": geral["banca"],
        "dataProva": geral["dataProva"], "horaProva": geral.get("horaProva", "08:00"),
        "duracaoMin": int(geral.get("duracaoMin", 180)), "notaMinima": float(geral.get("notaMinima", 50)),
        "materias": [], "aulas": [], "questoes": [],
    }
    if concurso["notaMinima"].is_integer():
        concurso["notaMinima"] = int(concurso["notaMinima"])
    # campos opcionais
    for campo in ("aviso", "notaExtra"):
        if geral.get(campo):
            concurso[campo] = geral[campo]
    if geral.get("maisQuestoes_url"):
        concurso["maisQuestoes"] = {"antes": geral.get("maisQuestoes_antes", ""), "nome": geral.get("maisQuestoes_nome", "Mais questões"),
                                    "url": geral["maisQuestoes_url"], "depois": geral.get("maisQuestoes_depois", "")}
    if geral.get("carimbo_assunto"):
        concurso["carimboAulas"] = {"assunto": geral["carimbo_assunto"], "nome": geral.get("carimbo_nome", "Aulas concluídas"),
                                    "desc": geral.get("carimbo_desc", "Concluiu as aulas do assunto")}

    for m in ler(pasta / "materias.csv"):
        concurso["materias"].append({"id": m["id"], "nome": m["nome"], "curto": m["curto"],
                                     "qtd": int(m["qtd"]), "valor": float(m["valor"].replace(",", "."))})
    ids_materia = {m["id"] for m in concurso["materias"]}

    aulas = {}
    for i, p in enumerate(ler(pasta / "aulas.csv"), start=2):
        if p["materia"] not in ids_materia:
            erros.append(f"aulas.csv linha {i}: matéria '{p['materia']}' não existe em materias.csv")
        if p["id_aula"] not in aulas:
            aulas[p["id_aula"]] = {"id": p["id_aula"], "materia": p["materia"], "assunto": p["assunto"],
                                   "titulo": p["titulo_aula"], "cards": []}
            concurso["aulas"].append(aulas[p["id_aula"]])
        aulas[p["id_aula"]]["cards"].append({"t": p["titulo_pagina"], "b": p["texto_pagina"]})

    vistos = set()
    for i, q in enumerate(ler(pasta / "questoes.csv"), start=2):
        alts = [q[f"alternativa_{l}"] for l in LETRAS if q.get(f"alternativa_{l}")]
        certa = q["correta"].upper()
        if q["id"] in vistos:
            erros.append(f"questoes.csv linha {i}: id '{q['id']}' repetido")
        if q["materia"] not in ids_materia:
            erros.append(f"questoes.csv linha {i}: matéria '{q['materia']}' não existe em materias.csv")
        if certa not in LETRAS[:len(alts)]:
            erros.append(f"questoes.csv linha {i}: resposta '{certa}' não corresponde a nenhuma alternativa")
            continue
        vistos.add(q["id"])
        item = {"id": q["id"], "materia": q["materia"], "assunto": q["assunto"], "enunciado": q["enunciado"],
                "alternativas": alts, "correta": LETRAS.index(certa), "explicacao": q["explicacao"],
                "origem": q.get("origem") or "inedita", "fonte": q.get("fonte") or "Questão inédita"}
        if q.get("texto"):
            item["texto"] = q["texto"]
        if q.get("fora_do_edital", "").lower() in ("sim", "s", "x", "1", "true"):
            item["extra"] = True
        concurso["questoes"].append(item)

    if erros:
        print("Corrija antes de continuar:")
        print("\n".join("  - " + e for e in erros))
        sys.exit(1)

    destino = RAIZ / "dados" / f"{nome}.json"
    destino.write_text(json.dumps(concurso, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{destino.name}: {len(concurso['aulas'])} aulas, {len(concurso['questoes'])} questões")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    converter(sys.argv[1])
