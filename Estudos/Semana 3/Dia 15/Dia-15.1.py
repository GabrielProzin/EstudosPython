'''
🟢 15.1 – Bloco de notas pessoal (básico)
Crie um programa que:

Pergunte o nome de um arquivo de texto a ser criado (ex: meu_diario.txt).
Peça ao usuário para digitar uma frase.
Grave essa frase no arquivo usando o modo "w".
Em seguida, reabra o arquivo em modo leitura ("r") e exiba o conteúdo no terminal.
Requisitos:

Usar with open(...) tanto para escrever quanto para ler.
Mostrar mensagens amigáveis no console.
'''

with open("AnotaçõesPython.txt", "r") as f:
    conteudo = f.read()
    print(conteudo)