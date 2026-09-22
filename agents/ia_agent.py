from tools.validator import validar_resultado
from agents.classificador import identificar_dominio, classificar_com_evidencia
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
    classificacao = classificar_com_evidencia(estoria)
    dominio = classificacao["dominio"]
    confianca = classificacao["confianca"]

    if dominio is None:
        return {
            "cenarios": ["Cenário não identificado"],
            "massas": [],
            "confianca": confianca
        }

    resultado = gerar_por_dominio(dominio)

    if not validar_resultado(resultado):
        raise ValueError("Resultado gerado pelo agente é inválido")

    resultado["confianca"] = confianca

    if confianca < 1.0:
        resultado["alerta"] = "Baixa confiança na classificação"

    return resultado
