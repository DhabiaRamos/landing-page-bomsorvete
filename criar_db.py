import sqlite3

conexao = sqlite3.connect("database.db")
cursor = conexao.cursor()

# Tabela de contato

cursor.execute("""
CREATE TABLE IF NOT EXISTS contatos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    telefone TEXT NOT NULL,
    mensagem TEXT NOT NULL        
    )

""")

# Tabela de pedidos

cursor.execute("""
    CREATE TABLE IF NOT EXISTS pedidos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT NOT NULL,
        pedido_original TEXT NOT NULL,
        status TEXT DEFAULT 'Pendente',
        arquivado INTEGER DEFAULT 0
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS itens_pedido (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pedido_id INTEGER NOT NULL,
    categoria TEXT,
    sabor TEXT,
    quantidade INTEGER,
    volume INTEGER,

    FOREIGN KEY (pedido_id)
    REFERENCES pedidos(id)
)
""")

conexao.commit()
conexao.close()

print("Banco criado com sucesso!")
