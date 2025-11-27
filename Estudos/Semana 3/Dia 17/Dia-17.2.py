'''
🟡 17.2 – Filtro de aprovados (intermediário)

Usando um DataFrame de alunos com colunas:

nome
nota1
nota2
nota3

Faça um programa que:

Leia os dados de um CSV (por exemplo notas_alunos.csv).
Crie uma coluna media com a média das 3 notas.
Crie uma coluna situacao com:

“Aprovado” se média ≥ 7
“Recuperação” se 5 ≤ média < 7
“Reprovado” se média < 5

Mostre:

Só os aprovados.
Só os reprovados.
Estatísticas gerais das médias (describe()).

Requisitos:

Usar operações vetoriais do Pandas (sem for se possível).
Salvar o resultado final em um CSV boletim_final.csv.
'''