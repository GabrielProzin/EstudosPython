'''
🐼 DIA 17 – Biblioteca Pandas
🟢 17.1 – DataFrame básico (básico)

Crie um script que:

Monte um DataFrame com 3 alunos, com colunas: nome, idade, nota.
Use df.head() para mostrar as primeiras linhas.
Use df.describe() para mostrar estatísticas (média, min, max da coluna nota e idade).

Requisitos:

Criar o DataFrame a partir de um dicionário Python.
'''

import pandas as pd

dados = {
    "Nome": ["Gabriel", "Jose", "Joao", "Ana", "Yas", "Yan"],
    "Idade": [21, 18, 20, 10, 60, 70],
    "Nota": [10, 9.5, 3.5, 5, 7, 8]
}

tabelaAlunos = pd.DataFrame(dados)
print(tabelaAlunos.head(3))
print(tabelaAlunos.describe())