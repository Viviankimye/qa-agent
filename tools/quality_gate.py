def avaliar_resultado(resultado):
    if resultado["confianca"] != 1.0:
        return False

    if not resultado["cenarios"]:
        return False

    if not resultado["massas"]:
        return False

    return True
