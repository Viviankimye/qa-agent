from harness.guardrails import validar_plano


def test_guardrail_aprova_plano_com_alta_confianca():
    plano = {
        "dominio": "login",
        "confianca": 1.0,
        "tarefas": [
            "gerar cenários",
            "gerar massas",
            "validar resultado"
        ]
    }

    resultado = validar_plano(plano)

    assert resultado["aprovado"] is True
    assert resultado["motivos"] == []


def test_guardrail_reprova_plano_com_baixa_confianca():
    plano = {
        "dominio": "login",
        "confianca": 0.5,
        "tarefas": [
            "gerar cenários",
            "gerar massas",
            "validar resultado"
        ]
    }

    resultado = validar_plano(plano)

    assert resultado["aprovado"] is False
    assert "Baixa confiança para execução" in resultado["motivos"]

def test_guardrail_reprova_plano_sem_dominio():
    plano = {
        "dominio": None,
        "confianca": 1.0,
        "tarefas": [
            "gerar cenários",
            "gerar massas",
            "validar resultado"
        ]
    }

    resultado = validar_plano(plano)

    assert resultado["aprovado"] is False
    assert "Domínio não definido para execução" in resultado["motivos"]

def test_guardrail_reprova_plano_sem_tarefas():
    plano = {
        "dominio": "login",
        "confianca": 1.0,
        "tarefas": []
    }

    resultado = validar_plano(plano)

    assert resultado["aprovado"] is False
    assert "Plano sem tarefas para execução" in resultado["motivos"]
