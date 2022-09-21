

# Código de Arnott Abaixo 20/09
#
# Faculdade SENAC PE
# Material de Apoio para Internet das Coisas
#
# Prof. Arnott Ramos Caiado
#
# ago/set 2022

# bibliotecas basicas
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Exemplo de um endpoit gerado automaticamente'

# exemplo de um endpoit para requisicoes basicas de consulta
@app.route('/getJson', methods=['GET'])
def getJson():
    cab = request.headers.get('Authorization-Token')
    return {"msg get": str(cab) }

# exemplo de um endpoit para requisicoes basicas POST. formato JSON
@app.route('/postJson', methods=['POST'])
def postJson():
    cab = request.headers.get('Authorization-Token')    # token que pode ser utilizado para validacao

    dados = request.get_json()                          # recebe os dados em formato json

    sensor  = dados["sensor"]                           # identifica cada elemento do json de origem
    valor = dados["valor"]

    # criar funcao para gravar dados
    gravaDados ( sensor, valor )

    return {"sensor": str(sensor) , "valor": str(valor)}


# end point para mostrar o uso da linha de comando com argumento
@app.route('/getLinha', methods=['GET'])
def getLinha():
    sensor = request.args.get('sensor')
    valor = request.args.get('valor')
    return {"Formato de linha http": "ok","sensor": str(sensor) , "valor": str(valor)}


# end point para receber dados no formato de form
@app.route('/postForm', methods=['GET','POST'])
def postForm():
    sensor = request.form['sensor']
    valor = request.form['valor']
    return {"Formato de form": "ok","sensor": str(sensor) , "valor": str(valor)}

# funcao para concatenar linha para arquivo csv
def montaStr( *args ) :
  st = ''
  t = len( args )
  for elemento in args :
    st = st + elemento
    t = t-1
    if t != 0 :
      st = st + ','
  st = st + "\n"
  return st


# grava dados
def gravaDados( sensor, valor ):
    return