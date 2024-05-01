import tkinter as tk
from tkinter import messagebox
from conexion import *


cursor = conn.cursor()


ventana = tk.Tk()
ventana.geometry("480x480")
ventana.title("Registro de Usuarios")

lblUsuario = tk.Label(text="Usuario:")
lblUsuario.grid(row=0, column=0)
entryUsuario = tk.Entry()
entryUsuario.grid(row=0, column=1)

lblPassword = tk.Label(text="Password:")
lblPassword.grid(row=1, column=0)
entryPassword = tk.Entry(show='*')
entryPassword.grid(row=1, column=1)

def registrarUsuario():
    usuario = entryUsuario.get()
    clave = entryPassword.get()
    sql = "INSERT INTO usuario(usuario, password) VALUES(%s,%s)"
    cursor.execute(sql,(usuario,clave))
    messagebox.showinfo("Alta de usuario", "Registro exitoso")
    
    # Confirmar los cambios y cerrar la conexión
    conn.commit()
    conn.close()

def limpiarForm():
    entryUsuario.delete(0,tk.END)
    entryPassword.delete(0, tk.END)

btnRegistro = tk.Button(text="Registrar", command=registrarUsuario)
btnRegistro.grid(row=2, column=0)

btnClear = tk.Button(text="Limpiar", command=limpiarForm)
btnClear.grid(row=2, column=1)

ventana.mainloop()