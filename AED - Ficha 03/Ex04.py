import os
import random
import traceback

# [Ficha 03 - Ex. 04] - Jogo de adivinhar o número (versão 1)

try:
    random, Acertou, tentativas = random.randint(1, 50), False, 0
    while not Acertou:
        if tentativas >= 10:
            print("\nEsgotou as 10 tentativas!")
            break
        isPalpiteCorrect = False
        while not isPalpiteCorrect:
            try:
                palpite = int(input("Palpite n. " + str(tentativas + 1) + ": "))
                if palpite > 0: isPalpiteCorrect = True
            except:
                continue
        tentativas += 1
        if palpite < random: print("Maior")
        elif palpite > random: print("Menor")
        else:
            print("Acertou")
            print("Utilizou " + str(tentativas) + " tentativas")
            Acertou = True
except Exception as e:
    print(str(e))
    traceback.print_exc()

os.system("pause")
