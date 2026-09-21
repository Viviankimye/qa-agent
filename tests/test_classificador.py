from agents.classificador import (
    identificar_dominio,
    classificar_com_evidencia,
    PALAVRAS_CHAVE
)

def test_classificador_identifica_login():
    assert identificar_dominio(
        "Como usuário, quero realizar login."
    ) == "login"

def test_classificador_identifica_cadastro():
    assert identificar_dominio(
        "Como visitante, quero criar minha conta."
    ) == "cadastro"    

def test_classificador_identifica_pix():
    assert identificar_dominio(
        "Como cliente, quero realizar um pagamento via Pix."
    ) == "pix"    

def test_classificador_identifica_recuperacao_senha():
    assert identificar_dominio(
        "Como usuário, esqueci minha senha."
    ) == "recuperacao_senha"

def test_classificador_identifica_renegociacao():
    assert identificar_dominio(
        "Como cliente, quero renegociar minha dívida."
    ) == "renegociacao" 

def test_classificador_retorna_none_para_estoria_invalida():
    assert identificar_dominio(
        "Como usuário, quero acessar o sistema."
    ) is None

def test_todos_os_dominios_possuem_palavras_chave():
    dominios_esperados = {
        "login",
        "cadastro",
        "pix",
        "recuperacao_senha",
        "renegociacao"
    }

    assert set(PALAVRAS_CHAVE.keys()) == dominios_esperados

def test_classificador_identifica_login_por_palavra_chave():
    assert identificar_dominio(
        "Como usuário, quero entrar na minha conta."
    ) == "login"

def test_classificador_retorna_evidencia():
    resultado = classificar_com_evidencia(
        "Como usuário, quero realizar login."
    )

    assert resultado["dominio"] == "login"
    assert "login" in resultado["palavras_encontradas"]

def test_classificador_retorna_evidencia_vazia_para_estoria_desconhecida():
    resultado = classificar_com_evidencia(
        "Como usuário, quero consultar meu saldo de pontos."
    )

    assert resultado["dominio"] is None
    assert resultado["palavras_encontradas"] == []

def test_classificador_identifica_multiplas_evidencias():
    resultado = classificar_com_evidencia(
        "Como usuário, quero entrar na minha conta para realizar login."
    )

    assert resultado["dominio"] == "login"
    assert "login" in resultado["palavras_encontradas"]
    assert "entrar na minha conta" in resultado["palavras_encontradas"]

def test_classificador_calcula_confianca_com_uma_evidencia():
    resultado = classificar_com_evidencia(
        "Como usuário, quero realizar login."
    )

    assert resultado["confianca"] == 0.5

def test_classificador_calcula_confianca_com_multiplas_evidencias():
    resultado = classificar_com_evidencia(
        "Como usuário, quero entrar na minha conta para realizar login."
    )

    assert resultado["confianca"] == 1.0

def test_classificador_retorna_confianca_zero_para_estoria_desconhecida():
    resultado = classificar_com_evidencia(
        "Como usuário, quero consultar meu saldo de pontos."
    )

    assert resultado["dominio"] is None
    assert resultado["palavras_encontradas"] == []
    assert resultado["confianca"] == 0.0
