from flask import Flask, render_template
import requests

app = Flask(__name__)

API_URL = "https://api.coinlore.net/api/tickers/"

@app.route('/')
def index():
    response = requests.get(API_URL)
    data = response.json()

    criptos = data['data']  

    return render_template('page_cripto.html', criptos=criptos)

@app.route('/cripto/<id>')
def detalle(id):
    url = f"https://api.coinlore.net/api/ticker/?id={id}"
    response = requests.get(url)
    cripto = response.json()[0]
   
    return render_template('detalle.html', cripto=cripto)

if __name__ == '__main__':
    app.run(debug=True)