import tkinter as tk
from tkinter import simpledialog, messagebox
import requests

def obtener_clima(ciudad):
    try:
        url = f"https://wttr.in/{ciudad}?format=3"
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            etiqueta_resultado.config(text=respuesta.text)
        else:
            etiqueta_resultado.config(text="Error al obtener el clima.")
    except Exception as e:
        etiqueta_resultado.config(text=f"Error: {e}")

def cambiar_ciudad():
    ciudad = simpledialog.askstring("Ciudad", "Ingresa ciudad o país:")
    if ciudad:
        obtener_clima(ciudad)

def mostrar_acerca_de():
    messagebox.showinfo("Acerca de", "Mini-App de Clima Creada por Israel G. Bistrain y Pachi. Síguenos en Mastodon: @supersnufkin.mastodon.social\nUsa wttr.in")

ventana = tk.Tk()
ventana.title("PachiClima")
ventana.geometry("300x150")
ventana.resizable(False, False)

etiqueta_resultado = tk.Label(ventana, text="Selecciona una ciudad", font=("Arial", 12), justify="center")
etiqueta_resultado.pack(pady=20)

boton_ciudad = tk.Button(ventana, text="Cambiar ciudad", command=cambiar_ciudad)
boton_ciudad.pack(pady=5)

boton_acerca = tk.Button(ventana, text="Acerca de", command=mostrar_acerca_de)
boton_acerca.pack(pady=5)

ventana.mainloop()
