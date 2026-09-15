def gerar():
    cenarios = [
        "Recuperação de senha com e-mail válido",
        "Recuperação de senha com e-mail não cadastrado",
        "Recuperação de senha com e-mail inválido",
        "Recuperação de senha com campo vazio"
    ]

    massas = [
        {
            "email": "cliente@email.com"
        },
        {
            "email": "email_nao_cadastrado@email.com"
        },
        {
            "email": "email_invalido"
        },
        {
            "email": ""
        }
    ]

    return {
        "cenarios": cenarios,
        "massas": massas
    }