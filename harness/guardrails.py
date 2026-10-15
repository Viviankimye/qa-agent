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


def validar_escopo_seguranca(escopo_autorizado, alvo):
    motivos = []

    if escopo_autorizado is None:
        motivos.append("Escopo de segurança não autorizado")
    elif (
        not isinstance(escopo_autorizado, dict)
        or not isinstance(escopo_autorizado.get("alvos"), list)
        or not escopo_autorizado["alvos"]
    ):
        motivos.append("Escopo de segurança inválido")

    if not isinstance(alvo, str) or not alvo.strip():
        motivos.append("Alvo de segurança inválido")
    elif (
        isinstance(escopo_autorizado, dict)
        and isinstance(escopo_autorizado.get("alvos"), list)
        and alvo not in escopo_autorizado["alvos"]
    ):
        motivos.append("Alvo fora do escopo autorizado")

    return {
        "aprovado": len(motivos) == 0,
        "motivos": motivos
    }
