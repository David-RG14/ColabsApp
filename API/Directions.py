# Importacion de librerias
from flask import Flask,jsonify,request
from flask_cors import CORS, cross_origin
import BackEnd.Functions as Callmethod
import BackEnd.GlobalInfo.ResponseMessages as mensajitos

# Instancia
app=Flask(__name__)
CORS(app)


# Mostrar Json creado (GET)
@app.route('/')
@cross_origin(allow_headers=['Content-Type'])
def Getmessage():
    try:
        objResult=Callmethod.fnMensajeGet()
        return objResult
    except Exception as e:
        print("Error en Getmessage",e)
        return jsonify(mensajitos.err500)


# Mostrar todos los registros User (GET)
@app.route('/getUsers')
@cross_origin(allow_headers=['Content-Type'])
def fnGetUsers():
    try:
        objResult=Callmethod.fnGetUsers()
        return objResult
    except Exception as e:
        print("Error en getUsers",e)
        return jsonify(mensajitos.err500)

# Borrar User por ID (DELETE)
@app.route('/deleteUsers/<id>', methods=['DELETE'])
@cross_origin(allow_headers=['Content-Type'])
def fnDeleteUsers(id):
    try:
        objResult = Callmethod.fnDeleteUsers(id)
        return objResult
    except Exception as e:
        print("Error en ruta deleteUser", e)
        return jsonify(mensajitos.err500)

# Insertar nuevo User (POST)
@app.route('/postUsers', methods=['POST'])
@cross_origin(allow_headers=['Content-Type'])
def fnPostUsers():
    try:
        objDato = request.get_json()
        objResult = Callmethod.fnPostUsers(objDato)
        return objResult
    except Exception as e:
        print("Error en ruta postUser", e)
        return jsonify(mensajitos.err500)

# Actualizar datos User por ID (PUT)
@app.route('/putUsers/<id>', methods=['PUT'])
@cross_origin(allow_headers=['Content-Type'])
def fnPutUsers(id):
    try:
        objDato = request.get_json()
        objResult = Callmethod.fnPutUsers(id, objDato)
        return objResult
    except Exception as e:
        print("Error en ruta updateUser:", e)
        return jsonify(mensajitos.err500)

# Buscador User por ID (GET) 
@app.route('/buscarUsers/<id>')
@cross_origin(allow_headers=['Content-Type'])
def fnBuscarUsers(id):
    try:
        objResult = Callmethod.fnBuscarUsers(id)
        return objResult
    except Exception as e:
        print("Error en ruta buscarUser:", e)
        return jsonify(mensajitos.err500)


# Mostrar todos los registros Colab (GET)
@app.route('/getColabs')
@cross_origin(allow_headers=['Content-Type'])
def fnGetColabs():
    try:
        objResult=Callmethod.fnGetColabs()
        return objResult
    except Exception as e:
        print("Error en getColabs",e)
        return jsonify(mensajitos.err500)

# Borrar Colab por ID (DELETE)
@app.route('/deleteColabs/<id>', methods=['DELETE'])
@cross_origin(allow_headers=['Content-Type'])
def fnDeleteColabs(id):
    try:
        objResult = Callmethod.fnDeleteColabs(id)
        return objResult
    except Exception as e:
        print("Error en ruta deleteColabs", e)
        return jsonify(mensajitos.err500)

# Insertar nuevo Colab (POST)
@app.route('/postColabs', methods=['POST'])
@cross_origin(allow_headers=['Content-Type'])
def fnPostColabs():
    try:
        objDato = request.get_json()
        objResult = Callmethod.fnPostColabs(objDato)
        return objResult
    except Exception as e:
        print("Error en ruta postColabs", e)
        return jsonify(mensajitos.err500)

# Actualizar datos Colab por ID (PUT)
@app.route('/putColabs/<id>', methods=['PUT'])
@cross_origin(allow_headers=['Content-Type'])
def fnPutColabs(id):
    try:
        objDato = request.get_json()
        objResult = Callmethod.fnPutColabs(id, objDato)
        return objResult
    except Exception as e:
        print("Error en ruta putColabs/<id>:", e)
        return jsonify(mensajitos.err500)

# Buscador Colab por ID (GET) 
@app.route('/buscarColabs/<id>')
@cross_origin(allow_headers=['Content-Type'])
def fnBuscarColabs(id):
    try:
        objResult = Callmethod.fnBuscarColabs(id)
        return objResult
    except Exception as e:
        print("Error en ruta buscarColabs/<id>:", e)
        return jsonify(mensajitos.err500)
    
# Ruta de la Pagina
if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000, debug=True, threaded=True)