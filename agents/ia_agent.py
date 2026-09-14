def gerar_massa(estoria):

    if "login" in estoria.lower():
        cenarios = [
            "Login com e-mail e senha válidos",
            "Login com senha inválida",
            "Login com e-mail inválido",
            "Login com campos vazios"
        ]
        massas = [
            {"email": "cliente@email.com", "senha": "Senha123"},
            {"email": "cliente@email.com", "senha": "senhaerrada"}
        ]

    elif "cadastro" in estoria.lower():
        cenarios = [
            "Cadastro com dados válidos",
            "Cadastro com e-mail já existente",
            "Cadastro com e-mail inválido",
            "Cadastro com campos obrigatórios vazios"
        ]
        massas = [
            {"nome": "João Silva", "email": "joao@email.com", "senha": "Senha123"},
            {"nome": "Maria Silva", "email": "email_invalido", "senha": "Senha123"}
        ]

    elif "pix" in estoria.lower() or "pagamento" in estoria.lower():
        cenarios = [
            "Pix válido",
            "Pix incorreto",
            "Pix expirado"
        ]
        massas = [
            {
                "valor": "100,00",
                "chave_pix": "joao@hotmail.com"
            },
            {
                "valor": "100,00",
                "chave_pix": "chave_invalida"
            },
            {
                "valor": "100,00",
                "prazo": "expirado",
                "chave_pix": "joao@hotmail.com"
            }
        ]

    elif "renegociacao" in estoria.lower() or "imovel" in estoria.lower():
        cenarios = [
            "Dado que o cliente possui uma dívida em aberto, quando ele solicita a renegociação, então o sistema deve apresentar as opções de parcelamento disponíveis.",
            "Dado que o cliente possui uma dívida em aberto, quando ele seleciona uma opção de parcelamento, então o sistema deve calcular o valor das parcelas e apresentar ao cliente.",
            "Dado que o cliente CNPJ 12345678901234, listo todos os produtos que são renegociaveis, faco o detalhe das pacelas,faco o agrupamento das parcelas, simulo a renegociação, efetivo o acordo, entao gero um numero de acordo",
        ]
        massas = [
            {
                "cnpj": "12345678901234",
                "produto": "12345",
                "contrato": "1234567890",
                "valor": "100000,00"       

            },
            {
                "cnpj": "12345678901244",
                "produto": "67890",
                "contrato": "1345678901",
                "valor": "300000,00" 
            },
            {
                "cnpj": "12345678901245",
                "produto": "12345",
                "contrato": "2345678901",
                "valor": "200000,00" 
            }
        ]
    else:
        cenarios = ["Cenário não identificado"]
        massas = []

    resultado = {
        "cenarios": cenarios,
        "massas": massas
    }

    return resultado