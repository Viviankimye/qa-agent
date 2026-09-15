from agents.ia_agent import gerar_massa


def test_identifica_login():
    resultado = gerar_massa(
        "Como usuário, quero realizar login na plataforma."
    )

    assert len(resultado["cenarios"]) > 0


def test_identifica_cadastro():
    resultado = gerar_massa(
        "Como visitante, quero realizar meu cadastro."
    )

    assert len(resultado["cenarios"]) > 0


def test_identifica_pix():
    resultado = gerar_massa(
        "Como cliente, quero realizar um pagamento via Pix."
    )

    assert len(resultado["cenarios"]) > 0


def test_estoria_desconhecida():
    resultado = gerar_massa(
        "Como usuário, quero recuperar minha senha."
    )

    assert resultado["cenarios"] != ["Cenário não identificado"]