import os
import traceback

# [Ficha 01 - Ex. 02] - Converte graus celsius para graus fahrenheit

try:
    isNumberCorrect = False
    while not isNumberCorrect:
        try:
            os.system('cls' if os.name=='nt' else 'clear')
            num = float(input("Introduza a temperatura (em Cº): "))
            isNumberCorrect = True
        except:
            continue
    print("\nEm fahrenheit: " + str(float(1.8 * num + 32)))
except Exception as e:
    print(str(e))
    traceback.print_exc()

os.system("pause")
