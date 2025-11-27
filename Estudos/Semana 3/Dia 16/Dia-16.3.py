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