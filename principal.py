#!/usr/bin/env python
# coding: utf-8

# In[5]:


from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

root = Tk()
root.withdraw()

window = Toplevel()
window.title("Programación II - Sistema Stock A.Ozuna")
window.geometry('980x680')
window.configure(bg='black')
window.protocol("WM_DELETE_WINDOW", root.destroy)

but = Button(window, text='deiconify')
but['command'] = root.deiconify
but.pack()

#Imagen Lápiz
path_lapiz=r'C:\Users\Agus\Downloads\pencil.jpg'

#Imagen Amoxicilina
path_pill=r'C:\Users\Agus\Downloads\pill.png'


#Imagen Trincheta
path_trincheta=r'C:\Users\Agus\Downloads\trench.png'


#Imagen Huevos
path_huevos=r'C:\Users\Agus\Downloads\eggs.png'



def seccion(path,Producto, Canvas_X, Canvas_Y, coordenada_X_linea_N, Cantidad_Inicial, cantidad_minima, Tipo):
    global Cantidad_Bodega, Cantidad_Minima, Entry_Cantidad_bodega, canvas, Abastecer
    Cantidad_Minima=cantidad_minima
    Cantidad_Bodega=Cantidad_Inicial
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(window, image = img)
    panel.image = img
    canvas = Canvas(window, width=488, height=275,bg='black')
    canvas.place(x=Canvas_X,y=Canvas_Y)
    canvas.create_image(190,50, image=img, anchor=NE)
    canvas.create_line(coordenada_X_linea_N,0,540,0,fill='purple',width=25)
    canvas.create_line(488,0,488,250,fill='purple',width=25)
    canvas.create_line(0,250,488,250,fill='purple',width=25)
    canvas.create_line(0,250,0,10,fill='purple',width=25)
    label_producto = Label(canvas, text=Producto,bg='black',font=('Open Sans',16),fg='white', relief=RAISED)
    label_producto.place(x=2,y=3) #Label2
    Tipo_=IntVar(canvas, value=Tipo)
    Tipo = Label(canvas, text='Tipo: ',bg='black',fg='purple', font=('Open Sans',10))
    Tipo.place(x=200,y=30) #Label
    Entry_Tipo = Entry(canvas,relief=SUNKEN, bg='gray', state=DISABLED, textvariable=Tipo_, justify=CENTER)
    Entry_Tipo.place(x=330,y=32) #Entry1white
    Cantidad_Bodega=IntVar(canvas, value=Cantidad_Inicial)
    Cantidad_bodega = Label(canvas, text='Cantidad bodega: ',bg='black',fg='purple', font=('Open Sans',10))
    Cantidad_bodega.place(x=200,y=70) #Label4
    Entry_Cantidad_bodega = Entry(canvas,relief=SUNKEN, bg='gray', textvariable=Cantidad_Bodega, state=DISABLED, justify=CENTER)
    Entry_Cantidad_bodega.place(x=330,y=72) #Entry2
    Valor_unitario = Label(canvas, text='Valor unitario: ',bg='black',fg='purple', font=('Open Sans',10))
    Valor_unitario.place(x=200,y=110) #Label5
    Entry_Valor_unitario = Entry(canvas,relief=SUNKEN, bg='gray', state=DISABLED)
    Entry_Valor_unitario.place(x=330,y=112) #Entry3
    Cantidad_vendidas = Label(canvas, text='Cantidad vendidas: ',bg='black',fg='purple', font=('Open Sans',10))
    Cantidad_vendidas.place(x=200,y=150) #Label6
    Entry_Cantidad_vendidas = Entry(canvas,relief=SUNKEN, bg='gray', state=DISABLED)
    Entry_Cantidad_vendidas.place(x=330,y=152) #Entry4
    Cantidad_Minima_var=IntVar(canvas, value=Cantidad_Minima)
    Cantidad_minima = Label(canvas, text='Cantidad mínima: ',bg='black',fg='purple', font=('Open Sans',10))
    Cantidad_minima.place(x=200,y=190) #Label7
    Entry_Cantidad_minima = Entry(canvas,relief=SUNKEN, bg='gray', state=DISABLED, textvariable=Cantidad_Minima_var, justify=CENTER)
    Entry_Cantidad_minima.place(x=330,y=192) #Entry5
    botones = Frame(canvas, height=20,width=50)
    botones.place(x=0,y=250)
    Abastecer = Button(botones, text='Abastecer', relief=SUNKEN,bg='black',fg='purple',width=22,justify=CENTER, font=('Open Sans',9))
    Abastecer.pack(side=LEFT)
    Vender = Button(botones, text='Vender',relief=SUNKEN,bg='black',fg='purple',width=22,justify=CENTER, font=('Open Sans',9))
    Vender.pack(side=LEFT)
    Cambiar = Button(botones, text='Cambiar',relief=SUNKEN,bg='black',fg='purple',width=22,justify=CENTER, font=('Open Sans',9))
    Cambiar.pack(side=LEFT)
    
def opciones():
    canvas = Canvas(window, width=976, height=150,bg='black')
    canvas.place(x=0,y=550)
    canvas.create_line(95,0,980,0,fill='purple',width=25)
    canvas.create_line(0,700,0,20,fill='purple',width=25)
    label = Label(canvas, text='Opciones',bg='black',fg='white', font=('Open Sans',16), relief=RAISED)
    label.place(x=2,y=3)
    botones = Frame(window, height=60,width=98)
    botones.place(x=60,y=590)
    Producto_mas_vendido = Button(botones, text='Producto más vendido',relief=SUNKEN,bg='black',fg='purple',width=30,height=5, justify=CENTER, font=('Open Sans',9))
    Producto_mas_vendido.pack(side=LEFT)
    Producto_menos_vendido = Button(botones, text='Producto menos vendido',relief=SUNKEN,bg='black',fg='purple',width=30,height=5, justify=CENTER, font=('Open Sans',9))
    Producto_menos_vendido.pack(side=LEFT)
    Promedio_ventas = Button(botones, text='Promedio ventas',relief=SUNKEN,bg='black',fg='purple',width=30,height=5, justify=CENTER, font=('Open Sans',9))
    Promedio_ventas.pack(side=LEFT)
    Dinero_en_caja = Button(botones, text='Dinero en caja',relief=SUNKEN,bg='black',fg='purple',width=30,height=5, justify=CENTER, font=('Open Sans',9))
    Dinero_en_caja.pack(side=LEFT)
    
    
seccion(path_lapiz, "Lápiz", 0, 0, 55, 15, 5,"Papelería")
seccion(path_pill, "Amoxicilina", 488, 0, 110, 20, 8,"Droguería")
seccion(path_huevos, "Huevos", 488, 275, 75, 6, 20,"Supermercado")
seccion(path_trincheta, "Trincheta", 0, 275, 95, 32, 10,"Papelería")
opciones()

    

window.mainloop()


# In[ ]:




