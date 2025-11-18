#Crie um programa chamado Ficha do Aluno:

#Peça:

#nome
#idade
#nota1
#nota2
#nota3
#Calcule a média

#Determine a situação:
#média >= 7 → Aprovado  
#5 <= média < 7 → Recuperação  
#< 5 → Reprovado

#Exiba um relatório assim:

#FICHA DO ALUNO
#Nome: Ana Souza
#Idade: 19
#Média: 6.3
#Situação: Recuperação

nome = input("Digite o nome do aluno: ")
idade = int(input("Digite a idade do aluno: "))
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    aprovacao = str('Aprovado!')
if 5 <= media < 7:
    aprovacao = str('Recuperação!')
if media < 5:
    aprovacao = str('Reprovado!')

print(f"FICHA DO ALUNO \n Nome: {nome} \n Idade: {idade} \n Média: {media} \n Situação: {aprovacao}")
