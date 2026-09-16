def validar_resultado(resultado):
    if "cenarios" not in resultado:
        return False

    if "massas" not in resultado:
        return False

    if not resultado["cenarios"]:
        return False

    if not resultado["massas"]:
        return False

    for massa in resultado["massas"]:
        if not isinstance(massa, dict):
            return False

        if not massa:
            return False

    return True