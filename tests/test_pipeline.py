from harness.pipeline import executar_pipeline

def test_pipeline_executa_fluxo_completo_de_login():
    resultado = executar_pipeline(
        "Como usuário, quero entrar na minha conta para realizar login."
    )

    assert resultado["spec"]["dominio"] == "login"
    assert resultado["plano"]["dominio"] == "login"
    assert resultado["resultado"]["cenarios"]
    assert resultado["resultado"]["massas"]
    assert resultado["verificacao"]["aprovado"] is True
    assert resultado["julgamento"]["aprovado"] is True


def test_pipeline_bloqueia_execucao_com_baixa_confianca():
    resultado = executar_pipeline(
        "Como usuário, quero realizar login."
    )

    assert resultado["guardrail"]["aprovado"] is False
    assert "Baixa confiança para execução" in resultado["guardrail"]["motivos"]

def test_pipeline_executa_completion_gate():
    resultado = executar_pipeline(
        "Como usuário, quero entrar na minha conta para realizar login."
    )

    assert "completion_gate" in resultado
    assert resultado["completion_gate"]["aprovado"] is True


def test_pipeline_executa_guardrail():
    resultado = executar_pipeline(
        "Como usuário, quero entrar na minha conta para realizar login."
    )

    assert "guardrail" in resultado
    assert resultado["guardrail"]["aprovado"] is True


def test_pipeline_registra_eventos_de_observabilidade():
    resultado = executar_pipeline(
        "Como usuário, quero entrar na minha conta para realizar login."
    )

    assert "eventos" in resultado
    assert "Spec criada" in resultado["eventos"]
    assert "Plano criado" in resultado["eventos"]
    assert "Guardrail aprovado" in resultado["eventos"]
    assert "Execução realizada" in resultado["eventos"]
    assert "Verificação realizada" in resultado["eventos"]
    assert "Judge executado" in resultado["eventos"]
    assert "Completion Gate executado" in resultado["eventos"]

def test_pipeline_executa_resilience():
    resultado = executar_pipeline(
        "Como usuário, quero entrar na minha conta para realizar login."
    )

    assert "resiliencia" in resultado
    assert resultado["resiliencia"]["status"] == "OK"
    assert resultado["resiliencia"]["intervencao_humana"] is False

def test_pipeline_escala_quando_completion_gate_reprova(monkeypatch):
    def completion_gate_reprovado(verificacao, julgamento):
        return {
            "aprovado": False,
            "motivos": ["Falha no Completion Gate"]
        }

    monkeypatch.setattr(
        "harness.pipeline.validar_conclusao",
        completion_gate_reprovado
    )

    resultado = executar_pipeline(
        "Como usuário, quero entrar na minha conta para realizar login."
    )

    assert resultado["completion_gate"]["aprovado"] is False
    assert resultado["resiliencia"]["status"] == "ESCALATED"
    assert resultado["resiliencia"]["intervencao_humana"] is True

def test_pipeline_registra_escalacao_na_observabilidade(monkeypatch):
    def completion_gate_reprovado(verificacao, julgamento):
        return {
            "aprovado": False,
            "motivos": ["Falha no Completion Gate"]
        }

    monkeypatch.setattr(
        "harness.pipeline.validar_conclusao",
        completion_gate_reprovado
    )

    resultado = executar_pipeline(
        "Como usuário, quero entrar na minha conta para realizar login."
    )

    assert resultado["resiliencia"]["intervencao_humana"] is True
    assert "Intervenção humana solicitada" in resultado["eventos"]

def test_pipeline_escala_quando_guardrail_reprova():
    resultado = executar_pipeline(
        "Como usuário, quero entrar na minha conta."
    )

    assert resultado["guardrail"]["aprovado"] is False
    assert resultado["resiliencia"]["status"] == "ESCALATED"
    assert resultado["resiliencia"]["intervencao_humana"] is True
