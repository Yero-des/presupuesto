import tkinter as tk
from tkinter import ttk, messagebox
from db import inicializar_db

def centrar_ventana(ventana, ancho, alto):
  screen_width = ventana.winfo_screenwidth()
  screen_height = ventana.winfo_screenheight()
  x = (screen_width - ancho) // 2
  y = (screen_height - alto) // 2
  ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

inicializar_db()

root = tk.Tk()
root.title("Presupuesto")
root.resizable(False, False)
centrar_ventana(root, 700, 500)

root.mainloop()