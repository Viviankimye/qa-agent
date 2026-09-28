def avaliar_resiliencia(resultado):
    if resultado["aprovado"]:
        status = "OK"
    else:
        status = "ESCALATED"

    return {
        "intervencao_humana": not resultado["aprovado"],
        "motivos": resultado["motivos"],
        "status": status
    }
