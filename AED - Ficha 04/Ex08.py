import os
import random
import traceback

# [Ficha 04 - Ex. 08] - Gera uma password de acordo com o nome introduzido

try:
    result = ""
    while True:
        try:
            nome = str(input("Nome: "))
            if nome.replace(" ", ""):
                if " " not in nome: break
        except:
            continue
    for x in range(len(nome)):
        if (x + 1) % 2 == 0:
            result += nome[x] + str(random.randint(0, 9))
    print(result + str(len(nome)))
except Exception as e:
    print(str(e))
    traceback.print_exc()

os.system("pause")
