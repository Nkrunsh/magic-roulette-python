from tkinter import messagebox, Label, Tk, END, Menu, Button
from tkinter.ttk import Combobox, Entry
from tkinter import filedialog 
import tkinter.font as font
import random, time

class UI:
    def __init__(self):

        #---- WINDOW OBJECT -----
        self.window = Tk()
        self.window.title("Ruleta Mágica ABG") 
        self.window.resizable(width=False, height=False)
        self.menubar = Menu(self.window)
        self.window.config(menu=self.menubar)
        self.window.configure(background='#ffffff')
        self.factorForma = 2.2

        #self.resolution = Menu(self.menubar,tearoff=0)
        #self.resolution.add_command(label="Normal", command=self.setSize(1.0))
        #self.resolution.add_command(label="Medio", command=self.setSize(1.6))
        #self.resolution.add_command(label="Grande", command=self.setSize(2.3))

        self.menubar.add_command(label = "Abrir", command=self.findFile)
        #self.menubar.add_cascade(label="Tamaño", menu=self.resolution)
        
        # ----- FONTS -----
        self.statusFont = font.Font(family='Consolas', size= int(10 * self.factorForma),  weight='bold')
        self.titleFont = font.Font(family='Lucida Console', size=int(20 * self.factorForma), weight='normal')
        self.winnerFont = font.Font(family='Bahnschrift', size = int(50 * self.factorForma))
        self.buttonFont = font.Font(family='Helvetica', size = int(20 * self.factorForma))        

        #---- VARIABLES ----
        self.participants = []
        self.loadedList = False

        #---- UI OBJECTS ----
        #self.openFile_btn = Button(self.window, text="Abrir Archivo", command=self.findFile)
        self.fileSelected_lbl = Label(self.window, text="  Aún no se ha cargado una lista de sorteo  ",font=self.statusFont , bg='#EC3E3E', fg='#ffffff')
        self.winnerTitle_lbl = Label(self.window, text="Gran Seleccionado",font=self.titleFont, bg='#ffffff', fg='#0052cc')
        self.winner_lbl = Label(self.window, text="--",font=self.winnerFont,fg='#0052cc', bg='#ffffff')
        self.getWinner_btn = Button(self.window, text="Obtener", command=self.getOpcion, bg='#0052cc', fg='#ffffff')
        self.getWinner_btn['font'] = self.buttonFont
        
    def drawUI(self):
        #---- Margen Izq y Der -----
        self.window.grid_columnconfigure(0, minsize=100 * self.factorForma)
        self.window.grid_columnconfigure(3, minsize=100 * self.factorForma)

        self.window.grid_rowconfigure(0, minsize=30 * self.factorForma)     # Margen 1
        self.fileSelected_lbl.grid(column =1, row=0)                        # Label Archivo Seleccionado
        self.window.grid_rowconfigure(2, minsize=10 * self.factorForma)     # Margen 2
        self.winnerTitle_lbl.grid(column =1, row=3)                         # Titulo del Ganador
        self.window.grid_rowconfigure(4, minsize=25 * self.factorForma)     # Margen 3
        self.winner_lbl.grid(column =1, row=5)                              # GANADOR
        self.window.grid_rowconfigure(6, minsize=25 * self.factorForma)     # Margen 4
        self.getWinner_btn.grid(column =1, row=7)                           # Boton
        self.window.grid_rowconfigure(8, minsize=25 * self.factorForma)


    def getOpcion(self):
        if self.loadedList:
            for _ in range(15):
                participant = random.choice(self.participants)
                self.winner_lbl.configure(text = participant)
                time.sleep(0.05)
                self.window.update()
        else:
            messagebox.showinfo(message="Para obtener un resultado, es necesario cargar una lista", title="No hay una lista cargada")

    def setSize(self, factor):
        self.factorForma = factor
        self.window.update()

    def findFile(self):
        self.fileDirectory = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Seleccione un Archivo", 
                                          filetypes = (("Text files", 
                                                        "*.txt*"), 
                                                       ("all files", 
                                                        "*.*")))
        #print(self.fileDirectory)
        try:
            self.getFileName()
            self.fileSelected_lbl.configure(text=f'Se ha cargado el archivo: {self.fileName}', bg='#ffffff', fg='#2AEC45')
            self.getParticipants()
            self.loadedList = True
        except:
            pass

    def getFileName(self):
        i = self.fileDirectory.index("/")
        i = i + 1
        self.fileName = self.fileDirectory[i:]
        print(self.fileName)
        while True:
            try:
                i = self.fileName.index("/")
            except:
                break
            if i >= 0:
                i = i + 1
                self.fileName= self.fileName[i:]   

    def getParticipants(self):
        try:
            self.f = open(self.fileDirectory)
        except:
            print("Un error al abrir el archivo")
        
        
        lines = self.f.readlines()
        for line in lines:
            self.participants.append(line[0:-2])            
                                                       
        if not self.f.closed:
            self.f.close() 
            if self.participants == []:
                messagebox.showinfo(message="El archivo seleccionado esta vacio", title="Alerta")


    def getfileDirectory(self):
        return self.fileDirectory
        
    def run(self):
        self.drawUI()
        self.window.mainloop()


if __name__ == "__main__":
    program = UI()
    program.run()