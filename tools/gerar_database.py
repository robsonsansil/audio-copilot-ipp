"""
==========================================================
Audio Copilot IPP
Gerador de database.js

Autor: Audio Copilot IPP

Descrição
---------
Lê todos os arquivos Markdown existentes em:

    docs/presets/

e gera automaticamente:

    web/presets/js/database.js

Não edite manualmente o arquivo database.js,
pois ele será sobrescrito sempre que este script
for executado.

==========================================================
"""

from pathlib import Path
import json

# ==========================================================
# CONFIGURAÇÃO
# ==========================================================

PROJETO = Path(__file__).resolve().parent.parent

PASTA_PRESETS = PROJETO / "docs" / "presets"

ARQUIVO_SAIDA = (
    PROJETO
    / "web"
    / "presets"
    / "js"
    / "database.js"
)

ARQUIVOS_IGNORADOS = {
    "README.md",
    "PRESETS-OFICIAIS.md"
}

# ==========================================================
# FUNÇÕES
# ==========================================================


def obter_titulo(markdown: str, chave: str) -> str:
    """
    Procura o primeiro título '# ' do Markdown.

    Caso não exista, utiliza o nome do arquivo.
    """

    for linha in markdown.splitlines():

        linha = linha.strip()

        if linha.startswith("# "):
            return linha[2:].strip()

    return chave.replace("-", " ").title()


# ==========================================================
# INÍCIO
# ==========================================================

print("=" * 60)
print("Audio Copilot IPP")
print("Gerador de database.js")
print("=" * 60)
print()

database = {}

arquivos = sorted(PASTA_PRESETS.rglob("*.md"))

# ==========================================================
# LEITURA DOS PRESETS
# ==========================================================

for arquivo in arquivos:

    if arquivo.name in ARQUIVOS_IGNORADOS:
        continue

    relativo = arquivo.relative_to(PASTA_PRESETS)

    print(f"Lendo: {relativo}")

    categoria = (
        relativo.parts[0]
        if len(relativo.parts) > 1
        else "geral"
    )

    chave = arquivo.stem

    markdown = arquivo.read_text(
        encoding="utf-8"
    )

    titulo = obter_titulo(
        markdown,
        chave
    )

    database[chave] = {

        "id": chave,

        "titulo": titulo,

        "categoria": categoria,

        "arquivo": arquivo.name,

        "caminho": str(relativo).replace("\\", "/"),

        "markdown": markdown

    }

# ==========================================================
# GARANTE A PASTA DE SAÍDA
# ==========================================================

ARQUIVO_SAIDA.parent.mkdir(
    parents=True,
    exist_ok=True
)

# ==========================================================
# GERA O ARQUIVO JAVASCRIPT
# ==========================================================

cabecalho = """// ======================================================
// Audio Copilot IPP
//
// ESTE ARQUIVO É GERADO AUTOMATICAMENTE.
//
// NÃO EDITE MANUALMENTE.
//
// Execute:
//
//     py tools/gerar_database.py
//
// ======================================================

const DATABASE =

"""

conteudo = cabecalho

conteudo += json.dumps(
    database,
    ensure_ascii=False,
    indent=4
)

conteudo += ";\n"

ARQUIVO_SAIDA.write_text(
    conteudo,
    encoding="utf-8"
)

# ==========================================================
# RESUMO
# ==========================================================

print()
print("-" * 60)
print(f"Presets encontrados : {len(database)}")
print(f"Arquivo gerado      : {ARQUIVO_SAIDA}")
print("-" * 60)
print()

print("Concluído com sucesso!")