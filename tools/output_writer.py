# tools/output_writer.py
# Salva o resultado do agente em arquivos locais

import os
from config.settings import OUTPUT_DIR

def salvar_resultado(nome, resultado):

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    salvar_markdown(nome, resultado)
    salvar_python(nome, resultado)

    print(f"\nArquivos salvos em: {OUTPUT_DIR}/")

def salvar_markdown(nome, resultado):

    caminho = f"{OUTPUT_DIR}/relatorio_{nome}.md"

    conteudo = f"# Relatório de QA — {nome}\n\n"

    conteudo += "## Cenários\n\n"
    for i, cenario in enumerate(resultado["cenarios"], 1):
        conteudo += f"{i}. {cenario}\n"

    conteudo += "\n## Massas de dados\n\n"
    for massa in resultado["massas"]:
        for campo, valor in massa.items():
            conteudo += f"- **{campo}:** {valor}\n"
        conteudo += "\n"

    with open(caminho, "w", encoding="utf-8") as arquivo:
        arquivo.write(conteudo)

    print(f"Relatório: {caminho}")    

def salvar_python(nome, resultado):

    caminho = f"{OUTPUT_DIR}/massas_{nome}.py"

    conteudo = f"# Massas de dados — {nome}\n\n"
    conteudo += f"CENARIOS = {resultado['cenarios']}\n\n"
    conteudo += f"MASSAS = {resultado['massas']}\n"

    with open(caminho, "w", encoding="utf-8") as arquivo:
        arquivo.write(conteudo)

    print(f"Massas Python: {caminho}")    