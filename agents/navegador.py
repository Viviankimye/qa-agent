# agents/navegador.py
# Aprendo Playwright — abrindo o navegador com Python

from playwright.sync_api import sync_playwright

def abrir_pagina(url):

    with sync_playwright() as p:

        navegador = p.chromium.launch(headless=False)

        pagina = navegador.new_page()

        pagina.goto(url)

        print(f"Título da página: {pagina.title()}")

        pagina.wait_for_timeout(3000)

        navegador.close()

def extrair_texto(url, seletor):

    with sync_playwright() as p:

        navegador = p.chromium.launch(headless=False)

        pagina = navegador.new_page()

        pagina.goto(url)

        pagina.wait_for_selector(seletor)

        elemento = pagina.query_selector(seletor)

        texto = elemento.inner_text()

        print(f"Texto extraído: {texto}")

        navegador.close()

        return texto

def extrair_lista(url, seletor):

    with sync_playwright() as p:

        navegador = p.chromium.launch(headless=False)

        pagina = navegador.new_page()

        pagina.goto(url)

        pagina.wait_for_selector(seletor)

        elementos = pagina.query_selector_all(seletor)

        textos = []

        for elemento in elementos:
            texto = elemento.inner_text()
            textos.append(texto)

        print(f"Total encontrado: {len(textos)}")
        for i, texto in enumerate(textos, 1):
            print(f"{i}. {texto}")

        navegador.close()

        return textos    