import pytest
from agents.ia_agent import (
    gerar_massa,
    identificar_dominio,
    gerar_por_dominio
)
from tools.validator import validar_resultado

def test_identifica_login():
    resultado = gerar_massa(
        "Como usuário, quero realizar login na plataforma."
    )

    assert "Login com e-mail e senha válidos" in resultado["cenarios"]
    assert "email" in resultado["massas"][0]
    assert "senha" in resultado["massas"][0]

def test_identifica_cadastro():
    resultado = gerar_massa(
        "Como visitante, quero realizar meu cadastro."
    )

    assert "Cadastro com dados válidos" in resultado["cenarios"]
    assert "nome" in resultado["massas"][0]
    assert "email" in resultado["massas"][0]
    assert "senha" in resultado["massas"][0]

def test_identifica_pix():
    resultado = gerar_massa(
        "Como cliente, quero realizar um pagamento via Pix."
    )

    assert "Pix válido" in resultado["cenarios"]
    assert "valor" in resultado["massas"][0]
    assert "chave_pix" in resultado["massas"][0]

def test_identifica_recuperacao_senha():
    resultado = gerar_massa(
        "Como usuário, quero recuperar minha senha."
    )

    assert resultado["cenarios"] != ["Cenário não identificado"]
    assert "email" in resultado["massas"][0]

def test_estoria_desconhecida():
    resultado = gerar_massa(
        "Como usuário, quero consultar meu saldo de pontos."
    )

    assert resultado["cenarios"] == ["Cenário não identificado"]
    assert resultado["massas"] == []    

def test_resultado_do_agente_e_valido():
    resultado = gerar_massa(
        "Como usuário, quero realizar login na plataforma."
    )

    assert validar_resultado(resultado) is True    

def test_identifica_login_com_entrar_na_conta():
    resultado = gerar_massa(
        "Como usuário, quero entrar na minha conta."
    )

def test_identifica_login_por_palavra_chave():
    resultado = gerar_massa(
        "Como usuário, preciso acessar minha conta."
    )

def test_recuperacao_senha_tem_prioridade_sobre_login():
    resultado = gerar_massa(
        "Como usuário, quero fazer login porque esqueci minha senha."
    )

    assert "Recuperação de senha com e-mail válido" in resultado["cenarios"]

def test_identifica_dominio_login():
    assert identificar_dominio(
        "Como usuário, quero realizar login na plataforma."
    ) == "login"


def test_identifica_dominio_cadastro():
    assert identificar_dominio(
        "Como visitante, quero realizar meu cadastro."
    ) == "cadastro"


def test_identifica_dominio_desconhecido():
    assert identificar_dominio(
        "Como usuário, quero consultar meu saldo."
    ) is None

def test_gerar_por_dominio_login():
    resultado = gerar_por_dominio("login")

    assert "Login com e-mail e senha válidos" in resultado["cenarios"]
    assert "email" in resultado["massas"][0]

def test_gerar_por_dominio_invalido():
    with pytest.raises(ValueError, match="Domínio não suportado"):
        gerar_por_dominio("dominio_inexistente")
