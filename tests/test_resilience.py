from harness.resilience import avaliar_resiliencia
from harness.observability import registrar_evento

def test_resilience_solicita_intervencao_humana():
    resultado = avaliar_resiliencia(
        {
            "aprovado": False,
            "motivos": ["Baixa confiança para execução"]
        }
    )

    assert resultado["intervencao_humana"] is True
    assert "Baixa confiança para execução" in resultado["motivos"]
    assert resultado["status"] == "ESCALATED"

def test_resilience_nao_solicita_intervencao_quando_aprovado():
    resultado = avaliar_resiliencia(
        {
            "aprovado": True,
            "motivos": []
        }
    )

    assert resultado["intervencao_humana"] is False
    assert resultado["motivos"] == []

def test_resilience_registra_escalacao():
    eventos = []

    resultado = avaliar_resiliencia(
        {
            "aprovado": False,
            "motivos": ["Falha no Completion Gate"]
        }
    )

    registrar_evento(
        eventos,
        "Intervenção humana solicitada"
    )

    assert resultado["status"] == "ESCALATED"
    assert "Intervenção humana solicitada" in eventos
