'''
🔴 Difícil — Sistema de alunos com dicionários

Crie um programa que:
Cadastre 3 alunos, cada um com:

nome
idade
nota
Armazene tudo em uma lista de dicionários.

Exemplo:
alunos = [
    {"nome": "Ana", "idade": 20, "nota": 8.5}
]
Depois:

Exiba o nome de todos os alunos
Calcule a média das notas
Mostre qual aluno tem a maior nota
Não use funções ainda — isso é para o dia 10.
'''

soma = 0
lista_alunos = []

for num in range(3):
    aluno = {}

    aluno["nome"] = input("Digite o nome do aluno: ")
    aluno["idade"] = int(input("Digite a idade do aluno: "))
    aluno["nota"] = float(input("Digite a nota do aluno: "))
    lista_alunos.append(aluno)

for aluno in lista_alunos:
    nota = aluno["nota"]
    soma += nota

media = soma / len(lista_alunos)

print(f"A média de nota dos alunos é {media:.2f}")

for aluno in lista_alunos:
    print(aluno["nome"])

maior = lista_alunos[0]

for aluno in lista_alunos:
    if aluno["nota"] > maior["nota"]:
        maior = aluno

print(f"O aluno {maior["nome"]} tem a maior nota {maior["nota"]}")