#6.2 — Intermediário:

#Peça um número e gere a tabuada dele (1 a 10).
numero = int(input("Digite um numero: "))
for num in range(1,11):
    resultado = numero * num
    print(resultado)

'''
CORREÇÕES // MELHORIAS

VERSÃO OTIMIZADA


numero = int(input("Digite um número: "))

for i in range(1, 10 + 1):
    print(f"{numero} x {i} = {numero * i}")


'''