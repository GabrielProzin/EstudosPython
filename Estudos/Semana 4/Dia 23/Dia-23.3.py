'''
🔴 23.3 – Difícil: Conversor resiliente com tratamento de erros

Bibliotecas:

import requests

Conceitos importantes:

try/except para tratar:

erro de conexão
resposta com status code diferente de 200
validar a moeda digitada
laço para repetir até o usuário digitar sair

Enunciado:
Monte um conversor em loop:

O usuário digita uma moeda (USD ou EUR) ou "sair" para fechar o programa.
Se a moeda for inválida, mostrar mensagem de erro e pedir novamente.

Para uma moeda válida:

pedir o valor
buscar a cotação na API
mostrar o valor convertido
Tratar erros de rede para o programa não quebrar se a API cair.
'''

#https://open.er-api.com/v6/latest/

import requests

def converter_valor(valor, cotacao):
    return valor * cotacao

print("Conversor de moedas para BRL")

while True:
    moeda = input("Digite a moeda (USD ou EUR) ou 'sair' para fechar o programa: ").upper()

    if moeda == 'SAIR':
        break

    if moeda not in ["USD", "EUR"]:
        print("Moeda inválida! Digite USD ou EUR.\n")
        continue

    try:

        url = f"https://open.er-api.com/v6/latest/{moeda}"
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Erro de conexão da API: {response.status_code}\n")
            continue

        dados = response.json()

        if dados["result"] == "error":
            print("Erro na cotação da moeda. \n")

        valor = float(input("Digite o valor que deseja converter: "))

        url = f"https://open.er-api.com/v6/latest/{moeda}"
        
        
        cotacao = dados["rates"]["BRL"]

        valor_convetido = converter_valor(valor, cotacao)
        
        print(f"{valor_convetido:.2f}")

    except ValueError:
        print("Digite um valor númerico válido!")
