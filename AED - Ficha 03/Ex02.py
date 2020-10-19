import os
import traceback

# [Ficha 03 - Ex. 02] - Repete a pergunta de acordo com o input do utilizador
#                       números e verifica qual dos números introduzidos é o maior
try:
    isMaxCorrect = False
    while not isMaxCorrect:
        try:
            maxNum = int(input("Indique a quantidade de números que pretende introduir: "))
            if maxNum > 0: isMaxCorrect = True
        except:
            continue
    maior = 0
    for x in range(maxNum):
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
