import sqlite3

# Conectando na base de dados
class Loja:
    
    def __init__(self) -> None:
        self.conn = sqlite3.connect('loja.db')
        self.cursor = self.conn.cursor()

    def cadastrar_novo_produto(self):
        valor = ''
        while type(valor) != float:
            produto = input('Nome do produto: ')
            try:
                valor = input('Valor do produto R$')
                if ',' in valor:
                    valor = valor.replace(',', '.')
                valor = float(valor)
            except ValueError:
                print('Coloque o valor em um formato válido.')

        try:
            self.cursor.execute('''
            INSERT INTO produtos (nome, valor) VALUES (?, ?)
            ''', (produto, valor))
            print('Produto cadastrado com sucesso!')
        except sqlite3.IntegrityError:
            print('Este produto já está cadastrado')

        self.conn.commit()

    def fechar_conexao(self):
        self.conn.close()

# Classe para pesquisar produtos
class PesquisarProduto(Loja):

    def por_faixa_de_preco(self, min_valor: float, max_valor: float):
        try:
            self.cursor.execute('''
            SELECT nome, valor FROM produtos WHERE valor BETWEEN ? AND ?
            ''', (min_valor, max_valor))
            resultados = self.cursor.fetchall()
            if resultados:
                for produto in resultados:
                    print(f'Produto: {produto[0]}, Valor: R${produto[1]:.2f}')
            else:
                print('Nenhum produto encontrado nessa faixa de preço.')
        except sqlite3.Error as e:
            print(f"Erro ao pesquisar produtos: {e}")

    def por_nome(self):
        nome = input('Digite o nome do produto que quer pesquisar: ')
        try:
            self.cursor.execute('''
            SELECT nome, valor FROM produtos WHERE nome LIKE ?
            ''', (f'%{nome}%',))
            resultados = self.cursor.fetchall()
            if resultados:
                for produto in resultados:
                    print(f'Produto: {produto[0]}, Valor: R${produto[1]:.2f}')
            else:
                print('Nenhum produto encontrado com esse nome.')
        except sqlite3.Error as e:
            print(f"Erro ao pesquisar produtos: {e}")

PesquisarProduto().por_nome()