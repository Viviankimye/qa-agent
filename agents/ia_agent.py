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


def identificar_dominio(estoria):
    texto = estoria.lower()

    if "senha" in texto or "recuperar" in texto:
        return "recuperacao_senha"

    if "login" in texto:
        return "login"

    if "cadastro" in texto:
        return "cadastro"

    if "pix" in texto or "pagamento" in texto:
        return "pix"

    if "renegociacao" in texto or "imovel" in texto:
        return "renegociacao"

    return None


def gerar_massa(estoria):
    dominio = identificar_dominio(estoria)

    if dominio is None:
        return {
            "cenarios": ["Cenário não identificado"],
            "massas": []
        }

    return DOMINIOS[dominio]()
