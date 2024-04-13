from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import *
import tkinter as tk
from Menu import MenuP

class DatosR:
    def __init__(self,ancho,alto):
        self.ventana= Tk()
        self.ancho= ancho
        self.alto= alto
        self.MB= PhotoImage(file="imagenes/LogoMB.png")
    
    def llamado(self):
        ciudad= self.ciudad.get()
        nombre= self.nombre.get()
        docu= self.documento.get()
        tel= self.celular.get()
        hora= self.horasDis.get()
        if ciudad == "" or nombre == "" or docu == "" or tel == "" or hora == "":
            messagebox.showerror(message="Hay campos sin llenar",title="Fields Error")  
        else:
            messagebox.showinfo(message="Datos ingresados satisfactoriamente",title="Info")
            miArch= 'recolecta.txt'
            self.f= open(miArch,"a")
            self.f.write(f"{nombre}\n{ciudad}\n{docu}\n{tel}\n{hora}\nRecoger en tienda")          
            self.ventana.destroy()
            self.f.close()
            mp= MenuP(900,600)
            mp.catalogo()
    
    def DatosRT(self):
        self.ventana.geometry(str(self.ancho)+"x"+str(self.alto))
        self.ventana.config(bg=('#f5f5cb'))
        self.ventana.resizable(width=0,height=0)
        self.ventana.title("Registrar Datos Entrega")
        self.ingresar= PhotoImage(file="imagenes/ingreseDatos.png")
        self.logo= tk.Label(image=self.MB, bd=0)
        self.logo.place(x=200,y=0)
        self.InDat= tk.Label(image=self.ingresar,bd=0)
        self.InDat.place(x=200,y=285)
        #Ciudad
        self.labCiu= Label(self.ventana,text="Sede: ", font=("Lucida Sans Unicode",13),background=('#f5f5cb')).place(x=100,y=340)
        self.ciudad= ttk.Combobox(self.ventana,values=("Pereira","Dosquebradas","La Virginia"),font=("Tahoma"),state="readonly")
        self.ciudad.place(x=370,y=340)
        #Nombre
        self.labNom= Label(self.ventana,text="Nombre de quien recoge: ", font=("Lucida Sans Unicode",13),background=('#f5f5cb')).place(x=100,y=380)
        self.nombre= ttk.Entry(self.ventana,width=25,font=("Tahoma"))
        self.nombre.place(x=370,y=380)
        #Documento
        self.labDoc= Label(self.ventana,text="Documento: ", font=("Lucida Sans Unicode",13),background=('#f5f5cb')).place(x=100,y=420)
        self.documento= ttk.Entry(self.ventana,width=15,font=("Tahoma"))
        self.documento.place(x=370,y=420)
        #Celular
        self.labCel= Label(self.ventana,text="Teléfono de contacto: ", font=("Lucida Sans Unicode",13),background=('#f5f5cb')).place(x=100,y=460)
        self.celular= ttk.Entry(self.ventana,width=15,font=("Tahoma"))
        self.celular.place(x=370,y=460)
        #Hora
        self.labHora= Label(self.ventana,text="Hora de entrega: ", font=("Lucida Sans Unicode",13),background=('#f5f5cb')).place(x=100,y=500)
        self.horasDis= ttk.Combobox(self.ventana,values=("11:00 AM","12:00 M","1:00 PM","2:00 PM","3:00 PM","4:00 PM"),font=("Tahoma"),width=13,state="readonly")
        self.horasDis.place(x=370,y=500)
        #Boton
        self.buton= tk.Button(self.ventana, text="Registrar y continuar", font=("Tahoma", 12),command=self.llamado,relief="flat", overrelief="raised",bg=("#aad450"),borderwidth=3,cursor="hand2")
        self.buton.place(x=260,y=550)


    

