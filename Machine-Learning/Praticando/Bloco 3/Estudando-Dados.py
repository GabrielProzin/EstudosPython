'''
🔗 BLOCO 3 — Relações entre variáveis (começa a pensar como ML)

Músicas explícitas tendem a ser mais populares ou menos populares?

A duração da música influencia a popularidade?

Existe correlação entre:

duração × popularidade?

popularidade do artista × popularidade da música?

Músicas muito longas são menos populares?

Músicas muito curtas são menos populares?

👉 Objetivo: pensar em padrões
'''

import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv("Machine-Learning/spotify_data clean.csv")

musicas_explicitas = dados.groupby("explicit")["track_popularity"].mean()
print(musicas_explicitas)

duracao_media = dados["track_duration_min"].mean()
print(f"{duracao_media:.2f}")


print(dados["track_duration_min"].describe())

plt.scatter(
    dados["track_duration_min"],
    dados["track_popularity"],
    alpha=0.3
)
plt.xlabel("Duração (min)")
plt.ylabel("Popularidade")
plt.show()