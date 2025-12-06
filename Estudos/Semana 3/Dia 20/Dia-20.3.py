'''
🔴 20.3 – Mini-relatório geral (difícil)

Com base no mesmo vendas.csv do dia 17:

Seu programa deve:

Ler o CSV com Pandas.

Analisar:

total de vendas no período; 🟢
mês com maior faturamento; 🟢
categoria com mais vendas.🟢

Criar:

um gráfico de barras com total de vendas por categoria (Matplotlib).

Salvar:

resumo em resumo_vendas.txt;
gráfico em arquivo de imagem grafico_vendas.png.
'''

import pandas as pd
import matplotlib.pyplot as plt

vendas = pd.read_csv("vendas_completo.csv", sep=",", encoding="utf-8")

vendas["data"] = pd.to_datetime(vendas["data"])

vendas["mes"] = vendas["data"].dt.month
vendas["total"] = vendas["quantidade"] * vendas["preco_unitario"]

vendas["total_vendas"] = vendas.groupby("mes")["total"].sum()

categoria_mais_vendida = vendas.groupby("categoria")["quantidade"].sum()
total_vendas = vendas.groupby("mes")["total"].sum()
maior_faturamento_categoria = vendas["total_vendas"].max()


# print(f"Total de vendas no período: ")
# print(f"{total_vendas}")
# print(f"Mês com o maior faturamento é de: {vendas["total_vendas"].max()}")
# print(f"Categoria com mais vendas: {categoria_mais_vendida.idxmax()}")


# plt.plot(categoria_mais_vendida)
# plt.xlabel("Categorias")
# plt.ylabel("Vendas")
# plt.title("Total de vendas por categoria")
# plt.show()

# total por periodo:

total_periodo = "\n".join(f"{mes}: {valor}" for mes, valor in total_vendas.items())

with open("resumo.txt", "w") as file:
    file.write(total_periodo)