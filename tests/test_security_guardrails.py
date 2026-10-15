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
