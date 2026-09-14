# tests/test_renegociacao.py
# Testes de renegociação usando massas geradas pelo agente

# tests/test_renegociacao.py
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "output"))

from massas_renegociacao_imovel import CENARIOS, MASSAS

def test_cenarios_foram_gerados():
    assert len(CENARIOS) > 0, "Nenhum cenário foi gerado!"

def test_massas_foram_geradas():
    assert len(MASSAS) > 0, "Nenhuma massa foi gerada!"

def test_todas_massas_tem_cnpj():
    for massa in MASSAS:
        assert "cnpj" in massa, f"Massa sem CNPJ: {massa}"

def test_todas_massas_tem_contrato():
    for massa in MASSAS:
        assert "contrato" in massa, f"Massa sem contrato: {massa}"

def test_cnpj_tem_14_digitos():
    for massa in MASSAS:
        cnpj = str(massa["cnpj"])
        assert len(cnpj) == 14, f"CNPJ inválido: {cnpj}"

def test_valor_nao_e_vazio():
    for massa in MASSAS:
        assert massa["valor"] != "", f"Valor vazio na massa: {massa}"