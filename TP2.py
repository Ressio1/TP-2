from flask import Flask
from subprocess import *
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/name')
def name():
    name = check_output("hostname", shell=True).decode('UTF-8')
    return name

@app.route('/<x>/<y>')
def Caractere(x,y):
    y = int(y)
    return x * y

