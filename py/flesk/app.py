import json

from flask import Flask, redirect, url_for, request, abort, render_template, make_response, Response
from json import dumps
from werkzeug.utils import secure_filename
import os
from models import db, Estud

app = Flask(__name__, static_folder='miracica/', template_folder='template')
app.secret_key = 'a1234'
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'imagem')

#bd
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///estud.db'

@app.route('/bank', methods=['GET', 'POST'])
def bank():
    estud = Estud.query.all()
    resut = [e.to_dict() for e in estud]
    print(estud)
    return Response(response=dumps(resut), status=200,content_type='application/json')
    #return render_template('bank.html', estud=estud)

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        estud = Estud(request.form['nome'], request.form['idade'])
        db.session.add(estud)
        db.session.commit()
        return redirect(url_for('bank'))
    return render_template('add.html')

@app.route('/Del/<int:id>', methods=['GET', 'POST'])
def Del(id):
    estud = Estud.query.get(id)
    db.session.delete(estud)
    db.session.commit()
    return redirect(url_for('bank'))

@app.route('/edit/<int:id>', methods=['PUT', 'POST'])
def edit(id):
    estud = Estud.query.get(id)
    if request.method == 'POST':
        estud.nome = request.form['nome']
        estud.idade = request.form['idade']
        db.session.commit()
        return redirect(url_for('bank'))
    return render_template('edit.html', estud=estud)

#forma 1 de cria rota
@app.route('/', methods=['GET', 'POST'])
def index():
    #q2 não funciona
    query2 = dumps(request.args)
    query = request.args.to_dict()
    print(query2, query)
    res = make_response((render_template('index.html', x=10, y=101, query=query)))

    return res

    #return render_template('index.html', x=10, y=101, query=query)

@app.route('/imagem', methods=['POST'])
def imagem():
    file = request.files['imagem']
    sp = os.path.join(UPLOAD_FOLDER, secure_filename(file.filename))
    file.save(sp)
    return 'ok'

@app.route('/cal/', methods=['POST'])
def cal():
    nota = sum([int(v) for v in request.form.to_dict().values()])

    res = make_response((render_template('cal.html', nota=nota)))
    if request.method == 'POST':
        dado = request.form['nota2']
        res.set_cookie('nota2', dado)

    print(request.method)
    return res

@app.route('/cok')
def cok():
    dados = request.cookies.get('nota2')
    return f'{dados}'

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
    db.init_app(app=app)
    with app.test_request_context():
        db.create_all()
    app.run(debug=True)