from agents.classificador import identificar_dominio
from agents.classificador import identificar_dominio, PALAVRAS_CHAVE

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