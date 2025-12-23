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
import matplotlib.pyplot as plt

dados = pd.read_csv("Machine-Learning/spotify_data clean.csv")

media_popularidade = dados["track_popularity"].mean()
print(f"A média de popularidade das músicas é de: {media_popularidade:.2f}")

faixas = pd.cut(
    dados["track_popularity"],
    bins=[0, 10, 30, 40, 60, 100]
)

print(faixas.value_counts().sort_index())

print("De acordo com a distribuição, ela é enviesada para baixo.")

popularidade_0 = dados["artist_popularity"].where(dados["artist_popularity"] == 0).count()

print(f"Quantidade de artistas com popularidade 0: {popularidade_0}")

top_10 = dados["artist_name"].value_counts().head(10)
top_10_populares = dados.groupby("artist_name")["artist_popularity"].mean().sort_values(ascending=False).head(10)

print(f"\nOs top 10 artistas com mais músicas no dataset é:")
print(top_10)

print("\nOs top 10 artistas mais populares:")
print(top_10_populares)

#Existe artista com poucas músicas e alta popularidade?

resumo_artistas = dados.groupby("artist_name").agg(
    quantidade_musicas=("track_name", "count"),
    popularidade_media=("artist_popularity", "mean")
)

artistas_poucas_e_populares = resumo_artistas[
    (resumo_artistas["quantidade_musicas"] <= 10) &
    (resumo_artistas["popularidade_media"] >= 80)
]

print(artistas_poucas_e_populares.head(10))
print("Sim, existem!")