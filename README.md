# Caderneta de Fiscal

App de estudos para concurso público. Tem aulas curtas, banco de questões, simulados cronometrados e um sistema de recompensas (XP, níveis, sequência de dias e carimbos). Funciona no navegador do celular e pode ser instalado como app no Android, inclusive para usar sem internet.

A primeira versão foi feita para o concurso de **Fiscal de Posturas da Prefeitura de Patrocínio Paulista-SP** (Concurso Público 01/2026, banca Império Concursos, prova em 17/01/2027). Outros concursos entram por planilha, sem mexer no código.

## O que tem no app

| Tela | O que faz |
| --- | --- |
| Início | Contagem de dias até a prova, nível e XP, meta de 15 questões por dia, sequência de dias e desempenho por matéria |
| Estudar | 26 aulas divididas por matéria; cada aula termina com as questões do mesmo assunto |
| Questões | 203 questões, filtradas por matéria, assunto, origem (prova real ou inédita) e situação (não feitas ou erradas), com explicação logo após cada resposta |
| Simulados | Completo (40 questões em 3 horas, com o peso de cada matéria do edital), rápido (10 em 15 minutos) e por matéria, com histórico de notas |
| Carimbos | 11 conquistas, troca de concurso, importação de conteúdo e backup do progresso |

### Conteúdo de Patrocínio Paulista

- **Conhecimentos Específicos:** Código de Posturas (Lei 686/1973 e LC 10/2013), Código Tributário Municipal (LC 55/2021), Código Sanitário do Estado de SP (Lei 10.083/1998), Lei Orgânica do Município (Lei 2.048/2005), rotina do fiscal e Informática.
- **Língua Portuguesa, Matemática e Conhecimentos Gerais**, conforme o Anexo I do edital.
- **120 questões de provas reais** de fiscal de posturas (Vunesp, Avança SP, AGIRH, IPEFAE e outras), tiradas do PCI Concursos.
- **83 questões inéditas**, escritas a partir do texto das leis.

> **Atenção:** os gabaritos oficiais das provas reais não estavam disponíveis. As respostas foram conferidas uma a uma pela lei ou pela conta, e cada questão avisa isso no app. Questões de temas que não estão no edital (licitação, NBR 9050, leis ambientais etc.) ficam no banco, mas fora dos simulados.

### Conteúdo de Oficial de Justiça (TJSP 2026, Vunesp)

- **19 aulas** pelo conteúdo programático do edital: atos do oficial no CPC, citação, hora certa, intimação, penhora, avaliação, citação e prisão no CPP, crimes contra a Administração, Constitucional, Estatuto SP, improbidade, Civil, LINDB, execução fiscal, Resolução CNJ 354/2020, taxa judiciária, Estatuto da Pessoa com Deficiência e Português da Vunesp.
- **224 questões de provas reais com gabarito oficial**: TJSP Escrevente 2025 e 2021, TJSP Oficial de Justiça 2009 e TJM-SP Oficial de Justiça 2011. As questões de Português trazem o texto da prova.
- **150 questões inéditas** no formato Vunesp, com o artigo de lei na explicação.
- Questões de provas antigas sobre artigos que o edital não pede, ou de atualidades de anos anteriores, ficam fora dos simulados.

---

## 1. Publicar no GitHub Pages

O GitHub Pages hospeda o app de graça e gera um endereço que abre em qualquer celular.

1. Crie uma conta em [github.com](https://github.com), se ainda não tiver.
2. Clique em **New repository**. Dê um nome (por exemplo, `caderneta-de-fiscal`), marque **Public** e clique em **Create repository**. O Pages gratuito só funciona com repositório público.
3. Na página do repositório, clique em **uploading an existing file** (ou **Add file → Upload files**).
4. Arraste **o conteúdo** desta pasta, e não a pasta em si: o `index.html` precisa ficar na raiz do repositório. Clique em **Commit changes**.
5. Vá em **Settings → Pages**. Em **Source**, escolha **Deploy from a branch**; em **Branch**, escolha **main** e **/ (root)**. Clique em **Save**.
6. Espere um ou dois minutos e recarregue a página. O endereço aparece no topo, no formato `https://SEU-USUARIO.github.io/caderneta-de-fiscal/`.

## 2. Instalar no celular Android

1. No celular, abra o **Google Chrome** (outros navegadores podem não oferecer a instalação).
2. Digite o endereço do GitHub Pages e espere o app carregar por completo.
3. Toque nos **três pontinhos** no canto superior direito.
4. Toque em **Instalar app**. Se não aparecer, use **Adicionar à tela inicial → Instalar**.
5. Confirme. O ícone azul **Caderneta** aparece na tela inicial.
6. Abra pelo ícone, com a internet ligada, ao menos uma vez. A partir daí ele funciona também sem internet.

**Quer um arquivo .apk?** Entre em [pwabuilder.com](https://www.pwabuilder.com), cole o endereço do GitHub Pages, clique em **Package for stores → Android → Generate** e baixe o pacote. Para instalar um .apk fora da Play Store, o Android pede para permitir "instalar apps desconhecidos" no gerenciador de arquivos.

**Atualizações:** quando uma versão nova for publicada, basta abrir o app com internet. Ele baixa a novidade sozinho e passa a usá-la na abertura seguinte.

## 3. Compartilhar com outras pessoas

O app não tem login nem servidor. Cada pessoa usa o mesmo endereço, e o progresso de cada uma fica guardado só no aparelho dela. Por isso:

- **Para compartilhar, basta mandar o link** do GitHub Pages. Cada pessoa segue o passo 2 para instalar.
- **Ninguém vê o progresso de ninguém.** XP, respostas, carimbos e simulados ficam no celular de cada um.
- **Não há custo nem limite de usuários**: o GitHub Pages serve o arquivo, e todo o resto roda no celular.
- **Cada pessoa pode estudar para um concurso diferente.** Em **Carimbos → Concursos → Adicionar concurso ou questões**, ela escolhe o arquivo `.json` do concurso dela (veja a seção 4). Esse concurso fica só no aparelho dela.
- **Para oferecer um concurso a todos**, coloque o `.json` na pasta `dados/` do repositório e mande o link do arquivo. Exemplo: `https://SEU-USUARIO.github.io/caderneta-de-fiscal/dados/nome-do-concurso.json`. A pessoa baixa e importa pelo app.
- **Para trocar o concurso que abre por padrão** para todo mundo, veja a seção 5.

Cuidados ao deixar o app público:

- O repositório e o conteúdo ficam visíveis para qualquer pessoa.
- As questões de provas reais pertencem às bancas. Mantenha a nota de uso para estudo e não cobre pelo acesso.
- Lembre quem usa de fazer o backup (seção 6), porque limpar o navegador apaga o progresso.

## 4. Criar ou editar um concurso pela planilha

Todo o conteúdo fica em planilhas, que podem ser abertas no **Excel**, no **LibreOffice** ou no **Google Planilhas**. Um script em Python converte as planilhas para o formato do app.

Cada concurso é uma pasta dentro de `planilhas/`, com quatro arquivos:

| Arquivo | Uma linha para cada | Colunas |
| --- | --- | --- |
| `concurso.csv` | informação geral | `campo`, `valor` (id, nome, orgao, banca, dataProva no formato AAAA-MM-DD, horaProva, duracaoMin, notaMinima) |
| `materias.csv` | matéria da prova | `id` (curto, sem espaço), `nome`, `curto` (nome no menu), `qtd` (questões na prova), `valor` (pontos por acerto) |
| `aulas.csv` | **página** de aula | `id_aula`, `materia`, `assunto`, `titulo_aula`, `titulo_pagina`, `texto_pagina` |
| `questoes.csv` | questão | `id`, `materia`, `assunto`, `enunciado`, `alternativa_A` a `alternativa_E`, `correta` (letra), `explicacao`, `origem`, `fonte`, `fora_do_edital`, `texto` (opcional) |

Dicas para preencher:

- **Aulas com várias páginas:** repita o mesmo `id_aula` em várias linhas, uma para cada página, na ordem em que devem aparecer.
- **Negrito:** escreva `**assim**` no texto da página.
- **Alternativas:** podem ser de 2 a 5. Deixe vazias as colunas que não usar.
- **`correta`:** a letra da alternativa certa (A, B, C, D ou E).
- **`origem`:** `prova` para questão de prova real, `inedita` para questão criada. Em `fonte`, escreva banca, órgão e ano.
- **`fora_do_edital`:** escreva `sim` para a questão ficar no banco, mas fora dos simulados.
- **`texto`:** opcional. Texto de apoio da questão (por exemplo, o texto de interpretação de Português). Aparece numa caixa que abre e fecha acima do enunciado.
- **Campos opcionais em `concurso.csv`:** `aviso` (explicação da nota mínima na tela inicial), `notaExtra` (aviso sobre questões fora do edital), `maisQuestoes_nome` e `maisQuestoes_url` (link para mais questões).
- **`assunto`:** use o mesmo texto na aula e nas questões. É assim que o botão "Praticar" de cada aula encontra as questões certas.
- Ao salvar, escolha **CSV UTF-8 (separado por vírgulas)**. No Google Planilhas: **Arquivo → Fazer download → Valores separados por vírgula**.

### Passo a passo de um concurso novo

1. Copie a pasta `planilhas/exemplo-novo-concurso` e dê a ela o nome do concurso (por exemplo, `planilhas/franca-agente-2027`).
2. Edite os quatro arquivos CSV.
3. Converta para o formato do app (é preciso ter o [Python 3](https://www.python.org/downloads/) instalado):

   ```bash
   cd fonte
   python3 planilha_para_json.py franca-agente-2027
   ```

   No Windows, troque `python3` por `python`. O script aponta erros com o número da linha: matéria que não existe, id repetido, resposta sem alternativa correspondente.

4. O arquivo `dados/franca-agente-2027.json` fica pronto. Importe pelo app (**Carimbos → Concursos**) ou publique no GitHub para compartilhar.

### Editar o concurso de Patrocínio Paulista

```bash
cd fonte
python3 planilha_para_json.py patrocinio-fiscal-2026   # planilhas -> JSON
python3 montar.py                                      # JSON -> index.html
```

Para transformar em planilha um JSON que já existe, use `python3 json_para_planilha.py nome-do-concurso`.

## 5. Escolher os concursos que vêm no app

O `index.html` já traz **Fiscal de Posturas (Patrocínio Paulista)** e **Oficial de Justiça (TJSP)**. Quem usa troca entre eles em **Carimbos → Estudando para**. O progresso de cada concurso é guardado separado.

A lista fica no topo do `fonte/montar.py`, na linha `CONCURSOS = [...]`. O primeiro da lista é o que abre para quem instala pela primeira vez. Também dá para passar os nomes na hora:

```bash
cd fonte
python3 montar.py patrocinio-fiscal-2026 oficial-justica-tjsp-2026 franca-agente-2027
```

Depois suba o `index.html` novo para o GitHub e, no `sw.js`, aumente o número em `caderneta-v6` (por exemplo, `caderneta-v7`). Isso faz os celulares baixarem a versão nova.

## 6. Backup do progresso

1. No app, vá em **Carimbos → Backup do progresso → Copiar backup**.
2. Guarde o texto copiado (numa conversa do WhatsApp com você mesmo, ou num e-mail).
3. No aparelho novo, cole o texto no mesmo campo e toque em **Restaurar backup**.

---

## Por que o app é em HTML e JavaScript, e não em Python?

O celular só roda, sem instalar nada, o que o navegador entende: HTML, CSS e JavaScript. Um app escrito em Python precisaria de ferramentas como Kivy ou BeeWare e do kit de desenvolvimento do Android para virar .apk. O resultado seria mais pesado, mais difícil de atualizar e não funcionaria no iPhone nem no computador.

Por isso a divisão ficou assim:

- **Conteúdo:** em planilhas, editáveis por qualquer pessoa.
- **Ferramentas:** em Python (`planilha_para_json.py`, `json_para_planilha.py`, `montar.py`), com comentários em português.
- **App:** em um único arquivo HTML, sem bibliotecas externas, que não precisa ser mexido para acrescentar conteúdo.

## Estrutura do projeto

```
caderneta-de-fiscal/
├── index.html                  App completo, com o concurso padrão embutido
├── manifest.webmanifest        Nome, cores e ícones para instalar no celular
├── sw.js                       Guarda o app para uso sem internet
├── icones/                     Ícones do app (192 e 512 px)
├── planilhas/                  CONTEÚDO EDITÁVEL (um concurso por pasta)
│   ├── patrocinio-fiscal-2026/   concurso.csv, materias.csv, aulas.csv, questoes.csv
│   └── exemplo-novo-concurso/    modelo para copiar
├── dados/                      Arquivos .json gerados a partir das planilhas
└── fonte/
    ├── template.html           Código do app, sem os dados
    ├── planilha_para_json.py   Planilhas -> JSON (com verificação de erros)
    ├── json_para_planilha.py   JSON -> planilhas
    └── montar.py               Template + JSON -> index.html
```

## Fontes do conteúdo

- Edital do Concurso Público 01/2026 de Patrocínio Paulista (Império Assessoria e Concursos).
- Textos das leis municipais (Lei 686/1973, LC 10/2013, LC 55/2021 e Lei Orgânica 2.048/2005), obtidos no Leis.org e no portal da Prefeitura.
- Lei Estadual 10.083/1998, pelo site da Assembleia Legislativa de SP.
- Provas anteriores de fiscal de posturas publicadas no [PCI Concursos](https://www.pciconcursos.com.br).
- Edital do concurso de Oficial de Justiça do TJSP (2026) e provas da Vunesp para o TJSP e o TJM-SP, com os gabaritos oficiais publicados pelos tribunais.

As questões de provas reais pertencem às respectivas bancas e foram incluídas apenas para estudo, sem fins comerciais.
