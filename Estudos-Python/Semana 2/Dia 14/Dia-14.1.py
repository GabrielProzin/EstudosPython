'''
📘 DIA 14 — Revisão + Mini-Projeto
🟢 Fácil — Revisão: listas + funções
Crie:

Uma função que recebe uma lista de nomes

Exibe cada nome com índice:
0 - Ana
1 - João
2 - Pedro
'''

nomes = ["Ana", "João", "Pedro"]

def lista_nome(nomes):
    for indice, nome in enumerate(nomes):
        print (indice, nome)

lista_nome(nomes)