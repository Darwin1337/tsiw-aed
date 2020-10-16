import os
import traceback

# [Ficha 01 - Ex. 01] - Converte polegadas em centímetros e milímetros

try:
    isNumberCorrect = False
    while not isNumberCorrect:
        os.system('cls' if os.name=='nt' else 'clear')
        try:
            num = int(input("Introduza um número em polegadas: "))
            if int(num) > 0:
                isNumberCorrect = True
        except:
            continue
    print("\nNúmero em milímetros: " + str(float(num * 25.4)) + "mm\nNúmero em centímetros: " +  str(float((num * 25.4) / 10)) + "cm" )
except Exception as e:
    print(str(e))
    traceback.print_exc()

os.system("pause")
