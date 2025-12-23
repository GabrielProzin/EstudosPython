'''
🟡 15.2 – Lista de tarefas com append (intermediário)

Crie um programa de lista de tarefas que:

Sempre escreva/adicione tarefas em um arquivo chamado tarefas.txt.
Mostre um pequeno menu:

1 - Adicionar tarefa
2 - Ver tarefas
3 - Sair

Ao escolher 1, peça uma descrição da tarefa e adicione ao final do arquivo (modo "a"), cada tarefa em uma linha.
Ao escolher 2, abra o arquivo em modo leitura, leia todas as linhas e mostre na tela assim:

--- SUAS TAREFAS ---
1) Lavar a louça
2) Estudar Python
3) ...

Requisitos extras:

Tratar o caso em que o arquivo ainda não existe (usar try/except FileNotFoundError e mostrar mensagem tipo “Nenhuma tarefa encontrada ainda.”).
'''

tarefas = []

menu = ("Selecione algumas das seguintes opções: \n 1 - Adicionar tarefa \n 2 - Ver tarefas \n 3 - Sair \n")


while True:

    print(menu)
    opcao = input(": ")

    if opcao == "1":
        tarefas = input("Digite a descrição da tarefa: ")
        with open("tarefas.txt", "a") as f:
            f.write(tarefas + "\n")
        print("Tarefa adicionada!")


    elif opcao == "2":
        print("--- SUAS TAREFAS ---")
        try: 
            with open("tarefas.txt", "r") as f:
                for i, tarefa in enumerate(f):
                    print(f"{i + 1}) {tarefa.strip()}")
                print("\n")
            #print(f.readlines())
        except FileNotFoundError:
            print("Nenhuma tarefa encontrada ainda.")

    elif opcao == "3":
        print("Saindo...")
        break

    else:
        print("Opção inválida. Tente novamente.")