import sqlite3
import PySimpleGUI as sg

# Conectando na base de dados
conn = sqlite3.connect('loja.db')

cursor = conn.cursor()

sg.theme('reddit')

def cadastrar_novo_produto():
    layout_cadastro = [
        [sg.Text('Nome do produto:')],
        [sg.Input(key='nome_produto')],
        [sg.Text('Valor do produto:')],
        [sg.Input(key='valor_produto')],
        [sg.Button('Cadastrar')]
    ]

    janela = sg.Window('Loja', layout=layout_cadastro)

    while True:
        evento, valores = janela.read()
        if evento == 'Cadastrar':
            produto = valores['nome_produto']
            valor = valores['valor_produto']
            try:
                if ',' in valor:
                    valor = valor.replace(',', '.')
                float(valor)
            except ValueError:
                sg.popup('Coloque o valor em um formato válido.')
            break
                
        elif evento == sg.WIN_CLOSED:
            break

    janela.close()

    try:
        cursor.execute('''
        INSERT INTO produtos (nome, valor) VALUES (?, ?)
        ''', (produto, valor))
        sg.popup('Produto cadastrado com sucesso!', text_color='green')
    except sqlite3.IntegrityError:
        sg.popup('Este produto já está cadastrado')

    conn.commit()

cadastrar_novo_produto()
conn.close()