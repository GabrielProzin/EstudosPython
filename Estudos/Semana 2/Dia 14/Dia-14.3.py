'''
🔴 Difícil — Mini-sistema de notas escolares
Crie um sistema que:

Cadastra N alunos

Para cada aluno:

nome
3 notas

Use funções:

calcular_media()
situacao() → retorna “Aprovado”, “Recuperação”, “Reprovado”
Armazene tudo em uma lista de dicionários

Exiba um boletim final no estilo:
--- BOLETIM FINAL ---
Ana - média 8.3 - Aprovada
Carlos - média 6.0 - Recuperação
João - média 4.7 - Reprovado
'''

alunos = []

def cadastrar_aluno(nome, nota1, nota2, nota3):
    return {
        "nome": nome,
        "nota1": nota1,
        "nota2": nota2,
        "nota3": nota3
    }

while True:
    print("Escolha alguma das seguintes opções: \n")
    print("1 - Cadastrar aluno")
    print("2 - finalizar cadastros")
    opcao = int(input(": "))

    if opcao == 1:
        nome = input("Digite o nome do aluno: ")
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        nota3 = float(input("Digite a terceira nota: "))

        alunos.append(cadastrar_aluno(nome, nota1, nota2, nota3))

