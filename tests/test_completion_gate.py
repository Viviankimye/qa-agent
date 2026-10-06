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


def test_completion_gate_reprova_verifier_sem_motivos():
    verificacao = {
        "aprovado": True
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
    assert "Verifier sem campo motivos" in resultado["motivos"]


def test_completion_gate_reprova_verifier_sem_aprovado():
    verificacao = {
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

    assert resultado["aprovado"] is False
    assert "Verifier sem campo aprovado" in resultado["motivos"]


def test_completion_gate_reprova_verifier_com_aprovado_invalido():
    verificacao = {
        "aprovado": "sim",
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

    assert resultado["aprovado"] is False
    assert "Verifier com campo aprovado inválido" in resultado["motivos"]


def test_completion_gate_reprova_verifier_com_motivo_invalido():
    verificacao = {
        "aprovado": False,
        "motivos": [123]
    }

    julgamento = {
        "aprovado": False,
        "motivos": ["Resultado inválido"]
    }

    resultado = validar_conclusao(
        verificacao,
        julgamento
    )

    assert resultado["aprovado"] is False
    assert (
        "Verifier com item de motivos inválido"
        in resultado["motivos"]
    )
