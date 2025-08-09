from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Cria o banco se não existir
def init_db():
    conn = sqlite3.connect("cardapio.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pratos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT,
            preco REAL NOT NULL
        )
    """)
    conn.commit()
    conn.close()

init_db()

# Página principal
@app.route("/")
def index():
    conn = sqlite3.connect("cardapio.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nome, descricao, preco FROM pratos")
    itens = cursor.fetchall()
    conn.close()
    return render_template("index.html", itens=itens)

# Painel admin para adicionar pratos
@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        nome = request.form["nome"]
        descricao = request.form["descricao"]
        preco = request.form["preco"]

        conn = sqlite3.connect("cardapio.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO pratos (nome, descricao, preco) VALUES (?, ?, ?)",
                        (nome, descricao, preco))
        conn.commit()
        conn.close()
        return redirect("/")

    return render_template("admin.html")

if __name__ == "__main__":
    app.run(debug=True)
