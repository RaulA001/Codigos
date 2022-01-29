from flask import Flask, redirect, url_for, request
app = Flask(__name__, static_folder='miracica/')

#lembra de voltar na aula 6

#forma 1 de cria rota
@app.route('/')
def index():
    return redirect(url_for('oi'))

@app.route('/oi/')
@app.route('/oi/<nome>', methods=['GET', 'POST'])
def oi(nome=''):
    res = f'<h1>oi {nome}</h1> {request.method}'
    return res
#forma 2 de cria rota

def test():
    return '<1>Testado2</h1>'
app.add_url_rule('/test', 'test', test)

if __name__ == '__main__':
    app.run(debug=True, port='3000')