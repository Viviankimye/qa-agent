from agents.classificador import classificar_com_evidencia


def criar_spec(estoria):
    classificacao = classificar_com_evidencia(estoria)
    dominio = classificacao["dominio"]

    if dominio is None:
        raise ValueError("Domínio não identificado")

    return {
        "dominio": dominio,
        "confianca": classificacao["confianca"],
        "requisitos": {
            "cenarios": True,
            "massas": True,
            "validacao": True
        }
    }