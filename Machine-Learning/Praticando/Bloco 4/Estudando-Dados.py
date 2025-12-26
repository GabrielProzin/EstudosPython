'''
🧮 BLOCO 4 — Qualidade dos dados (mentalidade profissional)

Existem valores nulos no dataset?

Alguma coluna parece inútil para ML?

Existem colunas que são apenas identificadores?

Existem colunas categóricas que precisariam ser transformadas?

O dataset está balanceado em popularidade?

Faz sentido criar uma coluna:

música popular (sim/não)?

👉 Objetivo: pensar em preparação de dados
'''

import pandas as pd

dados = pd.read_csv("Machine-Learning/spotify_data clean.csv")

print(dados.head(100))