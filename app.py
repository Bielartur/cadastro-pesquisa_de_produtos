import sqlite3

# Conectando na base de dados
class Loja:
    def conectar_bd():
        conn = sqlite3.connect('loja.db')
        cursor = conn.cursor()

        return conn, cursor
    
    def salvar_fechar_bd(conn):
        conn.commit()
        conn.close()
    
    def cadastrar_novo_produto(self) -> None:
        valor = ''
        produto = input('Nome do produto: ').strip().upper()
        while type(valor) != float: 
            try:
                valor = input('Valor do produto R$')
                if ',' in valor:
                    valor = valor.replace(',', '.')
                valor = round(float(valor), 2)
            except ValueError:
                print('Coloque o valor em um formato válido.')

        try:
            # Conectando na base de dados para efutuar a consulta
            conn, cursor = self.conectar_bd()

            cursor.execute('''
            INSERT INTO produtos (nome, valor) VALUES (?, ?)
            ''', (produto, valor))
            print('Produto cadastrado com sucesso!')

        except sqlite3.IntegrityError:
            print('Este produto já está cadastrado')

        self.salvar_fechar_bd(conn)

    # Classe para pesquisar produtos
    class PesquisarProduto():

        def por_faixa_de_preco(self):
            try:
                min_valor = input('Digite o valor mínimo do produto: ')
                max_valor = input('Digite o valor máximo do produto: ')

                if ',' in min_valor:
                    min_valor = min_valor.replace(',', '.')

                if ',' in max_valor:
                    max_valor = max_valor.replace(',', '.')

                min_valor, max_valor = float(min_valor), float(max_valor)
                
            except ValueError:
                print('Esse campo aceita apenas números.')
            try:
                # Conectando na base de dados para efutuar a consulta
                conn, cursor = Loja.conectar_bd()

                cursor.execute('''
                SELECT nome, valor FROM produtos WHERE valor BETWEEN ? AND ?
                ''', (min_valor, max_valor))

                resultados = cursor.fetchall()
                if resultados:
                    print('')
                    for produto in resultados:
                        print(f'{produto[0]} -> R${produto[1]:.2f}')
                else:
                    print('Nenhum produto encontrado nessa faixa de preço.')

                Loja.salvar_fechar_bd(conn)

            except sqlite3.Error as e:
                print(f"Erro ao pesquisar produtos: {e}")
                try:
                    # Fecha base de dados caso tenha sido aberta
                    conn.close()
                except sqlite3.Error:
                    pass

        def por_nome(self):
            # Conectando na base de dados para efutuar a consulta
            conn, cursor = Loja.conectar_bd()

            nome = input('Digite o nome do produto que quer pesquisar: ')
            try:
                cursor.execute('''
                SELECT nome, valor FROM produtos WHERE nome LIKE ?
                ''', (f'%{nome}%',))
                resultados = cursor.fetchall()
                if resultados:
                    for produto in resultados:
                        print(f'{produto[0]} -> R${produto[1]:.2f}')
                else:
                    print('Nenhum produto encontrado com esse nome.')

                Loja.salvar_fechar_bd(conn)

            except sqlite3.Error as e:
                print(f"Erro ao pesquisar produtos: {e}")
                try:
                    # Fecha base de dados caso tenha sido aberta
                    conn.close()
                except sqlite3.Error:
                    pass

        def por_categoria():
            pass

Loja().PesquisarProduto().por_nome()