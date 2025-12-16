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

while True:
    moeda = input("Digite a moeda: ")
    url = f"https://open.er-api.com/v6/latest/{moeda}"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:

            dados = response.json()
            cotacao = dados["rates"]["BRL"]
            
            if dados["result"] == "error":

                print("Digite uma moeda valida!")

            else:
                if moeda in dados["rates"]:

                    valor = input("Digite o valor: ")
                    conversao = converter_valor(valor, cotacao)
                else:
                    print(f"A moeda {moeda} não existe na cotação!")
        else:
            print(f"Código erro: {response}")    
    except KeyError:
        print("A moeda é somente letras!")