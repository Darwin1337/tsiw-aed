import os
import traceback

# [Ficha 06 - Ex. 04] - Lê a pontuação e o nome de 10 participantes num concurso de programação (pontuação de 0 a 20) e devolve
# uma nova lista apenas com as pontuações positivas (>=10) e os nomes dos alunos que as obteram

def apenasPositivas(a):
    positivas, result = [], ""
    for x in range(len(a)):
        if float(a[x].split(" - ")[1]) >= 10:
            positivas.append(a[x])
    for aluno in positivas:
        result += str(aluno) + "\n"
    return "\n" + result

try:
    participantes = []
    for x in range(10):
        while True:
            try:
                nome = str(input("Nome #" + str(x + 1) + ": "))
                if nome.replace(" ", ""): break
            except: continue
        while True:
            try:
                pontuacoes = float(str(input("Nota #" + str(x + 1) + ": ")).replace(",", "."))
                if pontuacoes >= 0 and pontuacoes <= 20:
                    participantes.append(str(nome) + " - " + str(pontuacoes))
                    break
            except: continue
    print(str(apenasPositivas(participantes)))
except Exception as e:
    print(str(e))
    traceback.print_exc()

os.system("pause")
