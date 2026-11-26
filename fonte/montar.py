"""Monta o index.html juntando o template do app com os concursos que já vêm instalados.

Uso, dentro da pasta fonte:
    python3 montar.py                       # usa os concursos listados em CONCURSOS, abaixo
    python3 montar.py nome-1 nome-2         # usa dados/nome-1.json e dados/nome-2.json

O primeiro da lista é o que abre por padrão para quem instala o app pela primeira vez.
Quem já usa o app continua no concurso que escolheu em "Estudando para".
"""
import json, pathlib, sys

CONCURSOS = ["patrocinio-fiscal-2026", "oficial-justica-tjsp-2026"]

aqui = pathlib.Path(__file__).resolve().parent
raiz = aqui.parent
nomes = sys.argv[1:] or CONCURSOS
lista = []
for nome in nomes:
    dados = json.loads((raiz / "dados" / f"{nome}.json").read_text(encoding="utf-8"))
    ids = [q["id"] for q in dados["questoes"]]
    assert len(ids) == len(set(ids)), f"Há questões com id repetido em {nome}"
    materias = {m["id"] for m in dados["materias"]}
    for q in dados["questoes"]:
        assert 0 <= q["correta"] < len(q["alternativas"]), f"Resposta fora das alternativas em {q['id']}"
        assert q["materia"] in materias, f"Matéria inexistente em {q['id']}"
    lista.append(dados)
    print(f"{nome}: {len(dados['aulas'])} aulas, {len(dados['questoes'])} questões")

json_txt = json.dumps(lista, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
html = (aqui / "template.html").read_text(encoding="utf-8")
html = html.replace('<meta name="theme-color" content="#2a4bd7">',
    '<meta name="theme-color" content="#2a4bd7">\n<link rel="manifest" href="manifest.webmanifest">\n'
    '<link rel="icon" href="icon-192.png">\n<link rel="apple-touch-icon" href="icon-192.png">')
html = html.replace("</body>", '<script>if("serviceWorker" in navigator)navigator.serviceWorker.register("./sw.js").catch(()=>{});</script>\n</body>')
html = html.replace("__DADOS__", json_txt)
(raiz / "index.html").write_text(html, encoding="utf-8")
print("index.html gerado com", len(lista), "concursos")
