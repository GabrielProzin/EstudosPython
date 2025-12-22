'''
🟢 27.1 – Fácil: Ler um arquivo CSV e mostrar total gasto
Bibliotecas necessárias:

pandas as pd

Conceitos importantes:

read_csv()
acessar colunas do DataFrame
sum()

Crie (ou use) um arquivo gastos.csv contendo duas colunas:

categoria,valor
alimentação,50
transporte,20
lazer,35

No Python:

carregue o arquivo usando pandas.read_csv()
exiba o total gasto, somando todos os valores da coluna valor.
Exemplo esperado no terminal:
Total gasto: R$ 105.00
'''

import pandas as pd

dados = pd.read_csv("gastos.csv")

total = dados["valor"].sum()

print(f"Total gasto: R${total}:.2f")