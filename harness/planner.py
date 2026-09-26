def criar_plano(spec):
    tarefas = []

    if spec["requisitos"]["cenarios"]:
        tarefas.append("gerar cenários")

    if spec["requisitos"]["massas"]:
        tarefas.append("gerar massas")

    if spec["requisitos"]["validacao"]:
        tarefas.append("validar resultado")

    return {
        "dominio": spec["dominio"],
        "confianca": spec["confianca"],
        "tarefas": tarefas
}