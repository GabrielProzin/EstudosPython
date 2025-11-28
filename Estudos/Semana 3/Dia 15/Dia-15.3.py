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

linhasAcessosLOG = []
contadorLogin = 0

with open("acessos.log", "r") as f:

    for linha in f:
        if linha.strip() == "":
            continue
        print(linha)


print(linhasAcessosLOG)