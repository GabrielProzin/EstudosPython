'''
🔴 24.3 – Difícil: Mini-robô que verifica um site periodicamente

Bibliotecas:

import time
import requests

Conceitos importantes:

laços com while True
time.sleep() para pausar o script
automação: verificar algo de tempos em tempos

Crie um script que:

Pergunte uma URL para monitorar.
A cada 30 segundos:
faça uma requisição para essa URL
mostre o horário da verificação e o status code
Se o status code for diferente de 200, exiba um alerta em destaque na tela.
(Depois você pode parar o script manualmente com CTRL+C.)
'''

import time
import requests

url = input("Digite qual url deseja monitorar: ")

while True:
    response = requests.get(url)
    status = response.status_code
    if status != 200:
        print("Algo na requisição deu errado!")
        break
    print(f"Horário de verificação: {time.strftime("%H:%M:%S")}, status code: {status}")
    time.sleep(30)