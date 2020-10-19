import os
import traceback

# [Ficha 03 - Ex. 03] - Determina o fatorial de um número
try:
    isNumCorrect = False
    while not isNumCorrect:
        try:
            num = int(input("Introduza um número: "))
            if num >= 0: isNumCorrect = True
        except:
            continue
    for x in range(num - 1, 0, -1):
        num *= int(x)
    print("Fatorial: " + str(num)) if num > 0 else print("Fatorial: 1")
except Exception as e:
    print(str(e))
    traceback.print_exc()

os.system("pause")
