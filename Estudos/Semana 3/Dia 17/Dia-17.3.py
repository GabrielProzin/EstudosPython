'''
🔴 17.3 – Analisando uma planilha de vendas (difícil)

Tenha um CSV vendas.csv com colunas:

data (AAAA-MM-DD)
produto
categoria
quantidade
preco_unitario

Seu programa deve:

Ler o CSV em um DataFrame.
Criar uma coluna valor_total = quantidade * preco_unitario.

Responder (e mostrar no terminal):

Total de vendas (somando valor_total).
Quantidade total vendida por categoria (usar groupby).
Produto mais vendido em quantidade.
Produto que mais gerou receita (valor_total).

Salvar um CSV resumo_categoria.csv com:

categoria
qtd_total
valor_total

Requisitos:

Usar groupby, sum() e sort_values().
'''

import pandas as pd

vendas = pd.read_csv("vendas.csv")

vendas["valor_total"] = vendas["quantidade"] * vendas["preco_unitario"]

print(f"O total de vendas foi de: R${vendas['valor_total'].sum():.2f}\n")

qntd_categoria = vendas.groupby("categoria")["quantidade"].sum()
print(qntd_categoria)

produto_mais_vendido = vendas.groupby("produto")["quantidade"].sum().idxmax()
print(produto_mais_vendido)

receita_por_produto = vendas.groupby("produto")["valor_total"].sum()
produto_maior_receita = receita_por_produto.idxmax()
print(f"Produto que mais gerou receita: {produto_maior_receita}")

resumo = vendas.groupby("categoria").agg(qtd_total = ("quantidade", "sum"), valor_total = ("valor_total", "sum"))
resumo = resumo.reset_index()
resumo.to_csv("resumo_categoria.csv", index=False)

