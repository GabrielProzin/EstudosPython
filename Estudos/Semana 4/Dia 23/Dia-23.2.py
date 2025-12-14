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
    url = "https://open.er-api.com/v6/latest/"
    url_completa = url + moeda
    response = requests.get(url_completa)
    lista_moedas = response.json()
    return lista_moedas

def converter_valor(valor):
    valor_convertido = moeda * valor
    return valor_convertido

print("Conversão de moedas para BRL")
moeda = input("Digite a moeda que deseja converter: ")
buscar_cotacao(moeda)

valor = float(input("Digite o valor: "))
converter_valor(valor)