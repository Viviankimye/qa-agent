from harness.pipeline import executar_pipeline


def test_pipeline_executa_fluxo_completo_de_login():
    resultado = executar_pipeline(
        "Como usuÃ¡rio, quero entrar na minha conta para realizar login."
    )

    assert resultado["spec"]["dominio"] == "login"
    assert resultado["plano"]["dominio"] == "login"
    assert resultado["resultado"]["cenarios"]
    assert resultado["resultado"]["massas"]
    assert resultado["verificacao"]["aprovado"] is True
    assert resultado["julgamento"]["aprovado"] is True

def test_pipeline_reprova_resultado_invalido():
    resultado = executar_pipeline(
        "Como usuÃ¡rio, quero realizar login."
    )

    assert resultado["verificacao"]["aprovado"] is False
    assert resultado["julgamento"]["aprovado"] is False
