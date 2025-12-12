'''
🔴 26.3 – Difícil: Bot que monitora o preço periodicamente

Bibliotecas:

import time

import requests

Conceitos importantes:

laço “infinito” com condição de saída

time.sleep() para verificar de tempos em tempos

combinação de API + lógica + automação simples

Enunciado:
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