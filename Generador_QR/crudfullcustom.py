import customtkinter as ctk
import pandas as pd
import sqlite3
import qrcode
from tkinter import *
import sqlite3
import qrcode
from tkinter import messagebox
import pandas as pd
from tkinter import Menu
from tkinter import filedialog


# Ventana de inicio de sesión
def login_window():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    root = ctk.CTk()
    root.geometry("500x350")
    root.title('Inicio de Sesión')

    # Función para verificar el inicio de sesión
    def verificar_login():
        username = entry_username.get()
        password = entry_password.get()

        # Verificar las credenciales (aquí debes agregar tu lógica de autenticación)
        if username == 'admin' and password == '12345':
            main_window()
            root.destroy()
        else:
            ctk.messagebox.showerror('Error', 'Credenciales incorrectas.')
    
    def salir_login():
        pass
        

    label_username = ctk.CTkLabel(root, text='Usuario:')
    label_username.pack()
    entry_username = ctk.CTkEntry(root)
    entry_username.pack()

    label_password = ctk.CTkLabel(root, text='Contraseña:')
    label_password.pack()
    entry_password = ctk.CTkEntry(root, show='*')
    entry_password.pack()

    button_login = ctk.CTkButton(root, text='Iniciar Sesión', command=verificar_login)
    button_login.pack(pady=12, padx=10)

    button_salir = ctk.CTkButton(root, text='Salir', command=salir_login)
    button_salir.pack(pady=12, padx=10)

    root.mainloop()
    

# Ventana principal (CRUD)
def main_window():
    # Conexión a la base de datos
    conn = sqlite3.connect('almacedb.db')
    c = conn.cursor()

    # Crear tabla si no existe
    c.execute('''CREATE TABLE IF NOT EXISTS productos
                (id INTEGER PRIMARY KEY, nombre TEXT, departamento TEXT, motherboard TEXT, cpu TEXT,  ram TEXT, hdd TEXT)''')

    def export_to_excel():
        # Obtener los datos ingresados por el usuario
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM productos")
        num_records = cursor.fetchone()[0]
        
        if num_records > 0:
            df = pd.read_sql_query("SELECT * FROM productos", conn)
            filename = filedialog.asksaveasfilename(defaultextension='.xlsx')
            df.to_excel(filename, index=False)
            messagebox.showinfo("Información", "El reporte en excel se generó con éxito")
        else:
            messagebox.showwarning("Advertencia", "No hay registros para exportar")
            
        cursor.close()
    
    # Función para insertar un nuevo producto
    def insert_producto():
        nombre = nombre_entry.get()
        departamento = departamento_entry.get()
        motherboard = motherboard_entry.get()
        cpu = cpu_entry.get()
        ram = ram_entry.get()
        hdd = hdd_entry.get()
        c.execute("INSERT INTO productos (nombre, departamento, motherboard, cpu, ram, hdd) VALUES (?, ?, ?, ?, ?, ?)",(nombre, departamento, motherboard, cpu, ram, hdd))
        conn.commit()
        update_listbox()
        messagebox.showinfo("Información","El registro fue agregado con éxito")    
        
    # Función para actualizar un producto
    def update_producto():
        selected_producto = listbox.curselection()[0]
        nombre = nombre_entry.get()
        departamento = departamento_entry.get()
        motherboard = motherboard_entry.get()
        cpu = cpu_entry.get()
        ram = ram_entry.get()
        hdd = hdd_entry.get()
        producto_id = listbox.get(selected_producto)[0]
        c.execute("UPDATE productos SET nombre=?, departamento=?, motherboard=?, cpu=?, ram=?, hdd=? WHERE id=?", (nombre, departamento, motherboard, cpu, ram, hdd, producto_id))
        conn.commit()
        update_listbox()
        messagebox.showinfo("Información","El registro fue actualizado con éxito")
        

    # Función para eliminar un producto
    def delete_producto():
        selected_producto = listbox.curselection()[0]
        producto_id = listbox.get(selected_producto)[0]
        c.execute("DELETE FROM productos WHERE id=?", (producto_id,))
        conn.commit()
        update_listbox()
        messagebox.showinfo("Información","El registro fue eliminado de la base de datos")

    # Función para mostrar los productos en la lista
    def update_listbox():
        listbox.delete(0, END)
        for row in c.execute("SELECT * FROM productos"):
            listbox.insert(END, row)


    # Función para generar código QR
    def generate_qr():
        selected_producto = listbox.curselection()[0]
        producto_id = listbox.get(selected_producto)[0]
        nombre = listbox.get(selected_producto)[1]
        departamento = listbox.get(selected_producto)[2]
        motherboard = listbox.get(selected_producto)[3]
        cpu = listbox.get(selected_producto)[4]
        ram = listbox.get(selected_producto)[5]
        hdd = listbox.get(selected_producto)[6]
        qr_data = f"Nombre: {nombre}\nDepartamento: {departamento}\nMotherboard: {motherboard}\nCpu: {cpu}\nRam: {ram}\nhdd: {hdd}"
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(qr_data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        filename = filedialog.asksaveasfilename(defaultextension='.png')
        img.save(filename)
        messagebox.showinfo("Información", message="Código QR generado y guardado correctamente.")

    # Crear ventana principal
    root = Tk()
    root.title("Generador de códigos QR")
    root.geometry("735x550")
    root.config(bg="#213151")

    # Crear campos de entrada y botones
    nombre_label = Label(root, text="Generador de QR", font=("Stencil", 16),bd=5, relief=FLAT, bg="Blue", width=25, height=3, fg="white")
    nombre_label.grid(padx=2, pady=2, rowspan=1, columnspan=6)
    nombre_label.config(bg="Blue")

    nombre_label = Label(root, text="Nombre:", bg="#213151", fg="white")
    nombre_label.grid(row=2, column=0)
    nombre_entry = Entry(root)
    nombre_entry.grid(row=2, column=1)

    departamento_label = Label(root, text="Departamento:", bg="#213151", fg="white")
    departamento_label.grid(row=2, column=2)
    departamento_entry = Entry(root)
    departamento_entry.grid(row=2, column=3)

    motherboard_label = Label(root, text="Motherboard:", bg="#213151", fg="white")
    motherboard_label.grid(row=2, column=4)
    motherboard_entry = Entry(root)
    motherboard_entry.grid(row=2, column=5)

    cpu_label = Label(root, text="CPU:", bg="#213151", fg="white")
    cpu_label.grid(row=3, column=0)
    cpu_entry = Entry(root)
    cpu_entry.grid(row=3, column=1)

    ram_label = Label(root, text="RAM:", bg="#213151", fg="white")
    ram_label.grid(row=3, column=2)
    ram_entry = Entry(root)
    ram_entry.grid(row=3, column=3)

    hdd_label = Label(root, text="HDD:", bg="#213151", fg="white")
    hdd_label.grid(row=3, column=4)
    hdd_entry = Entry(root)
    hdd_entry.grid(row=3, column=5)

    add_button = Button(root, text="Agregar", command=insert_producto, bg="blue", fg="white")
    add_button.grid(row=6, column=1)

    update_button = Button(root, text="Actualizar", command=update_producto, bg="blue", fg="white")
    update_button.grid(row=6, column=2)

    delete_button = Button(root, text="Eliminar", command=delete_producto, bg="red", fg="white")
    delete_button.grid(row=6, column=3)

    qr_button = Button(root, text="Generar QR", command=generate_qr, bg="blue", fg="white")
    qr_button.grid(row=6, column=4)

    excel_button = Button(root, text="Generar Excel", command=export_to_excel, bg="blue", fg="white")
    excel_button.grid(row=6, column=5)

    # Crear lista de productos
    listbox = Listbox(root, height=20, width=115, border=0)
    listbox.grid(row=8, column=0, columnspan="8", sticky="E", padx=8, pady=2)
    ScrollVert=Scrollbar(root, command=listbox.yview)
    ScrollVert.grid(row=8, column=8, sticky="nsew")
    listbox.config(yscrollcommand=ScrollVert.set)
    update_listbox()
    root.mainloop()
# Cerrar conexión a la base de datos
    conn.close()
login_window()
