'''
🟠 27.2 – Médio: Agrupar gastos por categoria
Bibliotecas necessárias:

pandas as pd

Conceitos importantes:

groupby()
agregação com sum()
sort (sort_values())

A partir do mesmo arquivo gastos.csv:

Leia o CSV com Pandas.
Agrupe por categoria usando:
df.groupby("categoria")["valor"].sum()
Mostre o total gasto em cada categoria.
Ordene da categoria mais cara para a mais barata.

Exemplo de saída:

Categoria      Valor
alimentação    300
transporte     120
lazer          75
'''