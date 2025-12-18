'''
🟠 25.2 – Médio: Conversor usando API (USD/EUR → BRL)

Bibliotecas:

import requests

Conceitos importantes:

juntar lógica + API
separar código em funções (obter_cotacao(moeda), converter(moeda, valor))

Monte um menu:

1 - Converter USD → BRL
2 - Converter EUR → BRL
0 - Sair

Ao escolher 1 ou 2:

busque a cotação na API
peça o valor
exiba o resultado formatado com 2 casas decimais.
'''
#https://open.er-api.com/v6/latest/

import requests

def obter_cotacao(moeda):
    url = f"https://open.er-api.com/v6/latest/{moeda}"
    response = requests.get(url)
    dados = response.json()
    return dados["rates"]["BRL"]
    
def converter(cotacao, valor):
    return valor * cotacao

while True:
    print("Escolha alguma das seguintes opções do menu: \n")
    print("1 - Converter USD → BRL")
    print("2 - Converter EUR → BRL")
    print("0 - Sair")
    opcao = int(input(": "))

    if opcao == 1:
        moeda = "USD"
        valor = float(input("Digite quantos dolares deseja converter: "))
        cotacao = obter_cotacao(moeda)
        conversao = converter(valor, cotacao)
        print(f"{valor} dolares convertido são R${conversao:.2f} reais")

    if opcao == 2:
        moeda = "EUR"
        valor = float(input("Digite quantos euros deseja converter: "))
        cotacao = obter_cotacao(moeda)
        conversao = converter(valor, cotacao)
        print(f"{valor} euros convertido são R${conversao:.2f} reais")
    
    if opcao == 0:
        print("Saindo...")
        break