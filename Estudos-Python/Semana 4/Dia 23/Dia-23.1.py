'''
🟢 23.1 – Fácil: Buscar e mostrar uma cotação simples

Bibliotecas:

import requests

Conceitos importantes:

requests.get()
response.status_code
response.json() (trabalhar com JSON)

Enunciado:

Use uma API pública de câmbio (por exemplo, uma que devolva USD/BRL).
Faça uma requisição GET.
Mostre na tela apenas a cotação atual do dólar em reais, algo como:
1 USD = 5.43 BRL


(Você pode escolher qualquer API gratuita; o importante é praticar requests + json.)
'''

#https://open.er-api.com/v6/latest/USD

import requests

url = "https://open.er-api.com/v6/latest/KZT"
response = requests.get(url)
print(response.status_code)
cotacao = response.json()
br = cotacao["rates"]["BRL"]
print(f"1 KZT = {br:.2f}")

print(cotacao)