import sqlite3
import bcrypt

# Classe para gerenciar a conexão com o banco de dados
class Database:
    def __init__(self, db_name='clientes.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL UNIQUE,
                senha BLOB NOT NULL  -- Usando BLOB para armazenar bytes
            )
        ''')
        self.conn.commit()

    def inserir_cliente(self, nome, senha):
        self.cursor.execute('''
            INSERT INTO Clientes (nome, senha) VALUES (?, ?)
        ''', (nome, senha))
        self.conn.commit()

    def buscar_cliente(self, nome):
        self.cursor.execute('''
            SELECT senha FROM Clientes WHERE nome = ?
        ''', (nome,))
        return self.cursor.fetchone()

    def fechar_conexao(self):
        self.conn.close()

# Classe para gerenciar clientes
class Cliente:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha  # Aqui, a senha já é um hash em bytes

    @staticmethod
    def criptografar_senha(senha):
        # Gerar um salt
        salt = bcrypt.gensalt()
        # Criptografar a senha
        return bcrypt.hashpw(senha.encode('utf-8'), salt)  # Certifique-se de codificar a senha

    def verificar_senha(self, senha):
        # Verificar se a senha fornecida corresponde à senha armazenada
        return bcrypt.checkpw(senha.encode('utf-8'), self.senha)  # Codifique a senha ao verificar

# Função para cadastrar um novo cliente
def cadastrar_cliente(db):
    nome = input("Digite o nome do cliente: ")
    senha = input("Digite a senha do cliente: ")
    senha_criptografada = Cliente.criptografar_senha(senha)  # Criptografa a senha

    try:
        db.inserir_cliente(nome, senha_criptografada)  # Armazena a senha criptografada
        print(f'Cliente {nome} cadastrado com sucesso!')
    except sqlite3.IntegrityError:
        print('Este cliente já está cadastrado.')

# Função para login do cliente
def login_cliente(db):
    nome = input("Digite o nome do cliente: ")
    senha = input("Digite a senha do cliente: ")

    senha_armazenada = db.buscar_cliente(nome)
    if senha_armazenada:
        # Use a senha armazenada (que está em bytes) para criar um Cliente
        cliente = Cliente(nome, senha_armazenada[0])  # senha_armazenada[0] é em bytes
        if cliente.verificar_senha(senha):
            print(f'Login bem-sucedido para {nome}!')
            return
        else:
            print('Senha incorreta.')
            return

    print('Cliente não encontrado.')

# Função principal para executar o aplicativo
def main():
    db = Database()  # Cria uma instância da classe Database

    while True:
        print("\nMenu:")
        print("1. Cadastrar cliente")
        print("2. Login do cliente")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_cliente(db)
        elif opcao == '2':
            login_cliente(db)
        elif opcao == '3':
            print("Saindo do aplicativo...")
            db.fechar_conexao()
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
