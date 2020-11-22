import os

# [Ficha 07 - Ex. 02] - Dada uma matriz - devolve a mesma só que transposta

def criarMatriz(width, height):
    initial, matrix = 1, []
    for i in range(height):
        line = []
        for j in range(width):
            line.append(initial)
            initial += 1
        matrix.append(line)
    return matrix

def matrizTransposta(a):
    matrix = []
    for j in range(len(a[0])):
        line = []
        for i in range(len(a)):
            line.append(a[i][j])
        matrix.append(line)
    return matrix

def printarMatriz(a):
    for line in a:
        print(str(line))

matrix = criarMatriz(3, 3)
newMatrix = matrizTransposta(matrix)

printarMatriz(matrix)
print()
printarMatriz(newMatrix)
