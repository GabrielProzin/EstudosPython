#📘 DIA 2 – Variáveis e Tipos de Dados (int, float, str, bool)
#2.1 — Básico:
#Crie 4 variáveis representando informações suas:

#nome
#idade
#altura

#está_estudando_python (True ou False)
#Depois exiba todas usando uma única linha de código.

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
altura = int(input("Digite a sua altura em centímetros: "))
esta_estudando_python = True

print(f"Eu me chamo {nome}, tenho {idade} anos e tenho {altura} centímetros de altura, e {esta_estudando_python}")


'''
CORREÇÕES // MELHORIAS

🔧 Melhorias opcionais

-altura deveria ser float e não int, para permitir valores como 175.5
-O booleano esta_estudando_python poderia ser exibido de forma mais amigável
-Pode colocar tudo em uma única linha de input se quiser simplificar

nome = input("Nome: ")
idade = int(input("Idade: "))
altura = float(input("Altura (cm): "))

esta_estudando_python = True

print(f"{nome}, {idade} anos, {altura} cm de altura — estudando Python: {esta_estudando_python}")


'''
