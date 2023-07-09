import tkinter as tk
import conexion_bd

def ventana_insercion():
    # Conectar a la base de datos
    conexion = conexion_bd.conectar()
    cursor = conexion.cursor()

    # Crear la ventana de inserción
    ventana = tk.Toplevel()
    ventana.title("Inserción de Registros")
    ventana.geometry("400x200")

    # Función para ejecutar una consulta SQL
    def ejecutar_consulta(consulta, valores=None):
        cursor.execute(consulta, valores)
        resultados = cursor.fetchall()
        return resultados

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

    # Función para insertar un registro en la tabla tipo_cabanya
    def insertar_tipo_cabanya():
        ventana_insertar = tk.Toplevel(ventana)
        ventana_insertar.title("Insertar tipo_cabanya")
        ventana_insertar.geometry("400x200")

        etiqueta_nombre = tk.Label(ventana_insertar, text="Nombre:")
        etiqueta_nombre.pack()

        entrada_nombre = tk.Entry(ventana_insertar)
        entrada_nombre.pack()

        def guardar_tipo_cabanya():
            nombre = entrada_nombre.get()
            consulta = "INSERT INTO tipo_cabanya (nombre) VALUES (%s)"
            valores = (nombre,)
            cursor.execute(consulta, valores)
            conexion.commit()
            ventana_insertar.destroy()
            tk.messagebox.showinfo("Éxito", "Registro insertado correctamente.")

        boton_guardar = tk.Button(ventana_insertar, text="Guardar", command=guardar_tipo_cabanya)
        boton_guardar.pack()

    # Función para insertar un registro en la tabla cabanyas
    def insertar_cabanyas():
        ventana_insertar = tk.Toplevel(ventana)
        ventana_insertar.title("Insertar cabanyas")
        ventana_insertar.geometry("400x250")

        etiqueta_tipo_id = tk.Label(ventana_insertar, text="ID del tipo:")
        etiqueta_tipo_id.pack()

        entrada_tipo_id = tk.Entry(ventana_insertar)
        entrada_tipo_id.pack()

        etiqueta_precio = tk.Label(ventana_insertar, text="Precio:")
        etiqueta_precio.pack()

        entrada_precio = tk.Entry(ventana_insertar)
        entrada_precio.pack()

        def guardar_cabanyas():
            tipo_id = int(entrada_tipo_id.get())
            precio = float(entrada_precio.get())
            consulta = "INSERT INTO cabanyas (tipo_id, precio) VALUES (%s, %s)"
            valores = (tipo_id, precio)
            cursor.execute(consulta, valores)
            conexion.commit()
            ventana_insertar.destroy()
            tk.messagebox.showinfo("Éxito", "Registro insertado correctamente.")

        boton_guardar = tk.Button(ventana_insertar, text="Guardar", command=guardar_cabanyas)
        boton_guardar.pack()

    # Función para insertar un registro en la tabla tipo_usuario
    def insertar_tipo_usuario():
        ventana_insertar = tk.Toplevel(ventana)
        ventana_insertar.title("Insertar tipo_usuario")
        ventana_insertar.geometry("400x200")

        etiqueta_nombre = tk.Label(ventana_insertar, text="Nombre:")
        etiqueta_nombre.pack()

        entrada_nombre = tk.Entry(ventana_insertar)
        entrada_nombre.pack()

        def guardar_tipo_usuario():
            nombre = entrada_nombre.get()
            consulta = "INSERT INTO tipo_usuario (nombre) VALUES (%s)"
            valores = (nombre,)
            cursor.execute(consulta, valores)
            conexion.commit()
            ventana_insertar.destroy()
            tk.messagebox.showinfo("Éxito", "Registro insertado correctamente.")

        boton_guardar = tk.Button(ventana_insertar, text="Guardar", command=guardar_tipo_usuario)
        boton_guardar.pack()

    # Función para insertar un registro en la tabla usuarios
    def insertar_usuarios():
        ventana_insertar = tk.Toplevel(ventana)
        ventana_insertar.title("Insertar usuarios")
        ventana_insertar.geometry("400x350")

        etiqueta_tipo_id = tk.Label(ventana_insertar, text="ID del tipo:")
        etiqueta_tipo_id.pack()

        entrada_tipo_id = tk.Entry(ventana_insertar)
        entrada_tipo_id.pack()

        etiqueta_rut = tk.Label(ventana_insertar, text="RUT:")
        etiqueta_rut.pack()

        entrada_rut = tk.Entry(ventana_insertar)
        entrada_rut.pack()

        etiqueta_nombre = tk.Label(ventana_insertar, text="Nombre:")
        etiqueta_nombre.pack()

        entrada_nombre = tk.Entry(ventana_insertar)
        entrada_nombre.pack()

        etiqueta_apellido = tk.Label(ventana_insertar, text="Apellido:")
        etiqueta_apellido.pack()

        entrada_apellido = tk.Entry(ventana_insertar)
        entrada_apellido.pack()

        etiqueta_email = tk.Label(ventana_insertar, text="Email:")
        etiqueta_email.pack()

        entrada_email = tk.Entry(ventana_insertar)
        entrada_email.pack()

        etiqueta_telefono = tk.Label(ventana_insertar, text="Teléfono:")
        etiqueta_telefono.pack()

        entrada_telefono = tk.Entry(ventana_insertar)
        entrada_telefono.pack()

        def guardar_usuarios():
            tipo_id = int(entrada_tipo_id.get())
            rut = int(entrada_rut.get())
            nombre = entrada_nombre.get()
            apellido = entrada_apellido.get()
            email = entrada_email.get()
            telefono = entrada_telefono.get()
            consulta = "INSERT INTO usuarios (tipo_id, rut, nombre, apellido, email, telefono) VALUES (%s, %s, %s, %s, %s, %s)"
            valores = (tipo_id, rut, nombre, apellido, email, telefono)
            cursor.execute(consulta, valores)
            conexion.commit()
            ventana_insertar.destroy()
            tk.messagebox.showinfo("Éxito", "Registro insertado correctamente.")

        boton_guardar = tk.Button(ventana_insertar, text="Guardar", command=guardar_usuarios)
        boton_guardar.pack()

    # Función para insertar un registro en la tabla reservas
    def insertar_reservas():
        ventana_insertar = tk.Toplevel(ventana)
        ventana_insertar.title("Insertar reservas")
        ventana_insertar.geometry("400x350")

        etiqueta_cabanya_id = tk.Label(ventana_insertar, text="ID dela cabaña:")
        etiqueta_cabanya_id.pack()

        entrada_cabanya_id = tk.Entry(ventana_insertar)
        entrada_cabanya_id.pack()

        etiqueta_usuario_id = tk.Label(ventana_insertar, text="ID del usuario:")
        etiqueta_usuario_id.pack()

        entrada_usuario_id = tk.Entry(ventana_insertar)
        entrada_usuario_id.pack()

        etiqueta_fecha_entrada = tk.Label(ventana_insertar, text="Fecha de entrada (YYYY-MM-DD):")
        etiqueta_fecha_entrada.pack()

        entrada_fecha_entrada = tk.Entry(ventana_insertar)
        entrada_fecha_entrada.pack()

        etiqueta_fecha_salida = tk.Label(ventana_insertar, text="Fecha de salida (YYYY-MM-DD):")
        etiqueta_fecha_salida.pack()

        entrada_fecha_salida = tk.Entry(ventana_insertar)
        entrada_fecha_salida.pack()

        def guardar_reservas():
            cabanya_id = int(entrada_cabanya_id.get())
            usuario_id = int(entrada_usuario_id.get())
            fecha_entrada = entrada_fecha_entrada.get()
            fecha_salida = entrada_fecha_salida.get()
            consulta = "INSERT INTO reservas (cabanya_id, usuario_id, fecha_entrada, fecha_salida) VALUES (%s, %s, %s, %s)"
            valores = (cabanya_id, usuario_id, fecha_entrada, fecha_salida)
            cursor.execute(consulta, valores)
            conexion.commit()
            ventana_insertar.destroy()
            tk.messagebox.showinfo("Éxito", "Registro insertado correctamente.")

        boton_guardar = tk.Button(ventana_insertar, text="Guardar", command=guardar_reservas)
        boton_guardar.pack()

    # Función para insertar un registro en la tabla metodo_pago
    def insertar_metodo_pago():
        ventana_insertar = tk.Toplevel(ventana)
        ventana_insertar.title("Insertar metodo_pago")
        ventana_insertar.geometry("400x200")

        etiqueta_nombre = tk.Label(ventana_insertar, text="Nombre:")
        etiqueta_nombre.pack()

        entrada_nombre = tk.Entry(ventana_insertar)
        entrada_nombre.pack()

        def guardar_metodo_pago():
            nombre = entrada_nombre.get()
            consulta = "INSERT INTO metodo_pago (nombre) VALUES (%s)"
            valores = (nombre,)
            cursor.execute(consulta, valores)
            conexion.commit()
            ventana_insertar.destroy()
            tk.messagebox.showinfo("Éxito", "Registro insertado correctamente.")

        boton_guardar = tk.Button(ventana_insertar, text="Guardar", command=guardar_metodo_pago)
        boton_guardar.pack()

    # Función para insertar un registro en la tabla pagos
    def insertar_pagos():
        ventana_insertar = tk.Toplevel(ventana)
        ventana_insertar.title("Insertar pagos")
        ventana_insertar.geometry("400x350")

        etiqueta_reserva_id = tk.Label(ventana_insertar, text="ID de la reserva:")
        etiqueta_reserva_id.pack()

        entrada_reserva_id = tk.Entry(ventana_insertar)
        entrada_reserva_id.pack()

        etiqueta_fecha_pago = tk.Label(ventana_insertar, text="Fecha de pago (YYYY-MM-DD):")
        etiqueta_fecha_pago.pack()

        entrada_fecha_pago = tk.Entry(ventana_insertar)
        entrada_fecha_pago.pack()

        etiqueta_monto = tk.Label(ventana_insertar, text="Monto:")
        etiqueta_monto.pack()

        entrada_monto = tk.Entry(ventana_insertar)
        entrada_monto.pack()

        etiqueta_metodo_pago = tk.Label(ventana_insertar, text="ID del método de pago:")
        etiqueta_metodo_pago.pack()

        entrada_metodo_pago = tk.Entry(ventana_insertar)
        entrada_metodo_pago.pack()

        def guardar_pagos():
            reserva_id = int(entrada_reserva_id.get())
            fecha_pago = entrada_fecha_pago.get()
            monto = float(entrada_monto.get())
            metodo_pago = int(entrada_metodo_pago.get())
            consulta = "INSERT INTO pagos (reserva_id, fecha_pago, monto, metodo_pago) VALUES (%s, %s, %s, %s)"
            valores = (reserva_id, fecha_pago, monto, metodo_pago)
            cursor.execute(consulta, valores)
            conexion.commit()
            ventana_insertar.destroy()
            tk.messagebox.showinfo("Éxito", "Registro insertado correctamente.")

        boton_guardar = tk.Button(ventana_insertar, text="Guardar", command=guardar_pagos)
        boton_guardar.pack()

    # Crear botones para insertar registros en cada tabla
    boton_insertar_tipo_cabanya = tk.Button(ventana, text="Insertar tipo_cabanya", command=insertar_tipo_cabanya)
    boton_insertar_tipo_cabanya.pack()

    boton_insertar_cabanyas = tk.Button(ventana, text="Insertar cabanyas", command=insertar_cabanyas)
    boton_insertar_cabanyas.pack()

    boton_insertar_tipo_usuario = tk.Button(ventana, text="Insertar tipo_usuario", command=insertar_tipo_usuario)
    boton_insertar_tipo_usuario.pack()

    boton_insertar_usuarios = tk.Button(ventana, text="Insertar usuarios", command=insertar_usuarios)
    boton_insertar_usuarios.pack()

    boton_insertar_reservas = tk.Button(ventana, text="Insertar reservas", command=insertar_reservas)
    boton_insertar_reservas.pack()

    boton_insertar_metodo_pago = tk.Button(ventana, text="Insertar metodo_pago", command=insertar_metodo_pago)
    boton_insertar_metodo_pago.pack()

    boton_insertar_pagos = tk.Button(ventana, text="Insertar pagos", command=insertar_pagos)
    boton_insertar_pagos.pack()

    # Cerrar la conexión a la base de datos al cerrar la ventana
    def cerrar_ventana():
        conexion_bd.cerrar_conexion(conexion)
        ventana.destroy()

    ventana.protocol("WM_DELETE_WINDOW", cerrar_ventana)

    # Ejecutar la ventana de inserción
    ventana.mainloop()