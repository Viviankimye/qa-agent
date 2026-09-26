from harness.planner import criar_plano


def test_planner_cria_plano_para_login():
    spec = {
        "dominio": "login",
        "confianca": 1.0,
        "requisitos": {
            "cenarios": True,
        "massas": True,
        "validacao": True
    }
}
    plano = criar_plano(spec)

    assert plano["dominio"] == "login"
    assert "gerar cenários" in plano["tarefas"]
    assert "gerar massas" in plano["tarefas"]
    assert "validar resultado" in plano["tarefas"]

def test_planner_respeita_requisito_desativado():
    spec = {
        "dominio": "login",
        "confianca": 1.0,
        "requisitos": {
            "cenarios": True,
            "massas": False,
            "validacao": True
    }
}

    plano = criar_plano(spec)

    assert "gerar cenários" in plano["tarefas"]
    assert "gerar massas" not in plano["tarefas"]
    assert "validar resultado" in plano["tarefas"]