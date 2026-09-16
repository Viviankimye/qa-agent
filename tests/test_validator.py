from tools.validator import validar_resultado


def test_resultado_valido():
    resultado = {
        "cenarios": ["Login válido"],
        "massas": [{"email": "teste@email.com", "senha": "123456"}]
    }

    assert validar_resultado(resultado) is True


def test_resultado_sem_cenarios():
    resultado = {
        "massas": [{"email": "teste@email.com", "senha": "123456"}]
    }

    assert validar_resultado(resultado) is False


def test_resultado_sem_massas():
    resultado = {
        "cenarios": ["Login válido"]
    }

    assert validar_resultado(resultado) is False

def test_resultado_vazio():
    resultado = {
        "cenarios": [],
        "massas": []
    }

def test_massa_nao_e_dicionario():
    resultado = {
        "cenarios": ["Login válido"],
        "massas": ["massa inválida"]
    }

def test_uma_massa_invalida_rejeita_resultado():
    resultado = {
        "cenarios": ["Login válido"],
        "massas": [
            {"email": "teste@email.com"},
            "massa inválida"
        ]
    }
def test_massa_vazia_rejeita_resultado():
    resultado = {
        "cenarios": ["Login válido"],
        "massas": [{}]
    }

    assert validar_resultado(resultado) is False
        