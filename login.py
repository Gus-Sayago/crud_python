import tkinter as tk
from tkinter import messagebox
from conexion import *

ventana = tk.Tk()
ventana.geometry("320x320")

cursor = conn.cursor()

lblUsuario = tk.Label(text="Usuario: ")
lblUsuario.grid(row=0, column=0)

entryUsuario = tk.Entry()
entryUsuario.grid(row=0, column=1)

lblClave = tk.Label(text="Contraseña: ")
lblClave.grid(row=1, column=0)

entryClave = tk.Entry(show="*")
entryClave.grid(row=1, column=1)


def login():
    usuario = entryUsuario.get()
    clave = entryClave.get()
    try:
        query = "SELECT * from usuario where usuario= %s  and password=%s"
        cursor.execute(query,(usuario,clave))
        if cursor.fetchone() is not None:
             messagebox.showinfo("Log In", "Inicio de sesión exitoso")
        else:
             messagebox.showerror("Log In", "Error al iniciar sesión")
    except mysql.connector.Error as err:
            print("Error al conectar a la base de datos:", err)
        

btnIngresar = tk.Button(text="Log In",command=login)
btnIngresar.grid(row=2, column=0)




ventana.mainloop()