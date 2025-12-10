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
import matplotlib.pyplot as plt

produto_digitado = input("Digite o nome do produto:")

with open("vendas_completo.csv", "r", encoding="utf-8") as file:
    vendas = pd.read_csv(file)

    filtro = vendas[vendas["produto"] == produto_digitado]

    filtro["total"] = filtro["quantidade"] * filtro["preco_unitario"]
    total = filtro["total"].sum()
    print(f"O total de vendas foi de: R${total}")

    quantidade_total = filtro["quantidade"].sum()
    print(f"A quantidade total vendida foi de: {quantidade_total} produtos")

    ticket_medio = total / quantidade_total
    print(f"O ticket médio é de: R${ticket_medio:.2f}")

    filtro["data"] = pd.to_datetime(filtro["data"])
    filtro["mes"] = filtro["data"].dt.month
    vendas_mes = filtro.groupby("mes")["quantidade"].sum()
    print(vendas_mes)

plt.plot(vendas_mes.index, vendas_mes.values)
plt.title(produto_digitado)
plt.xlabel("Mês")
plt.ylabel("Vendas")
plt.show()

plt.savefig(f"relatorio_{produto_digitado}.png")

filtro.to_csv(f"vendas_{produto_digitado}.csv")
