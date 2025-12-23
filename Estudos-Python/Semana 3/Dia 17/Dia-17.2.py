'''
🟡 17.2 – Filtro de aprovados (intermediário)

Usando um DataFrame de alunos com colunas:

nome
nota1
nota2
nota3

Faça um programa que:

Leia os dados de um CSV (por exemplo notas_alunos.csv).
Crie uma coluna media com a média das 3 notas.
Crie uma coluna situacao com:

“Aprovado” se média ≥ 7
“Recuperação” se 5 ≤ média < 7
“Reprovado” se média < 5

Mostre:

Só os aprovados.
Só os reprovados.
Estatísticas gerais das médias (describe()).

Requisitos:

Usar operações vetoriais do Pandas (sem for se possível).
Salvar o resultado final em um CSV boletim_final.csv.
'''
import pandas as pd

with open("notas_alunos.csv", "r") as f:
    arquivo = pd.read_csv(f)
    arquivo["media"] = ((arquivo["nota1"] + arquivo["nota2"] + arquivo["nota3"]) / 3).round(1)

    arquivo.loc[arquivo["media"] >= 7, "situacao"] = "Aprovado"
    arquivo.loc[(arquivo["media"] >= 5) & (arquivo["media"] < 7), "situacao"] = "Recuperação"
    arquivo.loc[arquivo["media"] < 5, "situacao"] = "Reprovado"
print(arquivo[arquivo["situacao"] == "Aprovado"])
print("\n")
print(arquivo[arquivo["situacao"] == "Reprovado"])
print("\n")
print(arquivo.describe().round(1))
arquivo.to_csv("boletim_final.csv", index=False)
