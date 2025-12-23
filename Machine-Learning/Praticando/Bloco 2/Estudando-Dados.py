'''
BLOCO 2 — Popularidade (muito importante)

Qual é a média de popularidade das músicas?

A distribuição da popularidade é:

concentrada?

espalhada?

enviesada para baixo?

Existem muitas músicas com popularidade 0?

Qual é o TOP 10 artistas com mais músicas no dataset?

Esses artistas também são os mais populares?

Existe artista com poucas músicas e alta popularidade?

👉 Objetivo: perceber que quantidade ≠ sucesso
'''

import pandas as pd

dados = pd.read_csv("Machine-Learning/spotify_data clean.csv")

media_popularidade = dados["artist_popularity"].mean()
print(f"A média de popularidade dos artistas é de: {media_popularidade:.2f}")