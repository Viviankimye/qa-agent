def gerar():
    cenarios = [
        "Cadastro com dados válidos",
        "Cadastro com e-mail já existente",
        "Cadastro com e-mail inválido",
        "Cadastro com campos obrigatórios vazios"
    ]

    massas = [
        {
            "nome": "João Silva",
            "email": "joao@email.com",
            "senha": "Senha123"
        },
        {
            "nome": "Maria Silva",
            "email": "email_invalido",
            "senha": "Senha123"
        }
    ]

    return {
        "cenarios": cenarios,
        "massas": massas
    }