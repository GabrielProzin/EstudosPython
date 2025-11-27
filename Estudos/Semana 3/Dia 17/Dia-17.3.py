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