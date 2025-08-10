import sqlite3

conn = sqlite3.connect('cardapio.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS pratos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    descricao TEXT,
    imagem TEXT
)
''')

# Inserindo alguns pratos
cursor.execute("INSERT INTO pratos (nome, descricao, imagem) VALUES (?, ?, ?)", 
               ("Hambúrguer Clássico", "Hambúrguer suculento com queijo, alface e tomate.", 
                "https://images.pexels.com/photos/1639557/pexels-photo-1639557.jpeg"))
cursor.execute("INSERT INTO pratos (nome, descricao, imagem) VALUES (?, ?, ?)", 
               ("X-bagunça", "Um hambúrguer com tudo que um hambúrguer precisa e um pouco mais", 
                "https://images.pexels.com/photos/156114/pexels-photo-156114.jpeg"))

conn.commit()
conn.close()
print("Banco de dados criado e populado!")
