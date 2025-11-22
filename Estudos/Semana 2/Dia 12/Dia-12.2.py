'''
🟡 Intermediário — Gerador de números aleatórios
Use o módulo random para:

Gerar um número aleatório entre 1 e 100
Pedir para o usuário tentar adivinhar

Mostrar:

“Acertou!”
ou “Errou! O número era X”
'''
import random

aleatorio = random.randrange(6)
numero = 0

numero = int(input("Digite um numero de 1 a 5: "))

if numero == aleatorio:
    print("voce acertou!")
else:
    print(f"voce errou! o numero era: {aleatorio}" )