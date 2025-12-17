'''
🟢 24.1 – Fácil: Abrir automaticamente um site no navegador

Bibliotecas:

import webbrowser

Conceitos importantes:

webbrowser.open()

automação simples (abrir URL com código)

Enunciado:
Crie um script que:

Pergunte ao usuário qual site ele quer abrir (ex: https://www.google.com).

Abra o site automaticamente no navegador padrão usando webbrowser.open().
'''

import webbrowser

site = input("Coloque o link do site que deseja abrir: ")

webbrowser.open(site)