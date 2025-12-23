'''
🟠 24.2 – Médio: Puxar HTML de uma página e mostrar o título

Bibliotecas:

import requests

(opcional) from bs4 import BeautifulSoup (se você quiser usar parsing de HTML)

Conceitos importantes:

automação via código sem precisar abrir o navegador
pegar HTML com requests.get()
encontrar uma informação dentro do HTML (por exemplo, <title>)

Enunciado:

Peça ao usuário uma URL.
Faça uma requisição com requests.

Mostre:

o status code
o tamanho do conteúdo (len do response.text)
(Opcional mais avançado) Se usar BeautifulSoup, extraia e mostre o <title> da página.
'''

import requests
from bs4 import BeautifulSoup

url = input("Digite o URL de algum site: ")

response = requests.get(url)

print(response.status_code)
html = response.text
print("Tamanho do conteúdo: ", len(html))

soup = BeautifulSoup(response.text, "html.parser")

if soup.title:
    print("O conteúdo dentro do title é:", soup.title.text)
else:
    print("Title não encontrado!")