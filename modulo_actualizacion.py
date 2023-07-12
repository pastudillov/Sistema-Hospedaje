import tkinter as tk
import conexion_bd
import tkinter.messagebox as messagebox

def ventana_actualizacion():
    # Conectar a la base de datos
    conexion = conexion_bd.conectar()
    cursor = conexion.cursor()

    # Crear la ventana de actualización
    ventana = tk.Toplevel()
    ventana.title("Actualización de Registros")
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

    # Función para validar si un ID de registro existe en una tabla
    def validar_id(id, tabla):
        consulta = f"SELECT id FROM {tabla} WHERE id = %s"
        valores = (id,)
        cursor.execute(consulta, valores)
        resultado = cursor.fetchone()
        if resultado:
            return True
        else:
            return False

    # Función para actualizar un registro en la tabla tipo_cabanya
    def actualizar_tipo_cabanya():
        ventana_actualizar = tk.Toplevel(ventana)
        ventana_actualizar.title("Actualizar tipo_cabanya")
        ventana_actualizar.geometry("400x200")

        etiqueta_id = tk.Label(ventana_actualizar, text="ID del registro a actualizar:")
        etiqueta_id.pack()

        entrada_id = tk.Entry(ventana_actualizar)
        entrada_id.pack()

        etiqueta_nombre = tk.Label(ventana_actualizar, text="Nuevo nombre:")
        etiqueta_nombre.pack()

        entrada_nombre = tk.Entry(ventana_actualizar)
        entrada_nombre.pack()

        def guardar_tipo_cabanya():
            # Obtener el nombre actual del registro
            id_actual = int(entrada_id.get())
            consulta_nombre_actual = "SELECT nombre FROM tipo_cabanya WHERE id = %s"
            cursor.execute(consulta_nombre_actual, (id_actual,))
            nombre_actual = cursor.fetchone()[0]

            id = int(entrada_id.get())
            nombre = entrada_nombre.get()

            if not validar_id(id, "tipo_cabanya"):
                messagebox.showerror("Error", "El ID de registro no existe.")
                return

            if nombre == "":
                nombre = nombre_actual

            consulta = "UPDATE tipo_cabanya SET nombre = %s WHERE id = %s"
            valores = (nombre, id)
            cursor.execute(consulta, valores)
            conexion.commit()
            ventana_actualizar.destroy()
            messagebox.showinfo("Éxito", "Registro actualizado correctamente.")

        boton_guardar = tk.Button(ventana_actualizar, text="Guardar", command=guardar_tipo_cabanya)
        boton_guardar.pack()

    # Función para actualizar un registro en la tabla cabanyas
    def actualizar_cabanyas():
        ventana_actualizar = tk.Toplevel(ventana)
        ventana_actualizar.title("Actualizar cabanyas")
        ventana_actualizar.geometry("400x250")

        etiqueta_id = tk.Label(ventana_actualizar, text="ID del registro a actualizar:")
        etiqueta_id.pack()

        entrada_id = tk.Entry(ventana_actualizar)
        entrada_id.pack()

        etiqueta_tipo_id = tk.Label(ventana_actualizar, text="Nuevo ID del tipo:")
        etiqueta_tipo_id.pack()

        entrada_tipo_id = tk.Entry(ventana_actualizar)
        entrada_tipo_id.pack()

        etiqueta_precio = tk.Label(ventana_actualizar, text="Nuevo precio:")
        etiqueta_precio.pack()

        entrada_precio = tk.Entry(ventana_actualizar)
        entrada_precio.pack()

        def guardar_cabanyas():
            id = int(entrada_id.get())
            tipo_id = int(entrada_tipo_id.get())
            precio = float(entrada_precio.get())
            consulta = "UPDATE cabanyas SET tipo_id = %s, precio = %s WHERE id = %s"
            valores = (tipo_id, precio, id)
            cursor.execute(consulta, valores)
            conexion.commit()
            ventana_actualizar.destroy()
            tk.messagebox.showinfo("Éxito", "Registro actualizado correctamente.")

        boton_guardar = tk.Button(ventana_actualizar, text="Guardar", command=guardar_cabanyas)
        boton_guardar.pack()

    # Función para actualizar un registro en la tabla tipo_usuario
    def actualizar_tipo_usuario():
        ventana_actualizar = tk.Toplevel(ventana)
        ventana_actualizar.title("Actualizar tipo_usuario")
        ventana_actualizar.geometry("400x200")

        etiqueta_id = tk.Label(ventana_actualizar, text="ID del registro a actualizar:")
        etiqueta_id.pack()

        entrada_id = tk.Entry(ventana_actualizar)
        entrada_id.pack()

        etiqueta_nombre = tk.Label(ventana_actualizar, text="Nuevo nombre:")
        etiqueta_nombre.pack()

        entrada_nombre = tk.Entry(ventana_actualizar)
        entrada_nombre.pack()

        def guardar_tipo_usuario():
            id = int(entrada_id.get())
            nombre = entrada_nombre.get()
            consulta = "UPDATE tipo_usuario SET nombre = %s WHERE id = %s"
            valores = (nombre, id)
            cursor.execute(consulta, valores)
            conexion.commit()
            ventana_actualizar.destroy()
            tk.messagebox.showinfo("Éxito", "Registro actualizado correctamente.")

        boton_guardar = tk.Button(ventana_actualizar, text="Guardar", command=guardar_tipo_usuario)
        boton_guardar.pack()

    # Función para actualizar un registro en la tabla usuarios
    def actualizar_usuarios():
        ventana_actualizar = tk.Toplevel(ventana)
        ventana_actualizar.title("Actualizar usuarios")
        ventana_actualizar.geometry("400x350")

        etiqueta_id = tk.Label(ventana_actualizar, text="ID del registro a actualizar:")
        etiqueta_id.pack()

        entrada_id = tk.Entry(ventana_actualizar)
        entrada_id.pack()

        etiqueta_tipo_id = tk.Label(ventana_actualizar, text="Nuevo ID del tipo:")
        etiqueta_tipo_id.pack()

        entrada_tipo_id = tk.Entry(ventana_actualizar)
        entrada_tipo_id.pack()

        etiqueta_rut = tk.Label(ventana_actualizar, text="Nuevo RUT:")
        etiqueta_rut.pack()

        entrada_rut = tk.Entry(ventana_actualizar)
        entrada_rut.pack()

        etiqueta_nombre = tk.Label(ventana_actualizar, text="Nuevo nombre:")
        etiqueta_nombre.pack()

        entrada_nombre = tk.Entry(ventana_actualizar)
        entrada_nombre.pack()

        etiqueta_apellido = tk.Label(ventana_actualizar, text="Nuevo apellido:")
        etiqueta_apellido.pack()

        entrada_apellido = tk.Entry(ventana_actualizar)
        entrada_apellido.pack()

        etiqueta_email = tk.Label(ventana_actualizar, text="Nuevo email:")
        etiqueta_email.pack()

        entrada_email = tk.Entry(ventana_actualizar)
        entrada_email.pack()

        etiqueta_telefono = tk.Label(ventana_actualizar, text="Nuevo teléfono:")
        etiqueta_telefono.pack()

        entrada_telefono = tk.Entry(ventana_actualizar)
        entrada_telefono.pack()

        def guardar_usuarios():
            # Obtener los valores actuales del registro
            id_actual = int(entrada_id.get())
            consulta_actual = "SELECT tipo_id, rut, nombre, apellido, email, telefono FROM usuarios WHERE id = %s"
            cursor.execute(consulta_actual, (id_actual,))
            valores_actuales = cursor.fetchone()

            id = int(entrada_id.get())
            tipo_id = int(entrada_tipo_id.get()) if entrada_tipo_id.get() != "" else valores_actuales[0]
            rut = int(entrada_rut.get()) if entrada_rut.get() != "" else valores_actuales[1]
            nombre = entrada_nombre.get()
            apellido = entrada_apellido.get()
            email = entrada_email.get()
            telefono = entrada_telefono.get()

            if not validar_id(id, "usuarios"):
                messagebox.showerror("Error", "El ID de registro no existe.")
                return

            if nombre == "":
                nombre = valores_actuales[2]

            if apellido == "":
                apellido = valores_actuales[3]

            if email == "":
                email = valores_actuales[4]

            if telefono == "":
                telefono = valores_actuales[5]

            consulta = "UPDATE usuarios SET tipo_id = %s, rut = %s, nombre = %s, apellido = %s, email = %s, telefono = %s WHERE id = %s"
            valores = (tipo_id, rut, nombre, apellido, email, telefono, id)
            cursor.execute(consulta, valores)
            conexion.commit()
            ventana_actualizar.destroy()
            messagebox.showinfo("Éxito", "Registro actualizado correctamente.")

        boton_guardar = tk.Button(ventana_actualizar, text="Guardar", command=guardar_usuarios)
        boton_guardar.pack()

    # Función para actualizar un registro en la tabla reservas
    def actualizar_reservas():
        ventana_actualizar = tk.Toplevel(ventana)
        ventana_actualizar.title("Actualizar reservas")
        ventana_actualizar.geometry("400x350")

        etiqueta_id = tk.Label(ventana_actualizar, text="ID del registro a actualizar:")
        etiqueta_id.pack()

        entrada_id = tk.Entry(ventana_actualizar)
        entrada_id.pack()

        etiqueta_cabanya_id = tk.Label(ventana_actualizar, text="Nuevo ID de la cabaña:")
        etiqueta_cabanya_id.pack()

        entrada_cabanya_id = tk.Entry(ventana_actualizar)
        entrada_cabanya_id.pack()

        etiqueta_usuario_id = tk.Label(ventana_actualizar, text="Nuevo ID del usuario:")
        etiqueta_usuario_id.pack()

        entrada_usuario_id = tk.Entry(ventana_actualizar)
        entrada_usuario_id.pack()

        etiqueta_fecha_entrada = tk.Label(ventana_actualizar, text="Nueva fecha de entrada (YYYY-MM-DD):")
        etiqueta_fecha_entrada.pack()

        entrada_fecha_entrada = tk.Entry(ventana_actualizar)
        entrada_fecha_entrada.pack()

        etiqueta_fecha_salida = tk.Label(ventana_actualizar, text="Nueva fecha de salida (YYYY-MM-DD):")
        etiqueta_fecha_salida.pack()

        entrada_fecha_salida = tk.Entry(ventana_actualizar)
        entrada_fecha_salida.pack()

        def guardar_reservas():
            try:
                id = int(entrada_id.get())
            except: 
                messagebox.showwarning(message="Debe llenar el campo ID")
            consulta_actual = "SELECT cabanya_id, usuario_id, fecha_entrada, fecha_salida FROM reservas WHERE id = %s"
            cursor.execute(consulta_actual, (id,))
            valores_actuales = cursor.fetchone()

            cabanya_id = int(entrada_cabanya_id.get()) if entrada_cabanya_id.get() != "" else valores_actuales[0]
            usuario_id = int(entrada_usuario_id.get()) if entrada_usuario_id.get() != "" else valores_actuales[1]
            fecha_entrada = entrada_fecha_entrada.get() if entrada_fecha_entrada.get() != "" else valores_actuales[2]
            fecha_salida = entrada_fecha_salida.get() if entrada_fecha_salida.get() != "" else valores_actuales[3]
            consulta = "UPDATE reservas SET cabanya_id = %s, usuario_id = %s, fecha_entrada = %s, fecha_salida = %s WHERE id = %s"
            valores = (cabanya_id, usuario_id, fecha_entrada, fecha_salida, id)
            cursor.execute(consulta, valores)
            conexion.commit()
            ventana_actualizar.destroy()
            tk.messagebox.showinfo("Éxito", "Registro actualizado correctamente.")

        boton_guardar = tk.Button(ventana_actualizar, text="Guardar", command=guardar_reservas)
        boton_guardar.pack()

    # Función para actualizar un registro en la tabla metodo_pago
    def actualizar_metodo_pago():
        ventana_actualizar = tk.Toplevel(ventana)
        ventana_actualizar.title("Actualizar metodo_pago")
        ventana_actualizar.geometry("400x200")

        etiqueta_id = tk.Label(ventana_actualizar, text="ID del registro a actualizar:")
        etiqueta_id.pack()

        entrada_id = tk.Entry(ventana_actualizar)
        entrada_id.pack()

        etiqueta_nombre = tk.Label(ventana_actualizar, text="Nuevo nombre:")
        etiqueta_nombre.pack()

        entrada_nombre = tk.Entry(ventana_actualizar)
        entrada_nombre.pack()

        def guardar_metodo_pago():
            id = int(entrada_id.get())
            nombre = entrada_nombre.get()
            consulta = "UPDATE metodo_pago SET nombre = %s WHERE id = %s"
            valores = (nombre, id)
            cursor.execute(consulta, valores)
            conexion.commit()
            ventana_actualizar.destroy()
            tk.messagebox.showinfo("Éxito", "Registro actualizado correctamente.")

        boton_guardar = tk.Button(ventana_actualizar, text="Guardar", command=guardar_metodo_pago)
        boton_guardar.pack()

    # Función para actualizar un registro en la tabla pagos
    def actualizar_pagos():
        ventana_actualizar = tk.Toplevel(ventana)
        ventana_actualizar.title("Actualizar pagos")
        ventana_actualizar.geometry("400x350")

        etiqueta_id = tk.Label(ventana_actualizar, text="ID del registro a actualizar:")
        etiqueta_id.pack()

        entrada_id = tk.Entry(ventana_actualizar)
        entrada_id.pack()

        etiqueta_reserva_id = tk.Label(ventana_actualizar, text="Nuevo ID de la reserva:")
        etiqueta_reserva_id.pack()

        entrada_reserva_id = tk.Entry(ventana_actualizar)
        entrada_reserva_id.pack()

        etiqueta_fecha_pago = tk.Label(ventana_actualizar, text="Nueva fecha de pago (YYYY-MM-DD):")
        etiqueta_fecha_pago.pack()

        entrada_fecha_pago = tk.Entry(ventana_actualizar)
        entrada_fecha_pago.pack()

        etiqueta_monto = tk.Label(ventana_actualizar, text="Nuevo monto:")
        etiqueta_monto.pack()

        entrada_monto = tk.Entry(ventana_actualizar)
        entrada_monto.pack()

        etiqueta_metodo_pago = tk.Label(ventana_actualizar, text="Nuevo ID del método de pago:")
        etiqueta_metodo_pago.pack()

        entrada_metodo_pago = tk.Entry(ventana_actualizar)
        entrada_metodo_pago.pack()

        def guardar_pagos():
            id = int(entrada_id.get())
            reserva_id = int(entrada_reserva_id.get())
            fecha_pago = entrada_fecha_pago.get()
            monto = float(entrada_monto.get())
            metodo_pago = int(entrada_metodo_pago.get())
            consulta = "UPDATE pagos SET reserva_id = %s, fecha_pago = %s, monto = %s, metodo_pago = %s WHERE id = %s"
            valores = (reserva_id, fecha_pago, monto, metodo_pago, id)
            cursor.execute(consulta, valores)
            conexion.commit()
            ventana_actualizar.destroy()
            tk.messagebox.showinfo("Éxito", "Registro actualizado correctamente.")

        boton_guardar = tk.Button(ventana_actualizar, text="Guardar", command=guardar_pagos)
        boton_guardar.pack()

    # Crear botones para actualizar registros en cada tabla
    boton_actualizar_tipo_cabanya = tk.Button(ventana, text="Actualizar tipo_cabanya", command=actualizar_tipo_cabanya)
    boton_actualizar_tipo_cabanya.pack()

    boton_actualizar_cabanyas = tk.Button(ventana, text="Actualizar cabanyas", command=actualizar_cabanyas)
    boton_actualizar_cabanyas.pack()

    boton_actualizar_tipo_usuario = tk.Button(ventana, text="Actualizar tipo_usuario", command=actualizar_tipo_usuario)
    boton_actualizar_tipo_usuario.pack()

    boton_actualizar_usuarios = tk.Button(ventana, text="Actualizar usuarios", command=actualizar_usuarios)
    boton_actualizar_usuarios.pack()

    boton_actualizar_reservas = tk.Button(ventana, text="Actualizar reservas", command=actualizar_reservas)
    boton_actualizar_reservas.pack()

    boton_actualizar_metodo_pago = tk.Button(ventana, text="Actualizar metodo_pago", command=actualizar_metodo_pago)
    boton_actualizar_metodo_pago.pack()

    boton_actualizar_pagos = tk.Button(ventana, text="Actualizar pagos", command=actualizar_pagos)
    boton_actualizar_pagos.pack()

    # Cerrar la conexión a la base de datos al cerrar la ventana
    def cerrar_ventana():
        conexion_bd.cerrar_conexion(conexion)
        ventana.destroy()

    ventana.protocol("WM_DELETE_WINDOW", cerrar_ventana)

    # Ejecutar la ventana de actualización
    ventana.mainloop()