'''
🟡 21.2 – Relatório por produto (intermediário)

Com um CSV vendas_produtos.csv:

data
produto
quantidade
preco_unitario

Faça:

Calcular valor_total. 🟢
Agrupar por produto e descobrir:
total vendido por produto; 🟢
produto mais vendido (em valor).
Gerar um gráfico de barras com produto x valor_total.
Salvar o gráfico como vendas_por_produto.png.
'''

import pandas as pd
import matplotlib.pyplot as plt

with open("vendas_completo.csv", "r", encoding="utf-8") as file:
    vendas = pd.read_csv(file)
    vendas["total"] = vendas["quantidade"] * vendas["preco_unitario"]
    valor_total = vendas["total"].sum()
    print(f"O valor total de vendas é R${valor_total}")

    valor_total_produto = vendas.groupby("produto")["total"].sum()
    print("\nO valor total vendido por produto é: \n")
    print(valor_total_produto)

    produto_mais_vendido = vendas.groupby("produto")["total"].sum()
    print(f"Produto mais vendido em valor: R${produto_mais_vendido.max()}")


    plt.bar(produto_mais_vendido.index, produto_mais_vendido.values)
    plt.xlabel("Produto")
    plt.ylabel("Valor total")
    plt.title("Valor total de vendas por produto")
    plt.savefig("vendas_por_produto.png")
    plt.show()