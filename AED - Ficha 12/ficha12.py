import sys
import os
import traceback
from tkinter import *
from tkinter import messagebox, ttk, filedialog
from PIL import ImageTk, Image

class MainProgram:
    def __init__(self, master):
        self.master = master
        self.master.geometry("850x500")
        self.master.title("Ficha 12")
        self.Layout()

    def Layout(self):
        def OpenImage():
            self.chosenPath = filedialog.askopenfilename(filetypes=[("Imagem", ".jpg .png")])
            if self.chosenPath:
                self.isDirectoryAlreadyPresent = False
                for i in range(self.listBox.size()):
                    if self.chosenPath == self.listBox.get(i):
                        self.isDirectoryAlreadyPresent = True
                        messagebox.showerror("Erro", "A imagem escolhida já se encontra no programa!")
                if not self.isDirectoryAlreadyPresent:
                    self.listBox.insert(END, self.chosenPath)
                ManagePictures()

        def RemoveImage():
            try:
                self.listBox.delete(self.listBox.curselection()[0])
                ManagePictures()
            except: pass

        def ManagePictures():
            if int(self.listBox.size()) >= 1:
                self.imageToUse = ImageTk.PhotoImage(Image.open(self.listBox.get(0)))
                self.selectedImagePath = self.listBox.get(0)
                self.showPicture = self.imageCanvas.create_image(200, 150, image = self.imageToUse)
            else: self.imageCanvas.delete("all")

        def PreviousImage():
            if list(self.listBox.get(0, END)).index(self.selectedImagePath) > 0:
                self.imageToUse = ImageTk.PhotoImage(Image.open(self.listBox.get(list(self.listBox.get(0, END)).index(self.selectedImagePath) - 1)))
                self.selectedImagePath = self.listBox.get(list(self.listBox.get(0, END)).index(self.selectedImagePath) - 1)
                self.showPicture = self.imageCanvas.create_image(200, 150, image = self.imageToUse)

        def NextImage():
            if list(self.listBox.get(0, END)).index(self.selectedImagePath) < self.listBox.size() - 1:
                self.imageToUse = ImageTk.PhotoImage(Image.open(self.listBox.get(list(self.listBox.get(0, END)).index(self.selectedImagePath) + 1)))
                self.selectedImagePath = self.listBox.get(list(self.listBox.get(0, END)).index(self.selectedImagePath) + 1)
                self.showPicture = self.imageCanvas.create_image(200, 150, image = self.imageToUse)

        def LastPic1():
            if int(self.listBox.size()) >= 1:
                self.imageToUse = ImageTk.PhotoImage(Image.open(self.listBox.get(0)))
                self.selectedImagePath = self.listBox.get(0)
                self.imageCanvas.itemconfig(self.showPicture, image = self.imageToUse)

        def LastPic2():
            if int(self.listBox.size()) >= 1:
                self.imageToUse = ImageTk.PhotoImage(Image.open(self.listBox.get(self.listBox.size() - 1)))
                self.selectedImagePath = self.listBox.get(self.listBox.size() - 1)
                self.imageCanvas.itemconfig(self.showPicture, image = self.imageToUse)

        self.listBox = Listbox(self.master, width = 50, height = 15)
        self.listBox.place(x = 5, y = 5)

        self.selecionarImagem = Button(self.master, text = "Selecionar imagem", width = 42, height = 2, command = OpenImage)
        self.selecionarImagem.place(x = 5, y = 265)

        self.removerImagem = Button(self.master, text = "Remover imagem", width = 42, height = 2, command = RemoveImage)
        self.removerImagem.place(x = 5, y = 325)

        self.imageCanvas = Canvas(self.master, width = 400, relief = "sunken", bd = "3")
        self.imageCanvas.place(x = 400, y = 5)

        self.lastPic1 = Button(self.master, text = "<<", width = 13, height = 1, command = LastPic1)
        self.lastPic1.place(x = 400, y = 300)

        self.previousPic = Button(self.master, text = "<", width = 13, height = 1, command = PreviousImage)
        self.previousPic.place(x = 500, y = 300)

        self.nextPic = Button(self.master, text = ">", width = 13, height = 1, command = NextImage)
        self.nextPic.place(x = 600, y = 300)

        self.lastPic2 = Button(self.master, text = ">>", width = 13, height = 1, command = LastPic2)
        self.lastPic2.place(x = 700, y = 300)

if __name__ == '__main__':
    root = Tk()
    app = MainProgram(root)
    root.mainloop()
