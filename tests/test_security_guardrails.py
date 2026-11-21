import harness.guardrails as guardrails


def test_rejeita_teste_de_seguranca_sem_escopo():
    avaliacao = guardrails.validar_escopo_seguranca(
        None,
        "https://staging.example.com"
    )

    assert avaliacao["aprovado"] is False
    assert (
        "Escopo de segurança não autorizado"
        in avaliacao["motivos"]
    )


def test_rejeita_escopo_em_formato_invalido():
    avaliacao = guardrails.validar_escopo_seguranca(
        ["https://staging.example.com"],
        "https://staging.example.com"
    )

    assert avaliacao["aprovado"] is False
    assert "Escopo de segurança inválido" in avaliacao["motivos"]



def test_rejeita_alvo_fora_do_escopo():
    avaliacao = guardrails.validar_escopo_seguranca(
        {"alvos": ["https://staging.example.com"]},
        "https://producao.example.com"
    )

    assert avaliacao["aprovado"] is False
    assert "Alvo fora do escopo autorizado" in avaliacao["motivos"]



def test_aceita_alvo_dentro_do_escopo():
    avaliacao = guardrails.validar_escopo_seguranca(
        {"alvos": ["https://staging.example.com"]},
        "https://staging.example.com"
    )

    assert avaliacao["aprovado"] is True
    assert avaliacao["motivos"] == []


def test_rejeita_alvo_que_nao_e_uma_url():
    alvo = "nao-e-uma-url"

    avaliacao = guardrails.validar_escopo_seguranca(
        {"alvos": [alvo]},
        alvo
    )

    assert avaliacao["aprovado"] is False
    assert "Alvo de segurança inválido" in avaliacao["motivos"]


def test_rejeita_url_com_http():
    alvo = "http://staging.example.com"

    avaliacao = guardrails.validar_escopo_seguranca(
        {"alvos": [alvo]},
        alvo
    )

    assert avaliacao["aprovado"] is False
    assert "Alvo de segurança inválido" in avaliacao["motivos"]


def test_rejeita_url_sem_hostname():
    alvo = "https:///"

    avaliacao = guardrails.validar_escopo_seguranca(
        {"alvos": [alvo]},
        alvo
    )

    assert avaliacao["aprovado"] is False
    assert "Alvo de segurança inválido" in avaliacao["motivos"]


def test_rejeita_url_com_credenciais():
    alvo = "https://usuario:senha@staging.example.com"

    avaliacao = guardrails.validar_escopo_seguranca(
        {"alvos": [alvo]},
        alvo
    )

    assert avaliacao["aprovado"] is False
    assert "Alvo de segurança inválido" in avaliacao["motivos"]


def test_rejeita_escopo_com_url_invalida():
    avaliacao = guardrails.validar_escopo_seguranca(
        {
            "alvos": [
                "https://staging.example.com",
                "nao-e-uma-url"
            ]
        },
        "https://staging.example.com"
    )

    assert avaliacao["aprovado"] is False
    assert "Escopo de segurança inválido" in avaliacao["motivos"]


def test_rejeita_localhost():
    alvo = "https://localhost"

    avaliacao = guardrails.validar_escopo_seguranca(
        {"alvos": [alvo]},
        alvo
    )

    assert avaliacao["aprovado"] is False
    assert "Alvo de segurança inválido" in avaliacao["motivos"]


def test_rejeita_ip_loopback():
    alvo = "https://127.0.0.1"

    avaliacao = guardrails.validar_escopo_seguranca(
        {"alvos": [alvo]},
        alvo
    )

    assert avaliacao["aprovado"] is False
    assert "Alvo de segurança inválido" in avaliacao["motivos"]


def test_rejeita_ip_privado():
    alvo = "https://192.168.1.10"

    avaliacao = guardrails.validar_escopo_seguranca(
        {"alvos": [alvo]},
        alvo
    )

    assert avaliacao["aprovado"] is False
    assert "Alvo de segurança inválido" in avaliacao["motivos"]


def test_rejeita_ip_privado_faixa_10():
    alvo = "https://10.0.0.5"

    avaliacao = guardrails.validar_escopo_seguranca(
        {"alvos": [alvo]},
        alvo
    )

    assert avaliacao["aprovado"] is False
    assert "Alvo de segurança inválido" in avaliacao["motivos"]


def test_rejeita_ipv6_loopback():
    alvo = "https://[::1]"

    avaliacao = guardrails.validar_escopo_seguranca(
        {"alvos": [alvo]},
        alvo
    )

    assert avaliacao["aprovado"] is False
    assert "Alvo de segurança inválido" in avaliacao["motivos"]


def test_rejeita_ipv6_privado():
    alvo = "https://[fc00::1]"

    avaliacao = guardrails.validar_escopo_seguranca(
        {"alvos": [alvo]},
        alvo
    )

    assert avaliacao["aprovado"] is False
    assert "Alvo de segurança inválido" in avaliacao["motivos"]


def test_rejeita_porta_invalida():
    alvo = "https://staging.example.com:abc"

    avaliacao = guardrails.validar_escopo_seguranca(
        {"alvos": [alvo]},
        alvo
    )

    assert avaliacao["aprovado"] is False
    assert "Alvo de segurança inválido" in avaliacao["motivos"]
