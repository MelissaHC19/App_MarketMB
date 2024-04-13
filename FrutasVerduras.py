from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import os
import tkinter as tk
import Menu
import Comprobante as Fc

class frutas:
    def __init__(self,ancho,alto):
        self.ventana= Tk()
        self.ancho= ancho
        self.alto= alto
        self.add= PhotoImage(file=("imagenes/añadir.png"))
        self.devolver= PhotoImage(file=("imagenes/devolver.png"))
        self.finalizar= PhotoImage(file=("imagenes/Finalizar.png"))
        self.pricesFv= [11000,500,2500,11000,600,1000,14000,600,8500]

    def retorno(self):
        if os.path.isfile("precios.txt"):
            if self.preciosT.closed == False:
                self.preciosT.close() 
            else:
                pass
        else:
            pass
        self.ventana.destroy()
        mp= Menu.MenuP(900,600)
        mp.catalogo()

    def GuardarDatos(self,index):
        self.preciosT= open("precios.txt","a")
        self.preciosT.write(f"{self.pricesFv[index]}\n")
    
    def fin(self):
        if os.path.isfile("precios.txt"):
            if self.preciosT.closed == False:
                self.preciosT.close()
            else:
                pass
            self.ventana.destroy()
            v6= Fc.facturacion(900,700)
            v6.facturaCompleta()
        else:
            messagebox.showerror(title="Error Productos",message="No hay productos registrados, ingrese al menos uno")
      

    def menuF(self):
        self.cat1= PhotoImage(file="imagenes/catFV.png")  
        self.ventana.geometry(str(self.ancho)+"x"+str(self.alto)) 
        self.ventana.resizable(width=0,height=0)
        self.ventana.title("Frutas y Verduras")
        self.logo= tk.Label(image=self.cat1, bd=0)
        self.logo.place(x=0,y=0)
        self.b01= tk.Button(image=self.devolver,command=self.retorno,relief="flat",overrelief="raised",bd=3,cursor="hand2")
        self.b01.place(x=27,y=21)
        self.b02= tk.Button(image=self.finalizar,command=self.fin,relief="flat",overrelief="raised",bd=3,cursor="hand2")
        self.b02.place(x=550,y=21)
        #11
        self.b1= tk.Button(image=self.add,command=self.manzanas,relief="flat",overrelief="raised",bd=3,cursor="hand2")
        self.b1.place(x=101,y=291)
        #12
        self.b2= tk.Button(image=self.add,command=self.banano,relief="flat",overrelief="raised",bd=3,cursor="hand2")
        self.b2.place(x=308,y=291)
        #13
        self.b3= tk.Button(image=self.add,command=self.pera,relief="flat",overrelief="raised",bd=3,cursor="hand2")
        self.b3.place(x=516,y=291)
        #21
        self.b4= tk.Button(image=self.add,command=self.lechuga,relief="flat",overrelief="raised",bd=3,cursor="hand2")
        self.b4.place(x=102,y=469)
        #22
        self.b5= tk.Button(image=self.add,command=self.tomate,relief="flat",overrelief="raised",bd=3,cursor="hand2")
        self.b5.place(x=307,y=469)
        #23
        self.b6= tk.Button(image=self.add,command=self.aguacate,relief="flat",overrelief="raised",bd=3,cursor="hand2")
        self.b6.place(x=517,y=469)
        #31
        self.b7= tk.Button(image=self.add,command=self.sandia,relief="flat",overrelief="raised",bd=3,cursor="hand2")
        self.b7.place(x=102,y=646)
        #32
        self.b8= tk.Button(image=self.add,command=self.cebolla,relief="flat",overrelief="raised",bd=3,cursor="hand2")
        self.b8.place(x=307,y=646)
        #33
        self.b7= tk.Button(image=self.add,command=self.brocoli,relief="flat",overrelief="raised",bd=3,cursor="hand2")
        self.b7.place(x=519,y=646)
        self.ventana.mainloop()
    
    def manzanas(self):
        messagebox.showinfo(message="Producto agregado satisfactoriamente")
        self.GuardarDatos(0)
    def banano(self):
        messagebox.showinfo(message="Producto agregado satisfactoriamente")
        self.GuardarDatos(1)
    def pera(self):
        messagebox.showinfo(message="Producto agregado satisfactoriamente")
        self.GuardarDatos(2)
    def lechuga(self):
        messagebox.showinfo(message="Producto agregado satisfactoriamente")
        self.GuardarDatos(3)
    def tomate(self):
        messagebox.showinfo(message="Producto agregado satisfactoriamente")
        self.GuardarDatos(4)
    def aguacate(self):
        messagebox.showinfo(message="Producto agregado satisfactoriamente")
        self.GuardarDatos(5)
    def sandia(self):
        messagebox.showinfo(message="Producto agregado satisfactoriamente")
        self.GuardarDatos(6)
    def cebolla(self):
        messagebox.showinfo(message="Producto agregado satisfactoriamente")
        self.GuardarDatos(7)
    def brocoli(self):
        messagebox.showinfo(message="Producto agregado satisfactoriamente")
        self.GuardarDatos(8)
#v3=frutas(700,700)
#v3.menuF() 

