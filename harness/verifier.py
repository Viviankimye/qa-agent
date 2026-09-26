def verificar_resultado(spec, resultado):
    motivos = []

    if resultado.get("confianca", 1.0) < 1.0:
        motivos.append("Baixa confiança na classificação")

    if resultado["dominio"] != spec["dominio"]:
        motivos.append("Domínio diferente da Spec")

    if spec["requisitos"]["cenarios"] and not resultado["cenarios"]:
        motivos.append("Resultado sem cenários")

    if spec["requisitos"]["massas"] and not resultado["massas"]:
        motivos.append("Resultado sem massas")

    for massa in resultado["massas"]:
        if not isinstance(massa, dict) or not massa:
            motivos.append("Massa inválida")

    return {
        "aprovado": len(motivos) == 0,
        "motivos": motivos
    }