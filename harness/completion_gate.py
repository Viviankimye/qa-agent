def validar_conclusao(verificacao, julgamento):
    motivos = []

    if not verificacao["aprovado"]:
        motivos.extend(verificacao["motivos"])

    if not julgamento["aprovado"]:
        motivos.extend(julgamento["motivos"])

    if not verificacao["aprovado"] and julgamento["aprovado"]:
        motivos.append(
            "Verifier reprovou, mas Judge aprovou"
        )

    return {
        "aprovado": len(motivos) == 0,
        "motivos": motivos
    }
