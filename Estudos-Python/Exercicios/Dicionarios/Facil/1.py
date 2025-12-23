'''
1. Cadastro simples

Crie um dicionário representando uma pessoa com as chaves:
nome, idade, cidade.
Depois, altere a idade e imprima o dicionário atualizado.
'''
lista_pessoas = []


for n in range(2):
    pessoa = {}
    pessoa["nome"] = input("Digite o nome da pessoa: ")
    pessoa["idade"] = int(input("Digite a idade: "))
    pessoa["cidade"] = input("Digite o nome da cidade: \n")
    lista_pessoas.append(pessoa)

alterarNome = input("Qual nome você deseja alterar? ")

encontrado = False

for dicionario in lista_pessoas:
    if dicionario["nome"] == alterarNome:
        dicionario["nome"] = input("Digite o novo nome: ")
        encontrado = True
        break

if not encontrado:
    print("pessoa não encontrada!")