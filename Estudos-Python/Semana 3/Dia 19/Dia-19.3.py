'''
🔴 19.3 – Comparação de vendas por mês (difícil)

Com duas listas:

meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"]
vendas_2024 = [1000, 1200, 900, 1500, 1700, 1600]
vendas_2025 = [1100, 1300, 950, 1550, 1800, 1750]

Seu programa deve:

Plotar um gráfico de linhas mostrando as duas séries (2024 e 2025).

Adicionar:

título
legenda
grade leve (grid(True)).
Destacar o mês com maior venda em 2025 com uma anotação (plt.annotate).
'''

import matplotlib.pyplot as plt

meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"]
vendas_2024 = [1000, 1200, 900, 1500, 1700, 1600]
vendas_2025 = [1100, 1300, 950, 1550, 1800, 1750]

maior_venda = max(vendas_2025)

maior_valor = max(vendas_2025)
indice_maior = vendas_2025.index(maior_valor)

x_ponto = meses[indice_maior]
y_ponto = vendas_2025[indice_maior]


plt.plot(meses, vendas_2024, label="2024")
plt.plot(meses, vendas_2025, label="2025")
plt.annotate(
    "maior venda",
    xy=(x_ponto, y_ponto),
    xytext=(x_ponto, y_ponto + 100),
    arrowprops={"arrowstyle": "->"}
)
plt.legend()
plt.title("Vendas no mês")
plt.grid(True)

plt.show()