'''
🟠 23.2 – Médio: Converter um valor em dólar ou euro

Bibliotecas:

import requests

Conceitos importantes:

ler dados do usuário (input)
usar a cotação da API para fazer contas
organizar o código em pequenas funções (por exemplo: buscar_cotacao(), converter_valor())

Enunciado:

Pergunte ao usuário:

Qual moeda ele quer converter: USD ou EUR
Qual valor ele quer converter (ex: 100).
Busque a cotação online da moeda escolhida para BRL.

Calcule o valor convertido e mostre:

100 USD = 543.00 BRL
'''
#https://open.er-api.com/v6/latest/USD

import requests

def buscar_cotacao(moeda):
    url = f"https://open.er-api.com/v6/latest/{moeda}"
    response = requests.get(url)
    dados = response.json()
    return dados["rates"]["BRL"]

def converter_valor(valor, cotacao):
    return valor * cotacao

print("Conversão de moedas para BRL")

moeda = input("Digite a moeda que deseja converter: ")
valor = float(input("Digite o valor: "))

cotacao = buscar_cotacao(moeda)
valor_convertido = converter_valor(valor, cotacao)

print(f"{valor:.2f} {moeda} = {valor_convertido:.2f} BRL")