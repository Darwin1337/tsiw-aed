import os
import traceback

# [Ficha 04 - Ex. 10] - Receber uma string do tipo: "Primeiro Manuel, Segundo Carla, Terceiro Andreia, Quarto Nuno"
#                       E imprimir duas strings que intercalem o texto inicial, por ex:
#                       String 1 = Primeiro Segundo Terceiro Quarto
#                       String 2 = Manuel Carla Andreia Nuno

try:
    result1, result2 = "", ""
    while True:
        try:
            texto = str(input("Texto inicial: "))
            if texto.replace(" ", "").replace(",", "") and "," in texto: break
        except:
            continue
    lista = texto.split(",")
    for x in range(len(lista)):
        for j in range(len(lista[x].strip().split(" "))):
            if j % 2 == 0: result1 += lista[x].strip().split(" ")[j] + " "
            else: result2 += lista[x].strip().split(" ")[j] + " "
    print("\n" + result1.strip() + "\n" + result2.strip())
except Exception as e:
    print(str(e))
    traceback.print_exc()

os.system("pause")
