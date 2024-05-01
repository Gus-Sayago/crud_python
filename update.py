import tkinter as tk
from tkinter import messagebox
from conexion import *

ventana = tk.Tk()
ventana.geometry("320x320")
ventana.title("Actualizar datos")


cursor = conn.cursor()
lblUsuario = tk.Label(text="Usuario: ")
lblUsuario.grid(row=0, column=0)

entryUsuario = tk.Entry()
entryUsuario.grid(row=0, column=1)

lblClave = tk.Label(text="Contraseña: ")
lblClave.grid(row=1, column=0)

entryClave = tk.Entry(show="*")
entryClave.grid(row=1, column=1)

lblUsuarioNuevo = tk.Label(text="Nuevo Usuario: ")
lblUsuarioNuevo.grid(row=2, column=0)

entryUsuarioNuevo = tk.Entry()
entryUsuarioNuevo.grid(row=2, column=1)

lblClaveNueva = tk.Label(text="Nueva Contraseña: ")
lblClaveNueva.grid(row=3, column=0)

entryClaveNueva = tk.Entry(show="*")
entryClaveNueva.grid(row=3, column=1)



def actualizar():
    nuevoUsuario = entryUsuarioNuevo.get()
    nuevaClave = entryClaveNueva.get()
    usuarioViejo = entryUsuario.get()
    
    # Verificar si el usuario antiguo existe
    buscar = "SELECT * FROM usuario WHERE usuario = %s"
    cursor.execute(buscar, (usuarioViejo,))
    usuario_encontrado = cursor.fetchone()
    conn.commit()
    
    #si existe el usuario actualizamos 
    if usuario_encontrado:
        query = "UPDATE usuario SET usuario = %s, password=%s WHERE usuario=%s"
        cursor.execute(query, (nuevoUsuario,nuevaClave,usuarioViejo))
        conn.commit()
        messagebox.showinfo("Update", "Datos actualizados correctamente.")
    else:
        messagebox.showerror("Update", "El usuario ingresado no existe.")

btnActualizar = tk.Button(text="Actualizar", command=actualizar)
btnActualizar.grid(row=4, column=0)




ventana.mainloop()