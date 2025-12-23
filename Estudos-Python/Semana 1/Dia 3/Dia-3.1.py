#📘 DIA 3 – Operadores (aritméticos, relacionais, lógicos)
#3.1 — Básico:

#Peça dois números ao usuário e exiba:

#soma
#multiplicação
#divisão
#resto da divisão


a = 0
b = 0
resultadoSoma = 0
resultadoMultiplicacao = 0
resultadoDivisao = 0
resultadoRestoDivisao = 0

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo núemro: "))

resultadoSoma = a + b
print(f"O resultado da soma entre os dois números é: {resultadoSoma}")
resultadoMultiplicacao = a * b
print(f"O resultado da multiplicação entre os dois números é: {resultadoMultiplicacao}")
resultadoDivisao = a / b
print(f"O resultado da divisão entre os dois números é: {resultadoDivisao}")
resultadoRestoDivisao = a % b
print(f"O resultado da resto da divisão entre os dois números é: {resultadoRestoDivisao}")


'''
CORREÇÕES // MELHORIAS

🔧 Melhorias

-Você criou as variáveis antes do input, mas elas não eram necessárias
-O código pode ser reduzido pela metade
-Visite uma lógica mais compacta


a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

print(f"Soma: {a + b}")
print(f"Multiplicação: {a * b}")
print(f"Divisão: {a / b}")
print(f"Resto da divisão: {a % b}")


'''