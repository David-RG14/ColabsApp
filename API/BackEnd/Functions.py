from flask import jsonify
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
import BackEnd.GlobalInfo.ResponseMessages as mensajitos
import BackEnd.GlobalInfo.Keys as ColabsKeys

# Coneccion con las tablas de Mongo
if ColabsKeys.dbconn==None:
    mongoConnect=MongoClient(ColabsKeys.strConnection)
    ColabsKeys.dbconn=mongoConnect[ColabsKeys.strDBConnection]
    dbUsers=ColabsKeys.dbconn["clUsuarios"]
    dbColabs=ColabsKeys.dbconn["clColabs"]


# Mostrar Json creado (GET)
def fnMensajeGet():
    try:
        return jsonify({"Mensaje": "Hola mundos"})
    except Exception as e:
        return jsonify({"Error":str(e)})

    
# Mostrar todos los registros User (GET)
def fnGetUsers():
    try:
        arrFinalUser=[]
        objQuery=dbUsers.find({})
        listUsers=list(objQuery)
        if len(listUsers)!=0:
            for objUser in listUsers:
                print(objUser)
                objFormateado={
                    "_id":str(objUser['_id']),
                    "strCorreo":objUser["strCorreo"],
                    "strPassword":objUser['strPassword'],
                    "strRol":objUser['strRol'],
                }
                arrFinalUser.append(objFormateado)
        objResponse=mensajitos.succ200.copy()
        objResponse['Respuesta']=arrFinalUser
        return jsonify(objResponse)
    except Exception as e:
        print("Error en fngetusers",e)
        return jsonify(mensajitos.err500)

# Borrar User por ID (DELETE)
def fnDeleteUsers(id):
    try:
        print("Los datos que eliminare: ", id)
        dbUsers.delete_one({"_id": ObjectId(id)})
        objResponse = mensajitos.succ200.copy()
        objResponse['Informacion_Borrada'] = True
        return jsonify(objResponse)
    except Exception as e:
        print("Error en fnDeleteUsers", e)
        return jsonify(mensajitos.err500)

# Insertar nuevo User (POST)
def fnPostUsers(objDato):
    try:
        print("Los datos para insertar: ", objDato)
        strCorreo = objDato.get("strCorreo")
        strPassword = objDato.get("strPassword")
        strRol = objDato.get("strRol")
        resultado = dbUsers.insert_one({
            "strCorreo": strCorreo,
            "strPassword": strPassword,
            "strRol": strRol
        })
        objResponse = mensajitos.succ200.copy()
        objResponse['id_insertado'] = str(resultado.inserted_id)
        objResponse['Informacion_Insertada'] = True
        return jsonify(objResponse)
    except Exception as e:
        print("Error en fnPutUsers", e)
        return jsonify(mensajitos.err500)

# Actualizar datos User por ID (PUT)
def fnPutUsers(id, objDato):
    try:
        print("ID a modificar:", id)
        print("Nuevos datos:", objDato)
        datos_actualizar = {}
        if "strCorreo" in objDato:
            datos_actualizar["strCorreo"] = objDato["strCorreo"]
        if "strPassword" in objDato:
            datos_actualizar["strPassword"] = objDato["strPassword"]
        if "strRol" in objDato:
            datos_actualizar["strRol"] = objDato["strRol"]
        # Usamos $set para actualizar solo los campos enviados
        resultado = dbUsers.update_one(
            {"_id": ObjectId(id)},
            {"$set": datos_actualizar}
        )
        if resultado.matched_count == 0:
            return jsonify({"status": 404, "message": "Usuario no encontrado"})
        objResponse = mensajitos.succ200.copy()
        objResponse['Informacion_Actualizada'] = True
        return jsonify(objResponse)
    except Exception as e:
        print("Error en fnUpdateUser:", e)
        return jsonify(mensajitos.err500)

# Buscador User por ID (GET)    
def fnBuscarUsers(id):
    try:
        print("ID recibido para búsqueda:", id)
        # Validar si el ID recibido es un ObjectId válido de MongoDB
        if not ObjectId.is_valid(id):
            return jsonify({"status": 400, "message": "El ID proporcionado no es válido"})
        # Consulta en MongoDB usando find_one
        usuario = dbUsers.find_one({"_id": ObjectId(id)})
        # Si no existe el registro
        if not usuario:
            return jsonify({"status": 404, "message": "Usuario no encontrado", "Respuesta": None})
        # Convertir ObjectId a String para que pueda convertirse a JSON sin error
        usuario["_id"] = str(usuario["_id"])
        objResponse = mensajitos.succ200.copy()
        objResponse['Respuesta'] = usuario
        return jsonify(objResponse)
    except Exception as e:
        print("Error en fnBuscarUser:", e)
        return jsonify(mensajitos.err500)

# Mostrar todos los registros Colab (GET)
def fnGetColabs():
    try:
        arrFinalColab=[]
        objQuery=dbColabs.find({})
        listColabs=list(objQuery)
        if len(listColabs)!=0:
            for objColab in listColabs:
                print(objColab)
                objFormateado={
                    "_id":str(objColab['_id']),
                    "strNombre":objColab["strNombre"],
                    "strApellido":objColab['strApellido'],
                    "strPuesto":objColab['strPuesto'],
                    "floatSueldo":objColab['floatSueldo'],
                    "strRfc":objColab['strRfc'],
                }
                arrFinalColab.append(objFormateado)
        objResponse=mensajitos.succ200.copy()
        objResponse['Respuesta']=arrFinalColab
        return jsonify(objResponse)
    except Exception as e:
        print("Error en fngetusers",e)
        return jsonify(mensajitos.err500)

# Borrar Colab por ID (DELETE)
def fnDeleteColabs(id):
    try:
        print("Los datos que eliminare: ", id)
        dbColabs.delete_one({"_id": ObjectId(id)})
        objResponse = mensajitos.succ200.copy()
        objResponse['Informacion_Borrada'] = True
        return jsonify(objResponse)
    except Exception as e:
        print("Error en fnDeleteColabs", e)
        return jsonify(mensajitos.err500)

# Insertar nuevo Colab (POST)
def fnPostColabs(objDato):
    try:
        print("Los datos para insertar: ", objDato)
        strNombre = objDato.get("strNombre")
        strApellido = objDato.get("strApellido")
        strPuesto = objDato.get("strPuesto")
        floatSueldo = objDato.get("floatSueldo")
        strRfc = objDato.get("strRfc")

        resultado = dbColabs.insert_one({
            "strNombre": strNombre,
            "strApellido": strApellido,
            "strPuesto": strPuesto,
            "floatSueldo": floatSueldo,
            "strRfc": strRfc
        })
        objResponse = mensajitos.succ200.copy()
        objResponse['id_insertado'] = str(resultado.inserted_id)
        objResponse['Informacion_Insertada'] = True
        return jsonify(objResponse)
    except Exception as e:
        print("Error en fnPostColabs", e)
        return jsonify(mensajitos.err500)

# Actualizar datos Colab por ID (PUT)
def fnPutColabs(id, objDato):
    try:
        print("ID a modificar:", id)
        print("Nuevos datos:", objDato)
        datos_actualizar = {}
        if "strNombre" in objDato:
            datos_actualizar["strNombre"] = objDato["strNombre"]
        if "strApellido" in objDato:
            datos_actualizar["strApellido"] = objDato["strApellido"]
        if "strPuesto" in objDato:
            datos_actualizar["strPuesto"] = objDato["strPuesto"]
        if "floatSueldo" in objDato:
            datos_actualizar["floatSueldo"] = objDato["floatSueldo"]
        if "strRfc" in objDato:
            datos_actualizar["strRfc"] = objDato["strRfc"]
        # Usamos $set para actualizar solo los campos enviados
        resultado = dbColabs.update_one(
            {"_id": ObjectId(id)},
            {"$set": datos_actualizar}
        )
        if resultado.matched_count == 0:
            return jsonify({"status": 404, "message": "Usuario no encontrado"})
        objResponse = mensajitos.succ200.copy()
        objResponse['Informacion_Actualizada'] = True
        return jsonify(objResponse)
    except Exception as e:
        print("Error en fnPutColabs:", e)
        return jsonify(mensajitos.err500)

# Buscador Colab por ID (GET)    
def fnBuscarColabs(id):
    try:
        print("ID recibido para búsqueda:", id)
        # Validar si el ID recibido es un ObjectId válido de MongoDB
        if not ObjectId.is_valid(id):
            return jsonify({"status": 400, "message": "El ID proporcionado no es válido"})
        # Consulta en MongoDB usando find_one
        usuario = dbColabs.find_one({"_id": ObjectId(id)})
        # Si no existe el registro
        if not usuario:
            return jsonify({"status": 404, "message": "Usuario no encontrado", "Respuesta": None})
        # Convertir ObjectId a String para que pueda convertirse a JSON sin error
        usuario["_id"] = str(usuario["_id"])
        objResponse = mensajitos.succ200.copy()
        objResponse['Respuesta'] = usuario
        return jsonify(objResponse)
    except Exception as e:
        print("Error en fnBuscarColabs:", e)
        return jsonify(mensajitos.err500)