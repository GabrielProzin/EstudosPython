'''
🔴 26.3 – Difícil: Bot que monitora o preço periodicamente

Bibliotecas:

import time
import requests

Conceitos importantes:

laço “infinito” com condição de saída
time.sleep() para verificar de tempos em tempos
combinação de API + lógica + automação simples

Crie um bot que:

Pergunte:
preço alvo
intervalo de verificação (em segundos)

A cada X segundos:

busque o preço atual (API)
mostre hora da checagem e o preço
se o preço for ≤ alvo, mostrar uma mensagem de ALERTA bem destacada
Permita sair do loop se o usuário digitar algo como CTRL+C (óbvio) ou, se quiser ser chique, você pode checar um comando tipo "sair" em algum momento.
'''
#https://open.er-api.com/v6/latest/

import time
import requests

def buscar_cotacao(moeda):
    url = f"https://open.er-api.com/v6/latest/{moeda}"
    response = requests.get(url)
    dados = response.json()
    return dados["rates"]["BRL"]

print("\n---Sistema de alerta de preços!---")

valor = float(input("Digite o valor da moeda: "))
moeda = input("Digite a moeda em (USD - EUR)").upper()

while True:

    cotacao = buscar_cotacao(moeda)
    hora = time.strftime("%H:%M")
    print(
        f"{hora} - Preço atual: {cotacao:.2f}\n Preço desejado: {valor:.2f}"
          )
    if cotacao <= valor:
        print("!!!O VALOR ESTÁ ABAIXO DO DESEJADO!!!")
        time.sleep(5)
    else:
        print("!!!O VALOR ESTÁ ACIMA DO DESEJADO!!!")
        time.sleep(5)
        continue   