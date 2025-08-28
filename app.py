from flask import Flask, render_template, abort, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = "segredo_super_secreto"

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

@app.route('/entradas')
def entradas():
    conn = get_db_connection()
    entradas = conn.execute("SELECT * FROM pratos WHERE nome LIKE '%Batata%' OR nome LIKE '%Nugget%' OR nome LIKE '%Salada%' OR nome LIKE '%Pastel%'").fetchall()
    conn.close()
    return render_template('entradas.html', pratos=entradas)

@app.route('/sobremesas')
def sobremesas():
    conn = get_db_connection()
    sobremesas = conn.execute("SELECT * FROM pratos WHERE nome LIKE '%Sorvete%' OR nome LIKE '%Bolo%' OR nome LIKE '%Pudim%'").fetchall()
    conn.close()
    return render_template('sobremesas.html', pratos=sobremesas)

@app.route('/prato/<int:prato_id>')
def detalhe_prato(prato_id):
    prato = get_prato_by_id(prato_id)
    if prato is None:
        abort(404)
    return render_template('detalhe.html', prato=prato)

@app.route('/configurar/<int:prato_id>', methods=["GET", "POST"])
def configurar_prato(prato_id):
    prato = get_prato_by_id(prato_id)
    if prato is None:
        abort(404)

    if request.method == "POST":
        # Ingredientes selecionados
        ingredientes = request.form.getlist("ingredientes")
        observacoes = request.form.get("observacoes", "")

        item = {
            "id": prato["id"],
            "nome": prato["nome"],
            "preco": 20.0,  # preço fictício (depois pode vir do banco)
            "ingredientes": ingredientes,
            "obs": observacoes
        }

        # Adicionar ao carrinho (na sessão)
        carrinho = session.get("carrinho", [])
        carrinho.append(item)
        session["carrinho"] = carrinho

        return redirect(url_for("finalizacao"))

    return render_template("configurar-prato.html", prato=prato)

@app.route('/remover/<int:index>')
def remover_item(index):
    carrinho = session.get("carrinho", [])
    if 0 <= index < len(carrinho):
        carrinho.pop(index)
        session["carrinho"] = carrinho
    return redirect(url_for("finalizacao"))

@app.route('/finalizacao')
def finalizacao():
    carrinho = session.get("carrinho", [])
    total = sum(item["preco"] for item in carrinho)
    return render_template("finalizacao.html", carrinho=carrinho, total=total)

@app.route('/pratos')
def pratos():
    return render_template('categorias-alimentos/pratos.html')

@app.route('/bebidas')
def bebidas():
    return render_template('categorias-alimentos/bebidas.html')

if __name__ == '__main__':
    app.run(debug=True)
