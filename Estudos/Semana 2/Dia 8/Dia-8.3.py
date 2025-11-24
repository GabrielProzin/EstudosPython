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
contadorTarefas = 0

adicionarTarefa = input("Adicionar tarefa: ")
tarefas.append(adicionarTarefa)
contadorTarefas += 1

while True:
    evento = input("Você quer adicionar, remover, ver as tarefas ou sair? ")

    if evento.lower() == 'adicionar':
        adicionarTarefa = input("Digite o nome da tarefa: ")
        tarefas.append(adicionarTarefa)
        print(f"{adicionarTarefa} adicionado com sucesso!")
        print(tarefas)
        contadorTarefas += 1
        
    if evento.lower() == 'remover':
        removerTarefa = input("Digite o nome da tarefa que deseja remover: ")

        if removerTarefa in tarefas:
            tarefas.remove(removerTarefa)
            print(f"{removerTarefa} removido com sucesso!")
            print(tarefas)

        else:
            print("Tarefa não encontrada")

    if evento.lower() == 'ver':
        print(f"Essa é a sua lista de tarefas: {tarefas}")
    
    if evento.lower() == 'sair':
        print(f"Foi adicionado ao total {contadorTarefas} tarefas")
        break
    