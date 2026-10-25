from urllib.parse import urlsplit


def validar_plano(plano):
    motivos = []

    if not isinstance(plano, dict):
        return {
            "aprovado": False,
            "motivos": ["Plano inválido"]
        }

    campos_obrigatorios = ["confianca", "dominio", "tarefas"]
    campos_ausentes = [
        campo for campo in campos_obrigatorios
        if campo not in plano
    ]

    if campos_ausentes:
        motivos.append("Plano inválido: campos obrigatórios ausentes")

    confianca = plano.get("confianca")
    if (
        isinstance(confianca, bool)
        or not isinstance(confianca, (int, float))
        or confianca < 1.0
    ):
        motivos.append("Baixa confiança para execução")

    dominio = plano.get("dominio")
    if not isinstance(dominio, str) or not dominio.strip():
        motivos.append("Domínio não definido para execução")

    tarefas = plano.get("tarefas")
    if not isinstance(tarefas, list) or not tarefas:
        motivos.append("Plano sem tarefas para execução")

    return {
        "aprovado": len(motivos) == 0,
        "motivos": motivos
    }



def validar_escopo_seguranca(escopo_autorizado, alvo):
    motivos = []

    if escopo_autorizado is None:
        motivos.append("Escopo de segurança não autorizado")
    elif (
        not isinstance(escopo_autorizado, dict)
        or not isinstance(escopo_autorizado.get("alvos"), list)
        or not escopo_autorizado["alvos"]
    ):
        motivos.append("Escopo de segurança inválido")

    def url_https_valida(valor):
        if not isinstance(valor, str) or not valor.strip():
            return False

        try:
            url = urlsplit(valor)
            return (
                url.scheme == "https"
                and bool(url.hostname)
                and url.username is None
                and url.password is None
            )
        except ValueError:
            return False

    if not url_https_valida(alvo):
        motivos.append("Alvo de segurança inválido")

    if (
        isinstance(escopo_autorizado, dict)
        and isinstance(escopo_autorizado.get("alvos"), list)
    ):
        alvos_autorizados = escopo_autorizado["alvos"]

        if not all(url_https_valida(item) for item in alvos_autorizados):
            motivos.append("Escopo de segurança inválido")
        elif url_https_valida(alvo) and alvo not in alvos_autorizados:
            motivos.append("Alvo fora do escopo autorizado")

    return {
        "aprovado": len(motivos) == 0,
        "motivos": motivos
    }
