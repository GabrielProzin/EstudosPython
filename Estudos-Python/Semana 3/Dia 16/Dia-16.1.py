'''
🟢 16.1 – Lendo um CSV simples (básico)

Crie um arquivo alunos.csv manualmente (no editor) com o conteúdo:

nome,nota
Ana,8.5
Carlos,6.0
João,4.7

Depois, escreva um programa que:
Leia esse CSV usando o módulo csv.
Para cada linha, imprima algo como:
Aluno Ana tirou 8.5

Requisitos:

Usar csv.reader.
Ignorar o cabeçalho (nome,nota).
'''

import csv

with open("alunos.csv", "r") as f:
    leitor = csv.reader(f)
    next(leitor)
    
    for linha in leitor:
        nome = linha[0]
        nota = linha[1]
        print(f"Aluno {nome} tirou {nota}")