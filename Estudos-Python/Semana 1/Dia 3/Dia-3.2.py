#3.2 — Intermediário:
#Crie um programa que pergunta três números e diz:

#qual é o maior
#qual é o menor
#se existe algum número igual entre eles

#Não pode usar listas ainda.
#Apenas operadores relacionais/lógicos.


numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))
numero3 = int(input("Digite o terceiro numero: "))

if numero1 > numero2 and numero1 > numero3:
    print(f"o numero {numero1} é o maior")
elif numero2 > numero1 and numero2 > numero3:
    print(f"o numero {numero2} é o maior")
else:
    print(f"o numero {numero3} é o maior")



if numero1 < numero2 and numero1 < numero3:
    print(f" o numero {numero1} é o menor")
elif numero2 < numero1 and numero2 < numero3:
    print(f"o numero {numero2} é o menor")
else:
    print(f"o numero {numero3} é o menor")



if numero1 == numero2:
    print("o primeiro e o segundo numero sao iguais")
elif numero1 == numero3:
    print("o primeiro e o terceiro numero sao iguais")
elif numero2 == numero3:
    print("o segundo e o terceiro numero sao iguais")
else:
    print("nao possui numeros iguais")


'''
CORREÇÕES // MELHORIAS

🔧 Melhorias

-Seu código funciona, mas repete bastante coisa
-Pode reduzir verificações repetidas
-O bloco que verifica números iguais pode ser mais elegante com um único if


a = int(input("Primeiro número: "))
b = int(input("Segundo número: "))
c = int(input("Terceiro número: "))

# Maior
if a > b and a > c:
    maior = a
elif b > a and b > c:
    maior = b
else:
    maior = c

# Menor
if a < b and a < c:
    menor = a
elif b < a and b < c:
    menor = b
else:
    menor = c

print(f"Maior número: {maior}")
print(f"Menor número: {menor}")

# Iguais
if a == b or a == c or b == c:
    print("Existe pelo menos um número igual.")
else:
    print("Não existem números iguais.")



'''