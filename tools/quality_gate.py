def avaliar_resultado(resultado):
    motivos = []

    if resultado["confianca"] != 1.0:
        motivos.append("Baixa confiança na classificação")

    if not resultado["cenarios"]:
        motivos.append("Resultado sem cenários")

    if not resultado["massas"]:
        motivos.append("Resultado sem massas")

    return {
        "aprovado": len(motivos) == 0,
        "motivos": motivos
    }
