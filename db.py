import sqlite3

def inicializar_db():
  conn = sqlite3.connect('presupuesto.db')
  cursor = conn.cursor()
  cursor.execute('''
    CREATE TABLE IF NOT EXISTS ingresos (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      fecha DATE NOT NULL,
      monto FLOAT NOT NULL,
      tipo VARCHAR(255) NOT NULL,
      es_ingreso BOOL NOT NULL,
      descripcion VARCHAR(255) NOT NULL
    )
  ''')
  conn.commit()
  conn.close()