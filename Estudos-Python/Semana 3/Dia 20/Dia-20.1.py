'''
🔁 DIA 20 – Revisão prática
🟢 20.1 – Resumo de estudos (básico)

Crie um script que:

Tenha um arquivo estudos.txt com linhas no formato:
2025-01-15;Python;2 (data; assunto; horas)

Leia o arquivo e mostre na tela um resumo:

Total de registros: X
Total de horas estudadas: Y
'''

horasSomadas = 0
contagemLinha = 0

with open("estudos.txt", "r", encoding="utf-8") as file:
    for linha in file:
        linha = linha.strip()
        partes = linha.split(";")

        if not linha:
            continue
        
        horaConvertida = float(partes[2])
        horasSomadas += horaConvertida
        contagemLinha +=1

print("Total de horas estudadas:", horasSomadas)
print("Total de registros:", contagemLinha)

    