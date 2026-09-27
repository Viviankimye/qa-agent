from harness.spec import criar_spec
from harness.planner import criar_plano
from harness.executor import executar_plano
from harness.verifier import verificar_resultado
from harness.judge import julgar_resultado
from harness.completion_gate import validar_conclusao
from harness.guardrails import validar_plano


def executar_pipeline(estoria):
    spec = criar_spec(estoria)

    plano = criar_plano(spec)

    guardrail = validar_plano(plano)

    if not guardrail["aprovado"]:
        return {
            "spec": spec,
            "plano": plano,
            "guardrail": guardrail
        }

    resultado = executar_plano(plano)

    verificacao = verificar_resultado(
        spec,
        resultado
    )

    julgamento = julgar_resultado(
        resultado,
        verificacao
    )

    completion_gate = validar_conclusao(
        verificacao,
        julgamento
    )

    return {
        "spec": spec,
        "plano": plano,
        "guardrail": guardrail,
        "resultado": resultado,
        "verificacao": verificacao,
        "julgamento": julgamento,
        "completion_gate": completion_gate
    }
