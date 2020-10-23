import os
import random
import traceback

# [Ficha 03 - Ex. 04] - Jogo de adivinhar o número (versão 1)

try:
    random, tentativas = random.randint(1, 50), 0
    while True:
        if tentativas >= 10:
            print("\nEsgotou as 10 tentativas!")
            break
        while True:
            try:
                palpite = int(input("Palpite n. " + str(tentativas + 1) + ": "))
                if palpite > 0:
                    tentativas += 1
                    break
            except:
                continue
        if palpite < random: print("Maior")
        elif palpite > random: print("Menor")
        else:
            print("Acertou\nUtilizou " + str(tentativas) + " tentativas")
            break
except Exception as e:
    print(str(e))
    traceback.print_exc()

os.system("pause")
