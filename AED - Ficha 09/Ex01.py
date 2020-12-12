import os
import datetime as date
import random
import time

# [Ficha 09 - Ex. 01] - Gera um ficheiro de texto com temperaturas aleatórias seguido da data e hora do seu registo
#                       Obs: se o ficheiro já existir o mesmo será substituido por valores novos

open(os.getcwd() + "\\temps_ex01.txt", "w").write("")
file =  open(os.getcwd() + "\\temps_ex01.txt", "a")

for i in range(30):
    print("A gerar temperatura " + str(i + 1) + "...")
    file.write(str(date.datetime.now().date()) + ";" + str(date.datetime.now().time().strftime("%H:%M:%S")) + ";" + str(random.randint(10, 25)) + "\n")
    time.sleep(1)

file.close()
