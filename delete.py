import tkinter as tk
from tkinter import messagebox
from conexion import *

ventana = tk.Tk()
ventana.geometry("320x320")
ventana.title("DELETE")

cursor = conn.cursor()


lblUsuario = tk.Label(text="Usuario: ")
lblUsuario.grid(row=0, column=0)

entryUsuario = tk.Entry()
entryUsuario.grid(row=0, column=1)

lblClave = tk.Label(text="Contraseña: ")
lblClave.grid(row=1, column=0)
entryClave = tk.Entry(show="*")
entryClave.grid(row=1, column=1)

def eliminar():
    usuario = entryUsuario.get()
    # Verificar si el usuario antiguo existe
    buscar = "SELECT * FROM usuario WHERE usuario = %s"
    cursor.execute(buscar, (usuario,))
    usuario_encontrado = cursor.fetchone()
    conn.commit()
    
    #si existe el usuario actualizamos 
    if usuario_encontrado:
        query = "DELETE FROM usuario WHERE usuario=%s"
        cursor.execute(query, (usuario,))
        conn.commit()
        messagebox.showinfo("Delete", "Usuario eliminado correctamente.")
    else:
        messagebox.showerror("Delete", "El usuario ingresado no existe.")


btnEliminar = tk.Button(text="Delete",command=eliminar)
btnEliminar.grid(row=2, column=0)

ventana.mainloop()