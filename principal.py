from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import os

master = tk.Tk()
master.geometry("1000x550")
master.title("Supermercado")

def AbastecerLapiz():
    cantAct=int(EntryCant_IzAr.get())
    cantMin=int(EntryCantMin_IzAr.get())
    if cantAct <= cantMin:
        cantAct+=1
        EntryCant_IzAr.config(state=NORMAL)
        EntryCant_IzAr.delete(0, END)
        EntryCant_IzAr.insert(0,cantAct)
        EntryCant_IzAr.config(state=DISABLED)


def AbastecerBorrador():
    cantAct=int(EntryCant_IzAb.get())
    cantMin = int(EntryCantMin_IzAb.get())
    if cantAct <= cantMin:
        cantAct+=1
        EntryCant_IzAb.config(state=NORMAL)
        EntryCant_IzAb.delete(0, END)
        EntryCant_IzAb.insert(0,cantAct)
        EntryCant_IzAb.config(state=DISABLED)


def AbastecerAspirina():
    cantAct=int(EntryCant_DerArr.get())
    cantMin = int(EntryCantMin_DerArr.get())
    if cantAct <= cantMin:
        cantAct+=1
        EntryCant_DerArr.config(state=NORMAL)
        EntryCant_DerArr.delete(0, END)
        EntryCant_DerArr.insert(0,cantAct)
        EntryCant_DerArr.config(state=DISABLED)


def AbastecerPan():
    cantAct=int(EntryCant_DerAb.get())
    cantMin = int(EntryCantMin_DerAb.get())
    if cantAct <= cantMin:
        cantAct+=1
        EntryCant_DerAb.config(state=NORMAL)
        EntryCant_DerAb.delete(0, END)
        EntryCant_DerAb.insert(0,cantAct)
        EntryCant_DerAb.config(state=DISABLED)

def VenderLapiz():
    cantAct = int(EntryCant_IzAr.get())
    if cantAct > 0:
        cantAct -= 1
        EntryCant_IzAr.config(state=NORMAL)
        EntryCant_IzAr.delete(0, END)
        EntryCant_IzAr.insert(0,cantAct)
        EntryCant_IzAr.config(state=DISABLED)

        ventAct= int(EntryCantVen_IzAr.get())
        ventAct+=1
        EntryCantVen_IzAr.config(state=NORMAL)
        EntryCantVen_IzAr.delete(0, END)
        EntryCantVen_IzAr.insert(0,ventAct)
        EntryCantVen_IzAr.config(state=DISABLED)


def VenderBorrador():
    cantAct = int(EntryCant_IzAb.get())
    if cantAct > 0:
        cantAct -= 1
        EntryCant_IzAb.config(state=NORMAL)
        EntryCant_IzAb.delete(0, END)
        EntryCant_IzAb.insert(0, cantAct)
        EntryCant_IzAb.config(state=DISABLED)

        ventAct = int(EntryCantVen_IzAb.get())
        ventAct += 1
        EntryCantVen_IzAb.config(state=NORMAL)
        EntryCantVen_IzAb.delete(0, END)
        EntryCantVen_IzAb.insert(0, ventAct)
        EntryCantVen_IzAb.config(state=DISABLED)

def VenderAspirina():
    cantAct = int(EntryCant_DerArr.get())
    if cantAct > 0:
        cantAct -= 1
        EntryCant_DerArr.config(state=NORMAL)
        EntryCant_DerArr.delete(0, END)
        EntryCant_DerArr.insert(0, cantAct)
        EntryCant_DerArr.config(state=DISABLED)

        ventAct = int(EntryCantVen_DerArr.get())
        ventAct += 1
        EntryCantVen_DerArr.config(state=NORMAL)
        EntryCantVen_DerArr.delete(0, END)
        EntryCantVen_DerArr.insert(0, ventAct)
        EntryCantVen_DerArr.config(state=DISABLED)


def VenderPan():
    cantAct = int(EntryCant_DerAb.get())
    if cantAct > 0:
        cantAct -= 1
        EntryCant_DerAb.config(state=NORMAL)
        EntryCant_DerAb.delete(0, END)
        EntryCant_DerAb.insert(0, cantAct)
        EntryCant_DerAb.config(state=DISABLED)

        ventAct = int(EntryCantVen_DerAb.get())
        ventAct += 1
        EntryCantVen_DerAb.config(state=NORMAL)
        EntryCantVen_DerAb.delete(0, END)
        EntryCantVen_DerAb.insert(0, ventAct)
        EntryCantVen_DerAb.config(state=DISABLED)

def CambiarLapiz():
    EntryCant_IzAr.config(state=NORMAL)
    EntryVal_IzAr.config(state=NORMAL)
    EntryCantVen_IzAr.config(state=NORMAL)
    EntryCantMin_IzAr.config(state=NORMAL)
    BotCambiar_IzAr.config(text="Guardar",command=FinalizarCambioLapiz, bg="green")

def FinalizarCambioLapiz():
    Cant=EntryCant_IzAr.get()
    Valor=EntryVal_IzAr.get()
    CantVen=EntryCantVen_IzAr.get()
    CantMin=EntryCantMin_IzAr.get()

    EntryCant_IzAr.delete(0, END)
    EntryCant_IzAr.insert(0, Cant)

    EntryVal_IzAr.delete(0, END)
    EntryVal_IzAr.insert(0, Valor)

    EntryCantVen_IzAr.delete(0, END)
    EntryCantVen_IzAr.insert(0, CantVen)

    EntryCantMin_IzAr.delete(0, END)
    EntryCantMin_IzAr.insert(0, CantMin)

    EntryCant_IzAr.config(state=DISABLED)
    EntryVal_IzAr.config(state=DISABLED)
    EntryCantVen_IzAr.config(state=DISABLED)
    EntryCantMin_IzAr.config(state=DISABLED)
    BotCambiar_IzAr.config(text="Cambiar",command=CambiarLapiz,bg="SystemButtonFace")

def CambiarBorrador():
    EntryCant_IzAb.config(state=NORMAL)
    EntryVal_IzAb.config(state=NORMAL)
    EntryCantVen_IzAb.config(state=NORMAL)
    EntryCantMin_IzAb.config(state=NORMAL)
    BotCambiar_IzAb.config(text="Guardar",command=FinalizarCambioBorrador, bg="green")

def FinalizarCambioBorrador():
    Cant=EntryCant_IzAb.get()
    Valor=EntryVal_IzAb.get()
    CantVen=EntryCantVen_IzAb.get()
    CantMin=EntryCantMin_IzAb.get()

    EntryCant_IzAb.delete(0, END)
    EntryCant_IzAb.insert(0, Cant)

    EntryVal_IzAb.delete(0, END)
    EntryVal_IzAb.insert(0, Valor)

    EntryCantVen_IzAb.delete(0, END)
    EntryCantVen_IzAb.insert(0, CantVen)

    EntryCantMin_IzAb.delete(0, END)
    EntryCantMin_IzAb.insert(0, CantMin)

    EntryCant_IzAb.config(state=DISABLED)
    EntryVal_IzAb.config(state=DISABLED)
    EntryCantVen_IzAb.config(state=DISABLED)
    EntryCantMin_IzAb.config(state=DISABLED)
    BotCambiar_IzAb.config(text="Cambiar",command=CambiarBorrador,bg="SystemButtonFace")

def CambiarAspirina():
    EntryCant_DerArr.config(state=NORMAL)
    EntryVal_DerArr.config(state=NORMAL)
    EntryCantVen_DerArr.config(state=NORMAL)
    EntryCantMin_DerArr.config(state=NORMAL)
    BotCambiar_DerArr.config(text="Guardar",command=FinalizarCambioAspirina, bg="green")

def FinalizarCambioAspirina():
    Cant=EntryCant_DerArr.get()
    Valor=EntryVal_DerArr.get()
    CantVen=EntryCantVen_DerArr.get()
    CantMin=EntryCantMin_DerArr.get()

    EntryCant_DerArr.delete(0, END)
    EntryCant_DerArr.insert(0, Cant)

    EntryVal_DerArr.delete(0, END)
    EntryVal_DerArr.insert(0, Valor)

    EntryCantVen_DerArr.delete(0, END)
    EntryCantVen_DerArr.insert(0, CantVen)

    EntryCantMin_DerArr.delete(0, END)
    EntryCantMin_DerArr.insert(0, CantMin)

    EntryCant_DerArr.config(state=DISABLED)
    EntryVal_DerArr.config(state=DISABLED)
    EntryCantVen_DerArr.config(state=DISABLED)
    EntryCantMin_DerArr.config(state=DISABLED)
    BotCambiar_DerArr.config(text="Cambiar",command=CambiarAspirina,bg="SystemButtonFace")

def CambiarPan():
    EntryCant_DerAb.config(state=NORMAL)
    EntryVal_DerAb.config(state=NORMAL)
    EntryCantVen_DerAb.config(state=NORMAL)
    EntryCantMin_DerAb.config(state=NORMAL)
    BotCambiar_DerAb.config(text="Guardar",command=FinalizarCambioPan, bg="green")

def FinalizarCambioPan():
    Cant=EntryCant_DerAb.get()
    Valor=EntryVal_DerAb.get()
    CantVen=EntryCantVen_DerAb.get()
    CantMin=EntryCantMin_DerAb.get()

    EntryCant_DerAb.delete(0, END)
    EntryCant_DerAb.insert(0, Cant)

    EntryVal_DerAb.delete(0, END)
    EntryVal_DerAb.insert(0, Valor)

    EntryCantVen_DerAb.delete(0, END)
    EntryCantVen_DerAb.insert(0, CantVen)

    EntryCantMin_DerAb.delete(0, END)
    EntryCantMin_DerAb.insert(0, CantMin)

    EntryCant_DerAb.config(state=DISABLED)
    EntryVal_DerAb.config(state=DISABLED)
    EntryCantVen_DerAb.config(state=DISABLED)
    EntryCantMin_DerAb.config(state=DISABLED)
    BotCambiar_DerAb.config(text="Cambiar",command=CambiarPan,bg="SystemButtonFace")

def ProdMasVend():
    lapiz=int(EntryCantVen_IzAr.get())
    borrador=int(EntryCantVen_IzAb.get())
    aspirina=int(EntryCantVen_DerArr.get())
    pan=int(EntryCantVen_DerAb.get())
    mayor=0
    if lapiz > borrador:
        if lapiz > aspirina:
            if lapiz > pan:
                mayor = LabelCantVenIzqAr
    if borrador > lapiz:
        if borrador > aspirina:
            if borrador > pan:
                mayor = LabelCantVenIzqAb
    if aspirina > borrador:
        if aspirina> lapiz:
            if aspirina > pan:
                mayor = LabelCantVenDerArr
    if pan > borrador:
        if pan> lapiz:
            if pan > aspirina:
                mayor = LabelCantVenDerAb
    if mayor != 0:
        mayor.config(bg="green")
        BotVender_DerAb.config(state=DISABLED)
        BotVender_DerArr.config(state=DISABLED)
        BotVender_IzAb.config(state=DISABLED)
        BotVender_IzAr.config(state=DISABLED)
        BotProdMasVend.config(text="Dejar de resaltar producto mas vendido",command=lambda: DejarResMasVen(mayor),bg="green",width=30)

def DejarResMasVen(mayor):
    mayor.config(bg="SystemButtonFace")
    BotVender_DerAb.config(state=NORMAL)
    BotVender_DerArr.config(state=NORMAL)
    BotVender_IzAb.config(state=NORMAL)
    BotVender_IzAr.config(state=NORMAL)
    BotProdMasVend.config(text="Mostrar producto mas vendido",width=25,command=ProdMasVend,bg="SystemButtonFace")

def ProdMenVend():
    lapiz=int(EntryCantVen_IzAr.get())
    borrador=int(EntryCantVen_IzAb.get())
    aspirina=int(EntryCantVen_DerArr.get())
    pan=int(EntryCantVen_DerAb.get())
    menor=0
    if lapiz < borrador:
        if lapiz < aspirina:
            if lapiz < pan:
                menor = LabelCantVenIzqAr
    if borrador < lapiz:
        if borrador < aspirina:
            if borrador < pan:
                menor = LabelCantVenIzqAb
    if aspirina < borrador:
        if aspirina < lapiz:
            if aspirina < pan:
                menor = LabelCantVenDerArr
    if pan < borrador:
        if pan < lapiz:
            if pan < aspirina:
                menor = LabelCantVenDerAb
    if menor != 0:
        menor.config(bg="red")
        BotVender_DerAb.config(state=DISABLED)
        BotVender_DerArr.config(state=DISABLED)
        BotVender_IzAb.config(state=DISABLED)
        BotVender_IzAr.config(state=DISABLED)
        BotProdMenVend.config(text="Dejar de resaltar producto menos vendido",command=lambda: DejarResMenVen(menor),bg="red",width=32)

def DejarResMenVen(menor):
    menor.config(bg="SystemButtonFace")
    BotVender_DerAb.config(state=NORMAL)
    BotVender_DerArr.config(state=NORMAL)
    BotVender_IzAb.config(state=NORMAL)
    BotVender_IzAr.config(state=NORMAL)
    BotProdMenVend.config(text="Mostrar producto menos vendido",width=25,command=ProdMenVend,bg="SystemButtonFace")

def PromVent():
    cantLapiz=int(EntryCantVen_IzAr.get())
    cantBorrador=int(EntryCantVen_IzAb.get())
    cantAspirina=int(EntryCantVen_DerArr.get())
    cantPan=int(EntryCantVen_DerAb.get())

    valLapiz=float(EntryVal_IzAr.get())
    valBorrador=float(EntryVal_IzAb.get())
    valAspirina=float(EntryVal_DerArr.get())
    valPan=float(EntryVal_DerAb.get())

    lapiz=cantLapiz*valLapiz
    borrador=cantBorrador*valBorrador
    aspirina=cantAspirina*valAspirina
    pan=cantPan*valPan

    total=lapiz+(lapiz*0.16)+borrador+(borrador*0.16)+aspirina+(aspirina*0.12)+pan+(pan*0.4)
    promedio=total/4
    promedio=str(promedio)
    LabelProm=Label(frameInf,text="Promedio de ventas: $"+promedio)
    LabelProm.grid(row=1,column=2)
    BotPromVent.config(text="Dejar de mostrar promedio",bg="yellow",command= lambda: OcultPromVent(LabelProm))

    def OcultPromVent(LabelProm):
        LabelProm.grid_forget()
        BotPromVent.config(text="Mostrar promedio ventas",width=25,command=PromVent,bg="SystemButtonFace")

def DineroCaja():
    cantLapiz=int(EntryCantVen_IzAr.get())
    cantBorrador=int(EntryCantVen_IzAb.get())
    cantAspirina=int(EntryCantVen_DerArr.get())
    cantPan=int(EntryCantVen_DerAb.get())

    valLapiz=float(EntryVal_IzAr.get())
    valBorrador=float(EntryVal_IzAb.get())
    valAspirina=float(EntryVal_DerArr.get())
    valPan=float(EntryVal_DerAb.get())

    lapiz=cantLapiz*valLapiz
    borrador=cantBorrador*valBorrador
    aspirina=cantAspirina*valAspirina
    pan=cantPan*valPan

    total=lapiz+(lapiz*0.16)+borrador+(borrador*0.16)+aspirina+(aspirina*0.12)+pan+(pan*0.4)
    total=str(total)
    LabelDinero=Label(frameInf,text="Dinero en caja: $"+total)
    LabelDinero.grid(row=1,column=1)
    BotDinero.config(text="Dejar de mostrar dinero en caja",bg="green",command= lambda: OcultDineroCaja(LabelDinero))

    def OcultDineroCaja(LabelDinero):
        LabelDinero.grid_forget()
        BotDinero.config(text="Mostrar Dinero en caja",width=25,command=DineroCaja,bg="SystemButtonFace")

frameIzqArr=Frame(master, width=400, height=200, highlightbackground = "black", highlightthickness = 1)
frameIzqAba=Frame(master, width=400, height=200, highlightbackground = "black", highlightthickness = 1)
frameDerArr=Frame(master, width=400, height=200, highlightbackground = "black", highlightthickness = 1)
frameDerAba=Frame(master, width=400, height=200, highlightbackground = "black", highlightthickness = 1)
frameInf=Frame(master, width=800,height=200,highlightbackground = "black", highlightthickness = 1)

master.grid_rowconfigure(2, weight=1)
master.grid_columnconfigure(1, weight=1)

frameIzqArr.grid(row=0,column=0)
frameIzqAba.grid(row=1,column=0)
frameDerArr.grid(row=0,column=1)
frameDerAba.grid(row=1,column=1)
frameInf.grid(row=2,column=0,columnspan=2)


#########################Frame izquierda-arriba#########################
frameactual=frameIzqArr
frameactual.grid_rowconfigure(2,weight=1)
frameactual.grid_columnconfigure(2,weight=1)
#Titulo del frame izquierdo arriba
Label(frameactual,text="Lapiz").grid(row=0,column=0,rowspan=2)

#Imagen identificativa del producto
img_IzAr = ImageTk.PhotoImage(Image.open("lapiz.bmp"))
panelimg_IzAr = Label(frameactual, image = img_IzAr)
panelimg_IzAr.grid(row=1,rowspan=5,column=0)

#Etiquetas de entradas
Label(frameactual,text="Tipo:",width=20,anchor="w").grid(row=1,column=1)
Label(frameactual,text="Cantidad bodega:",width=20,anchor="w").grid(row=2,column=1)
Label(frameactual,text="Valor unitario:",width=20,anchor="w").grid(row=3,column=1)
LabelCantVenIzqAr=Label(frameactual,text="Cantidad vendidas:",width=20,anchor="w")
LabelCantVenIzqAr.grid(row=4,column=1)
Label(frameactual,text="Cantidad minima:",width=20,anchor="w").grid(row=5,column=1)

#Entradas
#Entrada tipo
EntryTipo_IzAr=Entry(frameactual)
EntryTipo_IzAr.insert(0,"Papelería")
EntryTipo_IzAr.configure(state=DISABLED)
EntryTipo_IzAr.grid(row=1,column=2)

#Entrada cantidad
EntryCant_IzAr=Entry(frameactual)
EntryCant_IzAr.insert(0,"18")
EntryCant_IzAr.configure(state=DISABLED)
EntryCant_IzAr.grid(row=2,column=2)

#Entrada valor unitario
EntryVal_IzAr=Entry(frameactual)
EntryVal_IzAr.insert(0,"550.0")
EntryVal_IzAr.configure(state=DISABLED)
EntryVal_IzAr.grid(row=3,column=2)

#Entrada Cantidad vendida
EntryCantVen_IzAr=Entry(frameactual)
EntryCantVen_IzAr.insert(0,"0")
EntryCantVen_IzAr.configure(state=DISABLED)
EntryCantVen_IzAr.grid(row=4,column=2)

#Entrada Cantidad minima
EntryCantMin_IzAr=Entry(frameactual)
EntryCantMin_IzAr.insert(0,"5")
EntryCantMin_IzAr.configure(state=DISABLED)
EntryCantMin_IzAr.grid(row=5,column=2)

#Botones


#Boton de abastecer
BotAbast_IzAr=Button(frameactual,text="Abastecer",width=20,command=AbastecerLapiz)
BotAbast_IzAr.grid(row=6,column=0)

#Boton de vender
BotVender_IzAr=Button(frameactual,text="Vender",width=20,command=VenderLapiz)
BotVender_IzAr.grid(row=6,column=1)

#Boton de cambiar
BotCambiar_IzAr=Button(frameactual,text="Cambiar",width=20,command=CambiarLapiz)
BotCambiar_IzAr.grid(row=6,column=2)








#########################Frame izquierda-abajo#########################
frameactual=frameIzqAba
frameactual.grid_rowconfigure(2,weight=1)
frameactual.grid_columnconfigure(2,weight=1)
#Titulo del frame izquierdo arriba
Label(frameactual,text="Borrador").grid(row=0,column=0)

#Imagen identificativa del producto
img_IzAb = ImageTk.PhotoImage(Image.open("borrador.bmp"))
panelimg_IzAb = Label(frameactual, image = img_IzAb)
panelimg_IzAb.grid(row=1,rowspan=5,column=0)

#Etiquetas de entradas
Label(frameactual,text="Tipo:",width=20,anchor="w").grid(row=1,column=1)
Label(frameactual,text="Cantidad bodega:",width=20,anchor="w").grid(row=2,column=1)
Label(frameactual,text="Valor unitario:",width=20,anchor="w").grid(row=3,column=1)
LabelCantVenIzqAb=Label(frameactual,text="Cantidad vendidas:",width=20,anchor="w")
LabelCantVenIzqAb.grid(row=4,column=1)
Label(frameactual,text="Cantidad minima:",width=20,anchor="w").grid(row=5,column=1)

#Entradas
#Entrada tipo
EntryTipo_IzAb=Entry(frameactual)
EntryTipo_IzAb.insert(0,"Papelería")
EntryTipo_IzAb.configure(state=DISABLED)
EntryTipo_IzAb.grid(row=1,column=2)

#Entrada cantidad
EntryCant_IzAb=Entry(frameactual)
EntryCant_IzAb.insert(0,"30")
EntryCant_IzAb.configure(state=DISABLED)
EntryCant_IzAb.grid(row=2,column=2)

#Entrada valor unitario
EntryVal_IzAb=Entry(frameactual)
EntryVal_IzAb.insert(0,"207.3")
EntryVal_IzAb.configure(state=DISABLED)
EntryVal_IzAb.grid(row=3,column=2)

#Entrada Cantidad vendida
EntryCantVen_IzAb=Entry(frameactual)
EntryCantVen_IzAb.insert(0,"0")
EntryCantVen_IzAb.configure(state=DISABLED)
EntryCantVen_IzAb.grid(row=4,column=2)

#Entrada Cantidad minima
EntryCantMin_IzAb=Entry(frameactual)
EntryCantMin_IzAb.insert(0,"10")
EntryCantMin_IzAb.configure(state=DISABLED)
EntryCantMin_IzAb.grid(row=5,column=2)

#Botones
#Boton de abastecer
BotAbast_IzAb=Button(frameactual,text="Abastecer",width=20,command=AbastecerBorrador)
BotAbast_IzAb.grid(row=6,column=0)

#Boton de vender
BotVender_IzAb=Button(frameactual,text="Vender",width=20,command=VenderBorrador)
BotVender_IzAb.grid(row=6,column=1)

#Boton de cambiar
BotCambiar_IzAb=Button(frameactual,text="Cambiar",width=20,command=CambiarBorrador)
BotCambiar_IzAb.grid(row=6,column=2)




#########################Frame derecha arriba#########################
frameactual=frameDerArr
frameactual.grid_rowconfigure(2,weight=1)
frameactual.grid_columnconfigure(2,weight=1)
#Titulo del frame izquierdo arriba
Label(frameactual,text="Aspirina").grid(row=0,column=0)

#Imagen identificativa del producto
img_DerArr = ImageTk.PhotoImage(Image.open("aspirina.bmp"))
panelimg_DerArr = Label(frameactual, image = img_DerArr)
panelimg_DerArr.grid(row=1,rowspan=5,column=0)

#Etiquetas de entradas
Label(frameactual,text="Tipo:",width=20,anchor="w").grid(row=1,column=1)
Label(frameactual,text="Cantidad bodega:",width=20,anchor="w").grid(row=2,column=1)
Label(frameactual,text="Valor unitario:",width=20,anchor="w").grid(row=3,column=1)
LabelCantVenDerArr=Label(frameactual,text="Cantidad vendidas:",width=20,anchor="w")
LabelCantVenDerArr.grid(row=4,column=1)
Label(frameactual,text="Cantidad minima:",width=20,anchor="w").grid(row=5,column=1)

#Entradas
#Entrada tipo
EntryTipo_DerArr=Entry(frameactual)
EntryTipo_DerArr.insert(0,"Drogueria")
EntryTipo_DerArr.configure(state=DISABLED)
EntryTipo_DerArr.grid(row=1,column=2)

#Entrada cantidad
EntryCant_DerArr=Entry(frameactual)
EntryCant_DerArr.insert(0,"25")
EntryCant_DerArr.configure(state=DISABLED)
EntryCant_DerArr.grid(row=2,column=2)

#Entrada valor unitario
EntryVal_DerArr=Entry(frameactual)
EntryVal_DerArr.insert(0,"109.5")
EntryVal_DerArr.configure(state=DISABLED)
EntryVal_DerArr.grid(row=3,column=2)

#Entrada Cantidad vendida
EntryCantVen_DerArr=Entry(frameactual)
EntryCantVen_DerArr.insert(0,"0")
EntryCantVen_DerArr.configure(state=DISABLED)
EntryCantVen_DerArr.grid(row=4,column=2)

#Entrada Cantidad minima
EntryCantMin_DerArr=Entry(frameactual)
EntryCantMin_DerArr.insert(0,"8")
EntryCantMin_DerArr.configure(state=DISABLED)
EntryCantMin_DerArr.grid(row=5,column=2)

#Botones
#Boton de abastecer
BotAbast_DerArr=Button(frameactual,text="Abastecer",width=20,command=AbastecerAspirina)
BotAbast_DerArr.grid(row=6,column=0)

#Boton de vender
BotVender_DerArr=Button(frameactual,text="Vender",width=20,command=VenderAspirina)
BotVender_DerArr.grid(row=6,column=1)

#Boton de cambiar
BotCambiar_DerArr=Button(frameactual,text="Cambiar",width=20,command=CambiarAspirina)
BotCambiar_DerArr.grid(row=6,column=2)








#########################Frame derecha abajo#########################
frameactual=frameDerAba
frameactual.grid_rowconfigure(2,weight=1)
frameactual.grid_columnconfigure(2,weight=1)
#Titulo del frame izquierdo arriba
Label(frameactual,text="Pan").grid(row=0,column=0)

#Imagen identificativa del producto
img_DerAb = ImageTk.PhotoImage(Image.open("pan.bmp"))
panelimg_DerAb = Label(frameactual, image = img_DerAb)
panelimg_DerAb.grid(row=1,rowspan=5,column=0)

#Etiquetas de entradas
Label(frameactual,text="Tipo:",width=20,anchor="w").grid(row=1,column=1)
Label(frameactual,text="Cantidad bodega:",width=20,anchor="w").grid(row=2,column=1)
Label(frameactual,text="Valor unitario:",width=20,anchor="w").grid(row=3,column=1)
LabelCantVenDerAb=Label(frameactual,text="Cantidad vendidas:",width=20,anchor="w")
LabelCantVenDerAb.grid(row=4,column=1)
Label(frameactual,text="Cantidad minima:",width=20,anchor="w").grid(row=5,column=1)

#Entradas
#Entrada tipo
EntryTipo_DerAb=Entry(frameactual)
EntryTipo_DerAb.insert(0,"Supermercado")
EntryTipo_DerAb.configure(state=DISABLED)
EntryTipo_DerAb.grid(row=1,column=2)

#Entrada cantidad
EntryCant_DerAb=Entry(frameactual)
EntryCant_DerAb.insert(0,"15")
EntryCant_DerAb.configure(state=DISABLED)
EntryCant_DerAb.grid(row=2,column=2)

#Entrada valor unitario
EntryVal_DerAb=Entry(frameactual)
EntryVal_DerAb.insert(0,"150.0")
EntryVal_DerAb.configure(state=DISABLED)
EntryVal_DerAb.grid(row=3,column=2)

#Entrada Cantidad vendida
EntryCantVen_DerAb=Entry(frameactual)
EntryCantVen_DerAb.insert(0,"0")
EntryCantVen_DerAb.configure(state=DISABLED)
EntryCantVen_DerAb.grid(row=4,column=2)

#Entrada Cantidad minima
EntryCantMin_DerAb=Entry(frameactual)
EntryCantMin_DerAb.insert(0,"20")
EntryCantMin_DerAb.configure(state=DISABLED)
EntryCantMin_DerAb.grid(row=5,column=2)

#Botones
#Boton de abastecer
BotAbast_DerAb=Button(frameactual,text="Abastecer",width=20,command=AbastecerPan)
BotAbast_DerAb.grid(row=6,column=0)

#Boton de vender
BotVender_DerAb=Button(frameactual,text="Vender",width=20,command=VenderPan)
BotVender_DerAb.grid(row=6,column=1)

#Boton de cambiar
BotCambiar_DerAb=Button(frameactual,text="Cambiar",width=20,command=CambiarPan)
BotCambiar_DerAb.grid(row=6,column=2)

#########################Frame Inferior#########################
frameactual=frameInf
frameactual.grid_rowconfigure(2,weight=1)
frameactual.grid_columnconfigure(1,weight=1)

#Botones
#Boton de producto mas vendido
BotProdMasVend=Button(frameactual,text="Mostrar producto mas vendido",width=25,command=ProdMasVend)
BotProdMasVend.grid(row=0,column=0)

#Boton de producto menos vendido
BotProdMenVend=Button(frameactual,text="Mostrar producto menos vendido",width=25,command=ProdMenVend)
BotProdMenVend.grid(row=0,column=1)

#Boton promedio de ventas
BotPromVent=Button(frameactual,text="Mostrar promedio ventas",width=25,command=PromVent)
BotPromVent.grid(row=0,column=2)

#Dinero en caja
BotDinero=Button(frameactual,text="Mostrar Dinero en caja",width=25,command=DineroCaja)
BotDinero.grid(row=1,column=0)

master.mainloop()