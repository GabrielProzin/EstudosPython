'''
🔴 20.3 – Mini-relatório geral (difícil)

Com base no mesmo vendas.csv do dia 17:

Seu programa deve:

Ler o CSV com Pandas.

Analisar:

total de vendas no período;
mês com maior faturamento;
categoria com mais vendas.

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

#print(vendas["data"].dtype)

vendas["mes"] = vendas["data"].dt.month
vendas["total"] = vendas["quantidade"] * vendas["preco_unitario"]
vendas["total_vendas"] = vendas.groupby("mes")["total"].sum()

#print(vendas["total_vendas"].max())

categoria_mais_vendida = vendas.groupby("categoria")["quantidade"].sum()

#print(categoria_mais_vendida.idxmax())

plt.plot(categoria_mais_vendida)
plt.xlabel("Categorias")
plt.ylabel("Vendas")
#plt.plot()
plt.title("Total de vendas por categoria")
plt.show()