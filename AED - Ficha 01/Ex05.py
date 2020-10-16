import os
import traceback

# [Ficha 01 - Ex. 05] - Converte segundos para horas, minutos e segundos

try:
    isNumberCorrect = False
    while not isNumberCorrect:
        try:
            os.system('cls' if os.name=='nt' else 'clear')
            segundos = int(input("Introduza a quantidade de segundos: "))
            if segundos > 0:
                isNumberCorrect = True
        except:
            continue
    horas = int((segundos / 60) / 60)
    minutos = int((segundos / 60) - horas * 60)
    segundos = int(segundos - (((horas * 60) * 60) + (minutos * 60)))
    print("\nHoras: " + str(horas) + "\nMinutos: " + str(minutos) + "\nSegundos: " + str(segundos) + "\n")
except Exception as e:
    print(str(e))
    traceback.print_exc()

os.system("pause")
