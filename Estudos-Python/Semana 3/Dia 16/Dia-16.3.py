'''
16.3 – Fusão de dados CSV + JSON (difícil)

Suponha que você tenha:

Um arquivo alunos_notas.csv:

id,nome,nota
1,Ana,8.5
2,Carlos,6.0
3,João,4.7

E um arquivo alunos_info.json com:

[
    {"id": 1, "email": "ana@email.com"},
    {"id": 2, "email": "carlos@email.com"},
    {"id": 3, "email": "joao@email.com"}
]

Seu programa deve:

Ler o CSV e o JSON.
“Juntar” as informações pelo campo id.
Gerar um terceiro arquivo alunos_completo.json com objetos assim:

{
    "id": 1,
    "nome": "Ana",
    "nota": 8.5,
    "email": "ana@email.com"
}

Requisitos:

Usar dicionários para mapear por id.
Tratar se algum id existir em um arquivo e não no outro (por exemplo, pular ou marcar "email": null).
'''

import csv
import json

alunos_csv = []
alunos_json = []
mapa_json = {}
alunos_completo_json = []

with open("alunos_notas.csv", "r", encoding="utf-8") as arquivo_csv:
    leitor_arquivo_csv = csv.DictReader(arquivo_csv)

    for linha in leitor_arquivo_csv:
        alunos_csv.append({"id": int(linha["id"]), "nome": linha["nome"], "nota": linha["nota"]})
print("csv:", alunos_csv)

with open("alunos_info.json", "r", encoding="utf-8") as arquivo_json:
    leitor_arquivo_json = json.load(arquivo_json)

    for linha in leitor_arquivo_json:
        mapa_json[linha["id"]] = linha["email"]
print("json:", mapa_json)

for aluno in alunos_csv:
    id_atual = aluno["id"]

    alunos_completo_json.append({
        "id": id_atual,
        "nome": aluno["nome"],
        "nota": aluno["nota"],
        "email": mapa_json.get(id_atual, None)
    })


with open("alunos_completo.json", "w", encoding="utf-8") as alunos_completo:
    json.dump(alunos_completo_json, alunos_completo, indent=4)

print("Arquivo alunos_completo.json criado com sucesso!")