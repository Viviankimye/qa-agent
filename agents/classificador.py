PALAVRAS_CHAVE = {
    "login": [
        "login",
        "entrar na conta",
        "entrar na minha conta",
        "acessar minha conta"
    ],
    "cadastro": [
        "cadastro",
        "cadastrar",
        "criar conta",
        "criar minha conta"
    ],
    "pix": [
        "pix",
        "pagamento"
    ],
    "recuperacao_senha": [
        "recuperar senha",
        "esqueci minha senha",
        "senha"
    ],
    "renegociacao": [
        "renegociacao",
        "renegociação",
        "imovel",
        "dívida"
    ]
}

def _encontrar_evidencias(estoria, dominio):
    texto = estoria.lower()

    return [
        palavra
        for palavra in PALAVRAS_CHAVE[dominio]
        if palavra in texto
    ]


def identificar_dominio(estoria):
    prioridades = [
        "recuperacao_senha",
        "login",
        "cadastro",
        "pix",
        "renegociacao"
    ]

    for dominio in prioridades:
        evidencias = _encontrar_evidencias(estoria, dominio)

        if evidencias:
            return dominio

    return None


def classificar_com_evidencia(estoria):
    dominio = identificar_dominio(estoria)

    if dominio is None:
        return {
            "dominio": None,
            "palavras_encontradas": []
        }

    return {
        "dominio": dominio,
        "palavras_encontradas": _encontrar_evidencias(
            estoria,
            dominio
        )
    }
