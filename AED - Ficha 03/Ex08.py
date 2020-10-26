import os
import traceback

# [Ficha 03 - Ex. 08] - Ilustra os primeiros n termos da sequência de Fibonacci

try:
    lastFirst, lastSecond, current = 0, 1, 0
    while True:
        try:
            num = int(input("Introduza um número: "))
            if num > 0: break
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
