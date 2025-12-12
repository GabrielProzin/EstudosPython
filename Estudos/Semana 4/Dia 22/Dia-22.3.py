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

caminho = r"C:\Users\Gabriel Mendes\Desktop\EstudosPython\Estudos"
pastas = os.listdir(caminho)

print(pastas)