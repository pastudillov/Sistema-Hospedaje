import tkinter as tk
import conexion_bd

def ventana_consulta():
    # Conectar a la base de datos
    conexion = conexion_bd.conectar()
    cursor = conexion.cursor()

    # Verificar la conexión a la base de datos
    if conexion is None:
        tk.messagebox.showerror("Error", "No se pudo conectar a la base de datos")
        return

    # Crear la ventana de inserción
    ventana = tk.Toplevel()
    ventana.title("Consulta de Datos")
    ventana.geometry("400x200")

    # Función para ejecutar una consulta SQL
    def ejecutar_consulta(consulta):
        try:
            cursor.execute(consulta)
            resultados = cursor.fetchall()
            return resultados
        except Exception as e:
            tk.messagebox.showerror("Error", f"No se pudo ejecutar la consulta: {str(e)}")

    # Función para mostrar los resultados de una consulta en una ventana emergente
    def mostrar_resultados(resultados):
        ventana_resultados = tk.Toplevel(ventana)
        ventana_resultados.title("Resultados")
        ventana_resultados.geometry("400x300")

        etiqueta_resultados = tk.Label(ventana_resultados, text="Resultados:")
        etiqueta_resultados.pack()

        texto_resultados = tk.Text(ventana_resultados)
        texto_resultados.pack()

        for resultado in resultados:
            texto_resultados.insert(tk.END, str(resultado) + "\n")

    # Función para consultar la tabla tipo_cabanya
    def consultar_tipo_cabanya():
        consulta = "SELECT * FROM tipo_cabanya"
        resultados = ejecutar_consulta(consulta)
        mostrar_resultados(resultados)

    # Función para consultar la tabla cabanyas
    def consultar_cabanyas():
        consulta = "SELECT * FROM cabanyas"
        resultados = ejecutar_consulta(consulta)
        mostrar_resultados(resultados)

    # Función para consultar la tabla tipo_usuario
    def consultar_tipo_usuario():
        consulta = "SELECT * FROM tipo_usuario"
        resultados = ejecutar_consulta(consulta)
        mostrar_resultados(resultados)

    # Función para consultar la tabla usuarios
    def consultar_usuarios():
        consulta = "SELECT * FROM usuarios"
        resultados = ejecutar_consulta(consulta)
        mostrar_resultados(resultados)

    # Función para consultar la tabla reservas
    def consultar_reservas():
        consulta = "SELECT * FROM reservas"
        resultados = ejecutar_consulta(consulta)
        mostrar_resultados(resultados)

    # Función para consultar la tabla metodo_pago
    def consultar_metodo_pago():
        consulta = "SELECT * FROM metodo_pago"
        resultados = ejecutar_consulta(consulta)
        mostrar_resultados(resultados)

    # Función para consultar la tabla pagos
    def consultar_pagos():
        consulta = "SELECT * FROM pagos"
        resultados = ejecutar_consulta(consulta)
        mostrar_resultados(resultados)

    # Crear botones para realizar las consultas
    boton_tipo_cabanya = tk.Button(ventana, text="Consultar tipo_cabanya", command=consultar_tipo_cabanya)
    boton_tipo_cabanya.pack()

    boton_cabanyas = tk.Button(ventana, text="Consultar cabanyas", command=consultar_cabanyas)
    boton_cabanyas.pack()

    boton_tipo_usuario = tk.Button(ventana, text="Consultar tipo_usuario", command=consultar_tipo_usuario)
    boton_tipo_usuario.pack()

    boton_usuarios = tk.Button(ventana, text="Consultar usuarios", command=consultar_usuarios)
    boton_usuarios.pack()

    boton_reservas = tk.Button(ventana, text="Consultar reservas", command=consultar_reservas)
    boton_reservas.pack()

    boton_metodo_pago = tk.Button(ventana, text="Consultar metodo_pago", command=consultar_metodo_pago)
    boton_metodo_pago.pack()

    boton_pagos = tk.Button(ventana, text="Consultar pagos", command=consultar_pagos)
    boton_pagos.pack()

    # Cerrar la conexión a la base de datos al cerrar la ventana
    def cerrar_ventana():
        conexion_bd.cerrar_conexion(conexion)
        ventana.destroy()

    ventana.protocol("WM_DELETE_WINDOW", cerrar_ventana)

    # Ejecutar la ventana de inserción
    ventana.mainloop()