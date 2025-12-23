#📘 DIA 5 – Condicionais (if, elif, else)

#5.1 — Básico:

#Peça a idade e diga se é:

#menor de idade
#adulto
#idoso (60+)

idade = int(input("Digite a sua idade: "))

if idade < 18:
    print("voce é menor de idade")
elif idade >= 18 and idade <= 60:
    print("voce é maior de idade")
else:
    print("voce é idoso")


'''
CORREÇÕES // MELHORIAS

🔧 Melhoria

No segundo elif, você usou idade >= 18 and idade <= 60
Mas pode simplificar usando operador BETWEEN:


18 <= idade < 60


'''