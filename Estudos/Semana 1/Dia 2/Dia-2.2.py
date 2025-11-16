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


#output:
#PS C:\Users\Gabriel Mendes\Desktop\EstudosPython> & "C:/Users/Gabriel Mendes/AppData/Local/Programs/Python/Python313/python.exe" "c:/Users/Gabriel Mendes/Desktop/EstudosPython/Estudos/Semana 1/Dia-2.2.py"
#Digite o nome do produto: bola
#Digite o preço do produto: 2 
#Quantidade de produtos no estoque: 500
#Produto: bola
#Preço: 2.0
#Quantidade disponível: 500
#Valor total em estoque: 1000.0