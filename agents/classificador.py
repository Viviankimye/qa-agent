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

def identificar_dominio(estoria):
    texto = estoria.lower()

    prioridades = [
        "recuperacao_senha",
        "login",
        "cadastro",
        "pix",
        "renegociacao"

    ]
    for dominio in prioridades:
        for palavra in PALAVRAS_CHAVE[dominio]:
            if palavra in texto:
                return dominio
            
    return None