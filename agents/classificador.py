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

def _calcular_confianca(evidencias):
    if len(evidencias) == 0:
        return 0.0

    if len(evidencias) == 1:
        return 0.5

    return 1.0


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
            "palavras_encontradas": [],
            "confianca": 0.0
    }

    evidencias = _encontrar_evidencias(
        estoria,
        dominio
    )

    confianca = _calcular_confianca(evidencias)

    return {
        "dominio": dominio,
        "palavras_encontradas": evidencias,
        "confianca": confianca
    }


