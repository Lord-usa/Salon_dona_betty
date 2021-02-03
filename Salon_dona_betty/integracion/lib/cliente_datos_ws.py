import requests
import json

def guardar(datosContactoJson):
    
    try:
        url = 'http://127.0.0.1:9000/api/v1/contacto'
        print('CALL SAVE REST SERVICE -> {0}'.format(url))
        response = requests.post(url, data=datosContactoJson)
        
        codigo = response.json()['codigo']
        print('RESPONSE: {0}'.format(response.json()))

        if codigo == 1:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        print('Problemas con el servicio. Intentelo más tarde.')
        return False

def buscarTodo():
    try:
        url = 'http://127.0.0.1:9000/api/v1/contacto'
        print('CALL FIND ALL ID REST SERVICE -> {0}'.format(url))        
        response = requests.get(url)
        codigo = response.json()['codigo']
        print('RESPONSE: {0}'.format(response.json()))

        if codigo == 1:
            return response.json()['datos']
        else:
            return []

    except Exception as e:
        print(e)
        print('Problemas con el servicio. Intentelo más tarde.')
        return []

def eliminar_por_id(id):
    try:
        url = 'http://127.0.0.1:9000/api/v1/contacto'
        print('CALL DELETE BY ID REST SERVICE -> {0}'.format(url))        
        response = requests.delete(url, data={'id' : id})

        codigo = response.json()['codigo']
        print('RESPONSE: {0}'.format(response.json()))

        if codigo == 1:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        print('Problemas con el servicio. Intentelo más tarde.')
        return False 

def buscar_por_id(id):
    try:
        url = 'http://127.0.0.1:9000/api/v1/contacto/{0}'.format(id)
        print('CALL FIND BY ID REST SERVICE -> {0}'.format(url))
        response = requests.get(url)

        codigo = response.json()['codigo']
        print('RESPONSE: {0}'.format(response.json()))

        if codigo == 1:
            return response.json()['dato']
        else:
            return []
    except Exception as e:
        print(e)
        print('Problemas con el servicio. Intentelo más tarde.')
        return [] 

def actualizar(datosContactoJson):
    try:
        url = 'http://127.0.0.1:9000/api/v1/contacto'
        print('CALL UPDATE REST SERVICE -> {0}'.format(url))
        response = requests.put(url, data=datosContactoJson)
        
        codigo = response.json()['codigo']
        print('RESPONSE: {0}'.format(response.json()))

        if codigo == 1:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        print('Problemas con el servicio. Intentelo más tarde.')
        return False        
    