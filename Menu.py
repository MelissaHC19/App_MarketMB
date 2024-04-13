from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import tkinter as tk
import FrutasVerduras as Fv
import Lacteos as Lc
import Carnes as Cn

class MenuP:
    def __init__(self, ancho, alto):
        self.ventana= Tk()
        self.ancho= ancho
        self.alto= alto
        self.MB= PhotoImage(file="imagenes/LogoMB.png")
        self.logo1= PhotoImage(file="imagenes/botonFrutas.png")
        self.logo2= PhotoImage(file="imagenes/botonLacteos.png")
        self.logo3= PhotoImage(file="imagenes/botonCarnes.png")
        self.cat2= PhotoImage(file="imagenes/catL.png")        
        self.cat3= PhotoImage(file="imagenes/catC.png")
        self.sec= PhotoImage(file="imagenes/Secciones.png")
    
    def frutasVerduraS(self):
        self.ventana.destroy()
        v3=Fv.frutas(700,700)
        v3.menuF()

    def lacteoS(self):
        self.ventana.destroy()
        v4=Lc.lacteos(700,700)
        v4.menuL() 

    def carnes(self):
        self.ventana.destroy()
        v5=Cn.Carnes(700,700)
        v5.menuC() 

    def catalogo(self):
        self.ventana.geometry(str(self.ancho)+"x"+str(self.alto))
        self.ventana.config(bg=('#f5f5cb'))
        self.ventana.resizable(width=0,height=0)
        self.ventana.title("Catálogo")
        self.logo= tk.Label(image=self.MB, bd=0)
        self.logo.place(x=300,y=0)
        self.letraSec= tk.Label(image=self.sec,bd=0)
        self.letraSec.place(x=250,y=285)
        #Frutas y Verduras
        self.letra1= tk.Label(text="Frutas y Verduras",font=("Lucida Sans Unicode", 15),bg=("#ffd69e"),bd=0,width=20,height=8,anchor="n").place(x=63,y=370)
        self.frutas= tk.Button(image=self.logo1,bg=('white'),command=self.frutasVerduraS,height=133,relief="flat",overrelief="raised",cursor="hand2").place(x=80,y=400)
        #Lacteos
        self.letra2= tk.Label(text="Lácteos",font=("Lucida Sans Unicode", 15),bg=("#ffd69e"),bd=0,width=20,height=8,anchor="n").place(x=333,y=370)
        self.leche= tk.Button(image=self.logo2,bg=('white'),command=self.lacteoS,relief="flat",overrelief="raised",bd=2,cursor="hand2").place(x=350,y=400)
        #Carnes 
        self.letra3= tk.Label(text="Pollo, Carnes y Pescado",font=("Lucida Sans Unicode", 15),bg=("#ffd69e"),bd=0,width=20,height=8,anchor="n").place(x=603,y=370)
        self.carnes= tk.Button(image=self.logo3,bg=('white'),command=self.carnes,relief="flat",overrelief="raised",bd=2,cursor="hand2").place(x=620,y=400)
        self.ventana.mainloop()



