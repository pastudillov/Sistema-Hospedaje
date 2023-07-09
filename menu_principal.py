import tkinter as tk
import conexion_bd
import modulo_insercion
import modulo_consulta
import modulo_actualizacion
import modulo_eliminacion

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación de Base de Datos")
ventana.geometry("400x300")

# Funciones para abrir las ventanas de cada módulo
def abrir_ventana_insercion():
    modulo_insercion.ventana_insercion()

def abrir_ventana_consulta():
    modulo_consulta.ventana_consulta()

def abrir_ventana_actualizacion():
    modulo_actualizacion.ventana_actualizacion()

def abrir_ventana_eliminacion():
    modulo_eliminacion.ventana_eliminacion()

# Crear botones para acceder a las ventanas de inserción, actualización y eliminación
boton_insercion = tk.Button(ventana, text="Inserción de Registros", command=abrir_ventana_insercion)
boton_insercion.pack()

boton_consulta = tk.Button(ventana, text="Consulta de datos", command=abrir_ventana_consulta)
boton_consulta.pack()

boton_actualizacion = tk.Button(ventana, text="Actualización de Registros", command=abrir_ventana_actualizacion)
boton_actualizacion.pack()

boton_eliminacion = tk.Button(ventana, text="Eliminación de Registros", command=abrir_ventana_eliminacion)
boton_eliminacion.pack()

# Ejecutar la aplicación
ventana.mainloop()