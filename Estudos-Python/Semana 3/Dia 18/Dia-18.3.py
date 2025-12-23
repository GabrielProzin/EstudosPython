'''
🔴 18.3 – Simulação de dados (difícil)

Simule um cenário de 1000 medições de temperatura (em graus Celsius) usando NumPy:

Gere um array com 1000 valores seguindo uma distribuição normal com:

média 25
desvio padrão 3
(dica: np.random.normal)

Calcule:

média real dos dados
desvio padrão real dos dados
valor mínimo e máximo

Conte quantos dias tiveram temperatura:

abaixo de 20
acima de 30

Requisitos:

Usar funções de NumPy para tudo (evitar loops).
Mostrar os resultados bem formatados.
'''

import numpy as np

temperaturas = np.random.normal(loc=25, scale=3, size=1000)

temp_media = np.mean(temperaturas)
media_desvio = np.std(temperaturas)
temp_min = np.min(temperaturas)
temp_max = np.max(temperaturas)
qntd_acima_30 = np.sum(temperaturas > 30)
qntd_abaixo_20 = np.sum(temperaturas < 20)

print(temp_media)
print(media_desvio)
print(temp_min)
print(temp_max)
print(qntd_acima_30)
print(qntd_abaixo_20)

