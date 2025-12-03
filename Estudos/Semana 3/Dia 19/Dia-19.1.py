'''
📈 DIA 19 – Visualização com Matplotlib
🟢 19.1 – Gráfico de linha simples (básico)

Crie um gráfico de linha com:

eixo X: dias da semana (["Seg", "Ter", ...])
eixo Y: horas estudadas por dia

Tarefas:

Criar as listas com dias e horas.
Plotar um gráfico de linha.
Adicionar título, rótulos dos eixos (xlabel, ylabel).
'''

import matplotlib.pyplot as plt

dias = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"]
horas = [1, 2, 0, 3, 2.5, 4, 1.5]

plt.plot(dias, horas)
plt.title("Horas de estudo")
plt.xlabel("Horas")
plt.ylabel("Dias da semana")
plt.show()