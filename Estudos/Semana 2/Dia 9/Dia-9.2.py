'''
🟡 Intermediário — Cadastro em dicionário
Crie um dicionário com as seguintes chaves:
pessoa = {
    "nome": "",
    "idade": 0,
    "cidade": ""
}
O programa deve:

Preencher cada chave com input()
Exibir o dicionário completo
Mostrar todas as chaves usando .keys()
Mostrar todos os valores usando .values()
Exibir as duplas (chave, valor) usando .items()
'''

pessoa = {}
pessoa["nome"] = input("Digite o nome da pessoa: ")
pessoa["idade"] = input("Digite a idade: ")
pessoa["cidade"] = input("Digite o nome da cidade: ")
print(pessoa)

print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())