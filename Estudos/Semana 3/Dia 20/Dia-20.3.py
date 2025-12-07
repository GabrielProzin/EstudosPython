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

# Leitura
vendas = pd.read_csv("vendas_completo.csv", sep=",", encoding="utf-8")

# Tratamento
vendas["data"] = pd.to_datetime(vendas["data"])
vendas["mes"] = vendas["data"].dt.month
vendas["total"] = vendas["quantidade"] * vendas["preco_unitario"]

# Agrupamentos
total_vendas = vendas.groupby("mes")["total"].sum()
categoria_mais_vendida = vendas.groupby("categoria")["quantidade"].sum().idxmax()
mes_maior_faturamento = total_vendas.idxmax()

# ============================
# GERAÇÃO DO GRÁFICO POR CATEGORIA
# ============================
vendas_categoria = vendas.groupby("categoria")["total"].sum()

plt.figure(figsize=(8, 5))
plt.bar(vendas_categoria.index, vendas_categoria.values)
plt.xlabel("Categoria")
plt.ylabel("Total de Vendas (R$)")
plt.title("Total de Vendas por Categoria")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("grafico_vendas.png")
plt.close()

# ============================
# GERAÇÃO DO TEXTO DE RESUMO
# ============================

# total por mês
total_periodo = "\n".join(
    f"Mês {mes}: R${valor:.2f}" for mes, valor in total_vendas.items()
)

mais_vendido = f"A categoria mais vendida foi: {categoria_mais_vendida}"
maior_faturamento = (
    f"\nO mês de maior faturamento foi o mês {mes_maior_faturamento} "
    f"com R${total_vendas[mes_maior_faturamento]:.2f}"
)

with open("resumo_vendas.txt", "w", encoding="utf-8") as file:
    file.write("Total de vendas no período:\n")
    file.write(total_periodo)
    file.write("\n\n")
    file.write(maior_faturamento)
    file.write("\n")
    file.write(mais_vendido)
