#4.3 — Desafiador (Cenário real):

#Faça um mini sistema que pergunta:

#nome do cliente
#valor da compra
#valor pago

#Mostre:

#troco
#se foi pagamento exato (bool)
#se o cliente ficou devendo (bool)

nome = input("Digite o nome do cliente: ")
valorCompra = float(input("Digite o valor da compra: "))
valorPago = float(input("Digite o valor pago: "))

troco = valorPago - valorCompra

pagamentoExato = (troco == 0)
estaDevendo = (valorPago < valorCompra)

print(f"nome do cliente: {nome}")
print(f"valor da compra: R${valorCompra}")
print(f"valor pago: R${valorPago}")
print(f"valor do troco: R${troco}")
print(f"pagamento exato? {pagamentoExato}")
print(f"o cliente esta devendo? {estaDevendo}")