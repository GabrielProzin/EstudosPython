'''
🟡 20.2 – Planilha de alunos com Pandas + CSV (intermediário)

Use um arquivo alunos_notas.csv com colunas:

nome
nota1
nota2
nota3

Seu script deve:

Ler o CSV com Pandas.
Calcular a média e criar coluna media.
Salvar apenas nome e media em um novo CSV medias.csv.
Gerar um arquivo de texto aprovados.txt só com nomes dos alunos que tiveram média ≥ 7.
'''

import pandas as pd

medias = {}

with open("notas_alunos.csv", "r", encoding="utf-8") as file:
    dados = pd.read_csv(file)

    dados["media"] = ((dados["nota1"] + dados["nota2"] + dados["nota3"]) / 3).round(1)
    media = dados[["nome", "media"]]

print(media)

media.to_csv("medias.csv", index=False)

aprovados = []

with open("medias.csv", "r") as file:
    medias = pd.read_csv(file)

    for indice, linha in medias.iterrows():
        nome = linha["nome"]
        media = linha["media"]
        if media >= 7:
            aprovados.append(nome)
        with open("aprovados.txt", "w") as file:
            for aluno in aprovados:
                file.write(aluno + "\n")

print(aprovados)


