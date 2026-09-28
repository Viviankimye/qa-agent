from harness.spec import criar_spec
from harness.planner import criar_plano
from harness.executor import executar_plano
from harness.verifier import verificar_resultado
from harness.judge import julgar_resultado
from harness.completion_gate import validar_conclusao
from harness.guardrails import validar_plano
from harness.observability import registrar_evento
from harness.resilience import avaliar_resiliencia

def executar_pipeline(estoria):
    eventos = []

    spec = criar_spec(estoria)
    registrar_evento(eventos, "Spec criada")

    plano = criar_plano(spec)
    registrar_evento(eventos, "Plano criado")

    guardrail = validar_plano(plano)

    if not guardrail["aprovado"]:
        registrar_evento(
            eventos,
            "Guardrail reprovado"
        )

        resiliencia = avaliar_resiliencia(
            guardrail
        )

        if resiliencia["intervencao_humana"]:
            registrar_evento(
                eventos,
                "Intervenção humana solicitada"
            )

        return {
            "spec": spec,
            "plano": plano,
            "guardrail": guardrail,
            "resiliencia": resiliencia,
            "eventos": eventos
        }

    registrar_evento(
        eventos,
        "Guardrail aprovado"
    )

    resultado = executar_plano(plano)
    registrar_evento(
        eventos,
        "Execução realizada"
    )

    verificacao = verificar_resultado(
        spec,
        resultado
    )
    registrar_evento(
        eventos,
        "Verificação realizada"
    )

    julgamento = julgar_resultado(
        resultado,
        verificacao
    )
    registrar_evento(
        eventos,
        "Judge executado"
    )

    completion_gate = validar_conclusao(
        verificacao,
        julgamento
    )
    registrar_evento(
        eventos,
        "Completion Gate executado"
    )

    resiliencia = avaliar_resiliencia(
        completion_gate
    )

    if resiliencia["intervencao_humana"]:
        registrar_evento(
            eventos,
            "Intervenção humana solicitada"
        )

    return {
        "spec": spec,
        "plano": plano,
        "guardrail": guardrail,
        "resultado": resultado,
        "verificacao": verificacao,
        "julgamento": julgamento,
        "completion_gate": completion_gate,
        "resiliencia": resiliencia,
        "eventos": eventos
    }
