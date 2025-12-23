'''
🟡 Intermediário — Função com dois retornos
Crie uma função chamada soma_media(a, b, c) que retorna:

a soma dos três números
a média dos três números

Depois exiba:
Soma: X
Média: Y
'''

def soma_medida(a, b, c):
   soma = 0
   soma = a + b + c 
   
   media = 0
   media = soma / 3

   return soma, media

   
    
a = int(input("Digite um numero: "))
b = int(input("Digite outro numero: "))
c = int(input("Digite mais um numero: "))

soma, media = soma_medida(a, b, c)

print(f"A soma dos numeros é: {soma}")
print(f"A media dos numeros é: {media}")