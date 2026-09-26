from harness.verifier import verificar_resultado


def test_verifier_aprova_resultado_de_login_valido():
    spec = {
        "dominio": "login",
        "requisitos": {
            "cenarios": True,
            "massas": True,
            "validacao": True
        }
    }

    resultado = {
        "dominio": "login",
        "cenarios": [
            "Login com e-mail e senha vÃ¡lidos"
        ],
        "massas": [
            {
                "email": "cliente@email.com",
                "senha": "Senha123"
            }
        ]
    }

    avaliacao = verificar_resultado(spec, resultado)

    assert avaliacao["aprovado"] is True
    assert avaliacao["motivos"] == []

def test_verifier_reprova_resultado_sem_massas():
    spec = {
        "dominio": "login",
        "requisitos": {
            "cenarios": True,
            "massas": True,
            "validacao": True
        }
    }

    resultado = {
        "dominio": "login",
        "cenarios": [
            "Login com e-mail e senha vÃ¡lidos"
        ],
        "massas": []
    }

    avaliacao = verificar_resultado(spec, resultado)

    assert avaliacao["aprovado"] is False
    assert "Resultado sem massas" in avaliacao["motivos"]
