import pandas as pd

# 1️⃣ Criando o dataset
dados = {
    'horas_estudo': [1, 2, 3, 4, 5, 6, 7, 8],
    'faltas': [6, 5, 4, 3, 2, 2, 1, 0],
    'passou': [0, 0, 0, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(dados)

# 2️⃣ Separando entradas (X) e saída (y)
X = df[['horas_estudo', 'faltas']]
y = df['passou']

# 3️⃣ Separando dados de treino e teste
from sklearn.model_selection import train_test_split

X_treino, X_teste, y_treino, y_teste = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# 4️⃣ Criando o modelo de IA
from sklearn.linear_model import LogisticRegression

modelo = LogisticRegression()

# 5️⃣ Treinando o modelo
modelo.fit(X_treino, y_treino)

# 6️⃣ Fazendo previsões
previsoes = modelo.predict(X_teste)

# 7️⃣ Avaliando o modelo
from sklearn.metrics import accuracy_score

acuracia = accuracy_score(y_teste, previsoes)

print("Previsões:", previsoes.tolist())
print("Respostas reais:", y_teste.tolist())
print("Acurácia:", acuracia)
