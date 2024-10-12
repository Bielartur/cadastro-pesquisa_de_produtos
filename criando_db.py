import sqlite3

# Conectar à base de dados
conn = sqlite3.connect('loja.db')

# Criando um cursor para executar códigos em SQL
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT UNIQUE NOT NULL,
    valor DECIMAL(10, 2) NOT NULL,
    qtd_estoque INTEGER DEFAULT 0 
)
''')

conn.commit()
conn.close()