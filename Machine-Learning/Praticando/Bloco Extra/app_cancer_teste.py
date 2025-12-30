import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# =========================
# Título
# =========================
st.title("Classificação simples - Câncer de Mama")
st.write("Exemplo didático usando CSV + scikit-learn + Streamlit")

# =========================
# Carregar CSV
# =========================
df = pd.read_csv("data.csv")

# =========================
# LIMPEZA CORRETA DOS DADOS
# =========================

# Remover coluna lixo (100% NaN)
df = df.drop(columns=["Unnamed: 32"])

# Remover ID (não serve para ML)
df = df.drop(columns=["id"])

# Converter diagnóstico
# M = maligno (0), B = benigno (1)
df["diagnosis"] = df["diagnosis"].map({"M": 0, "B": 1})

# =========================
# Separar features e target
# =========================
X = df.drop(columns=["diagnosis"])
y = df["diagnosis"]

# =========================
# Treinar modelo simples
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

modelo = LogisticRegression(max_iter=1000)
modelo.fit(X_train, y_train)

# =========================
# Interface
# =========================
st.subheader("Simulação de um novo tumor")

radius_mean = st.slider(
    "Radius (mean)",
    float(X["radius_mean"].min()),
    float(X["radius_mean"].max()),
    float(X["radius_mean"].mean())
)

texture_mean = st.slider(
    "Texture (mean)",
    float(X["texture_mean"].min()),
    float(X["texture_mean"].max()),
    float(X["texture_mean"].mean())
)

# =========================
# Previsão
# =========================
if st.button("Analisar tumor"):

    # Criar entrada válida (sem NaN)
    novo_tumor = pd.DataFrame(
        [X.mean().values],
        columns=X.columns
    )

    novo_tumor["radius_mean"] = radius_mean
    novo_tumor["texture_mean"] = texture_mean

    resultado = modelo.predict(novo_tumor)

    if resultado[0] == 1:
        st.success("Resultado: Tumor BENIGNO (B)")
    else:
        st.error("Resultado: Tumor MALIGNO (M)")
