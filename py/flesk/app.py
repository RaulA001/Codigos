
from flask import Flask, redirect, url_for, request, abort, render_template
from json import dumps
app = Flask(__name__, static_folder='miracica/', template_folder='template')

#forma 1 de cria rota
@app.route('/')
def index():
    #q2 não funciona
    query2 = dumps(request.args)
    query = request.args.to_dict()
    print(query2, query)

    return render_template('index.html', x=10, y=101, query=query)

@app.route('/oi/', methods=['GET', 'POST'])
@app.route('/oi/<nome>')
def oi(nome=''):
    if True:
        print(request.method, request.args)
        res = f'<h1>oi {nome}</h1> <p>{dumps(request.form)} <br> {request.method}</p> <a href="http://127.0.0.1:5000/miracica/index.html">Voltar</a>'
        return res
    else:
        abort(403)
#forma 2 de cria rota

def test():
    print(request.method, ' | ', request.args)
    return f'<h1>Testado2</h1> <p>é {dumps(request.args)}<p>'
app.add_url_rule('/test', 'test', test)

if __name__ == '__main__':
    app.run(debug=True)