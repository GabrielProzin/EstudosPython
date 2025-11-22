'''
📘 DIA 11 — Escopo e Retorno Múltiplo
🟢 Fácil — Variável global vs local

Crie:

uma variável global chamada contador = 0
uma função chamada incrementar() que:
cria uma variável local chamada contador = 10
imprime o valor local
No final, imprima o valor global

O objetivo é entender a diferença entre variáveis globais e locais.
'''


contador  = 0

def incrementar():
    contador = 10
    print(f"{contador}")
print(f"{contador}")

incrementar()