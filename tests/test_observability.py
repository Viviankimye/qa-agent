from harness.observability import registrar_evento


def test_observability_registra_evento():
    eventos = []

    registrar_evento(
        eventos,
        "Spec criada"
    )

    assert eventos == [
        "Spec criada"
    ]
