import os

# [Ficha 07 - Ex. 04] - Gere um parque de estacionamento

def ParkVehicle():
    global parqueEstacionamento
    isSpotAvailable = False
    for i in range(3):
        if 0 in parqueEstacionamento[i]:
            isSpotAvailable = True
            print("\nFoi estacionado um veículo na fila " + str(i + 1) + ", lugar " + str(parqueEstacionamento[i].index(0) + 1))
            parqueEstacionamento[i][parqueEstacionamento[i].index(0)] = 1
            break
    if not isSpotAvailable: print("\nNão há lugares disponíveis!")
    ReturnMenu()

def TakeVehicleOut():
    global parqueEstacionamento
    if sum([sum(i) for i in parqueEstacionamento]) != 0:
        while True:
            try:
                fila = int(input("\nFila em que o veículo está estacionado: "))
                if fila in range(1, 4): break
            except: continue
        while True:
            try:
                lugar = int(input("\nLugar em que o veículo está estacionado: "))
                if lugar in range(1, 6): break
            except: continue
        if parqueEstacionamento[fila - 1][lugar - 1] == 1:
            parqueEstacionamento[fila - 1][lugar - 1] = 0
            print("\nO veículo escolhido foi retirado!")
        else: print("\nNão há nenhum veículo estacionado no lugar e fila escolhidos!")
    else: print("\nO parque de estacionamento já totalmente livre!")
    ReturnMenu()

def ParkingState():
    global parqueEstacionamento
    os.system("cls")
    possibleStates, totalParked = ["Livre", "Ocupado"], sum([sum(i) for i in parqueEstacionamento])
    print("--- ESTADO DO PARQUE ---".rjust(41) + "\n")
    print("Fila 1".rjust(16) + "Fila 2".rjust(16) + "Fila 3".rjust(16) + "\n")
    for i in range(5): print(str("Lugar " + str(i + 1)) + " |" + " ".join(possibleStates[parqueEstacionamento[j][i]].rjust(1 + len(possibleStates[parqueEstacionamento[j][i]])) if j == 0 else possibleStates[parqueEstacionamento[j][i]].rjust(10 + len(possibleStates[parqueEstacionamento[j][i]]) if possibleStates[parqueEstacionamento[j - 1][i]] == "Livre" else 8 + len(possibleStates[parqueEstacionamento[j][i]])) for j in range(3)))
    print("\nLugares livres: " + str(15 - totalParked))
    print("Lugares ocupados: " + str(totalParked))
    ReturnMenu()

def ReturnMenu():
    print("\n[1] - Voltar ao menu")
    print("[0] - Sair")
    while True:
        try:
            opcao = int(input("\nOpção: "))
            if opcao in range(0, 2): break
        except: continue
    if opcao == 1: ShowMenu()
    elif opcao == 2: os._exit(0)

def ShowMenu():
    while True:
        os.system("cls")
        print("--- PARQUE DE ESTACIONAMENTO ---\n")
        print("[1] – Entrada de veículo".rjust(28))
        print("[2] - Saída de veículo".rjust(26))
        print("[3] - Estado do parque".rjust(26))
        print("[0] - Sair".rjust(14))
        try:
            opcao = int(input("\nEscolha uma das opções disponíveis: "))
            if opcao in range(0, 4): break
        except: continue
    if opcao == 1: ParkVehicle()
    elif opcao == 2: TakeVehicleOut()
    elif opcao == 3: ParkingState()
    elif opcao == 0: os._exit(0)

parqueEstacionamento = []
for _ in range(3): parqueEstacionamento.append([0 for _ in range(5)])
ShowMenu()
