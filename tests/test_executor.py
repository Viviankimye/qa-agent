from harness.executor import executar_plano


def test_executor_gera_resultado_de_login():
    plano = {
        "dominio": "login",
        "confianca": 1.0,
        "tarefas": [
            "gerar cenários",
            "gerar massas",
            "validar resultado"
        ]
    }

    resultado = executar_plano(plano)

    assert resultado["dominio"] == "login"
    assert resultado["cenarios"]
    assert resultado["massas"]


def test_executor_nao_gera_massas_se_tarefa_nao_estiver_no_plano():
    plano = {
        "dominio": "login",
        "confianca": 1.0,
        "tarefas": [
            "gerar cenários"
        ]
    }

    resultado = executar_plano(plano)

    assert resultado["cenarios"]
    assert resultado["massas"] == []