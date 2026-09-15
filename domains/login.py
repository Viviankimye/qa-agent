def gerar():
    cenarios = [
        "Login com e-mail e senha válidos",
        "Login com senha inválida",
        "Login com e-mail inválido",
        "Login com campos vazios"
    ]

    massas = [
        {
            "email": "cliente@email.com",
            "senha": "Senha123"
        },
        {
            "email": "cliente@email.com",
            "senha": "senhaerrada"
        }
    ]

    return {
        "cenarios": cenarios,
        "massas": massas
    }