#5.3 — Desafiador:

#Sistema de classificação de IMC:

#peça peso
#peça altura
#calcule IMC
#exiba a categoria:


#<18.5: Abaixo do peso  
#18.5–24.9: Normal  
#25–29.9: Sobrepeso  
#>=30: Obesidade

peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em CM: "))
imc = (peso / ((altura / 100) ** 2))

if imc < 18.5:
    print("abaixo do peso")
elif imc >= 18.5 and imc < 25:
    print("normal")
elif imc >= 25 and imc < 30:
    print("sobrepeso")
elif imc >= 30:
    print("obesidade")


'''
CORREÇÕES // MELHORIAS

Versão otimizada: 
 

peso = float(input("Peso (kg): "))
altura = float(input("Altura (cm): ")) / 100

imc = peso / (altura ** 2)

if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("Normal")
elif imc < 30:
    print("Sobrepeso")
else:
    print("Obesidade")
   
    
'''