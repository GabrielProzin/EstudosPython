'''
🟡 Intermediário — Dicionário + funções

Crie uma função chamada cadastrar_produto() que:

recebe nome, quantidade e valor
retorna um dicionário
salve 3 produtos em uma lista
exiba o total de itens em estoque (somando as quantidades)
'''


produtos = []

def cadastrar_produto(nome, quantidade, valor):
    return {
        "nome": nome,
        "quantidade": quantidade,
        "valor": valor
    }

produtos.append(cadastrar_produto("garrafa", 100, 10))
produtos.append(cadastrar_produto("copo", 100, 1))
produtos.append(cadastrar_produto("celular",  50, 1000))

total_produtos = 0

for quantidadeProduto in produtos:
    total_produtos += quantidadeProduto["quantidade"]

print("Produtos cadastrados: ", produtos)
print("Total de produtos: ", total_produtos)
