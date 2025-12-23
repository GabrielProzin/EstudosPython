'''
Quantas músicas existem no dataset?

Quantos artistas únicos existem?

Qual é a duração média das músicas?

Qual é a música mais curta? E a mais longa?

A maioria das músicas é curta, média ou longa?

Quantas músicas são explícitas (explicit = True)?

A maioria das músicas é explícita ou não?
'''

import pandas as pd

dados = pd.read_csv("Machine-Learning/spotify_data clean.csv")

musicas_totais = dados["track_id"].count()
print(musicas_totais)

artistas_unicos = dados["artist_name"].value_counts().count()
print(artistas_unicos)

duracao_media = dados["track_duration_min"].mean()
print(f"Duração média das músicas: {duracao_media:.2f}")

musica_curta = dados["track_duration_min"].min()
print(f"{musica_curta:.2f}")

musica_longa = dados["track_duration_min"].max()
print(f"{musica_longa:.2f}")

curtas = dados[dados["track_duration_min"] < 2.5].shape[0]
print(curtas)
medias = dados[(dados["track_duration_min"] >= 2.5) & (dados["track_duration_min"] < 4)].shape[0]
print(medias)
longas = dados[dados["track_duration_min"] > 4].shape[0]
print(longas)

if curtas > medias and curtas > longas:
    print(f"A maioria das músicas são curtas, com {curtas} músicas.")
elif medias > curtas and medias > longas:
    print(f"A maioria das músicas são médias, com {medias} músicas.")
else:
    print(f"A maioria das músicas são longas, com {longas} músicas.")

musicas_explicita = dados["explicit"].where(dados["explicit"] == True).count()
#print(musicas_explicita)

musicas_restantes = musicas_totais - musicas_explicita

if musicas_explicita > musicas_restantes:
    print(f"A maioria das músicas são explicitas \nQuantidade de músicas explicitas: {musicas_explicita}")
else:
    print(f"A maioria das músicas não são explicitas \nQuantidade de músicas não explicitas: {musicas_restantes}")