'''
📘 DIA 12 — Módulos e Bibliotecas
🟢 Fácil — Usando a biblioteca math
Importe math e:

Peça um número

Mostre:

raiz quadrada (sqrt())
número elevado ao quadrado (pow())
'''

import math

numero = 0
numero = int(input("Digite um numero: "))
raiz = math.sqrt(numero)
quadrado = math.pow(numero,2)

print(f"A raiz quadrada do numero {numero} é: {raiz}")
print(f"O {numero} elevado ao quadrado é: {quadrado}")
