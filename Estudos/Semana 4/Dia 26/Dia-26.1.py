'''
🟢 26.1 – Fácil: Comparar preço com limite

Bibliotecas:

nenhuma (primeiro passo só com lógica)

Conceitos importantes:

condicionais if/else

Enunciado:

Peça ao usuário:

preço atual de um produto (digitado na mão)
preço desejado (alvo)
Se o preço atual for menor ou igual ao alvo:
mostre "Pode comprar! O preço já está bom."
Caso contrário:

mostre "Ainda está caro. Melhor esperar."
'''

valor_produto = float(input("Defina o preço do produto: R$"))
preco_desejado = float(input("Digite o valor desejado do produto: R$"))

if valor_produto <= preco_desejado:
    print("Pode comprar! O preço já está bom.")
else:
    print("Ainda está caro. Melhor esperar.")
