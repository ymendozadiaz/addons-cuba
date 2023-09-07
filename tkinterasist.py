import tkinter as tk
from tkinter import ttk

import openai
from dotenv import dotenv_values

# Carga las variables de entorno desde el archivo .env
config = dotenv_values(".env")
openai.api_key = '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'

# Crea la ventana principal
root = tk.Tk()
root.title("Asistente AI")
root.config(background="Black", borderwidth=3)

scrollbar = ttk.Scrollbar(root)

# Crea un cuadro de texto para mostrar los mensajes
messages_text = tk.Text(root, width=50, height=20, bg="#213151", fg="white", bd=5)
messages_text.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=messages_text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
messages_text.pack()

# Crea un cuadro de entrada para escribir los mensajes
input_entry = tk.Entry(root, width=45, font=("Arial", 12),bd=5, bg="Blue", fg="white")
input_entry.pack()



# Define la función para enviar mensajes al asistente
def send_message():
    message = input_entry.get()
    messages_text.insert(tk.END, "Usuario: " + message + "\n")
    input_entry.delete(0, tk.END)
    
    # Llama a OpenAI para obtener una respuesta
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=message,
        temperature=0.5,
        max_tokens=1000,
        n=1,
        stop=None,
    )
    
    # Agrega la respuesta del asistente al cuadro de texto
    assistant_message = response.choices[0].text.strip()
    messages_text.insert(tk.END, "Asistente: " + assistant_message + "\n")

# Crea un botón para enviar mensajes
send_button = tk.Button(root, text="Enviar", command=send_message)
send_button.pack()

# Ejecuta la aplicación
root.mainloop()
