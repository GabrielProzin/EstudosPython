'''
🟡 Intermediário — Calculadora com exceções
Crie uma calculadora que:

Pede dois números
Pede a operação (+, -, *, /)

Usa try/except para:

evitar erro de divisão por zero
evitar erro ao digitar letras
Continua pedindo até o usuário digitar “sair”
'''

n1 = 0
n2 = 0

while True:
    try:
        n1 = int(input("Digite um número: "))
        n2 = int(input("Digite outro número: "))
    except ValueError:
        print("Digite apenas números!")

    print("Escolha alguma das seguintes opções: \n")
    print("1 - somar")
    print("2 - subtrair")
    print("3 - multiplicar")
    print("4 - dividir")
    print("5 - sair")

    try:
        opcao = int(input(": "))

        if opcao == 1:
            resultado = n1 + n2
            print(resultado)
        if opcao == 2:
            resultado = n1 - n2
            print(resultado)
        if opcao == 3:
            resultado = n1 * n2
            print(resultado)
        if opcao == 4:
            resultado = n1 / n2
            print(resultado)
        if opcao == 5:
            break

    except ValueError:
        print("Escolha as opções de 1 a 5!")
    except ZeroDivisionError:
        print("Não é possível dividir um número por 0!")


    