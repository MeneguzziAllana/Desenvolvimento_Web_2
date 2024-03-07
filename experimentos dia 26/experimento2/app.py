# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

class ModeloArea:
    def calcular_area(self, comprimento, largura):
        return comprimento * largura

class VisaoArea:
    def renderizar(self, resultado=None):
        return render_template('index.html', resultado=resultado)

class ControladorArea:
    def __init__(self, modelo, visao):
        self.modelo = modelo
        self.visao = visao

    def index(self):
        return self.visao.renderizar()

    def calcular_area(self):
        comprimento = float(request.form['comprimento'])
        largura = float(request.form['largura'])
        resultado = self.modelo.calcular_area(comprimento, largura)
        return self.visao.renderizar(resultado=resultado)

modelo = ModeloArea()
visao = VisaoArea()
controlador = ControladorArea(modelo, visao)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return controlador.calcular_area()
    else:
        return controlador.index()

if __name__ == '__main__':
    app.run(debug=True)
