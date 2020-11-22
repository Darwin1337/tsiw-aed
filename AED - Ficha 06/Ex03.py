import os
import traceback

# [Ficha 06 - Ex. 03] - Lê a pontuação de 10 participantes num concurso de programação (pontuação de 0 a 20) e devolve
# uma nova lista apenas com as pontuações positivas (>=10)

def apenasPositivas(a):
    positivas = []
    for x in range(len(a)):
        if a[x] >= 10:
            positivas.append(a[x])
    return positivas

try:
    participantes = []
    for x in range(10):
        while True:
            try:
                pontuacoes = float(str(input("Nota #" + str(x + 1) + ": ")).replace(",", "."))
                if pontuacoes >= 0 and pontuacoes <= 20:
                    participantes.append(pontuacoes)
                    break
            except:
                continue
    result = apenasPositivas(participantes)
    for nota in result:
        print(str(nota))
except Exception as e:
    print(str(e))
    traceback.print_exc()

os.system("pause")
