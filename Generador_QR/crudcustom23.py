from tkinter import *
from tkinter import messagebox
from customtkinter import *
import sqlite3

# Función para crear la base de datos
def crear_bd():
    conn = sqlite3.connect('crud.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, telefono TEXT)')
    conn.commit()
    conn.close()

# Función para mostrar los registros en la tabla
def mostrar_registros():
    conn = sqlite3.connect('crud.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios')
    registros = cursor.fetchall()

    # Limpiar la tabla antes de mostrar los nuevos registros
    table.delete_all_rows()

    # Mostrar los registros en la tabla
    for registro in registros:
        table.add_row(registro[0], registro[1], registro[2])

    conn.close()

# Función para agregar un nuevo registro
def agregar_registro():
    nombre = entry_nombre.get()
    telefono = entry_telefono.get()

    if nombre and telefono:
        conn = sqlite3.connect('crud.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO usuarios (nombre, telefono) VALUES (?, ?)', (nombre, telefono))
        conn.commit()
        conn.close()

        messagebox.showinfo('Éxito', 'Registro agregado correctamente')
        mostrar_registros()
        entry_nombre.delete(0, END)
        entry_telefono.delete(0, END)
    else:
        messagebox.showwarning('Advertencia', 'Por favor, complete todos los campos')

# Función para actualizar un registro existente
def actualizar_registro():
    seleccionado = table.get_selected_row()

    if seleccionado:
        id = table.get_cell_value(seleccionado, 0)
        nombre = entry_nombre.get()
        telefono = entry_telefono.get()

        if nombre and telefono:
            conn = sqlite3.connect('crud.db')
            cursor = conn.cursor()
            cursor.execute('UPDATE usuarios SET nombre=?, telefono=? WHERE id=?', (nombre, telefono, id))
            conn.commit()
            conn.close()

            messagebox.showinfo('Éxito', 'Registro actualizado correctamente')
            mostrar_registros()
        else:
            messagebox.showwarning('Advertencia', 'Por favor, complete todos los campos')
    else:
        messagebox.showwarning('Advertencia', 'Por favor, seleccione un registro')

# Función para eliminar un registro existente
def eliminar_registro():
    seleccionado = table.get_selected_row()

    if seleccionado:
        id = table.get_cell_value(seleccionado, 0)
        nombre = table.get_cell_value(seleccionado, 1)

        respuesta = messagebox.askquestion('Confirmar', f'¿Está seguro de eliminar el registro de {nombre}?')

        if respuesta == 'yes':
            conn = sqlite3.connect('crud.db')
            cursor = conn.cursor()
            cursor.execute('DELETE FROM usuarios WHERE id=?', (id,))
            conn.commit()
            conn.close()

            messagebox.showinfo('Éxito', 'Registro eliminado correctamente')
            mostrar_registros()
    else:
        messagebox.showwarning('Advertencia', 'Por favor, seleccione un registro')

# Crear la ventana principal
ventana = Tk()

# Configurar la ventana principal
ventana.title('CRUD con Customtkinter')
ventana.geometry('500x400')

# Crear la tabla
table = CTkTextbox(ventana, ['ID', 'Nombre', 'Teléfono'], [70, 200, 150])
table.pack(pady=20)

# Crear los campos de entrada de datos
frame_campos = Frame(ventana)
frame_campos.pack()

label_nombre = Label(frame_campos, text='Nombre:')
label_nombre.grid(row=0, column=0, padx=10, pady=5)
entry_nombre = Entry(frame_campos)
entry_nombre.grid(row=0, column=1)

label_telefono = Label(frame_campos, text='Teléfono:')
label_telefono.grid(row=1, column=0, padx=10, pady=5)
entry_telefono = Entry(frame_campos)
entry_telefono.grid(row=1, column=1)

# Crear los botones
frame_botones = Frame(ventana)
frame_botones.pack()

boton_agregar = Button(frame_botones, text='Agregar', command=agregar_registro)
boton_agregar.grid(row=0, column=0, padx=5, pady=10)

boton_actualizar = Button(frame_botones, text='Actualizar', command=actualizar_registro)
boton_actualizar.grid(row=0, column=1, padx=5, pady=10)

boton_eliminar = Button(frame_botones, text='Eliminar', command=eliminar_registro)
boton_eliminar.grid(row=0, column=2, padx=5, pady=10)

# Crear la base de datos
crear_bd()

# Mostrar los registros al iniciar la aplicación
mostrar_registros()

# Iniciar el bucle del programa
ventana.mainloop()
