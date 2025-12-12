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