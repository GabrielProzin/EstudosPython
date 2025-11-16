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

#output:
#PS C:\Users\Gabriel Mendes\Desktop\EstudosPython> & "C:/Users/Gabriel Mendes/AppData/Local/Programs/Python/Python313/python.exe" "c:/Users/Gabriel Mendes/Desktop/EstudosPythonPS C:\Users\Gabriel Mendes\Desktop\EstudosPython> & "C:/Users/Gabriel Mendes/AppData/Local/Programs/Python/Python313/python.exe" "c:/Users/Gabriel Mendes/Desktop/EstudosPython/Estudos/Semana 1/Dia-2.3.py"
#Digite seu nome: gabriel
#Digite o ano de nascimento: 2004
#Digite o nome da cidade: goiania
#Digite o seu saldo bancário: 12301593
#Seu nome é gabriel, seu ano de nascimento é 2004, logo a sua idade é 21, saldo bancário: R$12301593.0 reais, possui cartão: True