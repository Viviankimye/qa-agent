# # tests/test_backend_renegociacao.py

import sys
import os
import requests

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "output"))
from massas_renegociacao_imovel import MASSAS

BASE_URL = "https://viacep.com.br/ws"

CEPS_VALIDOS = ["01310100", "04538133", "20040020"]
CEPS_INVALIDOS = ["00000000", "99999999"]

def test_api_esta_online():
    resposta = requests.get(f"{BASE_URL}/01310100/json/")
    assert resposta.status_code == 200, "API fora do ar!"

def test_cep_valido_retorna_campos_esperados():
    resposta = requests.get(f"{BASE_URL}/01310100/json/")
    dados = resposta.json()
    assert "cep"        in dados, "Campo cep não encontrado!"
    assert "logradouro" in dados, "Campo logradouro não encontrado!"
    assert "localidade" in dados, "Campo localidade não encontrado!"
    assert "uf"         in dados, "Campo uf não encontrado!"

def test_cep_invalido_retorna_erro():
    resposta = requests.get(f"{BASE_URL}/00000000/json/")
    dados = resposta.json()
    assert dados.get("erro") in [True, "true", "True"], "CEP inválido deveria retornar erro!"

def test_multiplos_ceps_validos():
    for cep in CEPS_VALIDOS:
        resposta = requests.get(f"{BASE_URL}/{cep}/json/")
        assert resposta.status_code == 200, f"CEP {cep} falhou!"
        dados = resposta.json()
        assert "cep" in dados, f"Resposta inválida para CEP {cep}"

def test_multiplos_ceps_invalidos():
    for cep in CEPS_INVALIDOS:
        resposta = requests.get(f"{BASE_URL}/{cep}/json/")
        dados = resposta.json()
        assert dados.get("erro") in [True, "true", "True"], f"CEP {cep} deveria retornar erro!"

def test_massas_tem_campos_obrigatorios():
    campos_obrigatorios = ["cnpj", "contrato", "valor"]
    for massa in MASSAS:
        for campo in campos_obrigatorios:
            assert campo in massa, f"Campo '{campo}' faltando na massa: {massa}"

def test_valores_das_massas_nao_sao_vazios():
    for massa in MASSAS:
        for campo, valor in massa.items():
            assert str(valor).strip() != "", \
                f"Campo '{campo}' está vazio na massa: {massa}"



# import sys
# import os
# import requests

# sys.path.append(os.path.join(os.path.dirname(__file__), "..", "output"))
# from massas_renegociacao_imovel import MASSAS

# BASE_URL = "https://brasilapi.com.br/api"

# def test_api_esta_online():
#     resposta = requests.get(f"{BASE_URL}/cnpj/v1/11222333000181")
#     assert resposta.status_code == 200, "API fora do ar!"

# def test_cnpj_valido_retorna_dados():
#     resposta = requests.get(f"{BASE_URL}/cnpj/v1/11222333000181")
#     dados = resposta.json()
#     assert "razao_social" in dados
#     assert "cnpj" in dados

# def test_cnpj_invalido_retorna_erro():
#     resposta = requests.get(f"{BASE_URL}/cnpj/v1/00000000000000")
#     assert resposta.status_code == 404, "CNPJ inválido deveria retornar 404!"

# def test_massas_geradas_tem_formato_valido():
#     for massa in MASSAS:
#         cnpj = str(massa["cnpj"])
#         assert len(cnpj) == 14, f"CNPJ com tamanho inválido: {cnpj}"
#         assert float(massa["valor"].replace(".", "").replace(",", ".")) > 0, \
#             f"Valor inválido: {massa['valor']}"