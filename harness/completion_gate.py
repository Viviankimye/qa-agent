def _validar_contrato(resultado, nome):
    motivos = []

    if "aprovado" not in resultado:
        motivos.append(f"{nome} sem campo aprovado")
    elif type(resultado["aprovado"]) is not bool:
        motivos.append(
            f"{nome} com campo aprovado inválido"
        )

    if "motivos" not in resultado:
        motivos.append(f"{nome} sem campo motivos")
    elif not isinstance(resultado["motivos"], list):
        motivos.append(
            f"{nome} com campo motivos inválido"
        )
    elif not all(
        isinstance(item, str)
        for item in resultado["motivos"]
    ):
        motivos.append(
            f"{nome} com item de motivos inválido"
        )

    return motivos


def validar_conclusao(verificacao, julgamento):
    motivos = []

    motivos.extend(
        _validar_contrato(verificacao, "Verifier")
    )
    motivos.extend(
        _validar_contrato(julgamento, "Judge")
    )

    if verificacao.get("aprovado") is False:
        if isinstance(verificacao.get("motivos"), list):
            motivos.extend(verificacao["motivos"])

    if julgamento.get("aprovado") is False:
        if isinstance(julgamento.get("motivos"), list):
            motivos.extend(julgamento["motivos"])

    if (
        verificacao.get("aprovado") is False
        and julgamento.get("aprovado") is True
    ):
        motivos.append(
            "Verifier reprovou, mas Judge aprovou"
        )

    return {
        "aprovado": len(motivos) == 0,
        "motivos": motivos
    }
