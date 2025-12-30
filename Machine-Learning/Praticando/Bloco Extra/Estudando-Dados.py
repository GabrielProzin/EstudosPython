'''
🎯 BLOCO 5 — Pensamento de ML (sem ML ainda)

Se você fosse prever popularidade:

isso seria regressão ou classificação?

Quais colunas você usaria como features?

Quais colunas você descartaria?

Você precisaria normalizar algum dado?

O problema parece simples ou complexo?

Você confia nesses dados para um modelo real?

👉 Objetivo: pensar como cientista de dados
'''

import streamlit as st
import pandas as pd

st.title("Análise de dados")

dados = pd.read_csv("spotify_data clean.csv")
print(dados)

st.write("Visualização dos dados:")
st.dataframe(dados.head())
