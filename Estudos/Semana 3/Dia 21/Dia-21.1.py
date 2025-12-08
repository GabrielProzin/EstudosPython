'''
📊 DIA 21 – Projeto: Relatório de vendas (CSV + Pandas + Matplotlib)

Aqui a ideia é você fazer algo mais “projetinho”.

🟢 21.1 – Relatório simples (básico)

Dado um CSV vendas_simples.csv com:

mes
valor

Faça:

Ler o CSV com Pandas.
Mostrar no terminal:
total no ano;
média por mês.
Plotar um gráfico de linha com mes x valor.
'''

import pandas as pd
import matplotlib.pyplot as plt

with open("vendas_simples.csv", "r") as file:
    vendas = pd.read_csv(file)

    vendas_total = vendas["valor"].sum()
    media_vendas = vendas["valor"].mean()

    print(f"O valor total de vendas no ano é R${vendas_total}")
    print(f"A média de vendas por mês é R${media_vendas:.0f}")

plt.plot(vendas["mes"], vendas["valor"])
plt.xlabel("Mês")
plt.ylabel("Valor")
plt.title("Vendas no ano")
plt.show()