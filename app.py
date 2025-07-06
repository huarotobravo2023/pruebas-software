from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui'

# Base de datos SQLite
DATABASE = 'notas.db'

def init_db():
    """Inicializa la base de datos SQLite"""
    conn = sqlite3.connect(DATABASE)
    conn.execute('''
        CREATE TABLE IF NOT EXISTS notas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            contenido TEXT NOT NULL,
            fecha TEXT NOT NULL,
            fecha_modificacion TEXT
        )
    ''')
    conn.commit()
    conn.close()

def get_db_connection():
    """Obtiene una conexión a la base de datos"""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Para acceder a las columnas por nombre
    return conn

def cargar_notas():
    """Carga todas las notas desde la base de datos"""
    conn = get_db_connection()
    notas = conn.execute('SELECT * FROM notas ORDER BY id DESC').fetchall()
    conn.close()
    return [dict(nota) for nota in notas]

def obtener_nota_por_id(nota_id):
    """Obtiene una nota específica por su ID"""
    conn = get_db_connection()
    nota = conn.execute('SELECT * FROM notas WHERE id = ?', (nota_id,)).fetchone()
    conn.close()
    return dict(nota) if nota else None

def crear_nota(titulo, contenido):
    """Crea una nueva nota en la base de datos"""
    conn = get_db_connection()
    fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    conn.execute(
        'INSERT INTO notas (titulo, contenido, fecha) VALUES (?, ?, ?)',
        (titulo, contenido, fecha)
    )
    conn.commit()
    conn.close()

def actualizar_nota(nota_id, titulo, contenido):
    """Actualiza una nota existente"""
    conn = get_db_connection()
    fecha_modificacion = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    conn.execute(
        'UPDATE notas SET titulo = ?, contenido = ?, fecha_modificacion = ? WHERE id = ?',
        (titulo, contenido, fecha_modificacion, nota_id)
    )
    conn.commit()
    conn.close()

def eliminar_nota(nota_id):
    """Elimina una nota de la base de datos"""
    conn = get_db_connection()
    conn.execute('DELETE FROM notas WHERE id = ?', (nota_id,))
    conn.commit()
    conn.close()

@app.route('/')
def index():
    """Página principal - muestra todas las notas"""
    notas = cargar_notas()
    return render_template('index.html', notas=notas)

@app.route('/nueva', methods=['GET', 'POST'])
def nueva_nota():
    """Crear una nueva nota"""
    if request.method == 'POST':
        titulo = request.form['titulo']
        contenido = request.form['contenido']
        
        if titulo and contenido:
            crear_nota(titulo, contenido)
            flash('Nota creada exitosamente!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Por favor completa todos los campos', 'error')
    
    return render_template('nueva_nota.html')

@app.route('/ver/<int:nota_id>')
def ver_nota(nota_id):
    """Ver una nota específica"""
    nota = obtener_nota_por_id(nota_id)
    
    if nota:
        return render_template('ver_nota.html', nota=nota)
    else:
        flash('Nota no encontrada', 'error')
        return redirect(url_for('index'))

@app.route('/editar/<int:nota_id>', methods=['GET', 'POST'])
def editar_nota(nota_id):
    """Editar una nota existente"""
    nota = obtener_nota_por_id(nota_id)
    
    if not nota:
        flash('Nota no encontrada', 'error')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        titulo = request.form['titulo']
        contenido = request.form['contenido']
        
        if titulo and contenido:
            actualizar_nota(nota_id, titulo, contenido)
            flash('Nota actualizada exitosamente!', 'success')
            return redirect(url_for('ver_nota', nota_id=nota_id))
        else:
            flash('Por favor completa todos los campos', 'error')
    
    return render_template('editar_nota.html', nota=nota)

@app.route('/eliminar/<int:nota_id>')
def eliminar_nota_route(nota_id):
    """Eliminar una nota"""
    eliminar_nota(nota_id)
    flash('Nota eliminada exitosamente!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Inicializar la base de datos al arrancar
    init_db()
    app.run(debug=True)
