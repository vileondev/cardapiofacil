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

# Novos pratos
cursor.execute("INSERT INTO pratos (nome, descricao, imagem) VALUES (?, ?, ?)", 
               ("Batata Frita", "Porção crocante de batata frita dourada.", 
                "https://images.pexels.com/photos/1583884/pexels-photo-1583884.jpeg"))

cursor.execute("INSERT INTO pratos (nome, descricao, imagem) VALUES (?, ?, ?)", 
               ("Nuggets de Frango", "Deliciosos nuggets de frango empanados e crocantes.", 
                "https://images.pexels.com/photos/4109234/pexels-photo-4109234.jpeg"))

cursor.execute("INSERT INTO pratos (nome, descricao, imagem) VALUES (?, ?, ?)", 
               ("Pizza de Calabresa", "Pizza saborosa com calabresa fatiada e cebola.", 
                "https://images.pexels.com/photos/2619967/pexels-photo-2619967.jpeg"))

cursor.execute("INSERT INTO pratos (nome, descricao, imagem) VALUES (?, ?, ?)", 
               ("Cachorro quente", "Cachorro-quente com salsicha, milho, batata palha e molhos.", 
                "https://images.pexels.com/photos/2232/vegetables-italian-pizza-restaurant.jpg"))

cursor.execute("INSERT INTO pratos (nome, descricao, imagem) VALUES (?, ?, ?)", 
               ("Tacos Mexicanos", "Tacos recheados com carne, alface, queijo e molho picante.", 
                "https://images.pexels.com/photos/461198/pexels-photo-461198.jpeg"))

cursor.execute("INSERT INTO pratos (nome, descricao, imagem) VALUES (?, ?, ?)", 
               ("Pastel de Carne", "Pastel frito recheado com carne moída temperada.", 
                "https://images.pexels.com/photos/6529668/pexels-photo-6529668.jpeg"))

cursor.execute("INSERT INTO pratos (nome, descricao, imagem) VALUES (?, ?, ?)", 
               ("Salada Caesar", "Salada leve com alface, frango grelhado e molho especial.", 
                "https://images.pexels.com/photos/1640777/pexels-photo-1640777.jpeg"))

cursor.execute("INSERT INTO pratos (nome, descricao, imagem) VALUES (?, ?, ?)", 
               ("Sushi Variado", "Combinado de sushis frescos com peixe cru e arroz temperado.", 
                "https://images.pexels.com/photos/3577561/pexels-photo-3577561.jpeg"))

cursor.execute("INSERT INTO pratos (nome, descricao, imagem) VALUES (?, ?, ?)", 
               ("Lasanha à Bolonhesa", "Lasanha gratinada com molho à bolonhesa e queijo.", 
                "https://images.pexels.com/photos/4109995/pexels-photo-4109995.jpeg"))

cursor.execute("INSERT INTO pratos (nome, descricao, imagem) VALUES (?, ?, ?)", 
               ("Sorvete de Chocolate", "Taça de sorvete cremoso de chocolate com cobertura.", 
                "https://images.pexels.com/photos/1352278/pexels-photo-1352278.jpeg"))

conn.commit()
conn.close()
print("Banco de dados criado e populado!")

