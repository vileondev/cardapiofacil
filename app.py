from flask import Flask, render_template, abort
import sqlite3

app = Flask(__name__)

DATABASE = 'cardapio.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def get_pratos():
    conn = get_db_connection()
    pratos = conn.execute('SELECT * FROM pratos').fetchall()
    conn.close()
    return pratos

def get_prato_by_id(prato_id):
    conn = get_db_connection()
    prato = conn.execute('SELECT * FROM pratos WHERE id = ?', (prato_id,)).fetchone()
    conn.close()
    return prato

@app.route('/')
def index():
    pratos = get_pratos()
    return render_template('index.html', pratos=pratos)

@app.route('/prato/<int:prato_id>')
def detalhe_prato(prato_id):
    prato = get_prato_by_id(prato_id)
    if prato is None:
        abort(404)
    return render_template('detalhe.html', prato=prato)

if __name__ == '__main__':
    app.run(debug=True)
