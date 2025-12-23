imc, peso, altura = 0

peso = int(input("Informe o seu peso em KG: "))
altura = int(input("Informe a sua altura em "))

def calcularIMC():
    imc = peso/(altura**altura)
    return print(f"O seu IMC é: {imc}")

calcularIMC()