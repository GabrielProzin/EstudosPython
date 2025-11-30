'''
🔴 15.3 – Analisador de logs (difícil)

Imagine que você tem um arquivo acessos.log com linhas nesse formato:

2025-01-10 09:15:23 - usuario: gabriel - acao: login
2025-01-10 09:20:10 - usuario: maria   - acao: login
2025-01-10 09:35:01 - usuario: gabriel - acao: logout
...

Crie um programa que:

Leia o arquivo linha a linha.
Conte quantos logins cada usuário fez.
Gere um novo arquivo chamado relatorio_acessos.txt com o seguinte formato:

--- RELATÓRIO DE ACESSOS ---
gabriel - 5 logins
maria   - 3 logins
joao    - 1 login

Requisitos:

Usar dicionários para contar logins por usuário.
Ignorar linhas vazias ou malformadas (usar try/except ou if pra validar o formato básico).
Fechar todos arquivos com with.
'''
contagem = {}

with open("acessos.log", "r") as f:

    for linha in f:
        if linha.strip() == "":
            continue
        linha = linha.strip()
        partes = linha.split(" - ")
        if len(partes) != 3:
            continue
        info_usuario = partes[1]
        info_acao = partes[2]
        try:
            chave_usuario, nome_usuario = info_usuario.split(":")
            chave_acao, acao_usuario = info_acao.split(":")

            nome_usuario = nome_usuario.strip()
            acao_usuario = acao_usuario.strip()
        except ValueError:
            continue

        if acao_usuario == "login":
            if nome_usuario not in contagem:
                contagem[nome_usuario] = 0
            contagem[nome_usuario] += 1

with open("relatorios_acessos.txt", "w") as f:
    palavra = ""
    f.write("--- RELATÓRIO DE ACESSOS ---\n")
    for usuario, qntd in contagem.items():
        if qntd == 1:
            palavra == "Login"
        else:
            palavra == "Logins"
        linha_relatorio = f"{usuario} - {qntd}{palavra}\n"
        f.write(linha_relatorio)