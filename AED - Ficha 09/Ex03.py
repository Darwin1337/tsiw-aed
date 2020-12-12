import os

# [Ficha 09 - Ex. 03] - Gere um ficheiro de texto de países e os seus respetivos continentes - Permite consultar todos os países,
#                       países por continente e n.º de países por continente

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

def InserirPais():
    if not os.path.exists(os.getcwd() + "\\files"):
        os.mkdir(os.getcwd() + "\\files")
    paisExiste = False
    while True:
        try:
            pais = str(input("\nNome do país: "))
            if pais.replace(" ", ""):
                paisExiste = False
                if os.path.exists(os.getcwd() + "\\files\\paises.txt"):
                    for i in open(os.getcwd() + "\\files\\paises.txt", "r").readlines():
                         if pais.lower() == i.split(";")[0].lower(): paisExiste = True
                if not paisExiste: break
                else: print("\nO país introduzido já se encontra no ficheiro de texto!")
        except: continue
    while True:
        try:
            continente = str(input("\nNome do continente: "))
            if continente.replace(" ", ""): break
        except: continue
    if not paisExiste: open(os.getcwd() + "\\files\\paises.txt", "a").write(pais + ";" + continente + "\n")
    BackToMenu()

def ConsultarDados():
    print("\n" + "País".rjust(10, " ") + "Continente".rjust(35, " "))
    print("---------------------------------------".rjust(45, " "))
    for i in open(os.getcwd() + "\\files\\paises.txt", "r").readlines():
        print(i.split(";")[0].rjust(6 + len(i.split(";")[0]), " ") + i.strip().split(";")[1].rjust((29 - len(i.strip().split(";")[0])) + len(i.strip().split(";")[1]), " "))
    BackToMenu()

def ConsultarPaises():
    if os.path.exists(os.getcwd() + "\\files\\paises.txt"):
        if len(open(os.getcwd() + "\\files\\paises.txt", "r").readlines()) > 0:
            while True:
                try:
                    continente = str(input("\nContinente a pesquisar: "))
                    if continente.replace(" ", ""): break
                except: continue
            paisExiste = False
            for i in open(os.getcwd() + "\\files\\paises.txt", "r").readlines():
                if continente.lower() == i.strip().split(";")[1].lower():
                    if not paisExiste:
                        paisExiste = True
                        print("\n" + "País".rjust(10, " ") + "Continente".rjust(35, " "))
                        print("---------------------------------------".rjust(45, " "))
                        print(i.split(";")[0].rjust(6 + len(i.split(";")[0]), " ") + i.strip().split(";")[1].rjust((29 - len(i.strip().split(";")[0])) + len(i.strip().split(";")[1]), " "))
                    else:
                        print(i.split(";")[0].rjust(6 + len(i.split(";")[0]), " ") + i.strip().split(";")[1].rjust((29 - len(i.strip().split(";")[0])) + len(i.strip().split(";")[1]), " "))
            if not paisExiste: print("\nNão foram encontrados países da " + " ".join(continente.split(" ")[n].capitalize() if len(continente.split(" ")[n]) > 2 else continente.split(" ")[n] for n in range(len(continente.split(" ")))))
        else: print("\nO ficheiro de texto não contém países")
    else: print("\nO ficheiro de texto ou a pasta não existe")
    BackToMenu()

def ConsultarNumPaises():
    if os.path.exists(os.getcwd() + "\\files\\paises.txt"):
        if len(open(os.getcwd() + "\\files\\paises.txt", "r").readlines()) > 0:
            while True:
                try:
                    continente = str(input("\nContinente a pesquisar: "))
                    if continente.replace(" ", ""): break
                except: continue
            paisCounter = 0
            for i in open(os.getcwd() + "\\files\\paises.txt", "r").readlines():
                if continente.lower() == i.strip().split(";")[1].lower():
                    paisCounter += 1
            if paisCounter == 0: print("\nNão foram encontrados países do continente da " + " ".join(continente.split(" ")[n].capitalize() if len(continente.split(" ")[n]) > 2 else continente.split(" ")[n] for n in range(len(continente.split(" ")))))
            else: print("\nO continente da " + " ".join(continente.split(" ")[n].capitalize() if len(continente.split(" ")[n]) > 2 else continente.split(" ")[n] for n in range(len(continente.split(" ")))) + " tem " + str(paisCounter) + " países presentes no ficheiro de texto")
        else: print("\nO ficheiro de texto não contém países")
    else: print("\nO ficheiro de texto ou a pasta não existe")
    BackToMenu()

def ShowMenu():
    while True:
        os.system("cls")
        print("--- [MENU] ---".rjust(27))
        print("\n[1] - Inserir países")
        print("[2] - Consultar dados")
        print("[3] - Consultar países por continente")
        print("[4] - Consultar n.º países por continente")
        print("[0] - Sair")
        try:
            opcao = int(input("\nOpção: "))
            if opcao in range(0, 5): break
        except: continue
    if opcao == 1: InserirPais()
    elif opcao == 2: ConsultarDados()
    elif opcao == 3: ConsultarPaises()
    elif opcao == 4: ConsultarNumPaises()
    elif opcao == 0: os._exit(0)

ShowMenu()
