'''
🔴 Difícil — Função que retorna múltiplos valores
Crie uma função chamada estatisticas(lista_numeros) que:

Recebe uma lista de números

Retorna:
maior número
menor número
média

Depois, no programa principal:

Peça 5 números ao usuário
Salve em uma lista
Chame a função e exiba os 3 resultados separados
'''

def estatisticas(lista_numeros):
    maior = lista_numeros[0]
    menor = lista_numeros[0]
    soma = 0

    for n in lista_numeros:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
        soma += n

    media = soma / len(lista_numeros)

    return maior, menor, media

lista_numeros = []

for n in range (0,5):
    numero = int(input("Digite um numero: "))
    lista_numeros.append(numero)
    
maior, menor, media = estatisticas(lista_numeros)

print(f"Lista digitada: {lista_numeros}")
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")
print(f"Média: {media}")
