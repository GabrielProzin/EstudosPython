'''
🟠 22.2 – Médio: Renomear um único arquivo com a data

Bibliotecas:

from datetime import datetime

import os

Conceitos importantes:

os.rename()
caminhos de arquivos (caminho_antigo, caminho_novo)
montar strings com f-strings

Enunciado:

Peça ao usuário o nome de um arquivo existente (por exemplo, relatorio.txt).
Gere um novo nome usando a data atual, nesse formato:
YYYY-MM-DD-relatorio.txt
Use os.rename() para renomear o arquivo.
Exiba uma mensagem confirmando a mudança.
(Dica: você pode testar criando um arquivo vazio antes, tipo relatorio.txt.)
'''

from datetime import datetime
import os

while True:
    nome_arquivo = input("Digite o nome do arquivo: ")

    if nome_arquivo == "relatorio.txt":
        data = datetime.now()
        data_formata = data.strftime("%Y-%m-%d")
        novo_nome = f"{data_formata}-{nome_arquivo}"
        os.rename(nome_arquivo, novo_nome)
        print(f"O nome do arquivo {nome_arquivo} foi alterado para '{novo_nome}'!")
        break
    else:
        print("Digite um arquivo existente!\n")