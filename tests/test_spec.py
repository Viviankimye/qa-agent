from harness.spec import criar_spec


def test_spec_de_login_define_requisitos_minimos():
    spec = criar_spec("Como usuário, quero realizar login.")

    assert spec["dominio"] == "login"
    assert "cenarios" in spec["requisitos"]
    assert "massas" in spec["requisitos"]
    assert "validacao" in spec["requisitos"]


def test_spec_rejeita_estoria_com_dominio_desconhecido():
    try:
        criar_spec("Como usuário, quero viajar para Marte.")
        assert False
    except ValueError as erro:
        assert str(erro) == "Domínio não identificado"