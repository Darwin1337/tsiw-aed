import os
import traceback

# [Ficha 03 - Ex. 02] - Repete a pergunta de acordo com o input do utilizador
#                       números e verifica qual dos números introduzidos é o maior
try:
    maior, media = 0, 0.0
    while True:
        try:
            maxNum = int(input("Indique a quantidade de números que pretende introduir: "))
            if maxNum > 0: break
        except:
            continue
    for x in range(maxNum):
        while True:
            try:
                num = int(input("Introduza o no. " + str(x + 1) + ": "))
                media += num
                break
            except:
                continue
        if int(num) > int(maior): maior = num
    print("A média é: " + str(float(media / maxNum)))
    print("\nO maior numero é: " + str(maior))
except Exception as e:
    print(str(e))
    traceback.print_exc()

os.system("pause")
