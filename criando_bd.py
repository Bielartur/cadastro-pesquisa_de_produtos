import sqlite3

# Conectar à base de dados
conn = sqlite3.connect('loja.db')

# Criando um cursor para executar códigos em SQL
cursor = conn.cursor()

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS produtos (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     nome TEXT UNIQUE NOT NULL,
#     valor DECIMAL(10, 2) NOT NULL,
#     qtd_estoque INTEGER DEFAULT 0 
# )
# ''')

cursor.execute('''

''')

conn.commit()
conn.close()

# Categorias

# Feminino:

# Vestidos
# Blusas
# Saias
# Calças
# Roupas de banho
# Casacos e jaquetas
# Acessórios (bolsas, bijuterias, lenços)
# Masculino:

# Camisetas
# Camisas
# Calças
# Shorts
# Roupas de banho
# Jaquetas e blusões
# Acessórios (cintos, bonés, relógios)
# Infantil:

# Roupas para bebês
# Roupas para meninos
# Roupas para meninas
# Acessórios infantis (chapéus, meias, mochilas)
# Calçados:

# Sapatos femininos
# Sapatos masculinos
# Tênis
# Botas
# Sandálias
# Atividades Esportivas:

# Roupas de ginástica
# Roupas de corrida
# Roupas de esportes aquáticos
# Acessórios esportivos (mochilas, faixas)
# Moda Plus Size:

# Roupas femininas plus size
# Roupas masculinas plus size
# Moda Sustentável:

# Roupas feitas de materiais reciclados
# Roupas de algodão orgânico
# Coleções Especiais:

# Roupas de festa
# Roupas de inverno
# Roupas de verão
# Roupas Íntimas:

# Lingerie feminina
# Cuecas e sungas masculinas
# Pijamas