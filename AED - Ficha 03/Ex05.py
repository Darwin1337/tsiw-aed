import os
import random
import traceback

# [Ficha 03 - Ex. 05] - Jogo de adivinhar o número (versão 2)

try:
    randonum, tentativas = random.randint(1, 50), 0
    while True:
        if tentativas >= 10:
            print("\nEsgotou as 10 tentativas!")
            while True:
                try:
                    newgame = str(input("\nIniciar novo jogo (S = Sim | N = Não): "))
                    if newgame.upper() == "S" or newgame.upper() == "N": break
                except:
                    continue
            if newgame.upper() == "S":
                tentativas = 0
                randonum = random.randint(1, 50)
            else: break
        while True:
            try:
                palpite = int(input("Palpite n. " + str(tentativas + 1) + ": "))
                if palpite > 0:
                    tentativas += 1
                    break
            except:
                continue
        if palpite < randonum: print("Maior")
        elif palpite > randonum: print("Menor")
        else:
            print("Acertou\nUtilizou " + str(tentativas) + " tentativas")
except Exception as e:
    print(str(e))
    traceback.print_exc()

os.system("pause")
