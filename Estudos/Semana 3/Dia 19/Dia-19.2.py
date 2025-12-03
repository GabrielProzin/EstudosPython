'''
🟡 19.2 – Gráfico de barras de notas por aluno (intermediário)

Usando nomes de alunos e suas médias finais:

Lista de nomes: ["Ana", "Carlos", "João", "Maria"]
Lista de médias: [8.5, 6.0, 4.7, 9.2]

Seu programa deve:

Plotar um gráfico de barras.
Colocar título: Boletim da Turma
Rotacionar levemente os nomes, se necessário.

Opcional: destacar visualmente quem tirou média ≥ 7 (ex: anotação de texto acima da barra ou cores diferentes).
'''

import matplotlib.pyplot as plt

nomes = ["Ana", "Carlos", "João", "Maria"]
medias = [8.5, 6.0, 4.7, 9.2]

red = ["red"]

plt.bar(nomes, medias, color=red >= 7)
plt.title("Boletim da Turma")
plt.xticks(rotation=30)
plt.show()

