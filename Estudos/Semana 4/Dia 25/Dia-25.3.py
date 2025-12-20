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

def montar_historico(moeda, valor, valor_convertido):
    resumo["moeda"] = moeda
    resumo["valor_original"] = valor
    resumo["valor_convertido"] = valor_convertido
    return resumo

historico = []
resumo = {}

contagem_conversao = 0

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

#Conversao em DOLAR
    if opcao == 1:
        moeda = "USD"
        cotacao = cotacao_moeda(moeda)

        valor = float(input("Quantos dolares deseja converter em reais? $"))
        valor_convertido = conversao_valor(cotacao, valor)
        valor_comparativo = valor_convertido

        if valor_comparativo > maior_conversao:
            maior_conversao = valor_comparativo

        cotacao_formatada = f"${valor} em reais são: R${valor_convertido:.2f}"
        
        historico.append(montar_historico(moeda, valor, valor_convertido))

        #historico.append(cotacao_formatada)

        total_conversao += valor_convertido
        contagem_conversao += 1
        continue

#Conversao em EURO
    if opcao == 2:
        moeda = "EUR"
        cotacao = cotacao_moeda(moeda)

        valor = float(input("Quantos euros deseja converter em reais? €"))
        valor_convertido = conversao_valor(cotacao, valor)
        valor_comparativo = valor_convertido

        if valor_comparativo > maior_conversao:
            maior_conversao = valor_comparativo

        cotacao_formatada = f"€{valor} em reais são: R${valor_convertido:.2f}"
        
        historico.append(montar_historico(moeda, valor, valor_convertido))

        #historico.append(cotacao_formatada)

        total_conversao += valor_convertido
        contagem_conversao += 1
        continue

#Resumo
    if opcao == 3:

        print(f"\nO valor total convertido foi de : R${total_conversao:.2f}")
        print(f"A maior conversão de valor foi de: R${maior_conversao:.2f}")
        print(f"Foram feitas {contagem_conversao} conversões ao total! \n")

        for indice in enumerate(historico):
            print(f"{historico}\n")

        #print(f"{historico}\n")
        continue

    if opcao == 0:
        print("Saindo...")
        break

    #finalizar historico em dicionario