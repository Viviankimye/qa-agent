def gerar():
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

    return {
        "cenarios": cenarios,
        "massas": massas
    }