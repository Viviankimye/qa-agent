def julgar_resultado(resultado, verificacao):
    if not verificacao["aprovado"]:
        return {
            "aprovado": False,
            "motivos": verificacao["motivos"]
        }

    return {
        "aprovado": True,
        "motivos": []
    }