from harness.completion_gate import validar_conclusao

def test_completion_gate_aprova_fluxo_concluido():
    verificacao = {
        "aprovado": True,
        "motivos": []
    }

    julgamento = {
        "aprovado": True,
        "motivos": []
    }

    resultado = validar_conclusao(
        verificacao,
        julgamento
    )

    assert resultado["aprovado"] is True
    assert resultado["motivos"] == []


def test_completion_gate_reprova_se_verifier_reprovar():
    verificacao = {
        "aprovado": False,
        "motivos": ["Resultado sem massas"]
    }

    julgamento = {
        "aprovado": False,
        "motivos": ["Resultado sem massas"]
    }

    resultado = validar_conclusao(
        verificacao,
        julgamento
    )

    assert resultado["aprovado"] is False
    assert "Resultado sem massas" in resultado["motivos"]


def test_completion_gate_reprova_contradicao_do_judge():
    verificacao = {
        "aprovado": False,
        "motivos": ["Resultado sem massas"]
    }

    julgamento = {
        "aprovado": True,
        "motivos": []
    }

    resultado = validar_conclusao(
        verificacao,
        julgamento
    )

    assert resultado["aprovado"] is False
    assert "Verifier reprovou, mas Judge aprovou" in resultado["motivos"]
