import os
import random
import traceback

# [Ficha 03 - Ex. 05] - Jogo de adivinhar o número (versão 2)

try:
    randonum, Acertou, tentativas = random.randint(1, 50), False, 0
    while not Acertou:
        if tentativas >= 10:
            print("\nEsgotou as 10 tentativas!")
            isStringCorrect = False
            while not isStringCorrect:
                try:
                    newgame = str(input("\nIniciar novo jogo (S = Sim | N = Não): "))
                    if newgame.upper() == "S" or newgame.upper() == "N": isStringCorrect = True
                except:
                    continue
            if newgame.upper() == "S":
                tentativas = 0
                randonum = random.randint(1, 50)
            else: break
        isPalpiteCorrect = False
        while not isPalpiteCorrect:
            try:
                palpite = int(input("Palpite n. " + str(tentativas + 1) + ": "))
                if palpite > 0: isPalpiteCorrect = True
            except:
                continue
        tentativas += 1
        if palpite < randonum: print("Maior")
        elif palpite > randonum: print("Menor")
        else:
            print("Acertou\nUtilizou " + str(tentativas) + " tentativas")
except Exception as e:
    print(str(e))
    traceback.print_exc()

os.system("pause")
