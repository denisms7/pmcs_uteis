from flask import Flask, render_template, Response, request
from contatos import df, categoria
from excel_30_formulas import dados_video
app = Flask(__name__)
app.config['TITLE'] = 'Uteis'


@app.route("/")
def homepage():
    return render_template('index.html')


@app.route("/hino")
def hino():
    return render_template('hino.html')


@app.route("/estrutura-organizacional")
def organograma():
    return render_template('organograma.html')


@app.route("/contatos")
def contatos():
    return render_template('contatos.html', contatos=df, categoria=categoria)

@app.route("/suporte")
def suporte():
    return render_template('suporte.html')

@app.route("/excel")
def curso_excel():
    return render_template('excel.html', dados_video=dados_video)

@app.route('/video/<file>')
def video(file):
    return render_template('stream.html',file=file)

@app.route("/<string:variavel>")
def erro_pag(variavel):
    return render_template('erro.html', variavel=variavel)


if __name__ == "__main__":
    app.run(debug=True, port=8080)


#if __name__ == "__main__":
#    app.run(host='0.0.0.0', debug=False, port=80)
