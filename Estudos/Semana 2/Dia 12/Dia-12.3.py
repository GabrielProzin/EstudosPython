'''
🔴 Difícil — Gerador de senha forte
Usando random e string:

Gere uma senha de 12 caracteres contendo:

letras maiúsculas
letras minúsculas
números
símbolos especiais
A senha não pode repetir 3 caracteres seguidos
A senha deve obrigatoriamente conter:
pelo menos 1 número
pelo menos 1 símbolo
'''

import random
import string

maisculas = string.ascii_uppercase
minuculas = string.ascii_lowercase
numeros = string.digits
simbolos = string.punctuation

todos = maisculas + minuculas + numeros + simbolos
senha = []

senha.append(random.choice(numeros))
senha.append(random.choice(simbolos))

while len(senha) < 12:
    novo = random.choice(todos)

    if len(senha) >= 2 and senha[-1] == novo and senha[-2] == novo:
        continue
    else:
        senha.append(novo)

random.shuffle(senha)
#senhaFinal = str(senha)
senhaFinal = "".join(senha)

print(senhaFinal)