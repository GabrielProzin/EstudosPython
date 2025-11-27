'''
🟡 16.2 – Convertendo CSV → JSON (intermediário)

Usando o mesmo alunos.csv (ou um maior, se quiser), crie um programa que:

Leia o CSV.
Construa uma lista de dicionários no formato:

[
    {"nome": "Ana", "nota": 8.5},
    {"nome": "Carlos", "nota": 6.0},
    ...
]

Salve essa lista em um arquivo alunos.json usando o módulo json.
Mostre uma mensagem tipo: “Arquivo alunos.json gerado com sucesso.”

Requisitos:

Usar csv.DictReader (para já vir com chaves).
Usar json.dump(..., indent=4) para deixar bonito.
'''