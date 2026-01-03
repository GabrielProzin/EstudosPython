'''
🟡 NÍVEL MÉDIO — “Treinar e avaliar o modelo”

📌 Conceitos trabalhados

Treino vs teste
Generalização
Acurácia

Exercícios práticos

Treinar o modelo com:

75% treino / 25% teste

Exibir:

previsões
valores reais
acurácia

Alterar test_size (ex: 0.2, 0.3) e observar:

a acurácia muda?

por quê?

🧠 O que você aprende

Resultado depende da divisão dos dados

Acurácia não é “verdade absoluta”

✔ Aqui você já está usando IA de verdade
'''

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

modelo = LogisticRegression()
data = load_breast_cancer()

x = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
modelo.fit(X_train, y_train)

previsao = modelo.predict(X_test)

print(f"acuracia: ", accuracy_score(y_test, previsao))
# X = data.data
# y = data.target
