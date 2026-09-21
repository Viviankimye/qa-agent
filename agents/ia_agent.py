from tools.validator import validar_resultado
from agents.classificador import identificar_dominio
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

def gerar_por_dominio(dominio):
    if dominio not in DOMINIOS:
        raise ValueError("Domínio não suportado")

    return DOMINIOS[dominio]()

def gerar_massa(estoria):
    dominio = identificar_dominio(estoria)

    if dominio is None:
        return {
            "cenarios": ["Cenário não identificado"],
            "massas": []
        }

    resultado = gerar_por_dominio(dominio)

    if not validar_resultado(resultado):
        raise ValueError("Resultado gerado pelo agente é inválido")

    return resultado