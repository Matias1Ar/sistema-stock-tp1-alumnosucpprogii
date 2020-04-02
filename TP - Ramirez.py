
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
import tkinter.font as font
import json

with open("stock.json", encoding ="utf-8-sig") as archivo:
    lista = json.load (archivo)

with open("ventas.json", encoding ="utf-8-sig") as archivo:
    lista_ventas = json.load (archivo)

window = Tk()
window.wm_title("Ventas & Stock")
window.config(background = "#F3F3F3")
window.geometry("900x700+10+20")
window.resizable(0,0)
style = ttk.Style()
style.configure('TButton', foreground='Blue', borderwidth=30,relief='groove', padding=7)

#imageEx = PhotoImage(file = 'pic06.gif',width=200,height=330)##### nombre de la image
#Label(window, image=imageEx).place(x=490, y=40)##### Ingresa las coordenadas de la imagen



def start():
    callable(panel01())
    callable(panel02())
    callable(panel03())
    callable(panel04())
    callable(panel05())






def panel01():
    recuadro01 = Canvas(window, width=435,
                height=280,
                borderwidth=2,bd=2,
                background='#F3F3F3',
                relief='groove')
    recuadro01.place(x=4, y=10)
    global lbl01
    lbl01 = Label(window,width=5, text="Lapiz", font="Arial")
    lbl01.place(x=15, y=3)
    global Entry_lap01
    Entry_lap01 = Entry(window, text="",width=13)
    Entry_lap01.place(x=240, y=75)
    global Entry_lap02
    Entry_lap02 = Entry(window, text="",width=13)
    Entry_lap02.place(x=240, y=103)
    global Entry_lap03
    Entry_lap03 = Entry(window, text="",width=13)
    Entry_lap03.place(x=240, y=133)
    global Entry_lap04
    Entry_lap04 = Entry(window, text="",width=13)
    Entry_lap04.place(x=240, y=163)
    global Entry_lap05
    Entry_lap05 = Entry(window, text="",width=13)
    Entry_lap05.place(x=240, y=193)

    lapiz_lbl01 = Label(window,width=6, text="Tipo:", font="Arial")
    lapiz_lbl01.place(x=90, y=75)
    global lapiz_lbl02
    lapiz_lbl02 = Label(window,width=15, text="Cantidad Bodega:", font="Arial")
    lapiz_lbl02.place(x=90, y=105)
    lapiz_lbl03 = Label(window,width=15, text="Valor Unitario:", font="Arial")
    lapiz_lbl03.place(x=90, y=130)
    lapiz_lbl04 = Label(window,width=15, text="Cantidad Vendidas:", font="Arial")
    lapiz_lbl04.place(x=90, y=160)
    lapiz_lbl05 = Label(window,width=15, text="Cantidad Minima:", font="Arial")
    lapiz_lbl05.place(x=90, y=190)

    rectang01 = Label(window, text=f"",width=15, borderwidth=4, relief="groove")
    rectang01.place(x=340, y=75)
    rectang02 = Label(window, text=f"",width=15, borderwidth=4, relief="groove")
    rectang02.place(x=340, y=105)
    rectang03 = Label(window, text=f"",width=15, borderwidth=2, relief="groove")
    rectang03.place(x=340, y=135)
    rectang04 = Label(window, text=f"",width=15, borderwidth=2, relief="groove")
    rectang04.place(x=340, y=165)
    rectang05 = Label(window, text=f"",width=15, borderwidth=2, relief="groove")
    rectang05.place(x=340, y=195)

    global button00
    button00 = Button(window, text="Abastecer",width=20, command=agregar)
    button00.place(x=13, y=250)
    global button01
    button01 = Button(window, text="Vender",width=20, command=vender)
    button01.place(x=155, y=250)
    global button02
    button02 = Button(window, text="Confirmar",width=20, command=Confirmar)
    button02.place(x=297, y=250)

def Confirmar():
    global producto
    producto = Entry_lap01.get()
    etq01 = Label(window, text=f"{producto}",width=15, borderwidth=4, relief="groove")
    etq01.place(x=340, y=75)
    global bodega
    bodega = int(Entry_lap02.get())
    etq02 = Label(window, text=f"{bodega}",width=15, borderwidth=4, relief="groove")
    etq02.place(x=340, y=105)
    global valor
    valor = int(Entry_lap03.get())
    etq03 = Label(window, text=f"{valor}",width=15, borderwidth=4, relief="groove")
    etq03.place(x=340, y=135)
    global vendidos
    vendidos = int(Entry_lap04.get())
    etq04 = Label(window, text=f"{vendidos}",width=15, borderwidth=4, relief="groove")
    etq04.place(x=340, y=165)
    global stock
    stock = int(Entry_lap05.get())
    etq05 = Label(window, text=f"{stock}",width=15, borderwidth=4, relief="groove")
    etq05.place(x=340, y=195)
    Entry_lap01.destroy()
    Entry_lap02.destroy()
    Entry_lap03.destroy()
    Entry_lap04.destroy()
    Entry_lap05.destroy()

def buscar_datos():
    etq01 = Label(window, text=f"{producto}",width=15, borderwidth=4, relief="groove")
    etq01.place(x=340, y=75)
    etq02 = Label(window, text=f"{bodega}",width=15, borderwidth=4, relief="groove")
    etq02.place(x=340, y=105)
    etq03 = Label(window, text=f"{valor}",width=15, borderwidth=4, relief="groove")
    etq03.place(x=340, y=135)
    etq04 = Label(window, text=f"{vendidos}",width=15, borderwidth=4, relief="groove")
    etq04.place(x=340, y=165)
    etq05 = Label(window, text=f"{stock}",width=15, borderwidth=4, relief="groove")
    etq05.place(x=340, y=195)
    button00 = Button(window, text="Abastecer",width=20, command=agregar)
    button00.place(x=13, y=250)
    button01 = Button(window, text="Vender",width=20, command=vender)
    button01.place(x=155, y=250)
    button02 = Button(window, text="Confirmar",width=20, command=Confirmar)
    button02.place(x=297, y=250)

def agregar():
    button01.state(['disabled'])
    button02.state(['disabled'])
    global Entry_00
    Entry_00 = Entry(window, text="",width=15)
    Entry_00.place(x=340, y=103)
    button00 = Button(window, text="Confirmar",width=20, command=confirma_stock)
    button00.place(x=13, y=250)

def confirma_stock():
    ingreso = int(Entry_00.get())
    global bodega
    bodega = int(bodega + ingreso)
    global suma
    etq02 = Label(window, text=f"{bodega}",width=15, borderwidth=4, relief="groove")
    etq02.place(x=340, y=105)
    Entry_00.destroy()
    print(bodega)
    callable(buscar_datos())

def vender():
    global vendidos
    vendidos += 1
    global bodega
    bodega -= 1
    etq04 = Label(window, text=f"{vendidos}",width=15, borderwidth=4, relief="groove")
    etq04.place(x=340, y=165)
    etq05 = Label(window, text=f"{bodega}",width=15, borderwidth=4, relief="groove")
    etq05.place(x=340, y=105)
    global costoLpz01
    costoLpz01 = float(vendidos * valor)
    rectang03 = Label(window, font='Arial', text="Costo Total $"+f"{costoLpz01}",width=18, borderwidth=5, relief="groove")
    rectang03.place(x=140, y=229)
    if bodega < stock:
        etq05 = Label(window, text=f"{stock}"+"  !!",width=15,borderwidth=2, relief="groove")
        etq05.place(x=340, y=195)
        etq05.configure(foreground="white", background="red")



def panel02():
    recuadro02 = Canvas(window, width=435,
                height=280,
                borderwidth=2,bd=2,
                background='#F3F3F3',
                relief='groove')
    recuadro02.place(x=4, y=303)
    global lbl77
    lbl77 = Label(window,width=8, text="Borrador", font="Arial")
    lbl77.place(x=15, y=295)

    global Entry_lap06
    Entry_lap06 = Entry(window, text="",width=13)
    Entry_lap06.place(x=240, y=375)
    global Entry_lap07
    Entry_lap07 = Entry(window, text="",width=13)
    Entry_lap07.place(x=240, y=403)
    global Entry_lap08
    Entry_lap08 = Entry(window, text="",width=13)
    Entry_lap08.place(x=240, y=433)
    global Entry_lap09
    Entry_lap09 = Entry(window, text="",width=13)
    Entry_lap09.place(x=240, y=460)
    global Entry_lap10
    Entry_lap10 = Entry(window, text="",width=13)
    Entry_lap10.place(x=240, y=490)

    lapiz_lbl08 = Label(window,width=6, text="Tipo:", font="Arial")
    lapiz_lbl08.place(x=90, y=375)
    global lapiz_lbl09
    lapiz_lbl09 = Label(window,width=15, text="Cantidad Bodega:", font="Arial")
    lapiz_lbl09.place(x=90, y=403)
    lapiz_lbl10 = Label(window,width=15, text="Valor Unitario:", font="Arial")
    lapiz_lbl10.place(x=90, y=433)
    lapiz_lbl11 = Label(window,width=15, text="Cantidad Vendidas:", font="Arial")
    lapiz_lbl11.place(x=90, y=463)
    lapiz_lbl12 = Label(window,width=15, text="Cantidad Minima:", font="Arial")
    lapiz_lbl12.place(x=90, y=493)

    rectang06 = Label(window, text=f"",width=15, borderwidth=4, relief="groove")
    rectang06.place(x=340, y=375)
    rectang07 = Label(window, text=f"",width=15, borderwidth=4, relief="groove")
    rectang07.place(x=340, y=403)
    rectang08 = Label(window, text=f"",width=15, borderwidth=2, relief="groove")
    rectang08.place(x=340, y=433)
    rectang09 = Label(window, text=f"",width=15, borderwidth=2, relief="groove")
    rectang09.place(x=340, y=463)
    rectang10 = Label(window, text=f"",width=15, borderwidth=2, relief="groove")
    rectang10.place(x=340, y=493)

    global button03
    button03 = Button(window, text="Abastecer",width=20, command=agregar02)
    button03.place(x=13, y=545)
    global button04
    button04 = Button(window, text="Vender",width=20, command=vender02)
    button04.place(x=155, y=545)
    global button05
    button05 = Button(window, text="Confirmar",width=20, command=Confirmar02)
    button05.place(x=297, y=545)

def Confirmar02():
    global producto02
    producto02 = Entry_lap06.get()
    etq01 = Label(window, text=f"{producto02}",width=15, borderwidth=4, relief="groove")
    etq01.place(x=340, y=375)
    global bodega02
    bodega02 = int(Entry_lap07.get())
    etq02 = Label(window, text=f"{bodega02}",width=15, borderwidth=4, relief="groove")
    etq02.place(x=340, y=403)
    global valor02
    valor02 = int(Entry_lap08.get())
    etq03 = Label(window, text=f"{valor02}",width=15, borderwidth=4, relief="groove")
    etq03.place(x=340, y=433)
    global vendidos02
    vendidos02 = int(Entry_lap09.get())
    etq04 = Label(window, text=f"{vendidos02}",width=15, borderwidth=4, relief="groove")
    etq04.place(x=340, y=463)
    global stock02
    stock02 = int(Entry_lap10.get())
    etq05 = Label(window, text=f"{stock02}",width=15, borderwidth=4, relief="groove")
    etq05.place(x=340, y=493)
    Entry_lap06.destroy()
    Entry_lap07.destroy()
    Entry_lap08.destroy()
    Entry_lap09.destroy()
    Entry_lap10.destroy()

def buscar_datos02():
    etq01 = Label(window, text=f"{producto02}",width=15, borderwidth=4, relief="groove")
    etq01.place(x=340, y=375)
    etq02 = Label(window, text=f"{bodega02}",width=15, borderwidth=4, relief="groove")
    etq02.place(x=340, y=403)
    etq03 = Label(window, text=f"{valor02}",width=15, borderwidth=4, relief="groove")
    etq03.place(x=340, y=433)
    etq04 = Label(window, text=f"{vendidos02}",width=15, borderwidth=4, relief="groove")
    etq04.place(x=340, y=463)
    etq05 = Label(window, text=f"{stock02}",width=15, borderwidth=4, relief="groove")
    etq05.place(x=340, y=493)
    button04 = Button(window, text="Abastecer",width=20, command=agregar02)
    button04.place(x=13, y=545)
    button05 = Button(window, text="Vender",width=20, command=vender02)
    button05.place(x=155, y=545)
    button06 = Button(window, text="Confirmar",width=20, command=Confirmar02)
    button06.place(x=297, y=545)

def agregar02():
    button04.state(['disabled'])
    button05.state(['disabled'])
    global Entry_02
    Entry_02 = Entry(window, text="",width=15)
    Entry_02.place(x=340, y=403)
    button00 = Button(window, text="Confirmar",width=20, command=confirma_stock02)
    button00.place(x=13, y=545)

def confirma_stock02():
    ingreso02 = int(Entry_02.get())
    global bodega02
    bodega02 = bodega02 + ingreso02
    etq02 = Label(window, text=f"{bodega02}",width=15, borderwidth=4, relief="groove")
    etq02.place(x=340, y=403)
    Entry_02.destroy()
    callable(buscar_datos02())

def vender02():
    global vendidos02
    vendidos02 += 1
    global bodega02
    bodega02 -= 1
    etq04 = Label(window, text=f"{vendidos02}",width=15, borderwidth=4, relief="groove")
    etq04.place(x=340, y=463)
    etq05 = Label(window, text=f"{bodega02}",width=15, borderwidth=4, relief="groove")
    etq05.place(x=340, y=403)
    global costoBor02
    costoBor02 = float(vendidos02 * valor02)
    rectang03 = Label(window, font='Arial', text="Costo Total $"+f"{costoBor02}",width=18, borderwidth=5, relief="groove")
    rectang03.place(x=140, y=523)
    if bodega02 < stock02:
        etq05 = Label(window, text=f"{stock02}"+"  !!",width=15,borderwidth=2, relief="groove")
        etq05.place(x=340, y=493)
        etq05.configure(foreground="white", background="red")


def panel03():
    recuadro03 = Canvas(window, width=435,
                height=280,
                borderwidth=2,bd=2,
                background='#F3F3F3',
                relief='groove')
    recuadro03.place(x=450, y=10)
    ################################################################33

    global lbl74
    lbl74 = Label(window,width=8, text="Aspirina", font="Arial")
    lbl74.place(x=465, y=3)
    global Entry_lap14
    Entry_lap14 = Entry(window, text="",width=13)
    Entry_lap14.place(x=685, y=75)
    global Entry_lap15
    Entry_lap15 = Entry(window, text="",width=13)
    Entry_lap15.place(x=685, y=103)
    global Entry_lap16
    Entry_lap16 = Entry(window, text="",width=13)
    Entry_lap16.place(x=685, y=133)
    global Entry_lap17
    Entry_lap17 = Entry(window, text="",width=13)
    Entry_lap17.place(x=685, y=163)
    global Entry_lap33
    Entry_lap33 = Entry(window, text="",width=13)
    Entry_lap33.place(x=685, y=193)

    lapiz_lbl13 = Label(window,width=6, text="Tipo:", font="Arial")
    lapiz_lbl13.place(x=530, y=70)
    global lapiz_lbl14
    lapiz_lbl14 = Label(window,width=15, text="Cantidad Bodega:", font="Arial")
    lapiz_lbl14.place(x=530, y=100)
    lapiz_lbl15 = Label(window,width=15, text="Valor Unitario:", font="Arial")
    lapiz_lbl15.place(x=530, y=130)
    lapiz_lbl16 = Label(window,width=15, text="Cantidad Vendidas:", font="Arial")
    lapiz_lbl16.place(x=530, y=160)
    lapiz_lbl17 = Label(window,width=15, text="Cantidad Minima:", font="Arial")
    lapiz_lbl17.place(x=530, y=190)

    rectang01 = Label(window, text=f"",width=15, borderwidth=4, relief="groove")
    rectang01.place(x=785, y=75)
    rectang02 = Label(window, text=f"",width=15, borderwidth=4, relief="groove")
    rectang02.place(x=785, y=105)
    rectang03 = Label(window, text=f"",width=15, borderwidth=2, relief="groove")
    rectang03.place(x=785, y=135)
    rectang04 = Label(window, text=f"",width=15, borderwidth=2, relief="groove")
    rectang04.place(x=785, y=165)
    rectang05 = Label(window, text=f"",width=15, borderwidth=2, relief="groove")
    rectang05.place(x=785, y=195)


    global button06
    button06 = Button(window, text="Abastecer",width=20, command=agregar03)
    button06.place(x=460, y=250)
    global button07
    button07 = Button(window, text="Vender",width=20, command=vender03)
    button07.place(x=603, y=250)
    global button08
    button08 = Button(window, text="Confirmar",width=20, command=Confirmar03)
    button08.place(x=745, y=250)

def Confirmar03():
    global producto03
    producto03 = Entry_lap14.get()
    etq01 = Label(window, text=f"{producto03}",width=15, borderwidth=4, relief="groove")
    etq01.place(x=785, y=75)
    global bodega03
    bodega03 = int(Entry_lap15.get())
    etq02 = Label(window, text=f"{bodega03}",width=15, borderwidth=4, relief="groove")
    etq02.place(x=785, y=105)
    global valor03
    valor03 = int(Entry_lap16.get())
    etq03 = Label(window, text=f"{valor03}",width=15, borderwidth=4, relief="groove")
    etq03.place(x=785, y=135)
    global vendidos03
    vendidos03 = int((Entry_lap17.get()))
    etq04 = Label(window, text=f"{vendidos03}",width=15, borderwidth=4, relief="groove")
    etq04.place(x=785, y=165)
    global stock03
    stock03 = int(Entry_lap33.get())
    etq05 = Label(window, text=f"{stock03}",width=15, borderwidth=4, relief="groove")
    etq05.place(x=785, y=195)
    Entry_lap14.destroy()
    Entry_lap15.destroy()
    Entry_lap16.destroy()
    Entry_lap17.destroy()
    Entry_lap33.destroy()


def buscar_datos03():
    etq01 = Label(window, text=f"{producto03}",width=15, borderwidth=4, relief="groove")
    etq01.place(x=785, y=75)
    etq02 = Label(window, text=f"{bodega03}",width=15, borderwidth=4, relief="groove")
    etq02.place(x=785, y=105)
    etq03 = Label(window, text=f"{valor03}",width=15, borderwidth=4, relief="groove")
    etq03.place(x=785, y=135)
    etq04 = Label(window, text=f"{vendidos03}",width=15, borderwidth=4, relief="groove")
    etq04.place(x=785, y=165)
    etq05 = Label(window, text=f"{stock03}",width=15, borderwidth=4, relief="groove")
    etq05.place(x=785, y=195)
    button06 = Button(window, text="Abastecer",width=20, command=agregar03)
    button06.place(x=460, y=250)
    button07 = Button(window, text="Vender",width=20, command=vender03)
    button07.place(x=603, y=250)
    button08 = Button(window, text="Confirmar",width=20, command=Confirmar03)
    button08.place(x=745, y=250)

def agregar03():
    button07.state(['disabled'])
    button08.state(['disabled'])
    global Entry_03
    Entry_03 = Entry(window, text="",width=15)
    Entry_03.place(x=785, y=105)
    button00 = Button(window, text="Confirmar",width=20, command=confirma_stock03)
    button00.place(x=460, y=250)

def confirma_stock03():
    ingreso03 = int(Entry_03.get())
    global bodega03
    bodega03 = bodega03 + ingreso03
    etq02 = Label(window, text=f"{bodega03}",width=15, borderwidth=4, relief="groove")
    etq02.place(x=785, y=105)
    Entry_03.destroy()
    callable(buscar_datos03())

def vender03():
    global vendidos03
    vendidos03 += 1
    global bodega03
    bodega03 -= 1
    etq04 = Label(window, text=f"{vendidos03}",width=15, borderwidth=4, relief="groove")
    etq04.place(x=785, y=165)
    etq05 = Label(window, text=f"{bodega03}",width=15, borderwidth=4, relief="groove")
    etq05.place(x=785, y=105)
    global costoAsp03
    costoAsp03 = float(vendidos03 * valor03)
    rectang03 = Label(window, font='Arial', text="Costo Total $"+f"{costoAsp03}",width=18, borderwidth=5, relief="groove")
    rectang03.place(x=590, y=229)
    if bodega03 < stock03:
        etq05 = Label(window, text=f"{stock03}"+"  !!",width=15,borderwidth=2, relief="groove")
        etq05.place(x=785, y=195)
        etq05.configure(foreground="white", background="red")


def panel04():
    recuadro04 = Canvas(window, width=435,
                height=280,
                borderwidth=2,bd=2,
                background='#F3F3F3',
                relief='groove')
    recuadro04.place(x=450, y=303)
###########################################################################

    global lbl18
    lbl18 = Label(window,width=5, text="Pan", font="Arial")
    lbl18.place(x=465, y=295)
    global Entry_lap18
    Entry_lap18 = Entry(window, text="",width=13)
    Entry_lap18.place(x=685, y=375)
    global Entry_lap19
    Entry_lap19 = Entry(window, text="",width=13)
    Entry_lap19.place(x=685, y=403)
    global Entry_lap20
    Entry_lap20 = Entry(window, text="",width=13)
    Entry_lap20.place(x=685, y=433)
    global Entry_lap21
    Entry_lap21 = Entry(window, text="",width=13)
    Entry_lap21.place(x=685, y=463)
    global Entry_lap22
    Entry_lap22 = Entry(window, text="",width=13)
    Entry_lap22.place(x=685, y=493)

    lapiz_lbl13 = Label(window,width=6, text="Tipo:", font="Arial")
    lapiz_lbl13.place(x=530, y=375)
    global lapiz_lbl14
    lapiz_lbl14 = Label(window,width=15, text="Cantidad Bodega:", font="Arial")
    lapiz_lbl14.place(x=530, y=403)
    lapiz_lbl15 = Label(window,width=15, text="Valor Unitario:", font="Arial")
    lapiz_lbl15.place(x=530, y=433)
    lapiz_lbl16 = Label(window,width=15, text="Cantidad Vendidas:", font="Arial")
    lapiz_lbl16.place(x=530, y=463)
    lapiz_lbl17 = Label(window,width=15, text="Cantidad Minima:", font="Arial")
    lapiz_lbl17.place(x=530, y=493)

    rectang01 = Label(window, text=f"",width=15, borderwidth=4, relief="groove")
    rectang01.place(x=785, y=375)
    rectang02 = Label(window, text=f"",width=15, borderwidth=4, relief="groove")
    rectang02.place(x=785, y=405)
    rectang03 = Label(window, text=f"",width=15, borderwidth=2, relief="groove")
    rectang03.place(x=785, y=435)
    rectang04 = Label(window, text=f"",width=15, borderwidth=2, relief="groove")
    rectang04.place(x=785, y=465)
    rectang05 = Label(window, text=f"",width=15, borderwidth=2, relief="groove")
    rectang05.place(x=785, y=495)


    global button22
    button22 = Button(window, text="Abastecer",width=20, command=agregar04)
    button22.place(x=460, y=545)
    global button23
    button23 = Button(window, text="Vender",width=20, command=vender04)
    button23.place(x=603, y=545)
    global button24
    button24 = Button(window, text="Confirmar",width=20, command=Confirmar04)
    button24.place(x=745, y=545)


def Confirmar04():
    global producto04
    producto04 = Entry_lap18.get()
    etq01 = Label(window, text=f"{producto04}",width=15, borderwidth=4, relief="groove")
    etq01.place(x=785, y=375)
    global bodega04
    bodega04 = int(Entry_lap19.get())
    etq02 = Label(window, text=f"{bodega04}",width=15, borderwidth=4, relief="groove")
    etq02.place(x=785, y=405)
    global valor04
    valor04 = int(Entry_lap20.get())
    etq03 = Label(window, text=f"{valor04}",width=15, borderwidth=4, relief="groove")
    etq03.place(x=785, y=435)
    global vendidos04
    vendidos04 = int(Entry_lap21.get())
    etq04 = Label(window, text=f"{vendidos04}",width=15, borderwidth=4, relief="groove")
    etq04.place(x=785, y=465)
    global stock04
    stock04 = int(Entry_lap22.get())
    etq05 = Label(window, text=f"{stock04}",width=15, borderwidth=4, relief="groove")
    etq05.place(x=785, y=495)
    Entry_lap18.destroy()
    Entry_lap19.destroy()
    Entry_lap20.destroy()
    Entry_lap21.destroy()
    Entry_lap22.destroy()

def buscar_datos04():
    etq01 = Label(window, text=f"{producto04}",width=15, borderwidth=4, relief="groove")
    etq01.place(x=785, y=375)
    etq02 = Label(window, text=f"{bodega04}",width=15, borderwidth=4, relief="groove")
    etq02.place(x=785, y=405)
    etq03 = Label(window, text=f"{valor04}",width=15, borderwidth=4, relief="groove")
    etq03.place(x=785, y=435)
    etq04 = Label(window, text=f"{vendidos04}",width=15, borderwidth=4, relief="groove")
    etq04.place(x=785, y=465)
    etq05 = Label(window, text=f"{stock04}",width=15, borderwidth=4, relief="groove")
    etq05.place(x=785, y=495)



def agregar04():
    button23.state(['disabled'])
    button24.state(['disabled'])
    global Entry_04
    Entry_04 = Entry(window, text="",width=15)
    Entry_04.place(x=785, y=405)
    button00 = Button(window, text="Confirmar",width=20, command=confirma_stock04)
    button00.place(x=460, y=545)

def confirma_stock04():
    ingreso04 = int(Entry_04.get())
    global bodega04
    bodega04 = bodega04 + ingreso04
    etq02 = Label(window, text=f"{bodega04}",width=15, borderwidth=4, relief="groove")
    etq02.place(x=785, y=405)
    Entry_04.destroy()
    button22 = Button(window, text="Abastecer",width=20, command=agregar04)
    button22.place(x=460, y=545)
    button23 = Button(window, text="Vender",width=20, command=vender04)
    button23.place(x=603, y=545)
    button24 = Button(window, text="Confirmar",width=20, command=Confirmar04)
    button24.place(x=745, y=545)
    callable(buscar_datos04)

def vender04():
    global vendidos04
    vendidos04 += 1
    global bodega04
    bodega04 -= 1
    etq04 = Label(window, text=f"{vendidos04}",width=15, borderwidth=4, relief="groove")
    etq04.place(x=785, y=465)
    etq05 = Label(window, text=f"{bodega04}",width=15, borderwidth=4, relief="groove")
    etq05.place(x=785, y=405)
    global costoPan04
    costoPan04 = float(vendidos04 * valor04)
    rectang03 = Label(window, font='Arial', text="Costo Total $"+f"{costoPan04}",width=18, borderwidth=5, relief="groove")
    rectang03.place(x=590, y=523)
    if bodega04 < stock04:
        etq05 = Label(window, text=f"{stock04}"+"  !!",width=15,borderwidth=2, relief="groove")
        etq05.place(x=785, y=495)
        etq05.configure(foreground="white", background="red")




def panel05():
    recuadro04 = Canvas(window, width=882,
                height=90,
                borderwidth=2,bd=2,
                background='#F3F3F3',
                relief='groove')
    recuadro04.place(x=4, y=598)
    lbl25 = Label(window,width=10, text="Opciones", font="Arial")
    lbl25.place(x=15, y=590)
    button33 = Button(window, text="Productos mas vendido",width=45, command= Prod_masV)
    button33.place(x=10, y=610)

    button34 = Button(window, text="Productos menos vendido",width=45, command=Prod_menV)
    button34.place(x=303, y=610)
    button35 = Button(window, text="Promedio de ventas",width=45, command=Prod_menV)
    button35.place(x=595, y=610)

    button37 = Button(window, text="Dinero en Caja",width=45, command=Totales)
    button37.place(x=303, y=647)


def Totales():
    global monto_total
    monto_total = int(costoLpz01+costoBor02+costoAsp03+costoPan04)

    global etqxx
    etqxx = Label(window, font='Arial', text=" Total de Ventas: $ "+f"{monto_total}",width=32,borderwidth=20, relief="groove")
    etqxx.place(x=10, y=660)
    etqxx.configure(foreground="white", background="red")

def Prod_masV():

    if costoLpz01 > costoBor02 and costoLpz01 > costoAsp03 and costoLpz01 > costoPan04:
        etq00 = Label(window, font='Arial', text="El producto mas vendido es: Lapiz",width=32,borderwidth=20, relief="groove")
        etq00.place(x=10, y=660)
        etq00.configure(foreground="white", background="red")
    elif costoBor02 > costoLpz01 and costoBor02 > costoAsp03 and costoBor02 > costoPan04:
        etq01 = Label(window, font='Arial', text="El producto mas vendido es: Borrador",width=32,borderwidth=20, relief="groove")
        etq01.place(x=10, y=660)
        etq01.configure(foreground="white", background="red")
    elif costoAsp03 > costoLpz01 and costoAsp03 > costoBor02 and costoAsp03 > costoPan04:
        etq02 = Label(window, font='Arial', text="El producto mas vendido es: Aspirina",width=32,borderwidth=20, relief="groove")
        etq02.place(x=10, y=660)
        etq02.configure(foreground="white", background="red")
    elif costoPan04 > costoLpz01 and costoPan04 > costoBor02 and costoPan04 > costoAsp03:
        etq03 = Label(window, font='Arial', text="El producto mas vendido es: Pan",width=32,borderwidth=20, relief="groove")
        etq03.place(x=10, y=660)
        etq03.configure(foreground="white", background="red")

def Prod_menV():

    if costoLpz01 < costoBor02 and costoLpz01 < costoAsp03 and costoLpz01 < costoPan04:
        etq00 = Label(window, font='Arial', text="El producto menos vendido es: Lapiz",width=32,borderwidth=20, relief="groove")
        etq00.place(x=10, y=660)
        etq00.configure(foreground="white", background="red")
    elif costoBor02 < costoLpz01 and costoBor02 < costoAsp03 and costoBor02 < costoPan04:
        etq01 = Label(window, font='Arial', text="El producto menos vendido es: Borrador",width=32,borderwidth=20, relief="groove")
        etq01.place(x=10, y=660)
        etq01.configure(foreground="white", background="red")
    elif costoAsp03 < costoLpz01 and costoAsp03 < costoBor02 and costoAsp03 < costoPan04:
        etq02 = Label(window, font='Arial', text="El producto menos vendido es: Aspirina",width=32,borderwidth=20, relief="groove")
        etq02.place(x=10, y=660)
        etq02.configure(foreground="white", background="red")
    elif costoPan04 < costoLpz01 and costoPan04 < costoBor02 and costoPan04 < costoAsp03:
        etq03 = Label(window, font='Arial', text="El producto menos vendido es: Pan",width=32,borderwidth=20, relief="groove")
        etq03.place(x=10, y=660)
        etq03.configure(foreground="white", background="red")





start()
window.mainloop()

