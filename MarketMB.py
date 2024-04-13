'''
PROYECTO FINAL PROGRAMACIÓN IV
Integrantes:
-Brandon Castaño Galeano
-Melissa Henao Cardona

05 diciembre 2022
'''

from tkinter import *
from DatosRT import DatosR
from DatosDomi import DatosD
import os

class ventana:
    def __init__(self,ancho,alto):
        self.Ventana= Tk()
        self.ancho= ancho
        self.alto= alto

    def Recoger(self):
        self.Ventana.destroy()
        v1= DatosR(700,600)
        v1.DatosRT()
    
    def Domicilios(self):
        self.Ventana.destroy()
        v2= DatosD(700,650)
        v2.DatosDm()
    
    def Principal(self):
        self.Ventana.geometry(str(self.ancho)+"x"+str(self.alto))
        self.Ventana.config(bg='#f5f5cb')
        self.Ventana.title("SupermercadoMB")
        self.Ventana.resizable(width=0,height=0)
        self.icono= PhotoImage(file="imagenes/icono.png")
        self.fondo= PhotoImage(file="imagenes/LogoMB.png")
        self.bienv= PhotoImage(file="imagenes/Bienvenida.png")
        self.photob1= PhotoImage(file="imagenes/RecogerTienda.png")
        self.photob2= PhotoImage(file="imagenes/Domicilio.png")
        self.welcome= Label(image=self.bienv, bd=0)
        self.welcome.place(x=200,y=270)    
        self.logo= Label(image= self.fondo, bd=0)
        self.logo.place(x=300,y=0)
        self.boton1= Button(self.Ventana, image=self.photob1, command=self.Recoger, relief="flat", overrelief="raised",borderwidth=5,cursor="hand2")
        self.boton1.place(bordermode=INSIDE, x=200, y=350)
        self.boton2= Button(self.Ventana, image=self.photob2, command=self.Domicilios, relief="flat", overrelief="raised",borderwidth=5,cursor="hand2")
        self.boton2.place(bordermode=INSIDE, x=480, y=350)
        self.Ventana.iconphoto(True,self.icono)
        self.Ventana.mainloop()
        return self.Ventana
    


        
asdf= ventana(900,600)
asdf.Principal()
if os.path.isfile("recolecta.txt") or os.path.isfile("precios.txt"): 
    os.remove("recolecta.txt")
    os.remove("precios.txt")
else:
    print("\t\t=============================================================")
    print("\t\t   Tenga feliz dia y gracias por visitar SUPERMERCADOS MB")
    print("\t\t=============================================================")