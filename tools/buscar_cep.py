# Fazendo requests com uma API real

import requests
#criando uma funcao de chamada, recebendo o parametro cep
def buscar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"

    resposta = requests.get(url)

    dados = resposta.json()

    return dados