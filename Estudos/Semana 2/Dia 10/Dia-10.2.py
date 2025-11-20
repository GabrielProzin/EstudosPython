'''
🟡 Intermediário — Função que calcula IMC
Crie uma função chamada calcular_imc(peso, altura) que:

Recebe peso e altura em metros
Calcula o IMC
Retorna o valor

No programa principal:

peça peso e altura
chame a função
exiba o IMC com duas casas decimais
'''

peso = int(input("Digite o seu peso em KG: "))
altura = float(input("Digite a sua altura em metros: "))

def calcular_imc():
    imc = peso / (altura ** 2)
    print(f"O seu IMC é: {imc:.2f}")

calcular_imc()