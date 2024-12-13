import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

def cargar_presupuestos(tree):

  for fila in tree.get_children():
    tree.delete(fila)

  conn = sqlite3.connect('presupuesto.db')
  cursor = conn.cursor()
  cursor.execute('SELECT * FROM presupuesto')
  for presupuesto in cursor.fetchall():
    tree.insert('', tk.END, values=presupuesto)
  conn.close()

def agregar_presupuesto(
  nombre, monto, fecha_inicio, fecha_fin, 
  entry_nombre, entry_monto, entry_fecha_inicio, entry_fecha_fin,
  cargar_presupuestos):

  nombre = entry_nombre.get()
  monto = entry_monto.get()
  fecha_inicio = entry_fecha_inicio.get()
  fecha_fin = entry_fecha_fin.get()

  try:
     
    # Validar formato de fechas
    fecha_inicio = datetime.strptime(fecha_inicio, '%Y-%m-%d').date()
    fecha_fin = datetime.strptime(fecha_fin, '%Y-%m-%d').date()

    if not monto.isdigit():
      messagebox.showerror("Error", "Por favor, ingrese un monto valido")
      return

    # Validar que el monto sea un número
    monto = float(monto)
    validacion = not nombre or not fecha_inicio or not fecha_fin

    if validacion:
      messagebox.showerror("Error", "Por favor, ingrese datos validos")
      return

    conn = sqlite3.connect('presupuesto.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO presupuesto (nombre, monto, fecha_inicio, fecha_fin) VALUES (?, ?, ?, ?)', (nombre, monto, fecha_inicio, fecha_fin ))
    conn.commit()
    conn.close()

    entry_nombre.delete(0, tk.END)
    entry_monto.delete(0, tk.END)
    entry_fecha_inicio.delete(0, tk.END)
    entry_fecha_fin.delete(0, tk.END)

    cargar_presupuestos()
    messagebox.showinfo("Éxito", "Presupuesto agregado exitosamente")

  except ValueError as e:
    messagebox.showerror("Error", f"Datos inválidos: {str(e)}")
  except Exception as e:
    messagebox.showerror("Error", f"Error al agregar presupuesto: {str(e)}")
