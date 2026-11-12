from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/calcular/<int:a>/<int:b>')
def calcular(a, b):
    soma = a + b
    subtracao = a - b
    multiplicacao = a * b
    resposta = {
        "a": a,
        "b": b,
        "soma": soma,
        "subtracao": subtracao,
        "multiplicacao": multiplicacao
    }
    return jsonify(resposta)
app.run(debug=True)
