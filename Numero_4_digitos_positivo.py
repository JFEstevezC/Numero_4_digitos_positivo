from tkinter import *
from tkinter import messagebox
# -------------------
# funciones de la app
# -------------------
def comprobar():
    z = int(x.get())
    if z >= 1000 and z < 10000:
        messagebox.showinfo("Número positivo de 4 digitos", "Comprobando")
        t_resultados.insert(INSERT, "El número es de 4 dígitos positivo " "\n")
    else:
        messagebox.showinfo("Número positivo de 4 digitos", "Comprobando")
        t_resultados.insert(INSERT, "El número no es de 4 dígitos positivo " "\n")
def borrar():
    messagebox.showinfo("Número positivo de 4 digitos", "Los datos seran borrados")
    x.set("")
    t_resultados.delete("1.0", "end")   
def salir():
    messagebox.showinfo("Número positivo de 4 digitos", "La aplicación se cerrará. ")
    ventana_principal.destroy()
# -------------------
# ventana principal
# -------------------
ventana_principal = Tk()

# Título de la ventana
ventana_principal.title("Sistemas UIS")

# Tamaño de la ventana
ventana_principal.geometry("500x500")

# Deshabilitar botón de maximixar
ventana_principal.resizable(0,0)

# Color de fondo de la ventana
ventana_principal.config(bg="black")

# -------------------
# variables globlales
# -------------------
x = StringVar()

# -------------------
# frame entrada datos
# -------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="green2", width=480, height=240)
frame_entrada.place(x=10, y=10)

# etiqueta para  el título de la app
titulo = Label(frame_entrada, text= "¿Es positivo de 4 digitos?")
titulo.config(bg="green2", fg="blue", font=("Arial",16))
titulo.place(x=120,y=5)

# Caja de entrada de texto
tx = Label(frame_entrada, text="Escriba el número para el cuál desea saber si es un número\n de 4 digitos positivo o no ")
tx.config(bg="green", fg="blue", font=("Times New Roman",12))
tx.place(x=20, y=50, width=500, height=70)

# Entrada
entry_x = Entry(frame_entrada, textvariable=x)
entry_x.config(bg="White", fg="black", font=("Times New Roman",16))
entry_x.focus_set()
entry_x.place(x=190, y=160, width=100, height=30)

# frame operaciones

frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg="blue", width=480, height=120)
frame_operaciones.place(x=10, y=250)

# Botón Sumar
bt_comprobar = Button(frame_operaciones, text="Comprobar", command=comprobar)
bt_comprobar.config(bg="white",  fg="black", font=("Times New Roman",16))
bt_comprobar.place(x=45, y=45, width=100, height=50)

# Botón Borrar
bt_borrar = Button(frame_operaciones, text="Borrar", command=borrar)
bt_borrar.config(bg="white", fg="black", font=("Times New Roman",16))
bt_borrar.place(x=190, y=45, width=100, height=50)

# Botón Salir
bt_salir = Button(frame_operaciones, text="Salir", command=salir)
bt_salir.config(bg="white", fg="black", font=("Times New Roman",16))
bt_salir.place(x=335, y=45, width=100, height=50)

# frame resultados
frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="red", width=480, height=120)
frame_resultados.place(x=10, y=370)

# Caja de salida de texto
t_resultados = Text(frame_resultados)
t_resultados.config(bg="lime green", fg="white", font=("Times New Roman",16))
t_resultados.place(x=10, y=10, width=460, height=80)

# Se ejecuta el método mainloop() de la clase Tk a través de la instancia ventana principal. Este método despliega una ventana simple en la pantalla y queda a la espera de lo que el usuario haga (click en un botón, escribir, etc) Cada acción del usuario se conoce como un evento. El método mainloop() es un bucle infinito.
ventana_principal.mainloop()