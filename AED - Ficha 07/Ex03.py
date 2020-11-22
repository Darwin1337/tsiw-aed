import os
import random
import sys

# [Ficha 07 - Ex. 03] - Dada uma matriz - devolve a mesma só que transposta

def criarMatriz():
    while True:
        try:
            tamanho = int(input("\nTamanho da matriz: "))
            if tamanho > 1 and tamanho <= 100: break
        except: continue
    initial = 1
    for i in range(tamanho):
        line = []
        for j in range(tamanho):
            num = random.randint(1, tamanho * tamanho)
            if num not in generatedMatrix: line.append(num)
        generatedMatrix.append(line)
    mostrarMenu()

def matrizTransposta():
    if len(generatedMatrix) > 0:
        matrix = []
        for j in range(len(generatedMatrix[0])):
            line = []
            for i in range(len(generatedMatrix)):
                line.append(generatedMatrix[i][j])
            matrix.append(line)
        print("\nOriginal:")
        printarMatriz(generatedMatrix)
        print("\nTransposta:")
        printarMatriz(matrix)
    else: print("\nPor favor inicie uma matriz!")
    voltarMenu()

def printarMatriz(a, b):
    print()
    for line in a:
        print(str(line))
    voltarMenu()

def voltarMenu():
    print("\n*******************************")
    print("[0] - Voltar ao menu")
    print("[1] - Sair")
    print("*******************************")
    while True:
        try:
            opt = int(input("\nOpção: "))
            if opt == 0:
                mostrarMenu()
                break
            elif opt == 1: raise SystemExit(0)
        except SystemExit: break
        except: continue

def mostrarMenu():
    while True:
        os.system("cls")
        print("+++     PROGRAMA MATRIZ     +++")
        print("*******************************")
        print("OPÇÕES DO MENU".center(30))
        print("[1] – Inicializar matriz")
        print("[2] - Calcular matriz transposta")
        print("[3] - Determinar o valor máximo")
        if len(generatedMatrix) > 0:
            print("[4] – Ver matriz original")
            print("[5] - Sair")
        else: print("[4] - Sair")

        print("*******************************")
        try:
            opcao = int(input("\nEscolha uma das opções disponíveis: "))
            if opcao == 1:
                criarMatriz()
                break
            elif opcao == 2:
                matrizTransposta()
                break
            elif opcao == 3:
                mostrarFila()
                break
            elif opcao == 4 and len(generatedMatrix) > 0:
                printarMatriz(generatedMatrix)
                break
            elif opcao == 4 and len(generatedMatrix) <= 0:
                raise SystemExit(0)
            elif len(generatedMatrix) > 0 and opcao == 5:
                raise SystemExit(0)
        except SystemExit: break
        except: continue

isMatrixGenerated = False
generatedMatrix = []
mostrarMenu()
