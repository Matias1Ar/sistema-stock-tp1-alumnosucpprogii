from tkinter import*
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

window = Tk()
window.title('Inventario: ')
window.geometry('1366x768')

#Funciones:

#Ventas:

def Venta_Lapiz ():
    bodega_lapiz = int(lbl_fila2C3_l.cget("text"))
    vender = bodega_lapiz - 1
    lbl_fila2C3_l.configure(text= int(vender))
    cant_ventas = int(lbl_fila4C3_l.cget("text"))
    vendidos = cant_ventas + 1
    lbl_fila4C3_l.configure(text = int(vendidos))
    Dinero_Caja()

def Venta_Aspirinas ():
    bodega_aspirinas = int(lbl_fila2C3_a.cget("text"))
    vender = bodega_aspirinas - 1
    lbl_fila2C3_a.configure(text= int(vender))
    cant_ventas = int(lbl_fila4C3_a.cget("text"))
    vendidos = cant_ventas + 1
    lbl_fila4C3_a.configure(text = int(vendidos))
    Dinero_Caja()

def Venta_goma_de_borrar ():
    bodega_goma_de_borrar = int(lbl_fila2C3_g.cget("text"))
    vender = bodega_goma_de_borrar - 1
    lbl_fila2C3_g.configure(text= int(vender))
    cant_ventas = int(lbl_fila4C3_g.cget("text"))
    vendidos = cant_ventas + 1
    lbl_fila4C3_g.configure(text = int(vendidos))
    Dinero_Caja()

def Venta_pan ():
    bodega_pan = int(lbl_fila2C3_p.cget("text"))
    vender = bodega_pan - 1
    lbl_fila2C3_p.configure(text= int(vender))
    cant_ventas = int(lbl_fila4C3_p.cget("text"))
    vendidos = cant_ventas + 1
    lbl_fila4C3_p.configure(text = int(vendidos))
    Dinero_Caja()

##############################################################################################################

#Abastecimientos:

def Abastecer_Lapiz():
    bodega_lapiz = int(lbl_fila2C3_l.cget("text"))
    min_lapiz = int(lbl_fila5C3_l.cget("text"))
    if bodega_lapiz <= min_lapiz:
        ventana_ingresar = tk.Toplevel(window)
        ventana_ingresar.title("Ingresar datos: ")
        ventana_ingresar.geometry("240x180")
        label_1 = Label(ventana_ingresar, text="Cantidad de productos\n que desea agregar: ")
        label_1.grid (column = 0, row = 0,sticky = 'n')
        Entry_1 = Entry (ventana_ingresar, relief = 'groove',bg = 'white',bd = 2, width = 25)
        Entry_1.grid (column = 0, row = 1)
        btn = Button (ventana_ingresar,text = 'Agregar',relief = 'groove',bg = 'lightyellow',bd = 3,height = 1, width = 28,command = lambda : [agregar()])
        btn.grid (column = 0, row = 2)
        def agregar():
            Agr = int(Entry_1.get())
            total = bodega_lapiz + Agr
            lbl_fila2C3_l.configure(text=int(total))
            ventana_ingresar.destroy()

def Abastecer_Aspirina():
    bodega_Aspirina = int(lbl_fila2C3_a.cget("text"))
    min_aspirina = int(lbl_fila5C3_a.cget("text"))
    if bodega_Aspirina <= min_aspirina:
        ventana_ingresar = tk.Toplevel(window)
        ventana_ingresar.title("Ingresar datos: ")
        ventana_ingresar.geometry("240x180")
        label_1 = Label(ventana_ingresar, text="Cantidad de productos\n que desea agregar: ")
        label_1.grid (column = 0, row = 0,sticky = 'n')
        Entry_1 = Entry (ventana_ingresar, relief = 'groove',bg = 'white',bd = 2, width = 25)
        Entry_1.grid (column = 0, row = 1)
        btn = Button (ventana_ingresar,text = 'Agregar',relief = 'groove',bg = 'lightyellow',bd = 3,height = 1, width = 28,command = lambda : [agregar()])
        btn.grid (column = 0, row = 2)
        def agregar():
            Agr = int(Entry_1.get())
            total = bodega_Aspirina + Agr
            lbl_fila2C3_a.configure(text=int(total))
            ventana_ingresar.destroy()

def Abastecer_goma_de_borrar():
    bodega_gdb = int(lbl_fila2C3_g.cget("text"))
    min_gdb = int(lbl_fila5C3_g.cget("text"))
    if bodega_gdb <= min_gdb:
        ventana_ingresar = tk.Toplevel(window)
        ventana_ingresar.title("Ingresar datos: ")
        ventana_ingresar.geometry("240x180")
        label_1 = Label(ventana_ingresar, text="Cantidad de productos\n que desea agregar: ")
        label_1.grid (column = 0, row = 0,sticky = 'n')
        Entry_1 = Entry (ventana_ingresar, relief = 'groove',bg = 'white',bd = 2, width = 25)
        Entry_1.grid (column = 0, row = 1)
        btn = Button (ventana_ingresar,text = 'Agregar',relief = 'groove',bg = 'lightyellow',bd = 3,height = 1, width = 28,command = lambda : [agregar()])
        btn.grid (column = 0, row = 2)
        def agregar():
            Agr = int(Entry_1.get())
            total = bodega_gdb + Agr
            lbl_fila2C3_g.configure(text=int(total))
            ventana_ingresar.destroy()

def Abastecer_pan():
    bodega_pan = int(lbl_fila2C3_p.cget("text"))
    min_pan = int(lbl_fila5C3_p.cget("text"))
    if bodega_pan <= min_pan:
        ventana_ingresar = tk.Toplevel(window)
        ventana_ingresar.title("Ingresar datos: ")
        ventana_ingresar.geometry("240x180")
        label_1 = Label(ventana_ingresar, text="Cantidad de productos\n que desea agregar: ")
        label_1.grid (column = 0, row = 0,sticky = 'n')
        Entry_1 = Entry (ventana_ingresar, relief = 'groove',bg = 'white',bd = 2, width = 25)
        Entry_1.grid (column = 0, row = 1)
        btn = Button (ventana_ingresar,text = 'Agregar',relief = 'groove',bg = 'lightyellow',bd = 3,height = 1, width = 28,command = lambda : [agregar()])
        btn.grid (column = 0, row = 2)
        def agregar():
            Agr = int(Entry_1.get())
            total = bodega_pan + Agr
            lbl_fila2C3_p.configure(text=int(total))
            ventana_ingresar.destroy()

##############################################################################################################

#Cambios:

def Cambios_Lapiz():
    ventana_ingresar = tk.Toplevel(window)
    ventana_ingresar.title("Ingresar datos: ")
    ventana_ingresar.geometry("240x180")
    label_1 = Label(ventana_ingresar, text="Cantidad de Bodega: ")
    label_1.grid(column=0, row=2, sticky='n')
    Entry_1 = Entry(ventana_ingresar, relief='groove', bg='white', bd=2, width=25)
    Entry_1.grid(column=0, row=3)
    label_2 = Label(ventana_ingresar, text="Valor Unitario: ")
    label_2.grid(column=0, row=4, sticky='n')
    Entry_2 = Entry(ventana_ingresar, relief='groove', bg='white', bd=2, width=25)
    Entry_2.grid(column=0, row=5)
    label_3 = Label(ventana_ingresar, text="Cantidad Mínima: ")
    label_3.grid(column=0, row=6, sticky='n')
    Entry_3 = Entry(ventana_ingresar, relief='groove', bg='white', bd=2, width=25)
    Entry_3.grid(column=0, row=7)
    btn = Button(ventana_ingresar, text='Cambiar datos', relief='groove', bg='lightyellow', bd=3, height=1, width=28,command=lambda: [Cambio_l()])
    btn.grid(column=0, row=8)

    def Cambio_l():
        Cambio_bodega = int(Entry_1.get())
        Cambio_val_u = int(Entry_2.get())
        Cambio_min = int(Entry_3.get())
        lbl_fila2C3_l.configure(text= Cambio_bodega)
        lbl_fila3C3_l.configure(text=Cambio_val_u)
        lbl_fila5C3_l.configure(text=Cambio_min)

def Cambios_Aspirinas():
    ventana_ingresar = tk.Toplevel(window)
    ventana_ingresar.title("Ingresar datos: ")
    ventana_ingresar.geometry("240x180")
    label_1 = Label(ventana_ingresar, text="Cantidad de Bodega: ")
    label_1.grid(column=0, row=2, sticky='n')
    Entry_1 = Entry(ventana_ingresar, relief='groove', bg='white', bd=2, width=25)
    Entry_1.grid(column=0, row=3)
    label_2 = Label(ventana_ingresar, text="Valor Unitario: ")
    label_2.grid(column=0, row=4, sticky='n')
    Entry_2 = Entry(ventana_ingresar, relief='groove', bg='white', bd=2, width=25)
    Entry_2.grid(column=0, row=5)
    label_3 = Label(ventana_ingresar, text="Cantidad Mínima: ")
    label_3.grid(column=0, row=6, sticky='n')
    Entry_3 = Entry(ventana_ingresar, relief='groove', bg='white', bd=2, width=25)
    Entry_3.grid(column=0, row=7)
    btn = Button(ventana_ingresar, text='Cambiar datos', relief='groove', bg='lightyellow', bd=3, height=1, width=28,command=lambda: [Cambio_A()])
    btn.grid(column=0, row=8)

    def Cambio_A():
        Cambio_bodega = int(Entry_1.get())
        Cambio_val_u = int(Entry_2.get())
        Cambio_min = int(Entry_3.get())
        lbl_fila2C3_a.configure(text= Cambio_bodega)
        lbl_fila3C3_a.configure(text=Cambio_val_u)
        lbl_fila5C3_a.configure(text=Cambio_min)

def Cambios_Gdb():
    ventana_ingresar = tk.Toplevel(window)
    ventana_ingresar.title("Ingresar datos: ")
    ventana_ingresar.geometry("240x180")
    label_1 = Label(ventana_ingresar, text="Cantidad de Bodega: ")
    label_1.grid(column=0, row=2, sticky='n')
    Entry_1 = Entry(ventana_ingresar, relief='groove', bg='white', bd=2, width=25)
    Entry_1.grid(column=0, row=3)
    label_2 = Label(ventana_ingresar, text="Valor Unitario: ")
    label_2.grid(column=0, row=4, sticky='n')
    Entry_2 = Entry(ventana_ingresar, relief='groove', bg='white', bd=2, width=25)
    Entry_2.grid(column=0, row=5)
    label_3 = Label(ventana_ingresar, text="Cantidad Mínima: ")
    label_3.grid(column=0, row=6, sticky='n')
    Entry_3 = Entry(ventana_ingresar, relief='groove', bg='white', bd=2, width=25)
    Entry_3.grid(column=0, row=7)
    btn = Button(ventana_ingresar, text='Cambiar datos', relief='groove', bg='lightyellow', bd=3, height=1, width=28,command=lambda: [Cambio_G()])
    btn.grid(column=0, row=8)

    def Cambio_G():
        Cambio_bodega = int(Entry_1.get())
        Cambio_val_u = int(Entry_2.get())
        Cambio_min = int(Entry_3.get())
        lbl_fila2C3_g.configure(text= Cambio_bodega)
        lbl_fila3C3_g.configure(text=Cambio_val_u)
        lbl_fila5C3_g.configure(text=Cambio_min)

def Cambios_Pan():
    ventana_ingresar = tk.Toplevel(window)
    ventana_ingresar.title("Ingresar datos: ")
    ventana_ingresar.geometry("240x180")
    label_1 = Label(ventana_ingresar, text="Cantidad de Bodega: ")
    label_1.grid(column=0, row=2, sticky='n')
    Entry_1 = Entry(ventana_ingresar, relief='groove', bg='white', bd=2, width=25)
    Entry_1.grid(column=0, row=3)
    label_2 = Label(ventana_ingresar, text="Valor Unitario: ")
    label_2.grid(column=0, row=4, sticky='n')
    Entry_2 = Entry(ventana_ingresar, relief='groove', bg='white', bd=2, width=25)
    Entry_2.grid(column=0, row=5)
    label_3 = Label(ventana_ingresar, text="Cantidad Mínima: ")
    label_3.grid(column=0, row=6, sticky='n')
    Entry_3 = Entry(ventana_ingresar, relief='groove', bg='white', bd=2, width=25)
    Entry_3.grid(column=0, row=7)
    btn = Button(ventana_ingresar, text='Cambiar datos', relief='groove', bg='lightyellow', bd=3, height=1, width=28,command=lambda: [Cambio_P()])
    btn.grid(column=0, row=8)

    def Cambio_P():
        Cambio_bodega = int(Entry_1.get())
        Cambio_val_u = int(Entry_2.get())
        Cambio_min = int(Entry_3.get())
        lbl_fila2C3_p.configure(text= Cambio_bodega)
        lbl_fila3C3_p.configure(text=Cambio_val_u)
        lbl_fila5C3_p.configure(text=Cambio_min)

##############################################################################################################

#Ventana de Opciones:

#Productos más vendidos:

def Mas_Vendido():
    Lapiz = int(lbl_fila4C3_l.cget("text"))
    Aspirinas = int(lbl_fila4C3_a.cget("text"))
    Gdb = int(lbl_fila4C3_g.cget("text"))
    Pan = int(lbl_fila4C3_p.cget("text"))
    if Lapiz > Aspirinas and Lapiz > Gdb and Lapiz > Pan:
        lbl_fila1_Opciones.configure (text = "Lapiz")
    elif Aspirinas > Lapiz and Aspirinas > Gdb and Aspirinas > Pan:
        lbl_fila1_Opciones.configure (text = "Aspirinas")
    elif Gdb > Lapiz and Gdb > Aspirinas and Gdb > Pan:
        lbl_fila1_Opciones.configure(text="Goma de borrar")
    elif Pan > Lapiz and Pan > Aspirinas and Pan > Gdb:
        lbl_fila1_Opciones.configure(text="Pan")
    elif Lapiz == 0 and Aspirinas == 0 and Gdb == 0 and Pan == 0:
        messagebox.showinfo('Error', 'No se ha podido analizar\nNo se ha realizado ventas', icon = 'error')
    else:
        messagebox.showinfo('Aviso', 'Existen varios productos',icon='warning')

def Menos_Vendido():
    Lapiz = int(lbl_fila4C3_l.cget("text"))
    Aspirinas = int(lbl_fila4C3_a.cget("text"))
    Gdb = int(lbl_fila4C3_g.cget("text"))
    Pan = int(lbl_fila4C3_p.cget("text"))
    if Lapiz < Aspirinas and Lapiz < Gdb and Lapiz < Pan:
        lbl_fila2_Opciones.configure(text="Lapiz")
    elif Aspirinas < Lapiz and Aspirinas < Gdb and Aspirinas < Pan:
        lbl_fila2_Opciones.configure(text="Aspirinas")
    elif Gdb < Lapiz and Gdb < Aspirinas and Gdb < Pan:
        lbl_fila2_Opciones.configure(text="Goma de borrar")
    elif Pan < Lapiz and Pan < Aspirinas and Pan < Gdb:
        lbl_fila2_Opciones.configure(text="Pan")
    elif Lapiz == 0 and Aspirinas == 0 and Gdb == 0 and Pan == 0:
        messagebox.showinfo('Error', 'No se ha podido analizar\nNo se ha realizado ventas', icon = 'error')
    else:
        messagebox.showinfo('Aviso', 'Existen varios productos',icon='warning')

def Promedio_Ventas ():
    Lapiz = int(lbl_fila4C3_l.cget("text"))
    Aspirinas = int(lbl_fila4C3_a.cget("text"))
    Gdb = int(lbl_fila4C3_g.cget("text"))
    Pan = int(lbl_fila4C3_p.cget("text"))
    Suma = Lapiz + Aspirinas + Gdb + Pan
    Promedio = Suma / 4
    lbl_fila3_Opciones.configure(text = Promedio)

def Dinero_Caja():
    iva_Lapiz = (float(lbl_fila3C3_l.cget("text"))*16)/100
    iva_Aspirina = (float(lbl_fila3C3_a.cget("text"))*12)/100
    iva_Borrador = (float(lbl_fila3C3_g.cget("text"))*16)/100
    iva_Pan = (float(lbl_fila3C3_p.cget("text"))*4)/100
    precio_Lapiz = float(lbl_fila3C3_l.cget("text")) + iva_Lapiz
    precio_Aspirina = float(lbl_fila3C3_a.cget("text")) + iva_Aspirina
    precio_Borrador = float(lbl_fila3C3_g.cget("text")) + iva_Borrador
    precio_Pan = float(lbl_fila3C3_p.cget("text")) + iva_Pan
    Lapiz_Vendidos = int(lbl_fila4C3_l.cget("text"))
    Aspirina_Vendidos = int(lbl_fila4C3_a.cget("text"))
    Borrador_Vendidos = int(lbl_fila4C3_g.cget("text"))
    Pan_Vendidos = int(lbl_fila4C3_p.cget("text"))
    total_Lapiz = precio_Lapiz * Lapiz_Vendidos
    total_Aspirina = precio_Aspirina * Aspirina_Vendidos
    total_Borrador = precio_Borrador * Borrador_Vendidos
    total_Pan = precio_Pan * Pan_Vendidos
    TOTAL = round (total_Lapiz + total_Aspirina + total_Borrador + total_Pan,2)
    lbl_fila4_Opciones.configure(text = '$' + str(TOTAL))

##############################################################################################################

#Imágen del Lápiz:

ventana = Frame(window)
ventana.grid(column = 0, row = 0,sticky = 'n')
ventana.config(bd=1,relief="ridge")

image = Image.open (r"C:\Users\brian\Music\Lapiz.jpg")
new_image = image.resize((186,209))

background_image = ImageTk.PhotoImage(new_image)
background_label = tk.Label(ventana,image=background_image,height = 186, width = 210)
background_label.grid(column = 0, row =0)

#Columna de frame del lápiz:

ventana_lapiz = Frame(window)
ventana_lapiz.grid(column = 1, row = 0,sticky = 'n')
ventana_lapiz.config(bd=1,relief="ridge")


lbl_fila1_l = Label(ventana_lapiz, text = 'Tipo:\n', font= ('Arial',10))
lbl_fila1_l.grid (column = 1, row = 2, sticky = 'w')

lbl_fila2_l = Label(ventana_lapiz, text = 'Cantidad Bodega:\n', font= ('Arial',10))
lbl_fila2_l.grid (column = 1, row = 3, sticky = 'w')

lbl_fila3_l = Label(ventana_lapiz, text = 'Valor Unitario:\n', font= ('Arial',10))
lbl_fila3_l.grid (column = 1, row = 4, sticky = 'w')

lbl_fila4_l = Label(ventana_lapiz, text = 'Cantidad vendidas:\n', font= ('Arial',10))
lbl_fila4_l.grid (column = 1, row = 5, sticky = 'w')

lbl_fila5_l= Label(ventana_lapiz, text = 'Cantidad minima:\n', font= ('Arial',10))
lbl_fila5_l.grid (column = 1, row = 6, sticky = 'w')

lbl_fila1C3_l = Label(ventana_lapiz, text = 'Papeleria', font= ('Arial',10),bg = 'white',relief = 'sunken', bd = 3, height = 1, width = 25)
lbl_fila1C3_l.grid (column = 2, row = 2, sticky = 'w')

lbl_fila2C3_l = Label(ventana_lapiz, text = '18', font= ('Arial',10),bg = 'white',relief = 'sunken', bd = 3, height = 1, width = 25)
lbl_fila2C3_l.grid (column = 2, row = 3, sticky = 'w')

lbl_fila3C3_l = Label(ventana_lapiz, text = '550.0', font= ('Arial',10),bg = 'white',relief = 'sunken', bd = 3, height = 1, width = 25)
lbl_fila3C3_l.grid (column = 2, row = 4, sticky = 'w')

lbl_fila4C3_l = Label(ventana_lapiz, text = '0', font= ('Arial',10),bg = 'white',relief = 'sunken', bd = 3, height = 1, width = 25)
lbl_fila4C3_l.grid (column = 2, row = 5, sticky = 'w')

lbl_fila5C3_l = Label(ventana_lapiz, text = '5', font= ('Arial',10),bg = 'white',relief = 'sunken', bd = 3, height = 1, width = 25)
lbl_fila5C3_l.grid (column = 2, row = 6, sticky = 'w')

#Botonos:

btn1_l = Button (ventana,text = 'Abastecer',relief = 'raised',bg = 'lightblue',bd = 3,height = 1, width = 28,command = lambda : [Abastecer_Lapiz()])
btn1_l.grid (column = 0, row = 7, sticky = 'e')

btn2_l = Button (ventana_lapiz,text = 'Vender',relief = 'raised',bg = 'lightblue',bd = 3,height = 1, width = 28,command = lambda : [Venta_Lapiz()])
btn2_l.grid (column = 1, row = 7)

btn3_l = Button (ventana_lapiz,text = 'Cambiar',relief = 'raised',bg = 'lightblue',bd = 3,height = 1, width = 28,command=lambda: [Cambios_Lapiz()])
btn3_l.grid (column = 2, row = 7)

##############################################################################################################

#Imágen de la aspirina:
ventana2 = Frame(window)
ventana2.grid(column = 2, row = 0,sticky = 'n')
ventana2.config(bd=1,relief="ridge")

image2 = Image.open (r"C:\Users\brian\Music\aspirinas.png")
new_image2 = image2.resize((186,209))
background_image2 = ImageTk.PhotoImage(new_image2)
background_label2 = tk.Label(ventana2,image=background_image2,height = 186, width = 209)
background_label2.grid(column = 2, row = 0)

#Columna frame de la aspirina:

ventana_Aspirina = Frame(window)
ventana_Aspirina.grid(column = 4, row = 0,sticky = 'n')
ventana_Aspirina.config(bd=1,relief="ridge")

lbl_fila1_a = Label(ventana_Aspirina, text = 'Tipo:\n', font= ('Arial',10))
lbl_fila1_a.grid (column = 4, row = 2, sticky = 'w')

lbl_fila2_a = Label(ventana_Aspirina, text = 'Cantidad Bodega:\n', font= ('Arial',10))
lbl_fila2_a.grid (column = 4, row = 3, sticky = 'w')

lbl_fila3_a = Label(ventana_Aspirina, text = 'Valor Unitario:\n', font= ('Arial',10))
lbl_fila3_a.grid (column = 4, row = 4, sticky = 'w')

lbl_fila4_a = Label(ventana_Aspirina, text = 'Cantidad vendidas:\n', font= ('Arial',10))
lbl_fila4_a.grid (column = 4, row = 5, sticky = 'w')

lbl_fila5_a = Label(ventana_Aspirina, text = 'Cantidad minima:\n', font= ('Arial',10))
lbl_fila5_a.grid (column = 4, row = 6, sticky = 'w')

lbl_fila1C3_a = Label(ventana_Aspirina, text = 'Drogería', font= ('Arial',10),bg = 'white',relief = 'sunken', bd = 3, height = 1, width = 25)
lbl_fila1C3_a.grid (column = 5, row = 2, sticky = 'w')

lbl_fila2C3_a = Label(ventana_Aspirina, text = '25', font= ('Arial',10),bg = 'white',relief = 'sunken', bd = 3, height = 1, width = 25)
lbl_fila2C3_a.grid (column = 5, row = 3, sticky = 'w')

lbl_fila3C3_a = Label(ventana_Aspirina, text = '109.5', font= ('Arial',10),bg = 'white',relief = 'sunken', bd = 3, height = 1, width = 25)
lbl_fila3C3_a.grid (column = 5, row = 4, sticky = 'w')

lbl_fila4C3_a = Label(ventana_Aspirina, text = '0', font= ('Arial',10),bg = 'white',relief = 'sunken', bd = 3, height = 1, width = 25)
lbl_fila4C3_a.grid (column = 5, row = 5, sticky = 'w')

lbl_fila5C3_a = Label(ventana_Aspirina, text = '8', font= ('Arial',10),bg = 'white',relief = 'sunken', bd = 3, height = 1, width = 25)
lbl_fila5C3_a.grid (column = 5, row = 6, sticky = 'w')

#Botones:

btn1_a = Button (ventana2,text = 'Abastecer',relief = 'raised',bg = 'lightblue',bd = 3,height = 1, width = 28,command = lambda : [Abastecer_Aspirina()])
btn1_a.grid (column = 2, row = 7, sticky = 'e')

btn2_a = Button (ventana_Aspirina,text = 'Vender',relief = 'raised',bg = 'lightblue',bd = 3,height = 1, width = 28,command = lambda : [Venta_Aspirinas()])
btn2_a.grid (column = 4, row = 7)

btn3_a = Button (ventana_Aspirina,text = 'Cambiar',relief = 'raised',bg = 'lightblue',bd = 3,height = 1, width = 28,command=lambda: [Cambios_Aspirinas()])
btn3_a.grid (column = 5, row = 7)

#####################################################################################################################

#Imágen de la goma de borrar:

ventana3 = Frame(window)
ventana3.grid(column = 0, row = 1,sticky = 'n')
ventana3.config(bd=1,relief="ridge")

image3= Image.open (r"C:\Users\brian\Music\goma_de_borrar.png")
new_image3 = image3.resize((186,209))
background_image3 = ImageTk.PhotoImage(new_image3)
background_label3 = tk.Label(ventana3,image=background_image3,height = 186, width = 209)
background_label3.grid(column =0 , row =1)

ventana_goma_de_borrar = Frame(window)
ventana_goma_de_borrar.grid(column = 1, row = 1,sticky = 'n')
ventana_goma_de_borrar.config(bd=1,relief="ridge")

#Columna frame de la goma de borrar:

lbl_fila1_g= Label(ventana_goma_de_borrar, text = 'Tipo:\n', font= ('Arial',10))
lbl_fila1_g.grid (column = 1, row = 2, sticky = 'w')

lbl_fila2_g = Label(ventana_goma_de_borrar, text = 'Cantidad Bodega:\n', font= ('Arial',10))
lbl_fila2_g.grid (column = 1, row = 3, sticky = 'w')

lbl_fila3_g = Label(ventana_goma_de_borrar, text = 'Valor Unitario:\n', font= ('Arial',10))
lbl_fila3_g.grid (column = 1, row = 4, sticky = 'w')

lbl_fila4_g = Label(ventana_goma_de_borrar, text = 'Cantidad vendidas:\n', font= ('Arial',10))
lbl_fila4_g.grid (column = 1, row = 5, sticky = 'w')

lbl_fila5_g = Label(ventana_goma_de_borrar, text = 'Cantidad minima:\n', font= ('Arial',10))
lbl_fila5_g.grid (column = 1, row = 6, sticky = 'w')

lbl_fila1C3_g = Label(ventana_goma_de_borrar, text = 'Papeleria', font= ('Arial',10),bg = 'white',relief = 'sunken', bd = 3, height = 1, width = 25)
lbl_fila1C3_g.grid (column = 2, row = 2, sticky = 'w')

lbl_fila2C3_g = Label(ventana_goma_de_borrar, text = '30', font= ('Arial',10),bg = 'white',relief = 'sunken', bd = 3, height = 1, width = 25)
lbl_fila2C3_g.grid (column = 2, row = 3, sticky = 'w')

lbl_fila3C3_g = Label(ventana_goma_de_borrar, text = '207.3', font= ('Arial',10),bg = 'white',relief = 'sunken', bd = 3, height = 1, width = 25)
lbl_fila3C3_g.grid (column = 2, row = 4, sticky = 'w')

lbl_fila4C3_g = Label(ventana_goma_de_borrar, text = '0', font= ('Arial',10),bg = 'white',relief = 'sunken', bd = 3, height = 1, width = 25)
lbl_fila4C3_g.grid (column = 2, row = 5, sticky = 'w')

lbl_fila5C3_g = Label(ventana_goma_de_borrar, text = '10', font= ('Arial',10),bg = 'white',relief = 'sunken', bd = 3, height = 1, width = 25)
lbl_fila5C3_g.grid (column = 2, row = 6, sticky = 'w')

#Botones:

btn1_g = Button (ventana3,text = 'Abastecer',relief = 'raised',bg = 'lightblue',bd = 3,height = 1, width = 28,command = lambda : [Abastecer_goma_de_borrar()])
btn1_g.grid (column = 0, row = 7, sticky = 'e')

btn2_g = Button (ventana_goma_de_borrar,text = 'Vender',relief = 'raised',bg = 'lightblue',bd = 3,height = 1, width = 28,command = lambda : [Venta_goma_de_borrar()])
btn2_g.grid (column = 1, row = 7)

btn3_g = Button (ventana_goma_de_borrar,text = 'Cambiar',relief = 'raised',bg = 'lightblue',bd = 3,height = 1, width = 28,command=lambda: [Cambios_Gdb()])
btn3_g.grid (column = 2, row = 7)

###################################################################################################################

#Imágen del pan:
ventana4 = Frame(window)
ventana4.grid(column = 2, row = 1,sticky = 'n')
ventana4.config(bd=1,relief="ridge")

image4 = Image.open (r"C:\Users\brian\Music\pan.png")
new_image4 = image4.resize((186,209))
background_image4 = ImageTk.PhotoImage(new_image4)
background_label4 = tk.Label(ventana4,image=background_image4,height = 186, width = 209)
background_label4.grid(column = 2, row = 1)

#Columna frame del pan:

ventana_pan = Frame(window)
ventana_pan.grid(column = 4, row = 1,sticky = 'n')
ventana_pan.config(bd=1,relief="ridge")

lbl_fila1_p = Label(ventana_pan, text = 'Tipo:\n', font= ('Arial',10))
lbl_fila1_p.grid (column = 4, row = 2, sticky = 'w')

lbl_fila2_p = Label(ventana_pan, text = 'Cantidad Bodega:\n', font= ('Arial',10))
lbl_fila2_p.grid (column = 4, row = 3, sticky = 'w')

lbl_fila3_p = Label(ventana_pan, text = 'Valor Unitario:\n', font= ('Arial',10))
lbl_fila3_p.grid (column = 4, row = 4, sticky = 'w')

lbl_fila4_p = Label(ventana_pan, text = 'Cantidad vendidas:\n', font= ('Arial',10))
lbl_fila4_p.grid (column = 4, row = 5, sticky = 'w')

lbl_fila5_p = Label(ventana_pan, text = 'Cantidad minima:\n', font= ('Arial',10))
lbl_fila5_p.grid (column = 4, row = 6, sticky = 'w')

lbl_fila1C3_p = Label(ventana_pan, text = 'Supermercado', font= ('Arial',10),bg = 'white',relief = 'sunken', bd = 3, height = 1, width = 25)
lbl_fila1C3_p.grid (column = 5, row = 2, sticky = 'w')

lbl_fila2C3_p = Label(ventana_pan, text = '15', font= ('Arial',10),bg = 'white',relief = 'sunken', bd = 3, height = 1, width = 25)
lbl_fila2C3_p.grid (column = 5, row = 3, sticky = 'w')

lbl_fila3C3_p = Label(ventana_pan, text = '150.0', font= ('Arial',10),bg = 'white',relief = 'sunken', bd = 3, height = 1, width = 25)
lbl_fila3C3_p.grid (column = 5, row = 4, sticky = 'w')

lbl_fila4C3_p = Label(ventana_pan, text = '0', font= ('Arial',10),bg = 'white',relief = 'sunken', bd = 3, height = 1, width = 25)
lbl_fila4C3_p.grid (column = 5, row = 5, sticky = 'w')

lbl_fila5C3_p = Label(ventana_pan, text = '20', font= ('Arial',10),bg = 'white',relief = 'sunken', bd = 3, height = 1, width = 25)
lbl_fila5C3_p.grid (column = 5, row = 6, sticky = 'w')

#Botones:

btn1_p = Button (ventana4,text = 'Abastecer',relief = 'raised',bg = 'lightblue',bd = 3,height = 1, width = 28,command = lambda : [Abastecer_pan()])
btn1_p.grid (column = 2, row = 7, sticky = 'e')

btn2_p = Button (ventana_pan,text = 'Vender',relief = 'raised',bg = 'lightblue',bd = 3,height = 1, width = 28,command = lambda : [Venta_pan()])
btn2_p.grid (column = 4, row = 7)

btn3_L = Button (ventana_pan,text = 'Cambiar',relief = 'raised',bg = 'lightblue',bd = 3,height = 1, width = 28,command=lambda: [Cambios_Pan()])
btn3_L.grid (column = 5, row = 7)

###################################################################################################################

#Imágen de Opciones(Carrito):

ventana_carrito = Frame(window)
ventana_carrito.grid(column = 0, row = 2,sticky = 'n')
ventana_carrito.config(bd=1,relief="sunken")

image5 = Image.open (r"C:\Users\brian\Music\carrito.png")
new_image5 = image5.resize((180,160))
background_image5 = ImageTk.PhotoImage(new_image5)
background_label5 = tk.Label(ventana_carrito,image=background_image5,height = 180, width = 160)
background_label5.grid(column = 0, row = 3)

##Columna frame de las opciones:

ventana_opciones = Frame(window)
ventana_opciones.grid(column = 1, row = 2,sticky = 'w')
ventana_opciones.config(bd=1,relief="sunken")

lbl_fila1_Opciones = Label(ventana_opciones, text = '', font= ('Arial',10),bg = 'white',relief = 'sunken', bd = 1, height = 1, width = 25)
lbl_fila1_Opciones.grid (column = 7, row = 14, sticky = 'w')

lbl_fila2_Opciones = Label(ventana_opciones, text = '', font= ('Arial',10),bg = 'white',relief = 'sunken', bd = 1, height = 1, width = 25)
lbl_fila2_Opciones.grid (column = 7, row = 15, sticky = 'w')

lbl_fila3_Opciones = Label(ventana_opciones, text = '', font= ('Arial',10),bg = 'white',relief = 'sunken', bd = 1, height = 1, width = 25)
lbl_fila3_Opciones.grid (column = 7, row = 16, sticky = 'w')

lbl_fila4_Opciones = Label(ventana_opciones, text = '', font= ('Arial',10),bg = 'white',relief = 'sunken', bd = 3, height = 2 , width = 25)
lbl_fila4_Opciones.grid (column = 7, row = 17, sticky = 'w')

#Botones:

btn = Button (ventana_opciones,text = 'Producto mas vendido',relief = 'raised',bg = 'lightgreen',bd = 1,height = 1, width = 28,command = lambda : [Mas_Vendido()])
btn.grid (column = 6, row = 14)

btn1 = Button (ventana_opciones,text = 'Producto menos vendido',relief = 'raised',bg = 'lightgreen',bd = 1,height = 1, width = 28,command = lambda : [Menos_Vendido()])
btn1.grid (column = 6, row = 15,sticky = 'e')

btn2 = Button (ventana_opciones,text = 'Promedio de ventas',relief = 'raised',bg = 'lightgreen',bd = 1,height = 1, width = 28,command = lambda : [Promedio_Ventas()])
btn2.grid (column = 6, row = 16)

label_din = Label (ventana_opciones,text = 'Dinero en Caja',relief = 'raised',bg = 'lightgreen',bd = 3,height =2, width = 28)
label_din.grid (column = 6, row = 17)

###################################################################################################################

window.mainloop()