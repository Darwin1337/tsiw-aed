import os

# [Ficha 07 - Ex. 01] - Simula um sistema de atendimento por fila
# A pessoa na primeira posição é a primeira a ser atendida (verificação da existência dessa pessoa)
# Ao tirar o ticket, a pessoa ocupará o primeiro lugar livre (verificação de existência de lugares livres)
# Capacidade de mostrar o estado atual da fila

def mostrarMenu():
    while True:
        os.system("cls")
        print("MENU".center(55) + "\n")
        print("[1] – Tirar Ticket".center(55))
        print("[2] - Atendimento".center(55))
        print("[3] - Estado da fila de espera".center(67))
        print("[0] - Sair".center(47))
        try:
            opcao = int(input("\nOpção: "))
            if opcao == 1:
                tirarTicket()
                break
            elif opcao == 2:
                atendimento()
                break
            elif opcao == 3:
                mostrarFila()
                break
            elif opcao == 0:
                raise SystemExit(0)
        except SystemExit: break
        except: continue

def mostrarFila():
    print("ESTADO DA FILA".center(55) + "\n")
    for x in range(len(fila)):
        num = ""
        if (x + 1) < 10: num = "0" + str(x + 1)
        else: num = str(x + 1)
        if fila[x] == 1: print(str("Posição " + num + ": Ocupado").center(55))
        else: print(str("Posição " + num + ": Desocupado").center(55))
    print("\nDos 20 lugares disponíveis, " + str(fila.count(0)) + " estão livres")
    voltarMenu()

def voltarMenu():
    print("\n[0] - Voltar ao menu")
    print("[1] - Sair")
    while True:
        try:
            opcao = int(input("\nOpção: "))
            if opcao == 0:
                mostrarMenu()
                break
            elif opcao == 1: raise SystemExit(0)
        except SystemExit: break
        except: continue

def tirarTicket():
    if fila.count(0) >= 1:
        fila[fila.index(0)] = 1
        print("\nSucesso! Está agora na posição " +  str(fila.count(1)) + " de 20")
    else:
        print("\nNão há lugares livres disponíveis!")
    voltarMenu()

def atendimento():
    if fila.count(1) > 0:
        try: fila[fila.index(0) - 1] = 0
        except: fila[19] = 0
        print("\nA pessoa em primeiro lugar foi atendida!")
    else: print("\nNão há pessoas na fila!")
    voltarMenu()

fila = [0 for x in range(20)]
mostrarMenu()
