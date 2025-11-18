#2.3 — Desafiador (Cenário real):
#Imagine que você é responsável por um sistema de cadastro simples.
#Crie variáveis representando um usuário:

#nome
#ano_nascimento
#cidade
#saldo_bancario (float)
#possui_cartao (bool)

#Depois calcule automaticamente a idade dele (assuma que estamos em 2025).
#Mostre tudo formatado.

nome = input("Digite seu nome: ")
ano_nascimento = int(input("Digite o ano de nascimento: "))
cidade = input("Digite o nome da cidade: ")
saldo_bancario = float(input("Digite o seu saldo bancário: "))
possui_cartao = True

idade = 2025 - ano_nascimento

print(f"Seu nome é {nome}, seu ano de nascimento é {ano_nascimento}, logo a sua idade é {idade}, saldo bancário: R${saldo_bancario} reais, possui cartão: {possui_cartao}")

'''
CORREÇÕES // MELHORIAS

🔧 Melhorias

-Separar as linhas do print fica mais organizado
-possui_cartao = True poderia ser variável recebida pelo usuário
-Valores monetários poderiam ter formatação melhor
-idade poderia ser calculada com ano atual automático usando módulo datetime (mas isso é pra frente)


nome = input("Nome: ")
ano_nascimento = int(input("Ano de nascimento: "))
cidade = input("Cidade: ")
saldo = float(input("Saldo bancário: "))

possui_cartao = True
idade = 2025 - ano_nascimento

print(
    f"Nome: {nome}\n"
    f"Idade: {idade}\n"
    f"Cidade: {cidade}\n"
    f"Saldo bancário: R${saldo:.2f}\n"
    f"Possui cartão: {possui_cartao}"
)


'''