import os
import traceback

# [Ficha 03 - Ex. 01] - Lê 10 números e verifica qual deles o maior
try:
    maior = 0
    for x in range(10):
        isNumberCorrect = False
        while not isNumberCorrect:
            try:
                num = int(input("Introduza o no. " + str(x + 1) + ": "))
                isNumberCorrect = True
            except:
                continue
            if int(num) > int(maior): maior = num
    print("O maior numero é: " + str(maior))
except Exception as e:
    print(str(e))
    traceback.print_exc()

os.system("pause")
