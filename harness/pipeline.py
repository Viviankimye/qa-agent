from harness.spec import criar_spec
from harness.planner import criar_plano
from harness.executor import executar_plano
from harness.verifier import verificar_resultado
from harness.judge import julgar_resultado


def executar_pipeline(estoria):
    spec = criar_spec(estoria)

    plano = criar_plano(spec)

    resultado = executar_plano(plano)

    verificacao = verificar_resultado(
        spec,
        resultado
    )

    julgamento = julgar_resultado(
        resultado,
        verificacao
    )

    return {
        "spec": spec,
        "plano": plano,
        "resultado": resultado,
        "verificacao": verificacao,
        "julgamento": julgamento
    }