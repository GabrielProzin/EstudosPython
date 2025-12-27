'''
🟢 NÍVEL FÁCIL — “Entender os dados antes da IA”

📌 Conceito trabalhado

Análise exploratória
Relação entre variável e resultado
“A IA só aprende o que os dados mostram”

Exercícios práticos

Criar gráficos para:

horas_estudo × passou
faltas × passou
estresse × passou

Para cada gráfico, responder:

Existe padrão claro?
Onde há mistura (0 e 1 juntos)?

🧠 O que você aprende

Nem toda variável é igualmente importante
Onde o modelo provavelmente vai errar
✔ Aqui não tem ML ainda, só pensamento crítico
✔ Isso já é parte essencial de IA
'''

import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv("Estudos-Python/Arquivos_Gerados/CSV/alunos_desempenho.csv")
#print(dados)

# plt.scatter(dados["horas_estudo"], dados["passou"])
# plt.xlabel("horas de estudo")
# plt.ylabel("passou (0 = não, 1 = sim)")
# plt.yticks([0, 1])
# plt.show()
# Os alunos começam a passar a partir de 5hrs de estudo
# Os 0 e 1 se misturam entre 5 e 7 horas de estudo

# plt.scatter(dados["faltas"], dados["passou"])
# plt.xlabel("Faltas")
# plt.ylabel("Passou")
# plt.show()
# Alunos que tiveram mais que 6 faltas não passaram
# Os 0 e 1 se misturam entre 3 e 5 faltas

# plt.scatter(dados["estresse"], dados["passou"])
# plt.xlabel("Estresse")
# plt.ylabel("Passou")
# plt.show()
# Alunos que tiveram o nivel de estresse 6 ou abaixo passaram
# Os 0 e 1 se misturam somente no nivel 6 de estresse