'''
🔴 22.3 – Difícil: Renomear vários arquivos de uma pasta

Bibliotecas:

from datetime import datetime
import os

Conceitos importantes:

os.listdir() para listar arquivos
os.path.join()
filtrar por extensão (.txt, .csv, etc.)
laços for para processar vários arquivos

Crie um script que:
Peça ao usuário o caminho de uma pasta (por exemplo: Estudos/Arquivos_Gerados).
Liste todos os arquivos dessa pasta.
Apenas para arquivos .txt, renomeie usando o formato:
YYYY-MM-DD-nome_original.txt

Exemplo: anotacoes.txt → 2025-12-11-anotacoes.txt
Mostre na tela cada renomeação feita.
(Desafio extra: tratar erros com try/except caso algum arquivo não possa ser renomeado.)
'''

from datetime import datetime
import os

data = datetime.now()
data_formata = data.strftime("%Y,%m,%d")

caminho = r"C:\Users\anapa\Downloads\EstudosPython\Estudos\Semana 4\Dia 22"
pastas = os.listdir(caminho)
print(pastas)
pasta = input("Digite qual pasta deseja acessar: ")

caminho_completo = os.path.join(caminho, pasta)
arquivos = os.listdir(caminho_completo)
print(arquivos)


arquivos_filtrados = [
    arquivo
    for arquivo in os.listdir(caminho_completo)
        if arquivo.endswith(".txt")
]