'''
📘 DIA 13 — Tratamento de erros
🟢 Fácil — Try/Except básico
Peça ao usuário um número e tente convertê-lo com int().

Se der erro, exiba:
Você não digitou um número válido.
'''

numero = 0

try:
    numero = int(input("Digite um numero: "))
except ValueError:
    print("Digite um numero válido")
