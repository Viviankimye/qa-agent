from unittest.mock import patch
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

def test_gerar_massa_retorna_resultado_valido():
    resultado = gerar_massa(
        "Como usuário, quero realizar cadastro."
    )

    assert validar_resultado(resultado) is True

def test_gerar_massa_rejeita_resultado_invalido():
    resultado_invalido = {
        "cenarios": [],
        "massas": []
    }

    with patch(
        "agents.ia_agent.gerar_por_dominio",
        return_value=resultado_invalido
    ):
        with pytest.raises(
            ValueError,
            match="Resultado gerado pelo agente é inválido"
        ):
            gerar_massa(
                "Como usuário, quero realizar login na plataforma."
            )

def test_gerar_por_dominio_chama_gerador_do_dominio():
    resultado_esperado = {
        "cenarios": ["Cenário de teste"],
        "massas": [{"campo": "valor"}]
    }

    with patch(
        "agents.ia_agent.DOMINIOS",
        {"login": lambda: resultado_esperado}
    ):
        resultado = gerar_por_dominio("login")

    assert resultado == resultado_esperado

@pytest.mark.parametrize(
    "dominio",
    [
        "login",
        "cadastro",
        "pix",
        "recuperacao_senha",
        "renegociacao"
    ]
)
def test_todos_os_dominios_geram_resultado_valido(dominio):
    resultado = gerar_por_dominio(dominio)

    assert validar_resultado(resultado) is True

@pytest.mark.parametrize(
    "estoria, dominio_esperado",
    [
        (
            "Como usuário, quero realizar login.",
            "login"
        ),
        (
            "Como usuário, esqueci minha senha.",
            "recuperacao_senha"
        ),
        (
            "Como visitante, quero criar minha conta.",
            "cadastro"
        ),
        (
            "Como cliente, quero realizar um pagamento via Pix.",
            "pix"
        ),
        (
            "Como cliente, quero renegociar minha dívida.",
            "renegociacao"
        )
    ]
)
def test_classificacao_de_estorias(estoria, dominio_esperado):
    assert identificar_dominio(estoria) == dominio_esperado

def test_ia_agent_identifica_classificacao_com_baixa_confianca():
    resultado = gerar_massa(
        "Como usuário, quero realizar login."
    )

    assert resultado["confianca"] == 0.5

def test_ia_agent_sinaliza_baixa_confianca():
    resultado = gerar_massa(
        "Como usuário, quero realizar login."
    )

    assert resultado["confianca"] == 0.5
    assert resultado["alerta"] == "Baixa confiança na classificação"

def test_ia_agent_nao_sinaliza_alta_confianca():
    resultado = gerar_massa(
        "Como usuário, quero entrar na minha conta para realizar login."
    )

    assert resultado["confianca"] == 1.0
    assert "alerta" not in resultado    

def test_ia_agent_reprova_resultado_com_baixa_confianca_no_quality_gate():
    resultado = gerar_massa(
        "Como usuário, quero realizar login."
    )

    assert resultado["confianca"] == 0.5
    assert resultado["quality_gate"]["aprovado"] is False
    assert "Baixa confiança na classificação" in resultado["quality_gate"]["motivos"]

def test_ia_agent_aprova_resultado_com_alta_confianca_no_quality_gate():
    resultado = gerar_massa(
        "Como usuário, quero entrar na minha conta para realizar login."
    )

    assert resultado["confianca"] == 1.0
    assert resultado["quality_gate"]["aprovado"] is True
    assert resultado["quality_gate"]["motivos"] == []
