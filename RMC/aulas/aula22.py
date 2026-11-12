from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World! Flask está funcionando!'

@app.route('/ola/<nome>')
def ola(nome):
    return f'Olá, {nome}! Bem-vindo ao Flask!'

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)