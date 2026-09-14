# Fluxo completo: estória → cenários → massas → arquivos

from config.settings import DOMAIN, FRAMEWORK, OUTPUT_DIR
from agents.ia_agent import gerar_massa
from tools.output_writer import salvar_resultado

def rodar_agente(estoria, nome):

    print("\n" + "="*40)
    print("QA Intelligence Agent")
    print(f"Domínio: {DOMAIN}")
    print(f"Framework: {FRAMEWORK}")
    print("="*40)

    print(f"\nAnalisando estória: {nome}...")
    resultado = gerar_massa(estoria)

    print(f"\n=== CENÁRIOS ENCONTRADOS ===")
    for i, cenario in enumerate(resultado["cenarios"], 1):
        print(f"{i}. {cenario}")

    print(f"\n=== MASSAS GERADAS ===")
    for massa in resultado["massas"]:
        for campo, valor in massa.items():
            print(f"  {campo}: {valor}")
        print("  ---")

    salvar_resultado(nome, resultado)

    print("\nAgente finalizado com sucesso!")
    print("="*40)


# Teste 1 — Pix
estoria_pix = """
Como cliente,
quero realizar um pagamento via Pix,
para pagar meu fornecedor rapidamente.
"""

rodar_agente(estoria_pix, "pagamento_pix")    

    # Teste 2 — Cadastro
estoria_cadastro = """
Como visitante,
quero realizar o cadastro na plataforma,
para acessar os serviços disponíveis.
"""

rodar_agente(estoria_cadastro, "cadastro_usuario")

estoria_renegociacao = """
Como cliente PJ,
quero renegociar minha dívida de imovel,
para regularizar minha situação financeira.
"""

rodar_agente(estoria_renegociacao, "renegociacao_imovel")