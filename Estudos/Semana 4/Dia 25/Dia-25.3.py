'''
🔴 25.3 – Difícil: Mini “aplicação” de conversão com resumo

Bibliotecas:

import requests

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

def cotacao_moeda(moeda):
    url = f"https://open.er-api.com/v6/latest/{moeda}"
    response = requests.get(url)
    dados = response.json()
    return dados["rates"]["BRL"]

def conversao_valor(cotacao, valor):
    return cotacao * valor

historico = []

contagem_conversao = 0

total_usd = 0
total_eur = 0

maior_usd = 0
maior_eur = 0

dolar_conversao = 0
euro_conversao = 0

total_conversao = 0
valor_conversao = 0
maior_conversao = 0

while True:

    print("---------//---------")
    print("1 - USD → BRL")
    print("2 - EUR → BRL")
    print("3 - Resumo")
    print("0 - SAIR")
    opcao = int(input("Digite alguma opção: "))

    if valor_conversao > maior_conversao:
        maior_conversao = valor_conversao

    total_conversao += valor_conversao

#Conversao em DOLAR
    if opcao == 1:
        moeda = "USD"
        cotacao = cotacao_moeda(moeda)

        valor = float(input("Quantos dolares deseja converter em reais? $"))
        dolar_conversao = conversao_valor(cotacao, valor)
        valor_conversao = dolar_conversao

        cotacao_formatada = f"${valor} em reais são: R${dolar_conversao:.2f}"
        
        historico.append(cotacao_formatada)

        total_usd += dolar_conversao
        contagem_conversao += 1
        continue

#Conversao em EURO
    if opcao == 2:
        moeda = "EUR"
        cotacao = cotacao_moeda(moeda)

        valor = float(input("Quantos euros deseja converter em reais? €"))
        euro_conversao = conversao_valor(cotacao, valor)
        valor_conversao = euro_conversao

        cotacao_formatada = f"€{valor} em reais são: R${euro_conversao:.2f}"
        
        historico.append(cotacao_formatada)

        total_eur += euro_conversao
        contagem_conversao += 1
        continue

#Resumo
    if opcao == 3:

        print(f"\nO valor total convertido foi de : R${total_conversao:.2f}")
        print(f"A maior conversão de valor foi de: R${maior_conversao:.2f}")
        print(f"Foram feitas {contagem_conversao} conversões ao total! \n")
        print(f"{historico}\n")
        continue

    if opcao == 0:
        print("Saindo...")
        break

    #fazer funçao para atualizar valor
    #finalizar historico em dicionario