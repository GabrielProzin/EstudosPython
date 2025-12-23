'''
🟠 26.2 – Médio: Buscar preço simulado via API

Bibliotecas:

import requests (podendo reaproveitar a API de câmbio ou outra qualquer que tenha um valor numérico)

Conceitos importantes:

Funções para separar responsabilidade:

buscar_preco_atual()
verificar_alerta(preco_atual, preco_alvo)
reaproveitar ideias do dia 23/25

Enunciado:
Simule um “bot” que:
Pergunte um preço alvo para um ativo (por exemplo, dólar, bitcoin, ação, etc.).
Busque o preço atual em uma API.
Compare com o preço alvo.
Mostre mensagem dizendo se deve alertar ou não.
(Você pode usar a mesma API de moedas, considerando o valor de uma delas como “preço”.)
'''

#https://open.er-api.com/v6/latest/

import requests

def buscar_preco_atual(moeda):
    url = f"https://open.er-api.com/v6/latest/{moeda}"
    response = requests.get(url)
    dados = response.json()
    return dados["rates"]["BRL"]

def verificar_alerta(preco_atual, preco_alvo):
    if preco_atual <= preco_alvo:
        mensagem = "Preço está ABAIXO do desejado!"
    else:
        mensagem = "Preço está ACIMA do desejado!"
    return mensagem

moeda = input("Digite a moeda desejda: ").upper()
preco_alvo = float(input("Digite o valor desejado: "))

preco_atual = buscar_preco_atual(moeda)
alerta = verificar_alerta(preco_atual, preco_alvo)
print(alerta)