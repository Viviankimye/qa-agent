
# tests/test_frontend_login.py
# Teste de frontend com Playwright + Pytest

from playwright.sync_api import sync_playwright


MASSAS_LOGIN = [
    {
        "usuario": "admin",
        "senha": "admin",
        "cenario": "Login com credenciais válidas",
        "resultado_esperado": "logout"
    },
    {
        "usuario": "",
        "senha": "",
        "cenario": "Login com campos vazios",
        "resultado_esperado": "login"
    },
    {
        "usuario": "admin",
        "senha": "senha_errada_123456",
        "cenario": "Login com credenciais inválidas",
        "resultado_esperado": "login"
    }
]


def test_login_valido():
    with sync_playwright() as p:
        navegador = p.chromium.launch(headless=False)
        pagina = navegador.new_page()

        pagina.goto("https://quotes.toscrape.com/login")

        pagina.fill("input[name='username']", "admin")
        pagina.fill("input[name='password']", "admin")
        pagina.click("input[type='submit']")

        pagina.wait_for_load_state("networkidle")

        logout = pagina.get_by_text("Logout")

        assert logout.is_visible(), \
            "Login válido deveria mostrar Logout!"

        print("\n✅ Login válido — PASSOU")

        navegador.close()


def test_login_campos_vazios():
    with sync_playwright() as p:
        navegador = p.chromium.launch(headless=False)
        pagina = navegador.new_page()

        pagina.goto("https://quotes.toscrape.com/login")

        pagina.fill("input[name='username']", "")
        pagina.fill("input[name='password']", "")
        pagina.click("input[type='submit']")

        pagina.wait_for_load_state("networkidle")

        assert "login" in pagina.url, \
            "Campos vazios deveriam permanecer no login!"

        print("\n✅ Login campos vazios — PASSOU")

        navegador.close()

def test_login_credenciais_invalidas():
    with sync_playwright() as p:
        navegador = p.chromium.launch(headless=False)
        pagina = navegador.new_page()

        pagina.goto("https://quotes.toscrape.com/login")

        pagina.fill("input[name='username']", "admin")
        pagina.fill("input[name='password']", "senha_errada_123456")
        pagina.click("input[type='submit']")

        pagina.wait_for_load_state("networkidle")

        logout_visivel = pagina.get_by_text("Logout").is_visible()

        assert not logout_visivel, (
            f"BUG: credenciais inválidas permitiram autenticação. "
            f"URL após tentativa: {pagina.url}"
        )

        navegador.close()