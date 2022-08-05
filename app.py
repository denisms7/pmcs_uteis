from flask import Flask, render_template, Response, request
from contatos import df, categoria

app = Flask(__name__)
app.config['TITLE'] = 'Uteis'


@app.route("/")
def homepage():
    title= 'INICIO'
    return render_template('index.html', title=title)

@app.route("/hino")
def hino():
    title= 'Hino Municipal'
    return render_template('hino.html', title=title)

@app.route("/estrutura-organizacional")
def organograma():
    title = 'Organograma'
    return render_template('organograma.html', title=title)

@app.route("/contatos")
def contatos():
    title = 'Contatos'
    return render_template('contatos.html', contatos=df, categoria=categoria, title=title)

@app.route("/suporte")
def suporte():
    title = 'Suporte'
    return render_template('suporte.html', title=title)

@app.route("/sim")
def sim_am():
    title = 'SIM-AM'
    return render_template('sim.html', title=title)

@app.route("/<string:variavel>")
def erro_pag(variavel):
    title = '#ERRO'
    return render_template('erro.html', variavel=variavel, title=title)


#if __name__ == "__main__":
#    app.run(debug=True, port=80)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, port=80)
