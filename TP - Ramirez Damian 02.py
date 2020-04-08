
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
import tkinter as tk
import tkinter.font
from PIL import Image, ImageTk




window = Tk()
window.wm_title("Sistema de Promedios")
window.config(background = "#F3F3F3")
window.geometry("900x480+10+20")
window.resizable(0,0)
style = ttk.Style()
style.configure('TButton', foreground='Blue', borderwidth=15,relief='groove', padding=3)

Alumnos_notas = [0,0,0,0,0,0,0,0,0,0,0,0]


def createCanvas(window):
    canvas = Canvas(window, bg ="#F3F3F3", borderwidth=2, bd=2, width=420, height=400,relief='groove')
    canvas.place(x=5, y=7)
    img = Image.open("pic09.png")
    canvas.image = ImageTk.PhotoImage(img)
    canvas.create_image(0,0, image=canvas.image, anchor='nw')

def start():
    callable(panel01())
    callable(panel05())

def panel01():
    createCanvas(window)
    recuadro01 = Canvas(window, width=450,
                height=400,
                borderwidth=2,bd=2,
                background='#F3F3F3',
                relief='groove')
    recuadro01.place(x=440, y=7)
    global lbl01
    lbl01 = Label(window,width=5, text="Notas", font='Arial')
    lbl01.place(x=450, y=2)

    lapiz_lbl01 = Label(window,width=12, text="Estudiante 01:", font="Arial")
    lapiz_lbl01.place(x=470, y=35)
    lapiz_lbl02 = Label(window,width=12, text="Estudiante 02:", font="Arial")
    lapiz_lbl02.place(x=470, y=65)
    lapiz_lbl03 = Label(window,width=12, text="Estudiante 03:", font="Arial")
    lapiz_lbl03.place(x=470, y=95)
    lapiz_lbl04 = Label(window,width=12, text="Estudiante 04:", font="Arial")
    lapiz_lbl04.place(x=470, y=125)
    lapiz_lbl05 = Label(window,width=12, text="Estudiante 05:", font="Arial")
    lapiz_lbl05.place(x=470, y=155)
    lapiz_lbl05 = Label(window,width=12, text="Estudiante 06:", font="Arial")
    lapiz_lbl05.place(x=470, y=185)
    lapiz_lbl01 = Label(window,width=12, text="Estudiante 07:", font="Arial")
    lapiz_lbl01.place(x=470, y=215)
    lapiz_lbl02 = Label(window,width=12, text="Estudiante 08:", font="Arial")
    lapiz_lbl02.place(x=470, y=245)
    lapiz_lbl03 = Label(window,width=12, text="Estudiante 09:", font="Arial")
    lapiz_lbl03.place(x=470, y=275)
    lapiz_lbl04 = Label(window,width=12, text="Estudiante 10:", font="Arial")
    lapiz_lbl04.place(x=470, y=305)
    lapiz_lbl05 = Label(window,width=12, text="Estudiante 11:", font="Arial")
    lapiz_lbl05.place(x=470, y=335)
    lapiz_lbl05 = Label(window,width=12, text="Estudiante 12:", font="Arial")
    lapiz_lbl05.place(x=470, y=365)


    rectang01 = Label(window, text=f"0",width=15, borderwidth=4, relief="groove",anchor='center')
    rectang01.place(x=620, y=35)
    rectang02 = Label(window, text=f"0",width=15, borderwidth=4, relief="groove",anchor='center')
    rectang02.place(x=620, y=65)
    rectang03 = Label(window, text=f"0",width=15, borderwidth=2, relief="groove",anchor='center')
    rectang03.place(x=620, y=95)
    rectang04 = Label(window, text=f"0",width=15, borderwidth=2, relief="groove",anchor='center')
    rectang04.place(x=620, y=125)
    rectang05 = Label(window, text=f"0",width=15, borderwidth=2, relief="groove",anchor='center')
    rectang05.place(x=620, y=155)
    rectang06 = Label(window, text=f"0",width=15, borderwidth=4, relief="groove",anchor='center')
    rectang06.place(x=620, y=185)
    rectang07 = Label(window, text=f"0",width=15, borderwidth=4, relief="groove",anchor='center')
    rectang07.place(x=620, y=215)
    rectang08 = Label(window, text=f"0",width=15, borderwidth=2, relief="groove",anchor='center')
    rectang08.place(x=620, y=245)
    rectang09 = Label(window, text=f"0",width=15, borderwidth=2, relief="groove",anchor='center')
    rectang09.place(x=620, y=275)
    rectang10 = Label(window, text=f"0",width=15, borderwidth=2, relief="groove",anchor='center')
    rectang10.place(x=620, y=305)
    rectang11 = Label(window, text=f"0",width=15, borderwidth=2, relief="groove",anchor='center')
    rectang11.place(x=620, y=335)
    rectang12 = Label(window, text=f"0",width=15, borderwidth=2, relief="groove",anchor='center')
    rectang12.place(x=620, y=365)


    button01 = Button(window, text="Cambiar", width=17, command=ingresa_btn01)
    button01.place(x=750, y=30)
    button02 = Button(window, text="Cambiar", width=17, command=ingresa_btn02)
    button02.place(x=750, y=60)
    button03 = Button(window, text="Cambiar", width=17, command=ingresa_btn03)
    button03.place(x=750, y=90)
    button04 = Button(window, text="Cambiar", width=17, command=ingresa_btn04)
    button04.place(x=750, y=120)
    button05 = Button(window, text="Cambiar", width=17, command=ingresa_btn05)
    button05.place(x=750, y=150)
    button06 = Button(window, text="Cambiar", width=17, command=ingresa_btn06)
    button06.place(x=750, y=180)
    button07 = Button(window, text="Cambiar", width=17, command=ingresa_btn07)
    button07.place(x=750, y=210)
    button08 = Button(window, text="Cambiar", width=17, command=ingresa_btn08)
    button08.place(x=750, y=240)
    button09 = Button(window, text="Cambiar", width=17, command=ingresa_btn09)
    button09.place(x=750, y=270)
    button10 = Button(window, text="Cambiar", width=17, command=ingresa_btn10)
    button10.place(x=750, y=300)
    button11 = Button(window, text="Cambiar", width=17, command=ingresa_btn11)
    button11.place(x=750, y=330)
    button12 = Button(window, text="Cambiar", width=17, command=ingresa_btn12)
    button12.place(x=750, y=360)




def ingresa_btn01():
    global Entry_Est
    Entry_Est = Entry(window, text="",width=15)
    Entry_Est.place(x=620, y=35)
    global buttonxx
    buttonxx = Button(window, text="Confirmar", width=17, command=confirma_ingreso)
    buttonxx.place(x=750, y=30)
    
def confirma_ingreso():
    nva_Nota = getdouble(Entry_Est.get())
    if nva_Nota >= 0 and nva_Nota <= 5:
        Alumnos_notas.pop(0)
        Alumnos_notas.insert(0,nva_Nota)           
        buttonxx.destroy()
        button01 = Button(window, text="Cambiar", width=17, command=ingresa_btn01)
        button01.place(x=750, y=30)
        rectang01 = Label(window, text=f"{nva_Nota}",width=15, borderwidth=4, relief="groove", anchor='center')
        rectang01.place(x=620, y=35)
        Entry_Est.destroy()
    else:
        messagebox.showinfo(title ='Atencion!! Ingreso Invalido',message = 'Los valores ingresados deben ser entre 0 y 5', icon = 'warning')
        Entry_Est.focus()
        
    
       
def ingresa_btn02():
    global buttonxx
    buttonxx = Button(window, text="Confirmar", width=17, command=confirma_ingreso02)
    buttonxx.place(x=750, y=60)
    global Entry_Est01
    Entry_Est01 = Entry(window, text="",width=15)
    Entry_Est01.place(x=620, y=65)

def confirma_ingreso02():
    nva_Nota = getdouble(Entry_Est01.get())
    if nva_Nota >= 0 and nva_Nota <= 5:
        nva_Nota = getdouble(Entry_Est01.get())
        Alumnos_notas.pop(1)
        Alumnos_notas.insert(1,nva_Nota)           
        buttonxx.destroy()
        button01 = Button(window, text="Cambiar", width=17, command=ingresa_btn02)
        button01.place(x=750, y=60)
        rectang01 = Label(window, text=f"{nva_Nota}",width=15, borderwidth=4, relief="groove", anchor='center')
        rectang01.place(x=620, y=65)
        Entry_Est01.destroy()
    else:
        messagebox.showinfo(title ='Atencion!! Ingreso Invalido',message = 'Los valores ingresados deben ser entre 0 y 5', icon = 'warning')
        Entry_Est.focus()
    
    
def ingresa_btn03():
    global buttonxx
    buttonxx = Button(window, text="Confirmar", width=17, command=confirma_ingreso03)
    buttonxx.place(x=750, y=90)
    global Entry_Est02
    Entry_Est02 = Entry(window, text="",width=15)
    Entry_Est02.place(x=620, y=95)

def confirma_ingreso03():
    nva_Nota = getdouble(Entry_Est02.get())
    if nva_Nota >= 0 and nva_Nota <= 5:
        nva_Nota = getdouble(Entry_Est02.get())
        Alumnos_notas.pop(2)
        Alumnos_notas.insert(2,nva_Nota)           
        buttonxx.destroy()
        button01 = Button(window, text="Cambiar", width=17, command=ingresa_btn03)
        button01.place(x=750, y=90)
        rectang01 = Label(window, text=f"{nva_Nota}",width=15, borderwidth=4, relief="groove", anchor='center')
        rectang01.place(x=620, y=95)
        Entry_Est02.destroy()
    else:
        messagebox.showinfo(title ='Atencion!! Ingreso Invalido',message = 'Los valores ingresados deben ser entre 0 y 5', icon = 'warning')
        Entry_Est.focus()
    
def ingresa_btn04():
    global buttonxx
    buttonxx = Button(window, text="Confirmar", width=17, command=confirma_ingreso04)
    buttonxx.place(x=750, y=120)
    global Entry_Est03
    Entry_Est03 = Entry(window, text="",width=15)
    Entry_Est03.place(x=620, y=125)

def confirma_ingreso04():
    nva_Nota = getdouble(Entry_Est03.get())
    if nva_Nota >= 0 and nva_Nota <= 5:
        nva_Nota = getdouble(Entry_Est03.get())
        Alumnos_notas.pop(3)
        Alumnos_notas.insert(3,nva_Nota)           
        buttonxx.destroy()
        button01 = Button(window, text="Cambiar", width=17, command=ingresa_btn04)
        button01.place(x=750, y=120)
        rectang01 = Label(window, text=f"{nva_Nota}",width=15, borderwidth=4, relief="groove", anchor='center')
        rectang01.place(x=620, y=125)
        Entry_Est03.destroy()
    else:
        messagebox.showinfo(title ='Atencion!! Ingreso Invalido',message = 'Los valores ingresados deben ser entre 0 y 5', icon = 'warning')
        Entry_Est.focus()
    
    
def ingresa_btn05():
    global buttonxx
    buttonxx = Button(window, text="Confirmar", width=17, command=confirma_ingreso05)
    buttonxx.place(x=750, y=150)
    global Entry_Est04
    Entry_Est04 = Entry(window, text="",width=15)
    Entry_Est04.place(x=620, y=155)

def confirma_ingreso05():
    nva_Nota = getdouble(Entry_Est04.get())
    if nva_Nota >= 0 and nva_Nota <= 5:
        nva_Nota = getdouble(Entry_Est04.get())
        Alumnos_notas.pop(4)
        Alumnos_notas.insert(4,nva_Nota)           
        buttonxx.destroy()
        button01 = Button(window, text="Cambiar", width=17, command=ingresa_btn05)
        button01.place(x=750, y=150)
        rectang01 = Label(window, text=f"{nva_Nota}",width=15, borderwidth=4, relief="groove", anchor='center')
        rectang01.place(x=620, y=155)
        Entry_Est04.destroy()
    else:
        messagebox.showinfo(title ='Atencion!! Ingreso Invalido',message = 'Los valores ingresados deben ser entre 0 y 5', icon = 'warning')
        Entry_Est.focus()
    

    
def ingresa_btn06():
    global buttonxx
    buttonxx = Button(window, text="Confirmar", width=17, command=confirma_ingreso06)
    buttonxx.place(x=750, y=180)
    global Entry_Est05
    Entry_Est05 = Entry(window, text="",width=15)
    Entry_Est05.place(x=620, y=185)

def confirma_ingreso06():
    nva_Nota = getdouble(Entry_Est05.get())
    if nva_Nota >= 0 and nva_Nota <= 5:
        nva_Nota = getdouble(Entry_Est05.get())
        Alumnos_notas.pop(5)
        Alumnos_notas.insert(5,nva_Nota)           
        buttonxx.destroy()
        button01 = Button(window, text="Cambiar", width=17, command=ingresa_btn06)
        button01.place(x=750, y=180)
        rectang01 = Label(window, text=f"{nva_Nota}",width=15, borderwidth=4, relief="groove", anchor='center')
        rectang01.place(x=620, y=185)
        Entry_Est05.destroy()
    else:
        messagebox.showinfo(title ='Atencion!! Ingreso Invalido',message = 'Los valores ingresados deben ser entre 0 y 5', icon = 'warning')
        Entry_Est.focus()

    
def ingresa_btn07():
    global buttonxx
    buttonxx = Button(window, text="Confirmar", width=17, command=confirma_ingreso07)
    buttonxx.place(x=750, y=210)
    global Entry_Est06
    Entry_Est06 = Entry(window, text="",width=15)
    Entry_Est06.place(x=620, y=215)

def confirma_ingreso07():
    nva_Nota = getdouble(Entry_Est06.get())
    if nva_Nota >= 0 and nva_Nota <= 5:
         nva_Nota = getdouble(Entry_Est06.get())
         Alumnos_notas.pop(6)
         Alumnos_notas.insert(6,nva_Nota)           
         buttonxx.destroy()
         button01 = Button(window, text="Cambiar", width=17, command=ingresa_btn07)
         button01.place(x=750, y=210)
         rectang01 = Label(window, text=f"{nva_Nota}",width=15, borderwidth=4, relief="groove", anchor='center')
         rectang01.place(x=620, y=215)
         Entry_Est06.destroy()
    else:
        messagebox.showinfo(title ='Atencion!! Ingreso Invalido',message = 'Los valores ingresados deben ser entre 0 y 5', icon = 'warning')
        Entry_Est.focus()

def ingresa_btn08():
    global buttonxx
    buttonxx = Button(window, text="Confirmar", width=17, command=confirma_ingreso08)
    buttonxx.place(x=750, y=240)
    global Entry_Est07
    Entry_Est07 = Entry(window, text="",width=15)
    Entry_Est07.place(x=620, y=245)

def confirma_ingreso08():
    nva_Nota = getdouble(Entry_Est07.get())
    if nva_Nota >= 0 and nva_Nota <= 5:
         nva_Nota = getdouble(Entry_Est07.get())
         Alumnos_notas.pop(7)
         Alumnos_notas.insert(7,nva_Nota)           
         buttonxx.destroy()
         button01 = Button(window, text="Cambiar", width=17, command=ingresa_btn08)
         button01.place(x=750, y=240)
         rectang01 = Label(window, text=f"{nva_Nota}",width=15, borderwidth=4, relief="groove", anchor='center')
         rectang01.place(x=620, y=245)
         Entry_Est07.destroy()
    else:
        messagebox.showinfo(title ='Atencion!! Ingreso Invalido',message = 'Los valores ingresados deben ser entre 0 y 5', icon = 'warning')
        Entry_Est.focus()

    
def ingresa_btn09():
    global buttonxx
    buttonxx = Button(window, text="Confirmar", width=17, command=confirma_ingreso09)
    buttonxx.place(x=750, y=270)
    global Entry_Est08
    Entry_Est08 = Entry(window, text="",width=15)
    Entry_Est08.place(x=620, y=275)

def confirma_ingreso09():
    nva_Nota = getdouble(Entry_Est08.get())
    if nva_Nota >= 0 and nva_Nota <= 5:
         nva_Nota = getdouble(Entry_Est08.get())
         Alumnos_notas.pop(8)
         Alumnos_notas.insert(8,nva_Nota)           
         buttonxx.destroy()
         button01 = Button(window, text="Cambiar", width=17, command=ingresa_btn08)
         button01.place(x=750, y=270)
         rectang01 = Label(window, text=f"{nva_Nota}",width=15, borderwidth=4, relief="groove", anchor='center')
         rectang01.place(x=620, y=275)
         Entry_Est08.destroy()
    else:
        messagebox.showinfo(title ='Atencion!! Ingreso Invalido',message = 'Los valores ingresados deben ser entre 0 y 5', icon = 'warning')
        Entry_Est.focus()

    
def ingresa_btn10():
    global buttonxx
    buttonxx = Button(window, text="Confirmar", width=17, command=confirma_ingreso10)
    buttonxx.place(x=750, y=300)
    global Entry_Est09
    Entry_Est09 = Entry(window, text="",width=15)
    Entry_Est09.place(x=620, y=305)

def confirma_ingreso10():
    nva_Nota = getdouble(Entry_Est09.get())
    if nva_Nota >= 0 and nva_Nota <= 5:
         nva_Nota = getdouble(Entry_Est09.get())
         Alumnos_notas.pop(9)
         Alumnos_notas.insert(9,nva_Nota)           
         buttonxx.destroy()
         button01 = Button(window, text="Cambiar", width=17, command=ingresa_btn10)
         button01.place(x=750, y=300)
         rectang01 = Label(window, text=f"{nva_Nota}",width=15, borderwidth=4, relief="groove", anchor='center')
         rectang01.place(x=620, y=305)
         Entry_Est09.destroy()
    else:
        messagebox.showinfo(title ='Atencion!! Ingreso Invalido',message = 'Los valores ingresados deben ser entre 0 y 5', icon = 'warning')
        Entry_Est.focus()

def ingresa_btn11():
    global buttonxx
    buttonxx = Button(window, text="Confirmar", width=17, command=confirma_ingreso11)
    buttonxx.place(x=750, y=330)
    global Entry_Est10
    Entry_Est10 = Entry(window, text="",width=15)
    Entry_Est10.place(x=620, y=335)

def confirma_ingreso11():
    nva_Nota = getdouble(Entry_Est10.get())
    if nva_Nota >= 0 and nva_Nota <= 5:
         nva_Nota = getdouble(Entry_Est10.get())
         Alumnos_notas.pop(10)
         Alumnos_notas.insert(10,nva_Nota)           
         buttonxx.destroy()
         button01 = Button(window, text="Cambiar", width=17, command=ingresa_btn11)
         button01.place(x=750, y=330)
         rectang01 = Label(window, text=f"{nva_Nota}",width=15, borderwidth=4, relief="groove", anchor='center')
         rectang01.place(x=620, y=335)
         Entry_Est10.destroy()
    else:
        messagebox.showinfo(title ='Atencion!! Ingreso Invalido',message = 'Los valores ingresados deben ser entre 0 y 5', icon = 'warning')
        Entry_Est.focus()
    

def ingresa_btn12():
    global buttonxx
    buttonxx = Button(window, text="Confirmar", width=17, command=confirma_ingreso12)
    buttonxx.place(x=750, y=360)
    global Entry_Est11
    Entry_Est11 = Entry(window, text="",width=15)
    Entry_Est11.place(x=620, y=365)

def confirma_ingreso12():
    nva_Nota = getdouble(Entry_Est11.get())
    if nva_Nota >= 0 and nva_Nota <= 5:
         nva_Nota = getdouble(Entry_Est11.get())
         Alumnos_notas.pop(11)
         Alumnos_notas.insert(11,nva_Nota)           
         buttonxx.destroy()
         button01 = Button(window, text="Cambiar", width=17, command=ingresa_btn12)
         button01.place(x=750, y=360)
         rectang01 = Label(window, text=f"{nva_Nota}",width=15, borderwidth=4, relief="groove", anchor='center')
         rectang01.place(x=620, y=365)
         Entry_Est11.destroy()
         print (Alumnos_notas)   
    else:
        messagebox.showinfo(title ='Atencion!! Ingreso Invalido',message = 'Los valores ingresados deben ser entre 0 y 5', icon = 'warning')
        Entry_Est.focus()





def panel05():
    recuadro04 = Canvas(window, width=885,
                height=50,
                borderwidth=2,bd=2,
                background='#F3F3F3',
                relief='groove')
    recuadro04.place(x=4, y=415)
    lbl25 = Label(window,width=10, text="Adicionales", font="Arial")
    lbl25.place(x=15, y=403)
    button33 = Button(window, text="Promedios",width=33, command=Promedio_al)
    button33.place(x=10, y=425)
    button34 = Button(window, text="# Mayor al Promedio",width=33, command=Mayor_nota)
    button34.place(x=230, y=425)
    button35 = Button(window, text="# Menor al Promedio",width=33, command=Menor_nota)
    button35.place(x=450, y=425)
    button37 = Button(window, text="# Calificacion Ideal",width=33, command=Mejor_nota)
    button37.place(x=670, y=425)
    
    
def Promedio_al():
    print (Alumnos_notas)
    num = 0
    for prom in Alumnos_notas:
        num += prom
    global Promedio
    Promedio = round( num / len(Alumnos_notas),2)
    lbl77 = Label(window,width=40, text='El promedio general es '+f"{Promedio}", font="Arial")
    lbl77.place(x=15, y=360)
    return Promedio

def Mayor_nota():
    contador = 0
    for notas in Alumnos_notas:
        if notas > Promedio:
            contador += 1
            lbl77 = Label(window,width=40, text='Estudiantes con notas mayores al Promedio: '+f"{contador}", font="Arial")
            lbl77.place(x=15, y=360)
            
def Menor_nota():
    contador = 0
    for notas in Alumnos_notas:
        if notas < Promedio:
            contador += 1
            lbl77 = Label(window,width=40, text='Estudiantes con notas menores al Promedio: '+f"{contador}", font="Arial")
            lbl77.place(x=15, y=360)
            
def Mejor_nota():
    contador = 0
    for notas in Alumnos_notas:
        if notas == 5:
            contador += 1
            lbl77 = Label(window,width=40, text='Estudiantes con calificacion ideal (5.0): '+f"{contador}", font="Arial")
            lbl77.place(x=15, y=360)


start()
window.mainloop()

