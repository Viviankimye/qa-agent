from tools.validator import validar_resultado
from domains import (
    login,
    cadastro,
    pix,
    renegociacao,
    recuperacao_senha
)


DOMINIOS = {
    "login": login.gerar,
    "cadastro": cadastro.gerar,
    "pix": pix.gerar,
    "renegociacao": renegociacao.gerar,
    "recuperacao_senha": recuperacao_senha.gerar
}

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
        "criar conta"
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


def gerar_massa(estoria):
    dominio = identificar_dominio(estoria)

    if dominio is None:
        return {
            "cenarios": ["Cenário não identificado"],
            "massas": []
        }

    resultado = DOMINIOS[dominio]()

    if not validar_resultado(resultado):
        raise ValueError("Resultado gerado pelo agente é inválido")

    return resultado
