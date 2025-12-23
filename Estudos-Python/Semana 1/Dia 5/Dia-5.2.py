#5.2 — Intermediário:

#Peça uma senha ao usuário.
#A senha correta é "Python123".

#Mostre “Acesso permitido” ou “Acesso negado”.

senha = str(input("Digite a senha: "))

if senha == 'Python123':
    print("Acesso permitido")
else:
    print("Acesso negado")



'''
CORREÇÕES // MELHORIAS

🔧 Pequena melhoria:

str() no input não é necessário
Tornar a comparação case-sensitive ou case-insensitive (opcional)


senha = input("Digite a senha: ")

if senha == "Python123":
    print("Acesso permitido")
else:
    print("Acesso negado")


'''