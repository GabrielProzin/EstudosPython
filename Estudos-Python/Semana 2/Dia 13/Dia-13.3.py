'''
🔴 Difícil — Sistema robusto de entrada

Crie uma função chamada ler_numero() que:

sempre retorna um número válido
deve ficar em loop até um número REAL ser digitado
só sai do loop quando a conversão para float funcionar
trate erros com try/except finally

Depois, use essa função para:

ler dois números
somá-los
exibir o resultado
'''
n1 = 0.0
n2 = 0.0

def ler_numero(n1 ,n2):
    resultado = n1 + n2
    print(f"A soma dos numeros eh: {resultado}")

while True:
    try:
        n1 = float(input("Digite um número: "))
        n2 = float(input("Digite outro número: "))
        break
    except ValueError:
        print("Digite somente numeros! \n" )

ler_numero(n1, n2)