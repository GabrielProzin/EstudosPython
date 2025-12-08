'''
🔴 21.3 – Relatório completo com filtros (difícil)

Com mesmo vendas_produtos.csv, crie um script interativo que:

Pergunta ao usuário um produto ou categoria (se tiver essa coluna).
Filtra o DataFrame apenas para esse critério.

Mostra:

total de vendas;
quantidade total vendida;
ticket médio (valor_total / quantidade).
Gera um gráfico de linha mostrando a evolução das vendas ao longo do tempo (por mês).

Salva:

gráfico com nome relatorio_<produto>.png;
CSV filtrado como vendas_<produto>.csv.
'''

import pandas as pd

mostrar_produtos  = []
produto_digitado = input("Digite o nome do produto:")