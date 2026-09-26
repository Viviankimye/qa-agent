from harness.judge import julgar_resultado


def test_judge_aprova_resultado_verificado():
    resultado = {
        "dominio": "login",
        "cenarios": [
            "Login com e-mail e senha vÃ¡lidos",
            "Login com senha invÃ¡lida"
        ],
        "massas": [
            {
                "email": "cliente@email.com",
                "senha": "Senha123"
            }
        ]
    }

    verificacao = {
        "aprovado": True,
        "motivos": []
    }

    julgamento = julgar_resultado(resultado, verificacao)

    assert julgamento["aprovado"] is True
    assert julgamento["motivos"] == []

def test_judge_reprova_quando_verifier_reprova():
    resultado = {
        "dominio": "login",
        "cenarios": [
            "Login com e-mail e senha vÃ¡lidos"
        ],
        "massas": []
    }

    verificacao = {
        "aprovado": False,
        "motivos": [
            "Resultado sem massas"
        ]
    }

    julgamento = julgar_resultado(resultado, verificacao)

    assert julgamento["aprovado"] is False
    assert "Resultado sem massas" in julgamento["motivos"]
