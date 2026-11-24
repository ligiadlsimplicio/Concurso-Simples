# Caderneta de Fiscal

App de estudos para concurso público. Tem aulas curtas, banco de questões, simulados cronometrados e um sistema de recompensas (XP, níveis, sequência de dias e carimbos). Funciona no navegador do celular e pode ser instalado como app no Android, inclusive para usar sem internet.

A primeira versão foi feita para o concurso de **Fiscal de Posturas da Prefeitura de Patrocínio Paulista-SP** (Concurso Público 01/2026, banca Império Concursos, prova em 17/01/2027). Ela está organizada para receber outros concursos sem mudar o código.

## O que tem no app

| Tela | O que faz |
| --- | --- |
| Início | Contagem de dias até a prova, nível e XP, meta de 15 questões por dia, sequência de dias e desempenho por matéria |
| Estudar | 26 aulas divididas por matéria; cada aula termina com as questões do mesmo assunto |
| Questões | 203 questões, filtradas por matéria, assunto, origem (prova real ou inédita) e situação (não feitas ou erradas), com explicação logo após cada resposta |
| Simulados | Completo (40 questões em 3 horas, com o peso de cada matéria do edital), rápido (10 em 15 minutos) e por matéria, com histórico de notas |
| Carimbos | 11 conquistas, troca de concurso, importação de conteúdo e backup do progresso |

### Conteúdo de Patrocínio Paulista

- **Conhecimentos Específicos:** Código de Posturas (Lei 686/1973 e LC 10/2013), Código Tributário Municipal (LC 55/2021), Código Sanitário do Estado de SP (Lei 10.083/1998), Lei Orgânica do Município (Lei 2.048/2005) e Informática.
- **Língua Portuguesa, Matemática e Conhecimentos Gerais**, conforme o Anexo I do edital.
- **120 questões de provas reais** de fiscal de posturas (Vunesp, Avança SP, AGIRH, IPEFAE e outras), tiradas do PCI Concursos.
- **83 questões inéditas**, escritas a partir do texto das leis.

> **Atenção:** os gabaritos oficiais das provas reais não estavam disponíveis. As respostas foram conferidas uma a uma pela lei ou pela conta, e cada questão avisa isso no app. Questões de temas que não estão no edital (licitação, NBR 9050, leis ambientais etc.) ficam no banco, mas fora dos simulados.

## Publicar no GitHub Pages

1. Crie um repositório novo no GitHub (por exemplo, `caderneta-de-fiscal`). Pode ser público ou privado; o Pages grátis exige repositório público.
2. Envie todos os arquivos desta pasta: no repositório, clique em **Add file → Upload files**, arraste o conteúdo da pasta e confirme em **Commit changes**.
3. Vá em **Settings → Pages**. Em **Source**, escolha **Deploy from a branch**, depois a branch **main** e a pasta **/ (root)**. Salve.
4. Em um ou dois minutos o endereço aparece no topo da página, no formato `https://SEU-USUARIO.github.io/caderneta-de-fiscal/`.

## Instalar no celular (Android)

1. Abra o endereço do GitHub Pages no **Chrome** do celular.
2. Toque nos três pontinhos e em **Instalar app** (ou **Adicionar à tela inicial**).
3. O ícone aparece na tela inicial. O app abre em tela cheia e funciona sem internet depois da primeira abertura.

Para gerar um arquivo **.apk**, cole o endereço do GitHub Pages em [pwabuilder.com](https://www.pwabuilder.com), clique em **Package for stores → Android** e baixe o pacote.

## Progresso e backup

O progresso fica salvo **no próprio aparelho**, sem login. Se o navegador for limpo ou o celular trocado, o histórico se perde. Para evitar isso:

1. No app, vá em **Carimbos → Backup do progresso → Copiar backup**.
2. Guarde o texto copiado (numa conversa do WhatsApp com você mesma, por exemplo).
3. No aparelho novo, cole o texto no mesmo lugar e toque em **Restaurar backup**.

## Adicionar outro concurso

Cada concurso é um arquivo `.json` na pasta `dados/`. O arquivo `dados/exemplo-novo-concurso.json` mostra o formato mínimo.

**Pelo próprio app (sem mexer no código):** em **Carimbos → Concursos → Adicionar concurso ou questões**, escolha o arquivo `.json`.

- Se o `id` for novo, o concurso aparece na lista "Estudando para", com progresso próprio.
- Se o `id` for de um concurso que já existe, as aulas e questões novas são acrescentadas a ele (as repetidas são ignoradas).

### Formato do arquivo

```json
{
  "id": "identificador-unico-do-concurso",
  "nome": "Nome do cargo",
  "orgao": "Prefeitura de Exemplo-SP",
  "banca": "Nome da banca",
  "dataProva": "2027-05-10",
  "horaProva": "09:00",
  "duracaoMin": 180,
  "notaMinima": 50,
  "materias": [
    { "id": "port", "nome": "Língua Portuguesa", "curto": "Português", "qtd": 10, "valor": 2.5 }
  ],
  "aulas": [
    { "id": "a-1", "materia": "port", "assunto": "Crase", "titulo": "Crase sem medo",
      "cards": [ { "t": "Título da página", "b": "Texto com **negrito** marcado assim." } ] }
  ],
  "questoes": [
    { "id": "q-1", "materia": "port", "assunto": "Crase",
      "enunciado": "Texto da pergunta",
      "alternativas": ["A", "B", "C", "D"],
      "correta": 1,
      "explicacao": "Por que essa é a certa.",
      "origem": "prova",
      "fonte": "Banca 2025 · Pref. Exemplo/SP · Cargo" }
  ]
}
```

| Campo | Observação |
| --- | --- |
| `materias[].qtd` e `valor` | Quantas questões a matéria tem na prova e quanto vale cada uma; o simulado completo usa esses números |
| `correta` | Posição da alternativa certa, começando em **0** (0 = A, 1 = B, 2 = C...) |
| `alternativas` | De 2 a 5 opções |
| `origem` | `"prova"` para questão de prova real, `"inedita"` para questão criada |
| `extra` | Opcional. Use `true` para questões fora do edital: elas ficam no banco, mas não entram nos simulados |

## Estrutura do projeto

```
caderneta-de-fiscal/
├── index.html                 App completo (já traz o concurso de Patrocínio Paulista embutido)
├── manifest.webmanifest       Nome, cores e ícones para instalar no celular
├── sw.js                      Guarda o app para uso sem internet
├── icones/                    Ícones do app (192 e 512 px)
├── dados/
│   ├── patrocinio-fiscal-2026.json   Aulas e questões de Patrocínio Paulista
│   └── exemplo-novo-concurso.json    Modelo para um concurso novo
└── fonte/
    ├── template.html          Código do app, sem os dados
    ├── conteudo_patrocinio.py Aulas e questões de Patrocínio em Python (gera o JSON)
    └── montar.py              Junta template + JSON e gera o index.html
```

### Atualizar o conteúdo de Patrocínio Paulista

Requer Python 3.

```bash
cd fonte
python3 conteudo_patrocinio.py   # regenera dados/patrocinio-fiscal-2026.json
python3 montar.py                # regenera o index.html
```

Depois de publicar uma versão nova, troque o número em `sw.js` (`caderneta-v3` → `caderneta-v4`) para os celulares baixarem a atualização.

## Fontes do conteúdo

- Edital do Concurso Público 01/2026 de Patrocínio Paulista (Império Assessoria e Concursos).
- Textos das leis municipais (Lei 686/1973, LC 10/2013, LC 55/2021 e Lei Orgânica 2.048/2005), obtidos no Leis.org e no portal da Prefeitura.
- Lei Estadual 10.083/1998, pelo site da Assembleia Legislativa de SP.
- Provas anteriores de fiscal de posturas publicadas no [PCI Concursos](https://www.pciconcursos.com.br).

As questões de provas reais pertencem às respectivas bancas e foram incluídas apenas para estudo pessoal.
