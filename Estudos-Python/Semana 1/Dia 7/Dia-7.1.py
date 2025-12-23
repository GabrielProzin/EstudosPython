#📘 DIA 7 – Revisão + Mini-projeto
#7.1 — Revisão Simples:

#Crie um programa que:

#pede nome
#pede idade
#se idade >= 18 → pode dirigir
#caso contrário → não pode

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))

if idade >= 18:
    print("Pode dirigir!")
else:
    print("Nao pode dirigir")