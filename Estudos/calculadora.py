numeroDigitado = int(input("Digie o número que deseja para apresentar a tabuada: "))
contador = 1

print(f"a tabuada de {numeroDigitado} é: ")
for contador in range(1, 11):
    resultado = numeroDigitado * contador
    print(f"{numeroDigitado} * {contador} = {resultado}")