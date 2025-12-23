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
valor = 0

def depositar(valor):
    global saldo
    saldo += valor
    print(f"Foi depositado R${valor} ao seu saldo!")
    return saldo

def sacar(valor):
    global saldo
    if valor <= saldo:
        saldo -= valor
        print(f"Foi retirado R${valor} do seu saldo!")
    else:
        print("O valor de sacar é maior que o seu saldo!")
    return saldo

def ver_saldo():

    return print(f"O valor do seu saldo é de: R${saldo}")

while True:
    print("Escolha alguma das seguintes opções: \n")
    print("1 - depositar \n")
    print("2 - sacar \n")
    print("3 - ver saldo \n")
    print("4 - sair \n")

    opcao = int(input(": "))
    if opcao == 1:
        valor = int(input("Digite o valor para depositar: "))
        depositar(valor)
    if opcao == 2:
        valor = int(input("Digite o valor em reais para sacar: "))
        sacar(valor)
    if opcao == 3:
        ver_saldo()
    if opcao == 4:
        break
