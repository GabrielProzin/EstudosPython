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


#output:
#PS C:\Users\Gabriel Mendes\Desktop\EstudosPython> & "C:/Users/Gabriel Mendes/AppData/Local/Programs/Python/Python313/python.exe" "c:/Users/Gabriel Mendes/Desktop/EstudosPython/Estudos/Semana 1/Dia 3/Dia-3.1.py"
#Digite o primeiro número: 10
#Digite o segundo núemro: 5
#O resultado da soma entre os dois números é: 15
#O resultado da multiplicação entre os dois números é: 50
#O resultado da divisão entre os dois números é: 2.0     
#O resultado da resto da divisão entre os dois números é: 0