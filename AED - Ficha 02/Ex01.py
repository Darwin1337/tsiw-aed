import os
import traceback

# [Ficha 02 - Ex. 01] - Verifica se o número introduzido é par ou ímpar

try:
    isNumberCorrect = False
    while not isNumberCorrect:
        try:
            os.system('cls' if os.name=='nt' else 'clear')
            num = int(input("Introduza um número em inteiro: "))
            if int(num) > 0:
                isNumberCorrect = True
        except:
            continue
        print("O número introduzido é par") if num % 2 == 0 else print("O número introduzido é ímpar")
except Exception as e:
    print(str(e))
    traceback.print_exc()

os.system("pause")
