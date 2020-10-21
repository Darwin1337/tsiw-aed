import os
import traceback

# [Ficha 03 - Ex. 10] - Converte número decimal em binário

try:
    isNumberCorrect, binario = False, ""
    while not isNumberCorrect:
        try:
            num = int(input("Introduza um número: "))
            if num >= 0:
                isNumberCorrect = True
        except:
            continue
    while num >= 1:
        binario += str(int(num % 2))
        num /= 2
    print("Binário: " + binario[::-1]) if num > 0 else print("Binário: 0")
except Exception as e:
    print(str(e))
    traceback.print_exc()

os.system("pause")
