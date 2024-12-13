import sqlite3

def inicializar_db():
    conn = sqlite3.connect('presupuesto.db')
    cursor = conn.cursor()

    # Crear tabla PRESUPUESTO
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS presupuesto (
            id VARCHAR(255) PRIMARY KEY,
            nombre VARCHAR(255) NOT NULL,
            monto FLOAT NOT NULL,
            fecha_inicio DATE NOT NULL,
            fecha_fin DATE NOT NULL
        )
    ''')

    # Crear tabla INGRESOS
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ingresos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            presupuesto VARCHAR(255) NOT NULL,
            fecha DATE NOT NULL,
            monto FLOAT NOT NULL,
            tipo VARCHAR(255) NOT NULL,
            es_ingreso BOOL NOT NULL,
            descripcion VARCHAR(255),
            FOREIGN KEY (presupuesto) REFERENCES presupuesto (id)
        )
    ''')

    conn.commit()
    conn.close()