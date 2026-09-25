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

    avaliacao = avaliar_resultado(resultado)

    assert avaliacao["aprovado"] is True
    assert avaliacao["motivos"] == []

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

    avaliacao = avaliar_resultado(resultado)

    assert avaliacao["aprovado"] is False
    assert "Baixa confiança na classificação" in avaliacao["motivos"]

def test_quality_gate_reprova_resultado_sem_confianca():
    resultado = {
        "cenarios": [
            "Cenário não identificado"
        ],
        "massas": [],
        "confianca": 0.0
    }

    avaliacao = avaliar_resultado(resultado)

    assert avaliacao["aprovado"] is False
    assert "Baixa confiança na classificação" in avaliacao["motivos"]
    assert "Resultado sem massas" in avaliacao["motivos"]

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

    avaliacao = avaliar_resultado(resultado)

    assert avaliacao["aprovado"] is False
    assert "Resultado sem cenários" in avaliacao["motivos"]

def test_quality_gate_reprova_resultado_sem_massas():
    resultado = {
        "cenarios": [
            "Login com e-mail e senha válidos"
        ],
        "massas": [],
        "confianca": 1.0
    }

    avaliacao = avaliar_resultado(resultado)

    assert avaliacao["aprovado"] is False
    assert "Resultado sem massas" in avaliacao["motivos"]

def test_quality_gate_retorna_motivo_quando_reprova_por_baixa_confianca():
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

    avaliacao = avaliar_resultado(resultado)

    assert avaliacao["aprovado"] is False
    assert "Baixa confiança na classificação" in avaliacao["motivos"]

def test_quality_gate_retorna_motivo_quando_nao_ha_cenarios():
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

    avaliacao = avaliar_resultado(resultado)

    assert avaliacao["aprovado"] is False
    assert "Resultado sem cenários" in avaliacao["motivos"]

def test_quality_gate_retorna_motivo_quando_nao_ha_massas():
    resultado = {
        "cenarios": [
            "Login com e-mail e senha válidos"
        ],
        "massas": [],
        "confianca": 1.0
    }

    avaliacao = avaliar_resultado(resultado)

    assert avaliacao["aprovado"] is False
    assert "Resultado sem massas" in avaliacao["motivos"]