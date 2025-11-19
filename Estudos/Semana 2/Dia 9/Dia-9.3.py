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
    alunos = {}

    alunos["nome"] = input("Digite o nome do aluno: ")
    alunos["idade"] = int(input("Digite a idade do aluno: "))
    alunos["nota"] = float(input("Digite a nota do aluno: "))
    lista_alunos.append(alunos)

for aluno in lista_alunos:
    soma += int(aluno["nota"])

for aluno in lista_alunos:

    if aluno[2]["nota"] < aluno[0]["nota"] > aluno[1]["nota"]:
        print("A maior nota é do aluno: ", aluno[0]["nome"])

    elif aluno[0]["nota"] < aluno[1]["nota"] > aluno[2]["nota"]:
        print("A maior nota é do aluno: ", aluno[1]["nome"])
    else:
        print("A maior nota é do aluno: ", aluno[2]["nome"])

media = soma / 3

print(f"A média de nota dos alunos é {media:.2f}")
print(lista_alunos)

