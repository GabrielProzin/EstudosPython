'''
3. Adicionar uma nova chave

Crie um dicionário com informações de um filme (título e ano).
Depois, adicione a chave “notaIMDb” com um valor numérico.
'''

filme = {"titulo": "", "ano": ""}

titulo = input("Digite o nome do filme")
ano = int(input("Digite o ano"))

filme.append(titulo)
print(filme)