#7.2 — Revisão Intermediária:

#Crie um programa que:

#pede três números
#pergunta se quer “somar”, “multiplicar” ou “descobrir maior número”
#realiza a operação
#mostra o resultado

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

while True:
    operacao = input("Voce quer somar, multiplicar ou descobrir o maior número?")
    if operacao == 'somar':
        resultadoSomar = n1 + n2 + n3
        print(f"A soma dos três números é: {resultadoSomar}")
        break
    if operacao == 'multiplicar':
        resultadoMultiplicar = n1 * n2 * n3
        print(f"A multiplicação dos três números é: {resultadoMultiplicar}")
        break
    if operacao == 'maior número':
        if n1 > n2 and n1 > n3:
            print(f"O maior número dos três é: {n1}")
            break
        if n2 > n3:
            print(f"O maior número dos três é: {n2}")
            break
        else: 
            print(f"O maior número dos três é: {n3}")
            break


'''
CORREÇÕES // MELHORIAS

🔧 Melhorias:

Usuário precisa escrever exatamente “maior número”
→ Melhor padronizar para: “maior”
Pode transformar as opções em minúsculas para evitar erros
Você pode reduzir vários break repetidos


n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
n3 = int(input("Terceiro número: "))

while True:
    op = input("Você quer somar, multiplicar ou maior? ").lower()

    if op == "somar":
        print(n1 + n2 + n3)
        break

    elif op == "multiplicar":
        print(n1 * n2 * n3)
        break

    elif op == "maior":
        maior = n1
        if n2 > maior: maior = n2
        if n3 > maior: maior = n3
        print(f"O maior número é {maior}")
        break

    else:
        print("Opção inválida. Tente novamente.")



'''