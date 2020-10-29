import flask
import json
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/v1/ressources/calculator/add', methods=['POST'])
def add():
    t = request.json
    print(t)
    sum = int(t['x']) + int(t['y'])
    print(str(sum))
    result = {'Summe' : str(sum)}
    print(result)
    return json.dumps(result)

@app.route('/v1/ressources/calculator/sub', methods=['POST'])
def sub():
    t = request.json
    print(t)
    diff = int(t['x']) - int(t['y'])
    print(str(diff))
    result = {'Differenz' : str(diff)}
    print(result)
    return json.dumps(result)

@app.route('/v1/ressources/calculator/mult', methods=['POST'])
def mult():
    t = request.json
    print(t)
    prod = int(t['x']) * int(t['y'])
    print(str(prod))
    result = {'Produkt' : str(prod)}
    print(result)
    return json.dumps(result)

@app.route('/v1/ressources/calculator/div', methods=['POST'])
def div():
    t = request.json
    print(t)
    div = int(t['x']) / int(t['y'])
    print(str(div))
    result = {'Quotient' : str(div)}
    print(result)
    return json.dumps(result)

#app.run()
app.run(host='0.0.0.0', port=80)