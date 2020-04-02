from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Tienda")
window.geometry("800x800")
#variables
producto1="lapiz"
producto2="aspirina"
producto3="borrador"
producto4="pan"
productom=""
resultado="1"
window.resizable(0,0)
#frameproductos1
miFrame1 = Frame(window,width="400", height="320",bd="10",relief="groove",bg="dark blue")
miFrame1.grid(row=0,column=0)
#frameproductos2
miFrame2 = Frame(window,width="400", height="320",bd="10",relief="groove",bg="dark blue")
miFrame2.grid(row=0,column=1)
#frameproducto3
miFrame3= Frame(window,width="400", height="320",bd="10",relief="groove",bg="dark blue")
miFrame3.grid(row=1,column=0)
#frameproducto4
miFrame4 = Frame(window,width="400", height="320",bd="10",relief="groove",bg="dark blue")
miFrame4.grid(row=1,column=1)
#frameopciones
miFrameop = Frame(window,width="800", height="160",bd="10",relief="groove",bg="dark blue")
miFrameop.place(x=0,y=640)
#crear label
def  crear_label(frame,nombre):
    listaEntry=list()
    y=30
    prod_nom=Label(frame, text=nombre, font=("Arial black ", 13),)
    prod_nom.place(x=0, y=0)
    Label(frame, text="Tipo : ", font=("Arial ", 11),bg="dark blue",fg="white").place(x=140, y=30)
    Label(frame, text="Cantidad bodega :", font=("Arial ", 11),bg="dark blue",fg="white").place(x=140, y=60)
    Label(frame, text="Valor unitario : ", font=("Arial ", 11),bg="dark blue",fg="white").place(x=140, y=90)
    Label(frame, text=" Cantidad vendida :", font=("Arial ", 11),bg="dark blue",fg="white").place(x=140, y=120)
    Label(frame, text=" Cantidad minima : ", font=("Arial ", 11),bg="dark blue",fg="white").place(x=140, y=150)
    for  i in  range(5):
        entry_resultados = Entry(frame)
        entry_resultados.configure(width="11")
        entry_resultados.place(x=270,y=y)
        listaEntry.append(entry_resultados)
        y+=30
    return  listaEntry
#crear botones
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


def cargarProductos(listaResultados,resulta1,resulta2,resulta3,resulta4,resulta5):
    listaResultados[0].insert(0,resulta1)
    listaResultados[1].insert(0,resulta2)
    listaResultados[2].insert(0,resulta3)
    listaResultados[3].insert(0,resulta4)
    listaResultados[4].insert(0,resulta5)
    #DESACTIVAR ENTRYS
    for i in range(5):
        listaResultados[i].config(state="disabled")


#creando labels
listaresfr1=crear_label(miFrame1,producto1)
listaresfr2=crear_label(miFrame2,producto2)
listaresfr3=crear_label(miFrame3,producto3)
listaresfr4=crear_label(miFrame4,producto4)
#cargarproductos
cargarframe1=cargarProductos(listaresfr1,"papeleria",18,550.0,0,5)
cargarframe2=cargarProductos(listaresfr2,"papeleria",18,550.0,0,5)
cargarframe3=cargarProductos(listaresfr3,"papeleria",18,550.0,0,5)
cargarframe4=cargarProductos(listaresfr4,"papeleria",18,550.0,0,5)



#Creando botones
listaBfram1=crearBotones(miFrame1)
listaBfram2=crearBotones(miFrame2)
listaBfram3=crearBotones(miFrame3)
listaBfram4=crearBotones(miFrame4)
window.mainloop()