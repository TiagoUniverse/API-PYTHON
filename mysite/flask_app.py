
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Tiagoo!!'



@app.route('/mostra/<string:numero>' , methods=['GET'])
def mostraDados(numero):
    return "Mensagem: Mostrando dados "+str(numero)



@app.route('/insere' , methods=['POST'])
def inserir():
    temp=request.form.get('temperatura')
    return "Insere:" +str(temp)