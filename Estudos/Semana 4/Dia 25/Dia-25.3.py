'''
🔴 25.3 – Difícil: Mini “aplicação” de conversão com resumo

Bibliotecas:

import requests
import time

laços
listas ou dicionários para armazenar histórico
exibição organizada (como se fosse um mini-sistema)

Crie um programa que:

Permita converter várias vezes entre:
USD → BRL
EUR → BRL
Guarde o histórico das conversões (moeda, valor_original, valor_convertido).

Ao digitar resumo, mostre:

Quantas conversões foram feitas
Qual foi o maior valor convertido
Total convertido (somando tudo em BRL)
'''

#https://open.er-api.com/v6/latest/

import requests
import time

def cotacao_moeda(moeda):
    url = f"https://open.er-api.com/v6/latest/{moeda}"
    response = requests.get(url)
    dados = response.json()
    return dados["rates"]["BRL"]

#def atualizar_lista():



historico = []

while True:

    print("1 - USD → BRL")
    print("2 - EUR → BRL")
    print("0 - SAIR")
    opcao = int(input("Digite alguma opção: "))

    if opcao == 1:
        moeda = "USD"
        cotacao = cotacao_moeda(moeda)

        cotacao_formatada = f"{time.strftime("%H:%M")} 1 {moeda} => R${cotacao:.2f}"
        
        historico.append(cotacao_formatada)
        print(historico)
        continue

    if opcao == 2:
        moeda = "EUR"
        cotacao = cotacao_moeda(moeda)

        cotacao_formatada = f"{time.strftime("%H:%M")} 1 {moeda} => R${cotacao:.2f}"
        
        historico.append(cotacao_formatada)
        print(historico)
        continue

    if opcao == 3:
        print("Saindo...")
        break

# puxar resumo


url = f"https://open.er-api.com/v6/latest/"

