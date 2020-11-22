import os
import traceback
import random

# [Ficha 06 - Ex. 10] - Lê o n.º de visitantes de uma exposição de domingo a sábado e permite listá-los de forma decrescente,
# ver a média diária de visitantes e saber qual dia se aproximou mais da média

def infoVisitantes(visitantes):
    result, soma, closest = [], 0, visitantes[0]
    for visitor in visitantes:
        soma += int(visitor.split(";")[0])
    media = float(soma / 7)
    for visitor in visitantes:
        if float(visitor.split(";")[0]) <= float(media):
            if float((media - float(visitor.split(";")[0]))) < float(closest.split(";")[0]) or visitor.split(";")[1] == "domingo": closest = str(float((media - float(visitor.split(";")[0])))) + ";" + visitor.split(";")[1] + ";" + visitor.split(";")[0]
        else:
            if float((float(visitor.split(";")[0]) - media)) < float(closest.split(";")[0]): closest = str(float((float(visitor.split(";")[0]) - media))) + ";" + visitor.split(";")[1] + ";" + visitor.split(";")[0]
    return str(float(soma / 7)), sorted(visitantes, key = lambda x: int(x.split(";")[0]), reverse=True), closest

try:
    diasSemana = ["domingo", "segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado"]
    visitantes = []
    for i in range(7):
        while True:
            try:
                qntVisit = int(input("Número de visitantes no dia de " + diasSemana[i] + ": "))
                if qntVisit >= 0:
                    visitantes.append(str(qntVisit) + ";" + diasSemana[i])
                    break
            except:
                continue
    resultado = infoVisitantes(visitantes)
    print("\nLista ordenada por ordem decrescente:\n")
    for i in range(len(resultado[1])):
        print("[" + str(resultado[1][i].split(";")[1]) + "]" + (" " * 20 - (2 + int(len(str(resultado[1][i].split(";")[1]))))) + str(resultado[1][i].split(";")[0]))
    print("\nMédia diária: %.2f" % float(resultado[0]))
    print("\nDia que se aproximou mais: " + str(resultado[2].split(";")[1]) + " com " + str(resultado[2].split(";")[2]) + " visitantes")
except Exception as e:
    print(str(e))
    traceback.print_exc()

os.system("pause")
