from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def raiz():
    return 'Olá mundo'

@app.route('/route2')
def rota2():
    return '<h1>Esta é a segunda rota da aplicação</h1>'

@app.route('/pessoas/<string:nome>/<string:cidade>')
def pessoas(nome, cidade):
    return jsonify({
        'nome': nome, 
        'cidade': cidade
                    })

app.run(debug=True)