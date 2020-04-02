from tkinter import*
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox


window = Tk()
window.title("Programación II - Sistema Stock")
window.geometry('1560x780')
#############################################################################################################################################################
#FUNCIONES
#VENTAS

def Venta_Lapiz ():
    bodega_Lapiz = int(lbl_fila2C3_L.cget("text"))
    vender = bodega_Lapiz - 1
    lbl_fila2C3_L.configure(text= int(vender))
    cant_Ventas = int(lbl_fila4C3_L.cget("text"))
    Vendidos = cant_Ventas + 1
    lbl_fila4C3_L.configure(text = int(Vendidos))
    Dinero_venta()

def Venta_Aspirina ():
    bodega_Aspirina = int(lbl_fila2C3_A.cget("text"))
    vender = bodega_Aspirina - 1
    lbl_fila2C3_A.configure(text= int(vender))
    cant_Ventas = int(lbl_fila4C3_A.cget("text"))
    Vendidos = cant_Ventas + 1
    lbl_fila4C3_A.configure(text = int(Vendidos))
    Dinero_venta()

def Venta_Borrador ():
    bodega_Aspirina = int(lbl_fila2C3_B.cget("text"))
    vender = bodega_Aspirina - 1
    lbl_fila2C3_B.configure(text= int(vender))
    cant_Ventas = int(lbl_fila4C3_B.cget("text"))
    Vendidos = cant_Ventas + 1
    lbl_fila4C3_B.configure(text = int(Vendidos))
    Dinero_venta()

def Venta_Pan ():
    bodega_Aspirina = int(lbl_fila2C3_P.cget("text"))
    vender = bodega_Aspirina - 1
    lbl_fila2C3_P.configure(text= int(vender))
    cant_Ventas = int(lbl_fila4C3_P.cget("text"))
    Vendidos = cant_Ventas + 1
    lbl_fila4C3_P.configure(text = int(Vendidos))
    Dinero_venta()


##############################################################
#ABASTECER

def Abastecer_Lapiz():
    bodega_Lapiz = int(lbl_fila2C3_L.cget("text"))
    minimo_Lapiz = int(lbl_fila5C3_L.cget("text"))
    if bodega_Lapiz < minimo_Lapiz:
        ventanaIngresar = tk.Toplevel(window)
        ventanaIngresar.title("Ingresar Datos")
        ventanaIngresar.geometry("240x180")
        Label_1 = Label(ventanaIngresar, text="Ingrese el numero de productos\n que desea agregar")
        Label_1.grid (column = 0, row = 0,sticky = 'n')
        Entry_1 = Entry (ventanaIngresar, relief = 'sunken',bg = 'white',bd = 2, width = 25)
        Entry_1.grid (column = 0, row = 1)
        btn = Button (ventanaIngresar,text = 'AGREGAR',relief = 'raised',bg = 'lightskyblue',bd = 3,height = 1, width = 28,command = lambda : [agregar()])
        btn.grid (column = 0, row = 2)
        def agregar():
            Agr = int(Entry_1.get())
            total = bodega_Lapiz + Agr
            lbl_fila2C3_L.configure(text=int(total))
            ventanaIngresar.destroy()

def Abastecer_Aspirina():
    bodega_Aspirina = int(lbl_fila2C3_A.cget("text"))
    minimo_Aspirina = int(lbl_fila5C3_A.cget("text"))
    if bodega_Aspirina < minimo_Aspirina:
        ventanaIngresar = tk.Toplevel(window)
        ventanaIngresar.title("Ingresar Datos")
        ventanaIngresar.geometry("240x180")
        Label_1 = Label(ventanaIngresar, text="Ingrese el numero de productos\n que desea agregar")
        Label_1.grid (column = 0, row = 0,sticky = 'n')
        Entry_1 = Entry (ventanaIngresar, relief = 'sunken',bg = 'white',bd = 2, width = 25)
        Entry_1.grid (column = 0, row = 1)
        btn = Button (ventanaIngresar,text = 'AGREGAR',relief = 'raised',bg = 'lightskyblue',bd = 3,height = 1, width = 28,command = lambda : [agregar()])
        btn.grid (column = 0, row = 2)
        def agregar():
            Agr = int(Entry_1.get())
            total = bodega_Aspirina + Agr
            lbl_fila2C3_A.configure(text=int(total))
            ventanaIngresar.destroy()

def Abastecer_Borrador():
    bodega_Borrador = int(lbl_fila2C3_B.cget("text"))
    minimo_Borrador = int(lbl_fila5C3_B.cget("text"))
    if bodega_Borrador < minimo_Borrador:
        ventanaIngresar = tk.Toplevel(window)
        ventanaIngresar.title("Ingresar Datos")
        ventanaIngresar.geometry("240x180")
        Label_1 = Label(ventanaIngresar, text="Ingrese el numero de productos\n que desea agregar")
        Label_1.grid (column = 0, row = 0,sticky = 'n')
        Entry_1 = Entry (ventanaIngresar, relief = 'sunken',bg = 'white',bd = 2, width = 25)
        Entry_1.grid (column = 0, row = 1)
        btn = Button (ventanaIngresar,text = 'AGREGAR',relief = 'raised',bg = 'lightskyblue',bd = 3,height = 1, width = 28,command = lambda : [agregar()])
        btn.grid (column = 0, row = 2)
        def agregar():
            Agr = int(Entry_1.get())
            total = bodega_Borrador + Agr
            lbl_fila2C3_B.configure(text=int(total))
            ventanaIngresar.destroy()

def Abastecer_Pan():
    bodega_Pan = int(lbl_fila2C3_P.cget("text"))
    minimo_Pan = int(lbl_fila5C3_P.cget("text"))
    if bodega_Pan < minimo_Pan:
        ventanaIngresar = tk.Toplevel(window)
        ventanaIngresar.title("Ingresar Datos")
        ventanaIngresar.geometry("240x180")
        Label_1 = Label(ventanaIngresar, text="Ingrese el numero de productos\n que desea agregar")
        Label_1.grid (column = 0, row = 0,sticky = 'n')
        Entry_1 = Entry (ventanaIngresar, relief = 'sunken',bg = 'white',bd = 2, width = 25)
        Entry_1.grid (column = 0, row = 1)
        btn = Button (ventanaIngresar,text = 'AGREGAR',relief = 'raised',bg = 'lightskyblue',bd = 3,height = 1, width = 28,command = lambda : [agregar()])
        btn.grid (column = 0, row = 2)
        def agregar():
            Agr = int(Entry_1.get())
            total = bodega_Pan + Agr
            lbl_fila2C3_P.configure(text=int(total))
            ventanaIngresar.destroy()


############################################################################################################################################################
#Producto mas Vendido

def Mas_Vendido():
    Lapiz = int(lbl_fila4C3_L.cget("text"))
    Aspirina = int(lbl_fila4C3_A.cget("text"))
    Borrador = int(lbl_fila4C3_B.cget("text"))
    Pan = int(lbl_fila4C3_P.cget("text"))
    if Lapiz > Aspirina and Lapiz > Borrador and Lapiz > Pan:
        lbl_fila1_Opciones.configure(text = 'Lapiz')
    elif Aspirina > Lapiz and Aspirina > Borrador and Aspirina > Pan:
        lbl_fila1_Opciones.configure(text = 'Aspirina')
    elif Borrador > Lapiz and Borrador > Aspirina and Borrador > Pan:
        lbl_fila1_Opciones.configure(text = 'Borrador')
    elif Pan > Lapiz and Pan > Aspirina and Pan > Borrador:
        lbl_fila1_Opciones.configure(text = 'Pan')
    elif Lapiz == 0 and Aspirina == 0 and Borrador == 0 and Pan == 0:
        messagebox.showinfo('Error', 'No se ha podido analizar\nNO EXISTEN VENTAS REALIZADAS', icon = 'error')
    else:
        messagebox.showinfo('Aviso', 'Existen Varios Productos',icon='warning')


def Menos_Vendido():
    Lapiz = int(lbl_fila4C3_L.cget("text"))
    Aspirina = int(lbl_fila4C3_A.cget("text"))
    Borrador = int(lbl_fila4C3_B.cget("text"))
    Pan = int(lbl_fila4C3_P.cget("text"))
    if Lapiz < Aspirina and Lapiz < Borrador and Lapiz < Pan:
        lbl_fila2_Opciones.configure(text = 'Lapiz')
    elif Aspirina < Lapiz and Aspirina < Borrador and Aspirina < Pan:
        lbl_fila2_Opciones.configure(text = 'Aspirina')
    elif Borrador < Lapiz and Borrador < Aspirina and Borrador < Pan:
        lbl_fila2_Opciones.configure(text = 'Borrador')
    elif Pan < Lapiz and Pan < Aspirina and Pan < Borrador:
        lbl_fila2_Opciones.configure(text = 'Pan')
    elif Lapiz == 0 and Aspirina == 0 and Borrador == 0 and Pan == 0:
        messagebox.showinfo('Error', 'No se ha podido analizar\nNO EXISTEN VENTAS REALIZADAS', icon = 'error')
    else:
        messagebox.showinfo('Aviso', 'Existen Varios Productos',icon='warning')

##############################################################################################################################################################
#DINERO OBTENIDO POR VENTA

def Dinero_venta():
    iva_Lapiz = (float(lbl_fila3C3_L.cget("text"))*16)/100
    iva_Aspirina = (float(lbl_fila3C3_A.cget("text"))*12)/100
    iva_Borrador = (float(lbl_fila3C3_B.cget("text"))*16)/100
    iva_Pan = (float(lbl_fila3C3_P.cget("text"))*4)/100
    precio_Lapiz = float(lbl_fila3C3_L.cget("text")) + iva_Lapiz
    precio_Aspirina = float(lbl_fila3C3_A.cget("text")) + iva_Aspirina
    precio_Borrador = float(lbl_fila3C3_B.cget("text")) + iva_Borrador
    precio_Pan = float(lbl_fila3C3_P.cget("text")) + iva_Pan
    Lapiz_Vendidos = int(lbl_fila4C3_L.cget("text"))
    Aspirina_Vendidos = int(lbl_fila4C3_A.cget("text"))
    Borrador_Vendidos = int(lbl_fila4C3_B.cget("text"))
    Pan_Vendidos = int(lbl_fila4C3_P.cget("text"))
    total_Lapiz = precio_Lapiz * Lapiz_Vendidos
    total_Aspirina = precio_Aspirina * Aspirina_Vendidos
    total_Borrador = precio_Borrador * Borrador_Vendidos
    total_Pan = precio_Pan * Pan_Vendidos
    TOTAL = round (total_Lapiz + total_Aspirina + total_Borrador + total_Pan,2)
    lbl_fila4_Opciones.configure(text = '$' + str(TOTAL))
#############################################################################################################################################################

def Promedio_de_ventas ():
    Lapiz = int(lbl_fila4C3_L.cget("text"))
    Aspirina = int(lbl_fila4C3_A.cget("text"))
    Borrador = int(lbl_fila4C3_B.cget("text"))
    Pan = int(lbl_fila4C3_P.cget("text"))
    Suma = Lapiz + Aspirina + Borrador + Pan
    Promedio = Suma/4
    lbl_fila3_Opciones.configure(text= Promedio)
#############################################################################################################################################################

def Cambiar_Lapiz ():
    ventanaIngresar = tk.Toplevel(window)
    ventanaIngresar.title("Ingresar Datos")
    ventanaIngresar.geometry("240x240")
    Label_1 = Label(ventanaIngresar, text="Modificar Bodega")
    Label_1.grid (column = 0, row = 0,sticky = 'n')
    Entry_1 = Entry (ventanaIngresar, relief = 'sunken',bg = 'white',bd = 2, width = 25)
    Entry_1.grid (column = 0, row = 1)
    Label_2 = Label(ventanaIngresar, text="Modificar Precio")
    Label_2.grid (column = 0, row = 2,sticky = 'n')
    Entry_2 = Entry (ventanaIngresar, relief = 'sunken',bg = 'white',bd = 2, width = 25)
    Entry_2.grid (column = 0, row = 3)
    Label_3 = Label(ventanaIngresar, text="Modificar Cantidad Minima")
    Label_3.grid (column = 0, row = 4,sticky = 'n')
    Entry_3 = Entry (ventanaIngresar, relief = 'sunken',bg = 'white',bd = 2, width = 25)
    Entry_3.grid (column = 0, row = 5)
    btn = Button (ventanaIngresar,text = 'CAMBIAR',relief = 'raised',bg = 'lightskyblue',bd = 3,height = 1, width = 28,command = lambda : [Cambiar()])
    btn.grid (column = 0, row = 6)
    def Cambiar():
        cambio_Bodega = int(Entry_1.get())
        cambio_Precio = float(Entry_2.get())
        cambio_Cminimo = int(Entry_3.get())
        lbl_fila2C3_L.configure(text = cambio_Bodega)
        lbl_fila3C3_L.configure(text = cambio_Precio)
        lbl_fila5C3_L.configure(text = cambio_Cminimo)
        ventanaIngresar.destroy()
#################################################################################################################################################################
def Cambiar_Aspirina ():
    ventanaIngresar = tk.Toplevel(window)
    ventanaIngresar.title("Ingresar Datos")
    ventanaIngresar.geometry("240x240")
    Label_1 = Label(ventanaIngresar, text="Modificar Bodega")
    Label_1.grid (column = 0, row = 0,sticky = 'n')
    Entry_1 = Entry (ventanaIngresar, relief = 'sunken',bg = 'white',bd = 2, width = 25)
    Entry_1.grid (column = 0, row = 1)
    Label_2 = Label(ventanaIngresar, text="Modificar Precio")
    Label_2.grid (column = 0, row = 2,sticky = 'n')
    Entry_2 = Entry (ventanaIngresar, relief = 'sunken',bg = 'white',bd = 2, width = 25)
    Entry_2.grid (column = 0, row = 3)
    Label_3 = Label(ventanaIngresar, text="Modificar Cantidad Minima")
    Label_3.grid (column = 0, row = 4,sticky = 'n')
    Entry_3 = Entry (ventanaIngresar, relief = 'sunken',bg = 'white',bd = 2, width = 25)
    Entry_3.grid (column = 0, row = 5)
    btn = Button (ventanaIngresar,text = 'CAMBIAR',relief = 'raised',bg = 'lightskyblue',bd = 3,height = 1, width = 28,command = lambda : [Cambiar()])
    btn.grid (column = 0, row = 6)
    def Cambiar():
        cambio_Bodega = int(Entry_1.get())
        cambio_Precio = float(Entry_2.get())
        cambio_Cminimo = int(Entry_3.get())
        lbl_fila2C3_A.configure(text = cambio_Bodega)
        lbl_fila3C3_A.configure(text = cambio_Precio)
        lbl_fila5C3_A.configure(text = cambio_Cminimo)
        ventanaIngresar.destroy()

##########################################################################################################################################################################
def Cambiar_Borrador ():
    ventanaIngresar = tk.Toplevel(window)
    ventanaIngresar.title("Ingresar Datos")
    ventanaIngresar.geometry("240x240")
    Label_1 = Label(ventanaIngresar, text="Modificar Bodega")
    Label_1.grid (column = 0, row = 0,sticky = 'n')
    Entry_1 = Entry (ventanaIngresar, relief = 'sunken',bg = 'white',bd = 2, width = 25)
    Entry_1.grid (column = 0, row = 1)
    Label_2 = Label(ventanaIngresar, text="Modificar Precio")
    Label_2.grid (column = 0, row = 2,sticky = 'n')
    Entry_2 = Entry (ventanaIngresar, relief = 'sunken',bg = 'white',bd = 2, width = 25)
    Entry_2.grid (column = 0, row = 3)
    Label_3 = Label(ventanaIngresar, text="Modificar Cantidad Minima")
    Label_3.grid (column = 0, row = 4,sticky = 'n')
    Entry_3 = Entry (ventanaIngresar, relief = 'sunken',bg = 'white',bd = 2, width = 25)
    Entry_3.grid (column = 0, row = 5)
    btn = Button (ventanaIngresar,text = 'CAMBIAR',relief = 'raised',bg = 'lightskyblue',bd = 3,height = 1, width = 28,command = lambda : [Cambiar()])
    btn.grid (column = 0, row = 6)
    def Cambiar():
        cambio_Bodega = int(Entry_1.get())
        cambio_Precio = float(Entry_2.get())
        cambio_Cminimo = int(Entry_3.get())
        lbl_fila2C3_B.configure(text = cambio_Bodega)
        lbl_fila3C3_B.configure(text = cambio_Precio)
        lbl_fila5C3_B.configure(text = cambio_Cminimo)
        ventanaIngresar.destroy()

##############################################################################################################################################################
def Cambiar_Pan ():
    ventanaIngresar = tk.Toplevel(window)
    ventanaIngresar.title("Ingresar Datos")
    ventanaIngresar.geometry("240x240")
    Label_1 = Label(ventanaIngresar, text="Modificar Bodega")
    Label_1.grid (column = 0, row = 0,sticky = 'n')
    Entry_1 = Entry (ventanaIngresar, relief = 'sunken',bg = 'white',bd = 2, width = 25)
    Entry_1.grid (column = 0, row = 1)
    Label_2 = Label(ventanaIngresar, text="Modificar Precio")
    Label_2.grid (column = 0, row = 2,sticky = 'n')
    Entry_2 = Entry (ventanaIngresar, relief = 'sunken',bg = 'white',bd = 2, width = 25)
    Entry_2.grid (column = 0, row = 3)
    Label_3 = Label(ventanaIngresar, text="Modificar Cantidad Minima")
    Label_3.grid (column = 0, row = 4,sticky = 'n')
    Entry_3 = Entry (ventanaIngresar, relief = 'sunken',bg = 'white',bd = 2, width = 25)
    Entry_3.grid (column = 0, row = 5)
    btn = Button (ventanaIngresar,text = 'CAMBIAR',relief = 'raised',bg = 'lightcyan',bd = 3,height = 1, width = 28,command = lambda : [Cambiar()])
    btn.grid (column = 0, row = 6)
    def Cambiar():
        cambio_Bodega = int(Entry_1.get())
        cambio_Precio = float(Entry_2.get())
        cambio_Cminimo = int(Entry_3.get())
        lbl_fila2C3_P.configure(text = cambio_Bodega)
        lbl_fila3C3_P.configure(text = cambio_Precio)
        lbl_fila5C3_P.configure(text = cambio_Cminimo)
        ventanaIngresar.destroy()
#############################################################################################################################################################3
#imagen Lapiz
ventana = Frame(window)
ventana.grid(column = 0, row = 0,sticky = 'w')
ventana.config(bd=5,relief="ridge")


image = Image.open (r"C:\Users\Pablo\Pictures\lapiz.png")
new_image = image.resize((256,215))
background_image = ImageTk.PhotoImage(new_image)
background_label = tk.Label(ventana,image=background_image,height = 215, width = 256)
background_label.grid(column = 0, row =0)


ventana_lapiz = Frame(window)
ventana_lapiz.grid(column = 1, row = 0,sticky = 'w')
ventana_lapiz.config(bd=5,relief="ridge")


lbl_fila1_L = Label(ventana_lapiz, text = 'Tipo:\n', font= ('Arial',10))
lbl_fila1_L.grid (column = 1, row = 2, sticky = 'w')

lbl_fila2_L = Label(ventana_lapiz, text = 'Cantidad Bodega:\n', font= ('Arial',10))
lbl_fila2_L.grid (column = 1, row = 3, sticky = 'w')

lbl_fila3_L = Label(ventana_lapiz, text = 'Valor Unitario:\n', font= ('Arial',10))
lbl_fila3_L.grid (column = 1, row = 4, sticky = 'w')

lbl_fila4_L = Label(ventana_lapiz, text = 'Cantidad vendidas:\n', font= ('Arial',10))
lbl_fila4_L.grid (column = 1, row = 5, sticky = 'w')

lbl_fila5_L = Label(ventana_lapiz, text = 'Cantidad minima:\n', font= ('Arial',10))
lbl_fila5_L.grid (column = 1, row = 6, sticky = 'w')
###################################################################################################################
#columna 3 LAPIZ
lbl_fila1C3_L = Label(ventana_lapiz, text = 'Papeleria', font= ('Arial',10),bg = 'white',relief = 'sunken', bd = 3, height = 1, width = 25)
lbl_fila1C3_L.grid (column = 2, row = 2, sticky = 'w')

lbl_fila2C3_L = Label(ventana_lapiz, text = '18', font= ('Arial',10),bg = 'white',relief = 'sunken', bd = 3, height = 1, width = 25)
lbl_fila2C3_L.grid (column = 2, row = 3, sticky = 'w')

lbl_fila3C3_L = Label(ventana_lapiz, text = '550.0', font= ('Arial',10),bg = 'white',relief = 'sunken', bd = 3, height = 1, width = 25)
lbl_fila3C3_L.grid (column = 2, row = 4, sticky = 'w')

lbl_fila4C3_L = Label(ventana_lapiz, text = '0', font= ('Arial',10),bg = 'white',relief = 'sunken', bd = 3, height = 1, width = 25)
lbl_fila4C3_L.grid (column = 2, row = 5, sticky = 'w')

lbl_fila5C3_L = Label(ventana_lapiz, text = '5', font= ('Arial',10),bg = 'white',relief = 'sunken', bd = 3, height = 1, width = 25)
lbl_fila5C3_L.grid (column = 2, row = 6, sticky = 'w')


btn1_L = Button (ventana,text = 'Abastecer',relief = 'raised',bg = 'lightyellow',bd = 3,height = 1, width = 28,command = lambda : [Abastecer_Lapiz()] )
btn1_L.grid (column = 0, row = 7, sticky = 'e')

btn2_L = Button (ventana_lapiz,text = 'Vender',relief = 'raised',bg = 'lightyellow',bd = 3,height = 1, width = 28,command = lambda : [Venta_Lapiz()])
btn2_L.grid (column = 1, row = 7, sticky = 'w')

btn3_L = Button (ventana_lapiz,text = 'Cambiar',relief = 'raised',bg = 'lightyellow',bd = 3,height = 1, width = 28,command = lambda : [Cambiar_Lapiz()])
btn3_L.grid (column = 2, row = 7,sticky = 'w')

##############################################################################################################

#Imagen Aspirina
ventana2 = Frame(window)
ventana2.grid(column = 2, row = 0,sticky = 'n')
ventana2.config(bd=5,relief="ridge")

image2 = Image.open (r"C:\Users\Pablo\Pictures\aspirina.jpg")
new_image2 = image2.resize((256,215))
background_image2 = ImageTk.PhotoImage(new_image2)
background_label2 = tk.Label(ventana2,image=background_image2,height = 215, width = 256)
background_label2.grid(column = 2, row = 0)

ventana_Aspirina = Frame(window)
ventana_Aspirina.grid(column = 4, row = 0,sticky = 'n')
ventana_Aspirina.config(bd=5,relief="ridge")

lbl_fila1_A = Label(ventana_Aspirina, text = 'Tipo:\n', font= ('Arial',10))
lbl_fila1_A.grid (column = 4, row = 2, sticky = 'w')

lbl_fila2_A = Label(ventana_Aspirina, text = 'Cantidad Bodega:\n', font= ('Arial',10))
lbl_fila2_A.grid (column = 4, row = 3, sticky = 'w')

lbl_fila3_A = Label(ventana_Aspirina, text = 'Valor Unitario:\n', font= ('Arial',10))
lbl_fila3_A.grid (column = 4, row = 4, sticky = 'w')

lbl_fila4_A = Label(ventana_Aspirina, text = 'Cantidad vendidas:\n', font= ('Arial',10))
lbl_fila4_A.grid (column = 4, row = 5, sticky = 'w')

lbl_fila5_A = Label(ventana_Aspirina, text = 'Cantidad minima:\n', font= ('Arial',10))
lbl_fila5_A.grid (column = 4, row = 6, sticky = 'w')
###################################################################################################################
#columna 3 ASPIRINA
lbl_fila1C3_A = Label(ventana_Aspirina, text = 'Drogueria', font= ('Arial',10),bg = 'white',relief = 'sunken', bd = 3, height = 1, width = 25)
lbl_fila1C3_A.grid (column = 5, row = 2, sticky = 'w')

lbl_fila2C3_A = Label(ventana_Aspirina, text = '25', font= ('Arial',10),bg = 'white',relief = 'sunken', bd = 3, height = 1, width = 25)
lbl_fila2C3_A.grid (column = 5, row = 3, sticky = 'w')

lbl_fila3C3_A = Label(ventana_Aspirina, text = '109.5', font= ('Arial',10),bg = 'white',relief = 'sunken', bd = 3, height = 1, width = 25)
lbl_fila3C3_A.grid (column = 5, row = 4, sticky = 'w')

lbl_fila4C3_A = Label(ventana_Aspirina, text = '0', font= ('Arial',10),bg = 'white',relief = 'sunken', bd = 3, height = 1, width = 25)
lbl_fila4C3_A.grid (column = 5, row = 5, sticky = 'w')

lbl_fila5C3_A = Label(ventana_Aspirina, text = '8', font= ('Arial',10),bg = 'white',relief = 'sunken', bd = 3, height = 1, width = 25)
lbl_fila5C3_A.grid (column = 5, row = 6, sticky = 'w')

btn1_A = Button (ventana2,text = 'Abastecer',relief = 'raised',bg = 'lightyellow',bd = 3,height = 1, width = 28,command = lambda : [Abastecer_Aspirina()] )
btn1_A.grid (column = 2, row = 7, sticky = 'e')

btn2_A = Button (ventana_Aspirina,text = 'Vender',relief = 'raised',bg = 'lightyellow',bd = 3,height = 1, width = 28,command = lambda : [Venta_Aspirina()])
btn2_A.grid (column = 4, row = 7)

btn3_A = Button (ventana_Aspirina,text = 'Cambiar',relief = 'raised',bg = 'lightyellow',bd = 3,height = 1, width = 28,command = lambda : [Cambiar_Aspirina()])
btn3_A.grid (column = 5, row = 7)
#####################################################################################################################
#BORRADOR
ventana3 = Frame(window)
ventana3.grid(column = 0, row = 1,sticky = 'w')
ventana3.config(bd=5,relief="ridge")

image3 = Image.open (r"C:\Users\Pablo\Pictures\borrador.jpg")
new_image3 = image3.resize((256,215))
background_image3 = ImageTk.PhotoImage(new_image3)
background_label3 = tk.Label(ventana3,image=background_image3,height = 215, width = 256)
background_label3.grid(column = 0, row = 1)

ventana_Borrador = Frame(window)
ventana_Borrador.grid(column = 1, row = 1,sticky = 'n')
ventana_Borrador.config(bd=5,relief="ridge")

lbl_fila1_B = Label(ventana_Borrador, text = 'Tipo:\n', font= ('Arial',10))
lbl_fila1_B.grid (column = 1, row = 8, sticky = 'w')

lbl_fila2_B = Label(ventana_Borrador, text = 'Cantidad Bodega:\n', font= ('Arial',10))
lbl_fila2_B.grid (column = 1, row = 9, sticky = 'w')

lbl_fila3_B = Label(ventana_Borrador, text = 'Valor Unitario:\n', font= ('Arial',10))
lbl_fila3_B.grid (column = 1, row = 10, sticky = 'w')

lbl_fila4_B = Label(ventana_Borrador, text = 'Cantidad vendidas:\n', font= ('Arial',10))
lbl_fila4_B.grid (column = 1, row = 11, sticky = 'w')

lbl_fila5_B = Label(ventana_Borrador, text = 'Cantidad minima:\n', font= ('Arial',10))
lbl_fila5_B.grid (column = 1, row = 12, sticky = 'w')
####################################################################################################################################################
#columna 3 BORRADOR
lbl_fila1C3_B = Label(ventana_Borrador, text = 'Papeleria', font= ('Arial',10),bg = 'white',relief = 'sunken', bd = 3, height = 1, width = 25)
lbl_fila1C3_B.grid (column = 2, row = 8, sticky = 'w')

lbl_fila2C3_B = Label(ventana_Borrador, text = '30', font= ('Arial',10),bg = 'white',relief = 'sunken', bd = 3, height = 1, width = 25)
lbl_fila2C3_B.grid (column = 2, row = 9, sticky = 'w')

lbl_fila3C3_B = Label(ventana_Borrador, text = '207.3', font= ('Arial',10),bg = 'white',relief = 'sunken', bd = 3, height = 1, width = 25)
lbl_fila3C3_B.grid (column = 2, row = 10, sticky = 'w')

lbl_fila4C3_B = Label(ventana_Borrador, text = '0', font= ('Arial',10),bg = 'white',relief = 'sunken', bd = 3, height = 1, width = 25)
lbl_fila4C3_B.grid (column = 2, row = 11, sticky = 'w')

lbl_fila5C3_B = Label(ventana_Borrador, text = '10', font= ('Arial',10),bg = 'white',relief = 'sunken', bd = 3, height = 1, width = 25)
lbl_fila5C3_B.grid (column = 2, row = 12, sticky = 'w')

btn1_B = Button (ventana3,text = 'Abastecer',relief = 'raised',bg = 'lightyellow',bd = 3,height = 1, width = 28,command = lambda : [Abastecer_Borrador()])
btn1_B.grid (column = 0, row = 13, sticky = 'e')

btn2_B = Button (ventana_Borrador,text = 'Vender',relief = 'raised',bg = 'lightyellow',bd = 3,height = 1, width = 28,command = lambda : [Venta_Borrador()])
btn2_B.grid (column = 1, row = 13)

btn3_B = Button (ventana_Borrador,text = 'Cambiar',relief = 'raised',bg = 'lightyellow',bd = 3,height = 1, width = 28,command = lambda : [Cambiar_Borrador()])
btn3_B.grid (column = 2, row = 13)

#######################################################################################################################################################
#Imagen Pan
ventana4 = Frame(window)
ventana4.grid(column = 2, row = 1,sticky = 'w')
ventana4.config(bd=5,relief="ridge")

image4 = Image.open (r"C:\Users\Pablo\Pictures\pan.jpg")
new_image4 = image4.resize((256,215))
background_image4 = ImageTk.PhotoImage(new_image4)
background_label4 = tk.Label(ventana4,image=background_image4,height = 215, width = 256)
background_label4.grid(column = 2, row = 1)

ventana_Pan = Frame(window)
ventana_Pan.grid(column = 4, row = 1,sticky = 'n')
ventana_Pan.config(bd=5,relief="ridge")

lbl_fila1_P = Label(ventana_Pan, text = 'Tipo:\n', font= ('Arial',10))
lbl_fila1_P.grid (column = 4, row = 8, sticky = 'w')

lbl_fila2_P = Label(ventana_Pan, text = 'Cantidad Bodega:\n', font= ('Arial',10))
lbl_fila2_P.grid (column = 4, row = 9, sticky = 'w')

lbl_fila3_P = Label(ventana_Pan, text = 'Valor Unitario:\n', font= ('Arial',10))
lbl_fila3_P.grid (column = 4, row = 10, sticky = 'w')

lbl_fila4_P = Label(ventana_Pan, text = 'Cantidad vendidas:\n', font= ('Arial',10))
lbl_fila4_P.grid (column = 4, row = 11, sticky = 'w')

lbl_fila5_P = Label(ventana_Pan, text = 'Cantidad minima:\n', font= ('Arial',10))
lbl_fila5_P.grid (column = 4, row = 12, sticky = 'w')
###################################################################################################################
#columna 3 PAN
lbl_fila1C3_P = Label(ventana_Pan, text = 'Supermercado', font= ('Arial',10),bg = 'white',relief = 'sunken', bd = 3, height = 1, width = 25)
lbl_fila1C3_P.grid (column = 5, row = 8, sticky = 'w')

lbl_fila2C3_P = Label(ventana_Pan, text = '15', font= ('Arial',10),bg = 'white',relief = 'sunken', bd = 3, height = 1, width = 25)
lbl_fila2C3_P.grid (column = 5, row = 9, sticky = 'w')

lbl_fila3C3_P = Label(ventana_Pan, text = '150.0', font= ('Arial',10),bg = 'white',relief = 'sunken', bd = 3, height = 1, width = 25)
lbl_fila3C3_P.grid (column = 5, row = 10, sticky = 'w')

lbl_fila4C3_P = Label(ventana_Pan, text = '0', font= ('Arial',10),bg = 'white',relief = 'sunken', bd = 3, height = 1, width = 25)
lbl_fila4C3_P.grid (column = 5, row = 11, sticky = 'w')

lbl_fila5C3_P = Label(ventana_Pan, text = '20', font= ('Arial',10),bg = 'white',relief = 'sunken', bd = 3, height = 1, width = 25)
lbl_fila5C3_P.grid (column = 5, row = 12, sticky = 'w')

btn1_P = Button (ventana4,text = 'Abastecer',relief = 'raised',bg = 'lightyellow',bd = 3,height = 1, width = 28,command = lambda : [Abastecer_Pan()])
btn1_P.grid (column = 2, row = 13,sticky = 'e')

btn2_P = Button (ventana_Pan,text = 'Vender',relief = 'raised',bg = 'lightyellow',bd = 3,height = 1, width = 28,command = lambda : [Venta_Pan()])
btn2_P.grid (column = 4, row = 13)

btn3_P = Button (ventana_Pan,text = 'Cambiar',relief = 'raised',bg = 'lightyellow',bd = 3,height = 1, width = 28,command = lambda : [Cambiar_Pan()])
btn3_P.grid (column = 5, row = 13)

##################################################################################################################################################
#CALCULADORA


ventana_Calculadora = Frame(window)
ventana_Calculadora.grid(column = 0, row = 2,sticky = 'n')
ventana_Calculadora.config(bd=5,relief="sunken")

image5 = Image.open (r"C:\Users\Pablo\Pictures\calculadora.jpg")
new_image5 = image5.resize((256,215))
background_image5 = ImageTk.PhotoImage(new_image5)
background_label5 = tk.Label(ventana_Calculadora,image=background_image5,height = 215, width = 256)
background_label5.grid(column = 0, row = 3)

ventana_opciones = Frame(window)
ventana_opciones.grid(column = 1, row = 2,sticky = 'w')
ventana_opciones.config(bd=8,relief="sunken")

btn = Button (ventana_opciones,text = 'Producto mas vendido',relief = 'raised',bg = 'lightskyblue',bd = 3,height = 1, width = 28,command = lambda : [Mas_Vendido()])
btn.grid (column = 6, row = 14)

btn1 = Button (ventana_opciones,text = 'Producto menos vendido',relief = 'raised',bg = 'lightskyblue',bd = 3,height = 1, width = 28,command = lambda : [Menos_Vendido()])
btn1.grid (column = 6, row = 15,sticky = 'e')

btn2 = Button (ventana_opciones,text = 'Primedio de ventas',relief = 'raised',bg = 'lightskyblue',bd = 3,height = 1, width = 28,command = lambda : [Promedio_de_ventas()])
btn2.grid (column = 6, row = 16)

btn3 = Label (ventana_opciones,text = 'Dinero en Caja',relief = 'raised',bg = 'lightskyblue',bd = 3,height = 2, width = 28)
btn3.grid (column = 6, row = 17)

#####################################################################################################################################################

lbl_fila1_Opciones = Label(ventana_opciones, text = '', font= ('Arial ',10),bg = 'white',relief = 'sunken', bd = 3, height = 1, width = 25)
lbl_fila1_Opciones.grid (column = 7, row = 14, sticky = 'w')

lbl_fila2_Opciones = Label(ventana_opciones, text = '', font= ('Arial',10),bg = 'white',relief = 'sunken', bd = 3, height = 1, width = 25)
lbl_fila2_Opciones.grid (column = 7, row = 15, sticky = 'w')

lbl_fila3_Opciones = Label(ventana_opciones, text = '', font= ('Arial',10),bg = 'white',relief = 'sunken', bd = 3, height = 1, width = 25)
lbl_fila3_Opciones.grid (column = 7, row = 16, sticky = 'w')

lbl_fila4_Opciones = Label(ventana_opciones, text = '', font= ('Arial',9,'bold'),bg = 'lightcyan',relief = 'sunken', bd = 5, height = 2, width = 25)
lbl_fila4_Opciones.grid (column = 7, row = 17, sticky = 'w')

window.mainloop()
