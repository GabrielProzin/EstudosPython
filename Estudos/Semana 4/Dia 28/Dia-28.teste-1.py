import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

dados = pd.read_csv("alunos_desempenho.csv")

resultado = dados["passou"].value_counts()
aulas_assistidas = dados["assistiu_aulas"].value_counts()
horas_estudadas = dados["horas_estudo"].value_counts()
quantidade_faltas = dados["faltas"].value_counts()


pd.crosstab(dados["horas_estudo"], dados["passou"]).plot(kind="bar", figsize=(10,6), color=["salmon", "lightblue"])
plt.xlabel("Horas estudadas")
plt.ylabel("Aprovação")
plt.show()




# print(resultado)
# print(aulas_assistidas)
# print(horas_estudadas)
# print(quantidade_faltas)