import tkinter as tk
import conexion_bd
import tkinter.messagebox as messagebox

def ventana_eliminacion():
    # Conectar a la base de datos
    conexion = conexion_bd.conectar()
    cursor = conexion.cursor()

    # Crear la ventana de eliminación
    ventana = tk.Toplevel()
    ventana.title("Eliminación de Registros")
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

    # Función para eliminar un registro de la tabla tipo_cabanya
    def eliminar_tipo_cabanya():
        ventana_eliminar = tk.Toplevel(ventana)
        ventana_eliminar.title("Eliminar tipo_cabanya")
        ventana_eliminar.geometry("400x200")

        etiqueta_id = tk.Label(ventana_eliminar, text="ID del registro a eliminar:")
        etiqueta_id.pack()

        entrada_id = tk.Entry(ventana_eliminar)
        entrada_id.pack()

        def eliminar_registro():
            id = entrada_id.get()
            if id.isdigit():
                id = int(id)
                consulta = "DELETE FROM tipo_cabanya WHERE id = %s"
                valores = (id,)
                cursor.execute(consulta, valores)
                conexion.commit()
                ventana_eliminar.destroy()
                messagebox.showinfo("Éxito", "Registro eliminado correctamente.")
            else:
                messagebox.showerror("Error", "El ID debe ser un valor numérico.")

        boton_eliminar = tk.Button(ventana_eliminar, text="Eliminar", command=eliminar_registro)
        boton_eliminar.pack()

    # Función para eliminar un registro de la tabla cabanyas
    def eliminar_cabanyas():
        ventana_eliminar = tk.Toplevel(ventana)
        ventana_eliminar.title("Eliminar cabanyas")
        ventana_eliminar.geometry("400x200")

        etiqueta_id = tk.Label(ventana_eliminar, text="ID del registro a eliminar:")
        etiqueta_id.pack()

        entrada_id = tk.Entry(ventana_eliminar)
        entrada_id.pack()

        def eliminar_registro():
            id = entrada_id.get()
            if id.isdigit():
                id = int(id)
                consulta = "DELETE FROM cabanyas WHERE id = %s"
                valores = (id,)
                cursor.execute(consulta, valores)
                conexion.commit()
                ventana_eliminar.destroy()
                messagebox.showinfo("Éxito", "Registro eliminado correctamente.")
            else:
                messagebox.showerror("Error", "El ID debe ser un valor numérico.")

        boton_eliminar = tk.Button(ventana_eliminar, text="Eliminar", command=eliminar_registro)
        boton_eliminar.pack()

    # Función para eliminar un registro de la tabla tipo_usuario
    def eliminar_tipo_usuario():
        ventana_eliminar = tk.Toplevel(ventana)
        ventana_eliminar.title("Eliminar tipo_usuario")
        ventana_eliminar.geometry("400x200")

        etiqueta_id = tk.Label(ventana_eliminar, text="ID del registro a eliminar:")
        etiqueta_id.pack()

        entrada_id = tk.Entry(ventana_eliminar)
        entrada_id.pack()

        def eliminar_registro():
            id = entrada_id.get()
            if id.isdigit():
                id = int(id)
                consulta = "DELETE FROM tipo_usuario WHERE id = %s"
                valores = (id,)
                cursor.execute(consulta, valores)
                conexion.commit()
                ventana_eliminar.destroy()
                messagebox.showinfo("Éxito", "Registro eliminado correctamente.")
            else:
                messagebox.showerror("Error", "El ID debe ser un valor numérico.")

        boton_eliminar = tk.Button(ventana_eliminar, text="Eliminar", command=eliminar_registro)
        boton_eliminar.pack()

    # Función para eliminar un registro de la tabla usuarios
    def eliminar_usuarios():
        ventana_eliminar = tk.Toplevel(ventana)
        ventana_eliminar.title("Eliminar usuarios")
        ventana_eliminar.geometry("400x200")

        etiqueta_id = tk.Label(ventana_eliminar, text="ID del registro a eliminar:")
        etiqueta_id.pack()

        entrada_id = tk.Entry(ventana_eliminar)
        entrada_id.pack()

        def eliminar_registro():
            id = entrada_id.get()
            if id.isdigit():
                id = int(id)
                consulta = "DELETE FROM usuarios WHERE id = %s"
                valores = (id,)
                cursor.execute(consulta, valores)
                conexion.commit()
                ventana_eliminar.destroy()
                messagebox.showinfo("Éxito", "Registro eliminado correctamente.")
            else:
                messagebox.showerror("Error", "El ID debeser un valor numérico.")

        boton_eliminar = tk.Button(ventana_eliminar, text="Eliminar", command=eliminar_registro)
        boton_eliminar.pack()

    # Función para eliminar un registro de la tabla reservas
    def eliminar_reservas():
        ventana_eliminar = tk.Toplevel(ventana)
        ventana_eliminar.title("Eliminar reservas")
        ventana_eliminar.geometry("400x200")

        etiqueta_id = tk.Label(ventana_eliminar, text="ID del registro a eliminar:")
        etiqueta_id.pack()

        entrada_id = tk.Entry(ventana_eliminar)
        entrada_id.pack()

        def eliminar_registro():
            id = entrada_id.get()
            if id.isdigit():
                id = int(id)
                consulta = "DELETE FROM reservas WHERE id = %s"
                valores = (id,)
                cursor.execute(consulta, valores)
                conexion.commit()
                ventana_eliminar.destroy()
                messagebox.showinfo("Éxito", "Registro eliminado correctamente.")
            else:
                messagebox.showerror("Error", "El ID debe ser un valor numérico.")

        boton_eliminar = tk.Button(ventana_eliminar, text="Eliminar", command=eliminar_registro)
        boton_eliminar.pack()

    # Función para eliminar un registro de la tabla metodo_pago
    def eliminar_metodo_pago():
        ventana_eliminar = tk.Toplevel(ventana)
        ventana_eliminar.title("Eliminar metodo_pago")
        ventana_eliminar.geometry("400x200")

        etiqueta_id = tk.Label(ventana_eliminar, text="ID del registro a eliminar:")
        etiqueta_id.pack()

        entrada_id = tk.Entry(ventana_eliminar)
        entrada_id.pack()

        def eliminar_registro():
            id = entrada_id.get()
            if id.isdigit():
                id = int(id)
                consulta = "DELETE FROM metodo_pago WHERE id = %s"
                valores = (id,)
                cursor.execute(consulta, valores)
                conexion.commit()
                ventana_eliminar.destroy()
                messagebox.showinfo("Éxito", "Registro eliminado correctamente.")
            else:
                messagebox.showerror("Error", "El ID debe ser un valor numérico.")

        boton_eliminar = tk.Button(ventana_eliminar, text="Eliminar", command=eliminar_registro)
        boton_eliminar.pack()

    # Función para eliminar un registro de la tabla pagos
    def eliminar_pagos():
        ventana_eliminar = tk.Toplevel(ventana)
        ventana_eliminar.title("Eliminar pagos")
        ventana_eliminar.geometry("400x200")

        etiqueta_id = tk.Label(ventana_eliminar, text="ID del registro a eliminar:")
        etiqueta_id.pack()

        entrada_id = tk.Entry(ventana_eliminar)
        entrada_id.pack()

        def eliminar_registro():
            id = entrada_id.get()
            if id.isdigit():
                id = int(id)
                consulta = "DELETE FROM pagos WHERE id = %s"
                valores = (id,)
                cursor.execute(consulta, valores)
                conexion.commit()
                ventana_eliminar.destroy()
                messagebox.showinfo("Éxito", "Registro eliminado correctamente.")
            else:
                messagebox.showerror("Error", "El ID debe ser un valor numérico.")

        boton_eliminar = tk.Button(ventana_eliminar, text="Eliminar", command=eliminar_registro)
        boton_eliminar.pack()

    # Crear botones para eliminar registros en cada tabla
    boton_eliminar_tipo_cabanya = tk.Button(ventana, text="Eliminar tipo_cabanya", command=eliminar_tipo_cabanya)
    boton_eliminar_tipo_cabanya.pack()

    boton_eliminar_cabanyas = tk.Button(ventana, text="Eliminar cabanyas", command=eliminar_cabanyas)
    boton_eliminar_cabanyas.pack()

    boton_eliminar_tipo_usuario = tk.Button(ventana, text="Eliminar tipo_usuario", command=eliminar_tipo_usuario)
    boton_eliminar_tipo_usuario.pack()

    boton_eliminar_usuarios = tk.Button(ventana, text="Eliminar usuarios", command=eliminar_usuarios)
    boton_eliminar_usuarios.pack()

    boton_eliminar_reservas = tk.Button(ventana, text="Eliminar reservas", command=eliminar_reservas)
    boton_eliminar_reservas.pack()

    boton_eliminar_metodo_pago = tk.Button(ventana, text="Eliminar metodo_pago", command=eliminar_metodo_pago)
    boton_eliminar_metodo_pago.pack()

    boton_eliminar_pagos = tk.Button(ventana, text="Eliminar pagos", command=eliminar_pagos)
    boton_eliminar_pagos.pack()

    # Cerrar la conexión a la base de datos al cerrar la ventana
    def cerrar_ventana():
        conexion_bd.cerrar_conexion(conexion)
        ventana.destroy()

    ventana.protocol("WM_DELETE_WINDOW", cerrar_ventana)

    # Ejecutar la ventana de eliminación
    ventana.mainloop()