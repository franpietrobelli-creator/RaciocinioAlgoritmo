from flask import Flask, request

app = Flask(__name__)

@app.get("/")
def hello():
        return "Hello, Word!"

@app.get("/soma")
def somar():
            a = float(request.args["a"]) #numero
            b = float(request.args["b"]) #numero
            c = request.args["c"] #texto 
           

            return {"Resultado": a*b, "abc": c}

app.run()
