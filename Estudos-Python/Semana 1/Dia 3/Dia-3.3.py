#3.3 — Desafiador:
#Faça um “simulador de aprovação”:
#Peça 3 notas de um aluno.

#Calcule a média.
#O aluno está aprovado se:

#média >= 7 e nenhum valor é 0

#Mostre:

#Média final: X
#Aprovado: True/False

nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))

media = int((nota1 + nota2 + nota3) /3)

aprovado = (media >= 7) and (nota1 != 0 and nota2 != 0 and nota3 != 0)

print(f"media final é {media}")
print(f"aprovado: {aprovado}")