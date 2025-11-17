#6.3 — Desafiador:

#Crie um “cofre”:

#senha correta: "4321"
#o usuário pode tentar infinitas vezes
#se acertar → mostra “Acesso liberado” e encerra
#se digitar "sair" → encerra sem liberar
#continue pedindo até resolver
#Use while + break.

senha = int(4321)


while True:
    descobrirSenha = int(input("Digite a senha: "))

    if descobrirSenha == 'sair':
        break
    
    if descobrirSenha == 4321:
        print("Acesso liberado")
        break
    print("Acesso negado")