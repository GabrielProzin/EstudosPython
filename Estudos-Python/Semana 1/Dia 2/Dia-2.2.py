#2.2 — Intermediário:
#Crie um programa que receba três informações de um produto:

#nome (string)
#preço (float)
#quantidade_em_estoque (int)

#Mostre um resumo assim:
#Produto: Tênis
#Preço unitário: 250.0
#Quantidade disponível: 12
#Valor total em estoque: 3000.0

nome = str(input("Digite o nome do produto: "))
preco = float(input("Digite o preço do produto: "))
quantidade_em_estoque = int(input("Quantidade de produtos no estoque: "))
valor_em_estoque = quantidade_em_estoque * preco

print(f"Produto: {nome}\n Preço: {preco}\n Quantidade disponível: {quantidade_em_estoque}\n Valor total em estoque: {valor_em_estoque}")


'''
CORREÇÕES // MELHORIAS

🔧 Melhorias

-str() no input é desnecessário (input já é string)
-Pode formatar valores em dinheiro com 2 casas decimais
-Pode alinhar melhor o print


nome = input("Nome do produto: ")
preco = float(input("Preço do produto: "))
quantidade = int(input("Quantidade em estoque: "))

total = preco * quantidade

print(
    f"Produto: {nome}\n"
    f"Preço unitário: R${preco:.2f}\n"
    f"Quantidade disponível: {quantidade}\n"
    f"Valor total em estoque: R${total:.2f}"
)

'''
