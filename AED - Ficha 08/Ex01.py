import os
import sys
import random

# [Ficha 08 - Ex. 01] - [Ficha Opcional] - Implementa o jogo do galo
#                       Work in progress...

def startSoloPlayerGame():
    global gameStarted, currentTurn, playerSymbol, game, available, playerIs

    if not gameStarted:
        resetVariables()
        gameStarted = True
        playerIs = random.randint(0, 1)
    else:
        if currentTurn == 1: currentTurn = 0
        else: currentTurn = 1

    updateScreen(False, True)

    if playerIs == currentTurn:
        while True:
            try:
                jogada = int(input("\nJogada: "))
                if jogada in available: break
            except: continue
    else:
        # Implementar jogada do computador sem ser
        # computerMove()
        jogada = random.choice(available)

    currentPos, jogadaDone = 9, False
    for i in range(len(game)):
        for j in range(len(game[i]) - 1, -1, -1):
            if jogada == currentPos:
                game[i][j] = playerSymbol[currentTurn]
                available.pop(available.index(jogada))
                jogadaDone = True
                break
            currentPos -= 1
        if jogadaDone: break

    if 9 - len(available) >= 5:
        if isGameOver():
            updateScreen(True, True)
            gameStarted = False
            if currentTurn == 0:
                if currentTurn == playerIs: print("\nO jogo terminou. O vencedor foi o jogador 1 (X)!")
                else: print("\nO jogo terminou. O vencedor foi o jogador 1 (X) [COMPUTADOR]!")
            else:
                if currentTurn == playerIs: print("\nO jogo terminou. O vencedor foi o jogador 2 (O)!")
                else: print("\nO jogo terminou. O vencedor foi o jogador 2 (O) [COMPUTADOR]!")
            goBackPrompt()
        else:
            if len(available) == 0:
                updateScreen(True, True)
                gameStarted = False
                print("\nO jogo terminou empatado!")
                goBackPrompt()
    startSoloPlayerGame()

def computerMove():
    pass

def startMultiPlayerGame():
    global gameStarted, currentTurn, playerSymbol, game, available

    if not gameStarted:
        resetVariables()
        gameStarted = True
    else:
        if currentTurn == 1: currentTurn = 0
        else: currentTurn = 1

    updateScreen(False, False)

    while True:
        try:
            jogada = int(input("\nJogada: "))
            if jogada in available: break
        except: continue

    currentPos, jogadaDone = 9, False
    for i in range(len(game)):
        for j in range(len(game[i]) - 1, -1, -1):
            if jogada == currentPos:
                game[i][j] = playerSymbol[currentTurn]
                available.pop(available.index(jogada))
                jogadaDone = True
                break
            currentPos -= 1
        if jogadaDone: break

    if 9 - len(available) >= 5:
        if isGameOver():
            updateScreen(True, False)
            gameStarted = False
            print("\nO jogo terminou. O vencedor foi o jogador 1 (X)!") if currentTurn == 0 else print("\nO jogo terminou. O vencedor foi o jogador 2 (O)!")
            goBackPrompt()
        else:
            if len(available) == 0:
                updateScreen(True, False)
                gameStarted = False
                print("\nO jogo terminou empatado!")
                goBackPrompt()
    startMultiPlayerGame()

def gameControls():
    os.system("cls")
    print("--------- CONTROLOS ---------\n")
    print("Utiliza as seguintes teclas do NUMPAD para controlar cada posição.\n")
    controls = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
    for i in range(len(controls)):
        print(" . ".join(str(controls[i][j]) for j in range(len(controls[i]))))
    goBackPrompt()

def exitGame():
    os._exit(0)

def isGameOver():
    global game

    if "-" not in game[1][1]:
        if game[0][0] == game[1][1] and game[1][1] == game[2][2]: return True
        if game[0][2] == game[1][1] and game[1][1] == game[2][0]: return True
    for i in range(3):
        if "-" not in game[i]:
            if len(set(game[i])) == 1: return True
    if "-" not in game[0][0]:
        if game[0][0] == game[1][0] and game[1][0] == game[2][0]: return True
    if "-" not in game[0][1]:
        if game[0][1] == game[1][1] and game[1][1] == game[2][1]: return True
    if "-" not in game[0][2]:
        if game[0][2] == game[1][2] and game[1][2] == game[2][2]: return True

    return False

def goBackPrompt():
    print("\n[1] - Voltar ao menu")
    print("[2] - Sair")
    while True:
        try:
            opcao = int(input("\nOpção: "))
            if opcao in range(1, 3): break
        except: continue
    if opcao == 1: gameMenu()
    elif opcao == 2: exitGame()

def updateScreen(a, b):
    global game, currentTurn, playerIs
    os.system("cls")
    print("Jogo:\n")
    for i in range(len(game)):
        print(" . ".join(str(game[i][j]) for j in range(len(game[i]))))
    if not a:
        if not b:
            if currentTurn == 0: print("\nVez: Jogador 1 (X)")
            else: print("\nVez: Jogador 2 (O)")

def resetVariables():
    global currentTurn, game, available, playerIs
    currentTurn, game, available = random.randint(0, 1), [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]], [7, 8, 9, 4, 5, 6, 1, 2, 3]

def gameMenu():
    while True:
        os.system("cls")
        print("--------- JOGO DO GALO ---------\n")
        print("[1] - Começar jogo - 1 jogador")
        print("[2] - Começar jogo - 2 jogadores")
        print("[3] - Controlos")
        print("[4] - Sair")
        try:
            opcao = int(input("\nOpção: "))
            if opcao in range(1, 5): break
        except: continue
    if opcao == 1: startSoloPlayerGame()
    elif opcao == 2: startMultiPlayerGame()
    elif opcao == 3: gameControls()
    elif opcao == 4: exitGame()

# Player 1 = 0
# Player 2 = 1

gameStarted, currentTurn, playerIs = False, 0, 0
playerSymbol, game, available = ["X", "O"], [], []
gameMenu()
