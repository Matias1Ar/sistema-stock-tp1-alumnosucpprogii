from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Tienda")
window.geometry("800x800")
#variables globales
dineroEnCaja=0
producMasV=""
producMenosV=""
ProMventas=0.0
window.resizable(0,0)
#productos

def  crear_label(frame):
    listaEntry=list()
    nombre=""
    y=30
    Label(frame, text="Tipo : ", font=("Arial  ", 11),bg="dark blue",fg="white").place(x=140, y=30)
    Label(frame, text="Cantidad bodega :", font=("Arial ", 11),bg="dark blue",fg="white").place(x=140, y=60)
    Label(frame, text="Valor unitario : ", font=("Arial ", 11),bg="dark blue",fg="white").place(x=140, y=90)
    Label(frame, text=" Cantidad vendida :", font=("Arial ", 11),bg="dark blue",fg="white").place(x=140, y=120)
    Label(frame, text=" Cantidad minima : ", font=("Arial ", 11),bg="dark blue",fg="white").place(x=140, y=150)
    for  i in  range(5):
        if i == 0:
            prod_nom = Label(frame, text="", font=("Arial black ", 13), )
            prod_nom.place(x=0, y=0)
            listaEntry.append(prod_nom)

        entry_resultados = Entry(frame)
        entry_resultados.configure(width="13")
        entry_resultados.place(x=270,y=y)
        listaEntry.append(entry_resultados)
        y+=30
    return  listaEntry
#cargar resultado de productos
def cargarProductos(listaResultados,tipo,cantidadB,valorU,cantidasV,cantidadM,producto):
    listaResultados[0].config(text=producto)
    listaResultados[1].insert(0,tipo)
    listaResultados[2].insert(0,cantidadB)
    listaResultados[3].insert(0,valorU)
    listaResultados[4].insert(0,cantidasV)
    listaResultados[5].insert(0,cantidadM)
    for i in range(1,6):
        listaResultados[i].config(state="disable")
def crearBotones(frame):
    listaBtnes = list()
    btnAbastecer = Button(frame,width="14",height="2",text="Abastecer")
    btnAbastecer.place(x=5,y=250)
    btnVender = Button(frame,width="14",height="2",text="Vender")
    btnVender.place(x=130,y=250)
    btnCambiar = Button(frame,width="14",height="2",text="Cambiar")
    btnCambiar.place(x=255,y=250)
    listaBtnes.append(btnAbastecer)
    listaBtnes.append(btnVender)
    listaBtnes.append(btnCambiar)
    return listaBtnes


#frameproductos1
miFrame1 = Frame(window,width="400", height="320",bd="10",relief="groove",bg="dark blue")
miFrame1.grid(row=0,column=0)
producto1="lapiz"

#frameproductos2
producto2="aspirina"
miFrame2 = Frame(window,width="400", height="320",bd="10",relief="groove",bg="dark blue")
miFrame2.grid(row=0,column=1)
#frameproducto3
producto3="borrador"
miFrame3= Frame(window,width="400", height="320",bd="10",relief="groove",bg="dark blue")
miFrame3.grid(row=1,column=0)
#frameproducto4
producto4="pan"
miFrame4 = Frame(window,width="400", height="320",bd="10",relief="groove",bg="dark blue")
miFrame4.grid(row=1,column=1)
#frameopciones
miFrameop = Frame(window,width="800", height="160",bd="10",relief="groove",bg="dark blue")
miFrameop.place(x=0,y=640)
#crear label
def vender(listaresultados):
    def  aceptar():
        cantidadB = int(listaresultados[2].get())
        cantV = int(cantidad_V.get())
        if cantV <= cantidadB:
            cantidadB = cantidadB-cantV
            cantidadB=str(cantidadB)
            listaresultados[2].config(state="normal")
            listaresultados[2].delete(0,END)
            listaresultados[2].insert(0,cantidadB)
            listaresultados[2].config(state="disabled")
            window2.destroy()

        else:
            Label(window2, text="No tienes stock ", font=("Arial  ", 11), fg="Red").place(x=0, y=90)
    window2 = Tk()
    window2.title("venta")
    window2.geometry("200x200")
    Label(window2, text="ingrese la cantidad a vender : ", font=("Arial  ", 11)).place(x=0, y=2)
    btnOP1 = Button(window2, width="10", height="1", text="aceptar",command=aceptar)
    btnOP1.place(x=5, y=60)
    cantidad_V = Entry(window2)
    cantidad_V.configure(width="11")
    cantidad_V.place(x=40, y=30)
#crear botones






    #DESACTIVAR ENTRYS


#creando labels
listaresfr1=crear_label(miFrame1)
listaresfr2=crear_label(miFrame2)
listaresfr3=crear_label(miFrame3)
listaresfr4=crear_label(miFrame4)
#cargarproductos
cargarframe1=cargarProductos(listaresfr1,"Papeleria",18,550.0,0,5,producto1)
cargarframe2=cargarProductos(listaresfr2,"Drogueria",25,109.5,0,8,producto2)
cargarframe3=cargarProductos(listaresfr3,"Papeleria",30,207.3,0,10,producto3)
cargarframe4=cargarProductos(listaresfr4,"Supermercado",15,150.0,0,20,producto4)
#venderRestar en stock



def  modficarV(listaresultados):
    return  None







#venderframee1
listaBfram1=crearBotones(miFrame1)
def vende1():
    vender(listaresfr1)
listaBfram1[1].config(command=vende1)
#venderframe2
listaBfram2=crearBotones(miFrame2)
def vende2():
    vender(listaresfr2)
listaBfram2[1].config(command=vende2)
#venderframe3
listaBfram3=crearBotones(miFrame3)
def vende3():
    vender(listaresfr3)
listaBfram3[1].config(command=vende3)
#vendeframe4
listaBfram4=crearBotones(miFrame4)
def vende4():
    vender(listaresfr4)
listaBfram4[1].config(command=vende4)
#Botones opciones
Label(miFrameop, text="Opciones: ", font=("Arial  ", 11), bg="dark blue", fg="white").place(x=0, y=0)
btnOP1 = Button(miFrameop, width="30", height="1", text="Producto Más vendido")
btnOP1.place(x=5, y=30)
btnOP2 = Button(miFrameop, width="30", height="1", text="Producto Menos Vendido")
btnOP2.place(x=250, y=30)
btnOP3 = Button(miFrameop, width="30", height="1", text="Dinero en Caja")
btnOP3.place(x=5, y=60)
btnOP4 = Button(miFrameop, width="30", height="1", text="Promedio de Ventas")
btnOP4.place(x=250, y=60)


window.mainloop()
