#6.2 — Intermediário:

#Peça um número e gere a tabuada dele (1 a 10).
contador = 1
numero = int(input("Digite um numero: "))
for num in range(1,11):
    resultado = numero * num
    print(resultado)