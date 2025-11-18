'''
🔴 Difícil — Gerenciador de lista de tarefas

Crie um programa que simule um mini “To-do list”:
Comece com uma lista vazia tarefas = []

O usuário pode:

adicionar tarefa
remover tarefa
ver todas as tarefas
sair
Use um loop while que só para quando o usuário digitar “sair”
Se tentar remover uma tarefa que não existe, mostre uma mensagem:
“Tarefa não encontrada”
Ao final, exiba quantas tarefas foram adicionadas no total.
'''

tarefas = []

while True:
    evento = input("Adicione uma tarefa: ")
    if evento.lower() == 'adicionar':
        adicionarTarefa = input("Digite o nome da tarefa: ")
        tarefas.append(adicionarTarefa)
        print(f"{adicionarTarefa} adicionado com sucesso!")
        print("")
    elif evento.lower() == 'remover':
        removerTarefa = input("Digite o nome da tarefa que deseja remover")
        
