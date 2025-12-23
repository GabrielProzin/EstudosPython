'''
🧮 DIA 18 – Biblioteca NumPy
🟢 18.1 – Operações básicas com arrays (básico)

Crie um script que:

Cria um array com as idades de 5 pessoas.

Calcule e imprima:

média das idades
idade mínima
idade máxima
Some 1 ano a todas as idades (simulando “ano seguinte”) e mostre o novo array.

Requisitos:

Usar np.array e funções do próprio NumPy (mean, min, max).
'''

import numpy as np

idades = np.array([1, 2, 3, 4, 5])

print(f"A média das idades é: {np.mean(idades)}")
print(f"A menor idade é: {np.min(idades)}")
print(f"A maior idade é: {np.max(idades)}")

soma_idades = idades + 1

print(f"A idade no próximo ano é: {soma_idades}")