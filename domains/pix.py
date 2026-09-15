def gerar():
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

    return {
        "cenarios": cenarios,
        "massas": massas
    }