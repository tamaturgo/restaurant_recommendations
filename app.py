from flask import Flask, render_template, url_for, request
import pandas as pd

app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        quantidade = request.form['quantidade']
        # Lê os dados do arquivo CSV para um DataFrame
        df = pd.read_csv('restaurantes.csv')

        # Converte os dados do DataFrame em uma lista de dicionários
        restaurantes = df.to_dict('records')

        restaurantes = restaurantes[:int(quantidade)]

        # Renderiza o template da página, passando os dados dos restaurantes como variáveis
        return render_template('index.html', restaurantes=restaurantes)

    else:

        # Lê os dados do arquivo CSV para um DataFrame
        df = pd.read_csv('restaurantes.csv')

        # Converte os dados do DataFrame em uma lista de dicionários
        restaurantes = df.to_dict('records')

        # Renderiza o template da página, passando os dados dos restaurantes como variáveis
        return render_template('index.html', restaurantes=restaurantes)
