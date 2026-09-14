# 🤖 QA Agent

Agente de QA desenvolvido em Python para auxiliar na criação, execução e análise de testes automatizados.

O projeto utiliza **Python, Pytest e Playwright** para automatizar testes de frontend e backend, permitindo estruturar cenários de teste e analisar os resultados de forma organizada.

---

## 🚀 Objetivo

O **QA Agent** tem como objetivo facilitar atividades de Quality Assurance através da automação de testes e do uso de agentes para apoiar a análise dos cenários.

Entre os objetivos do projeto estão:

* Automatizar testes de aplicações web.
* Criar cenários de teste para diferentes comportamentos da aplicação.
* Executar testes automatizados utilizando Pytest.
* Utilizar Playwright para testes de frontend.
* Organizar ferramentas e agentes em uma estrutura modular.
* Identificar falhas funcionais através dos testes.
* Gerar resultados que possam ser utilizados na análise de qualidade.

---

## 🛠️ Tecnologias

* **Python 3.14**
* **Pytest**
* **Playwright**
* **Git**
* **GitHub**

---

## 📁 Estrutura do projeto

```text
qa-agent/
│
├── agents/
│   ├── ia_agent.py
│   └── navegador.py
│
├── config/
│   └── settings.py
│
├── tests/
│   ├── test_backend_renegociacao.py
│   ├── test_frontend_login.py
│   └── test_renegociacao.py
│
├── tools/
│   ├── buscar_cep.py
│   └── output_writer.py
│
├── main.py
├── .gitignore
└── README.md
```

### Principais diretórios

**`agents/`**

Contém os agentes responsáveis pelas funcionalidades de automação e interação com o sistema.

**`config/`**

Centraliza configurações utilizadas pelo projeto.

**`tests/`**

Contém os testes automatizados do projeto, incluindo cenários de frontend e backend.

**`tools/`**

Contém ferramentas auxiliares utilizadas pelos agentes e pelos testes.

**`main.py`**

Ponto de entrada principal da aplicação.

---

## ⚙️ Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/Viviankimye/qa-agent.git
```

Entre na pasta:

```bash
cd qa-agent
```

### 2. Crie um ambiente virtual

No Windows:

```powershell
python -m venv .venv
```

Ative o ambiente virtual:

```powershell
.venv\Scripts\Activate.ps1
```

Caso esteja utilizando o Prompt de Comando:

```cmd
.venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install pytest playwright
```

### 4. Instale os navegadores do Playwright

```bash
playwright install
```

---

## 🧪 Executando os testes

Para executar todos os testes:

```bash
pytest
```

Para executar os testes com mais detalhes:

```bash
pytest -v
```

Para executar somente os testes de login:

```bash
pytest tests/test_frontend_login.py -v
```

---

## 🌐 Testes de Frontend

O projeto utiliza **Playwright** para automatizar interações com aplicações web.

Um dos cenários implementados testa o fluxo de login:

```text
┌─────────────────────────────┐
│        Tela de Login        │
└──────────────┬──────────────┘
               │
               ▼
      Preenche usuário/senha
               │
               ▼
          Clica Login
               │
               ▼
       Valida comportamento
               │
       ┌───────┴────────┐
       ▼                ▼
     PASS              FAIL
```

Atualmente existem cenários para:

* Login com credenciais válidas.
* Login com campos vazios.
* Login com credenciais inválidas.

### Exemplo

```python
pagina.fill("input[name='username']", "admin")
pagina.fill("input[name='password']", "admin")
pagina.click("input[type='submit']")
```

O teste então verifica o comportamento esperado da aplicação.

---

## 🔍 Exemplo de resultado

Ao executar:

```bash
pytest -v
```

um resultado pode ser semelhante a:

```text
tests/test_frontend_login.py::test_login_valido PASSED
tests/test_frontend_login.py::test_login_campos_vazios PASSED
tests/test_frontend_login.py::test_login_credenciais_invalidas FAILED
```

Uma falha não significa necessariamente que o teste está incorreto.

Por exemplo, se o requisito determinar que credenciais inválidas devem ser rejeitadas, mas a aplicação permitir o login, o teste pode identificar um possível **defeito funcional**.

---

## 🧠 Conceito do QA Agent

O projeto busca evoluir de uma suíte tradicional de testes automatizados para um fluxo no qual um agente possa auxiliar na interpretação dos cenários.

A ideia é trabalhar com o seguinte fluxo:

```text
        Cenário de teste
              │
              ▼
        QA Agent
              │
              ▼
      Execução do teste
              │
              ▼
       Resultado Pytest
              │
       ┌──────┴──────┐
       ▼             ▼
      PASS           FAIL
       │             │
       │             ▼
       │       Análise do erro
       │             │
       └──────┬──────┘
              ▼
        Resultado QA
```

---

## 📌 Status do projeto

🚧 **Em desenvolvimento**

O projeto está sendo desenvolvido de forma incremental, começando pela automação dos cenários de teste e pela estruturação dos agentes e ferramentas auxiliares.

### Implementado

* [x] Estrutura inicial do projeto.
* [x] Integração com Pytest.
* [x] Testes automatizados de frontend.
* [x] Automação de navegador com Playwright.
* [x] Cenários de login.
* [x] Estrutura inicial de agentes.
* [x] Ferramentas auxiliares.

### Próximos passos

* [ ] Melhorar a interpretação automática dos resultados.
* [ ] Gerar relatórios de execução.
* [ ] Expandir a cobertura de testes.
* [ ] Melhorar a geração automática de cenários.
* [ ] Integrar diferentes tipos de testes.
* [ ] Evoluir a análise de falhas utilizando IA.
* [ ] Criar uma interface para execução dos testes.

---

## 👩‍💻 Autora

**Vivian Akutsu**

Projeto desenvolvido para estudos e evolução prática em:

* Quality Assurance
* Automação de testes
* Python
* Pytest
* Playwright
* Inteligência Artificial
* Engenharia de Software

---

## 📄 Licença

Este projeto está em desenvolvimento e destinado principalmente a fins de estudo e portfólio.
