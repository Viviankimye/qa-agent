def validar_plano(plano):
    motivos = []

    if plano["confianca"] < 1.0:
        motivos.append(
            "Baixa confiança para execução"
        )

    if plano["dominio"] is None:
        motivos.append(
            "Domínio não definido para execução"
        )

    if not plano["tarefas"]:
        motivos.append(
            "Plano sem tarefas para execução"
        )

    return {
        "aprovado": len(motivos) == 0,
        "motivos": motivos
    }
