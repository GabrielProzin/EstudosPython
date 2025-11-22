'''
🔴 Difícil — Sistema de banco com saldo (escopo)
Crie:

Uma variável global saldo = 0

Funções:

depositar(valor) → aumenta o saldo
sacar(valor) → diminui o saldo (mas só se tiver dinheiro)
ver_saldo() → mostra o saldo

Use um while com opções:

depositar
sacar
ver saldo
sair

Use a palavra-chave global para modificar a variável global.
'''

saldo = 0

def depositar(valor):
    saldo += valor
    print(f"Foi depositado R${valor} ao seu saldo!")
    return saldo

def sacar(valor):
    if valor < saldo:
        saldo -= valor
        print(f"Foi retirado R${valor} do seu saldo!")
    else:
        print("O valor de sacar é maior que o seu saldo!")
    return saldo

def ver_saldo(saldo):
    print(f"O valor do seu saldo é de: R${saldo}")

while True:
    print("Escolha alguma das seguintes opções: \n")
    opcao = int(print("1 - depositar \n"))
    opcao = int(print("2 - sacar \n"))
    opcao = int(print("3 - ver saldo \n"))
    opcao = int(print("4 - sair \n"))
