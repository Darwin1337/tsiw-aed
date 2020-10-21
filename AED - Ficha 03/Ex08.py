import os
import traceback

# [Ficha 03 - Ex. 08] - Ilustra os primeiros n termos da sequência de Fibonacci

try:
    isNumberCorrect, lastFirst, lastSecond, current = False, 0, 1, 0
    while not isNumberCorrect:
        try:
            num = int(input("Introduza um número: "))
            if num > 0:
                isNumberCorrect = True
        except:
            continue
    for x in range(num):
        if x > 0: current = lastFirst + lastSecond
        lastFirst = lastSecond
        lastSecond = current
        print(str(x + 1) + ": " + str(current))
except Exception as e:
    print(str(e))
    traceback.print_exc()

os.system("pause")
