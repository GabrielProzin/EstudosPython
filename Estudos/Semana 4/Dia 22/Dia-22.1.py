'''
🟢 22.1 – Fácil: Mostrar data atual e gerar nome de arquivo

Bibliotecas:

from datetime import datetime

Conceitos importantes:

datetime.now()
strftime() para formatar a data em string

Crie um programa que:
Pegue a data atual do sistema.
Formate a data no padrão YYYY-MM-DD (ex: 2025-12-11).

Gere um nome de arquivo automático no formato:
backup-YYYY-MM-DD.txt

Mostre esse nome de arquivo na tela (não precisa criar o arquivo ainda).
'''

from datetime import datetime

data_agora = datetime.now()
print(data_agora)

data_formatada = data_agora.strftime("%Y-%m-%d")
print(data_formatada)

nome_arquivo = f"backup-{data_formatada}.txt"

print(nome_arquivo)