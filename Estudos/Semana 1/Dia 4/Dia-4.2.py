#4.2 — Intermediário:

#Crie um programa que pede:

#distância percorrida (km)
#tempo gasto (horas)
#Calcule a velocidade média.

distanciaKM = int(input("Digite a distancia percorrida em KM: "))
tempoGasto = int(input("Digite o tempo gasto na distancia percorrida: "))

velocidadeMedia = int(distanciaKM / tempoGasto)

print(f" a sua velocidade media é de {velocidadeMedia}km/h")