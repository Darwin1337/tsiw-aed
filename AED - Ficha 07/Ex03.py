import os
import random

# [Ficha 07 - Ex. 03] - Gere matrizes - Permite criar, transpor e determinar o valor máximo de matrizes

def criarMatriz():
    global generatedMatrix, originalVersion
    generatedMatrix.clear()
    while True:
        try:
            tamanho = int(input("\nTamanho da matriz: "))
            if tamanho > 1 and tamanho <= 100: break
        except: continue
    for i in range(tamanho):
        line = []
        for j in range(tamanho):
            num = random.randint(10, 100)
            if num not in generatedMatrix: line.append(num)
        generatedMatrix.append(line)
    originalVersion += 1
    print("\nMatriz criada com sucesso!")
    voltarMenu()

def matrizTransposta():
    global generatedMatrix, generatedMatrixTranposed, originalVersion, transposedVersion
    if len(generatedMatrixTranposed) == 0:
        if len(generatedMatrix) > 0:
            matrix = []
            for j in range(len(generatedMatrix[0])):
                line = []
                for i in range(len(generatedMatrix)):
                    line.append(generatedMatrix[i][j])
                generatedMatrixTranposed.append(line)
            transposedVersion += 1
            print("\nTransposição da matriz gerada com sucesso!")
            matrizTransposta()
        else:
            print("\nPor favor inicie uma matriz!")
            voltarMenu()
    else:
        if transposedVersion != originalVersion:
            generatedMatrixTranposed.clear()
            matrizTransposta()
        else: printarMatriz(generatedMatrixTranposed)

def valorMaximo():
    global generatedMatrix
    if len(generatedMatrix) > 0:
        maximum = 0
        for i in range(len(generatedMatrix)):
            if max(generatedMatrix[i]) > maximum:
                maximum = max(generatedMatrix[i])
        print("\nO maior valor pertencente à matriz é: " + str(maximum))
    else: print("\nPor favor inicie uma matriz!")
    voltarMenu()

def voltarMenu():
    print("\n*******************************")
    print("[1] - Voltar ao menu")
    print("[0] - Sair")
    print("*******************************")
    while True:
        try:
            opcao = int(input("\nOpção: "))
            if opcao in range(0, 2): break
        except: continue
    if opcao == 1: mostrarMenu()
    elif opcao == 2: os._exit(0)

def printarMatriz(a):
    print()
    for i in range(len(a)):
        print(" ".join(str(a[i][j]) for j in range(len(a[i]))))
    voltarMenu()

def mostrarMenu():
    global generatedMatrix, generatedMatrixTranposed
    while True:
        os.system("cls")
        print("+++     PROGRAMA MATRIZ     +++")
        print("*******************************")
        print("OPÇÕES DO MENU".center(30))
        print("[1] – Inicializar matriz")
        print("[2] - Calcular/ver matriz transposta")
        print("[3] - Determinar o valor máximo")
        if len(generatedMatrix) > 0:
            print("[4] – Ver matriz original")
            print("[5] - Sair")
        else: print("[4] - Sair")
        print("*******************************")
        try:
            opcao = int(input("\nEscolha uma das opções disponíveis: "))
            if len(generatedMatrix) == 0:
                if opcao in range(1, 5): break
            else:
                if opcao in range(1, 6): break
        except: continue
    if opcao == 1: criarMatriz()
    elif opcao == 2: matrizTransposta()
    elif opcao == 3: valorMaximo()
    elif opcao == 4 and len(generatedMatrix) > 0: printarMatriz(generatedMatrix)
    elif opcao == 4 and len(generatedMatrix) == 0: os._exit(0)
    elif opcao == 5 and len(generatedMatrix) > 0: os._exit(0)

generatedMatrix, generatedMatrixTranposed = [], []
originalVersion, transposedVersion = 0, 0
mostrarMenu()
