'''
🟡 Intermediário — Lista de compras dinâmica
Crie uma lista vazia chamada lista_compras.
O programa deve:

Pedir ao usuário 3 itens para adicionar à lista usando append()
Mostrar a lista completa
Perguntar qual item ele deseja remover
Remover o item com remove() e exibir a lista atualizada
Mostrar se um item específico (ex: “arroz”) está ou não está na lista usando in
'''
lista_compras=[]
for num in range(3):
    item = input(f"Digite o item {num + 1}: ")
    lista_compras.append(item)

print(f"Sua lista de compras: {lista_compras}")

removerItem = input("Digite o nome do item para remover: ")
if removerItem in lista_compras:
    lista_compras.remove(removerItem)
    print(f"O item {removerItem} foi removido com sucesso!")
else: 
    print("Esse item não existe na lista!")

print(f"Lista atualizada: {lista_compras}")

produto = input("Digite o nome do produto para verificar: ")
if produto in lista_compras:
    print(f"O produto {produto} está inserido na lista")
else:
    print(f"O produto {produto} NÃO está na lista!")