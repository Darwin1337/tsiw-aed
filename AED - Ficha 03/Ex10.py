import os
import traceback

# [Ficha 03 - Ex. 10] - Converte um número decimal em binário

try:
    isNumberCorrect, binario = False, ""
    while not isNumberCorrect:
        try:
            num = int(input("Introduza um número: "))
            if num >= 1 and num <= 99:
                isNumberCorrect = True
        except:
            continue
    while num >= 1:
        binario += str(int(num % 2))
        num /= 2
    print("Binário: " + binario[::-1])
except Exception as e:
    print(str(e))
    traceback.print_exc()

os.system("pause")
