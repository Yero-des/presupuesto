import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from db import inicializar_db
from controllers.presupuesto import *

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

# Inputs
###################################
frame_form = tk.Frame(root)
frame_form.pack(pady=10)

tk.Label(frame_form, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
entry_nombre = tk.Entry(frame_form)
entry_nombre.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_form, text="Monto:").grid(row=1, column=0, padx=5, pady=5)
entry_monto = tk.Entry(frame_form)
entry_monto.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_form, text="Fecha inicio:").grid(row=2, column=0, padx=5, pady=5)
entry_fecha_inicio = DateEntry(frame_form, date_pattern="yyyy-mm-dd")
entry_fecha_inicio.grid(row=2, column=1, pady=5)

tk.Label(frame_form, text="Fecha fin:").grid(row=3, column=0, padx=5, pady=5)
entry_fecha_fin = DateEntry(frame_form, date_pattern="yyyy-mm-dd")
entry_fecha_fin.grid(row=3, column=1, pady=5)

# Botones
###################################
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

btn_agregar = tk.Button(
  frame_buttons, 
  text="Agregar", 
  command=lambda: agregar_presupuesto(
    entry_nombre.get(), entry_monto.get(), entry_fecha_inicio.get(), entry_fecha_fin.get(),
    entry_nombre, entry_monto, entry_fecha_inicio, entry_fecha_fin,
    lambda: cargar_presupuestos(tree)
  )
)
btn_agregar.grid(row=0, column=0, padx=5)

# Tabla de usuarios
###################################
frame_table = tk.Frame(root)
frame_table.pack(pady=10)

columns = ("ID", "Nombre", "Monto", "Fecha_inicio", "Fecha_fin")
tree = ttk.Treeview(frame_table, columns=columns, show="headings")
tree.heading("ID", text="ID")
tree.heading("Nombre", text="Nombre") 
tree.heading("Monto", text="Monto")
tree.heading("Fecha_inicio", text="Fecha inicio")
tree.heading("Fecha_fin", text="Fecha fin")

tree.column("ID", width=50)
tree.column("Nombre", width=150)
tree.column("Monto", width=50)
tree.column("Fecha_inicio", width=50)
tree.column("Fecha_fin", width=50)

tree.pack()

cargar_presupuestos(tree)

root.mainloop()