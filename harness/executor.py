
from domains.login import gerar
from harness.guardrails import validar_plano


EXECUTORES = {
    "login": gerar
}


def executar_plano(plano):
    guardrail = validar_plano(plano)

    if not guardrail["aprovado"]:
        raise ValueError("Plano reprovado")

    dominio = plano["dominio"]

    if dominio not in EXECUTORES:
        raise ValueError("Domínio não suportado")

    resultado = EXECUTORES[dominio]()

    return {
        "dominio": dominio,
        "cenarios": (
            resultado["cenarios"]
            if "gerar cenários" in plano["tarefas"]
            else []
        ),
        "massas": (
            resultado["massas"]
            if "gerar massas" in plano["tarefas"]
            else []
        ),
        "confianca": plano["confianca"]
    }
