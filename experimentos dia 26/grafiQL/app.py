from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/consultar_paises', methods=['POST'])
def consultar_paises():
    query = """
    {
      countries {
        code
        name
        native
        emoji
        currency
      }
    }
    """
    url = 'https://countries.trevorblades.com/'
    response = requests.post(url, json={'query': query})
    if response.status_code == 200:
        data = response.json()
        paises = data['data']['countries']
        return jsonify(paises)
    else:
        return jsonify({'error': 'Erro ao consultar a API'})

if __name__ == '__main__':
    app.run(debug=True)
