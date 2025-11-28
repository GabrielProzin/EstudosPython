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
nomeArquivo = input("Digite o nome do arquivo que voce deseja criar: ")
arquivo = nomeArquivo + '.txt'
print(arquivo)
frase = input("Digite a frase que deseja colocar dentro do arquivo: ")

with open(arquivo, "w") as f:
    conteudo = f.write(frase)


with open(arquivo, "r") as f:
    print(f.read())