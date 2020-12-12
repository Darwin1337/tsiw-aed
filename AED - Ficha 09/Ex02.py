import os

# [Ficha 09 - Ex. 02] - Gere os dados do ficheiro de texto "temps_ex01.txt" (gerado no exercício anterior) - Permite consultar
#                       os dados na íntegra ou por estatística (temperatura máxima, mínima e média)

def BackToMenu():
    print("\n[1] - Voltar ao menu")
    print("[0] - Sair")
    while True:
        try:
            opcao = int(input("\nOpção: "))
            if opcao in range(0, 2): break
        except: continue
    if opcao == 1: ShowMenu()
    elif opcao == 2: os._exit(0)

def ConsultaData():
    os.system("cls")
    print("Data".rjust(20) + "Hora".rjust(30) + "Temperatura".rjust(40))
    print("--------------------------------------------------------------------------".rjust(90))
    temps = open(os.getcwd() + "\\temps_ex01.txt", "r").readlines()
    for a in temps:
        print(a.split(";")[0].rjust(26) + a.split(";")[1].rjust(28) + a.strip().split(";")[2].rjust(27))
    BackToMenu()

def ConsultaEstatistica():
    temps = open(os.getcwd() + "\\temps_ex01.txt", "r").readlines()
    min = 99
    for i in temps:
        if int(i.strip().split(";")[2]) < min:
            min = int(i.strip().split(";")[2])
    max = 0
    for i in temps:
        if int(i.strip().split(";")[2]) > max:
            max = int(i.strip().split(";")[2])
    soma = 0
    for i in temps:
        soma += int(i.strip().split(";")[2])
    media = int(soma / len(temps))
    os.system("cls")
    print("Temperatura mínima: " + str(min))
    print("Temperatura máxima: " + str(max))
    print("Média de temperaturas: " + str(media))
    BackToMenu()

def ShowMenu():
    while True:
        os.system("cls")
        print("--- MENU ---".rjust(20))
        print("\n[1] - Consulta todos os dados")
        print("[2] - Consulta por estatística")
        print("[0] - Sair")
        try:
            opcao = int(input("\nOpção: "))
            if opcao in range(0, 3): break
        except: continue
    if opcao == 1: ConsultaData()
    elif opcao == 2: ConsultaEstatistica()
    elif opcao == 0: os._exit(0)

ShowMenu()
