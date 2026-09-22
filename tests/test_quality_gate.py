from tools.quality_gate import avaliar_resultado


def test_quality_gate_aprova_resultado_com_alta_confianca():
    resultado = {
        "cenarios": [
            "Login com e-mail e senha válidos"
        ],
        "massas": [
            {
                "email": "cliente@email.com",
                "senha": "Senha123"
            }
        ],
        "confianca": 1.0
    }

    assert avaliar_resultado(resultado) is True

def test_quality_gate_reprova_resultado_com_baixa_confianca():
    resultado = {
        "cenarios": [
            "Login com e-mail e senha válidos"
        ],
        "massas": [
            {
                "email": "cliente@email.com",
                "senha": "Senha123"
            }
        ],
        "confianca": 0.5
    }

    assert avaliar_resultado(resultado) is False

def test_quality_gate_reprova_resultado_sem_confianca():
    resultado = {
        "cenarios": [
            "Cenário não identificado"
        ],
        "massas": [],
        "confianca": 0.0
    }

    assert avaliar_resultado(resultado) is False

def test_quality_gate_reprova_resultado_sem_cenarios():
    resultado = {
        "cenarios": [],
        "massas": [
            {
                "email": "cliente@email.com",
                "senha": "Senha123"
            }
        ],
        "confianca": 1.0
    }

    assert avaliar_resultado(resultado) is False

def test_quality_gate_reprova_resultado_sem_massas():
    resultado = {
        "cenarios": [
            "Login com e-mail e senha válidos"
        ],
        "massas": [],
        "confianca": 1.0
    }

    assert avaliar_resultado(resultado) is False    