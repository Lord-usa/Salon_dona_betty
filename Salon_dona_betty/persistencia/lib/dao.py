from persistencia.models import DatosContacto
from django.core.exceptions import ObjectDoesNotExist, EmptyResultSet
from django.db import IntegrityError, Error
from datetime import datetime

def guardar(datosContacto):
    try:
        datosContacto.save()
        print('Datos Contacto Guardado')
        print(datosContacto)
        return True
    except IntegrityError as e:
        print(e)
        print('ERROR: Datos Contacto no fue almacenado.')
        return False 

def buscarTodo():
    try:
        return DatosContacto.objects.all()
    except EmptyResultSet as e:
        print('No se encontraron resultados')
        return []
    except Error as e:
        print('ERROR: {1}'.format(e))
        return[]

def eliminar_por_id(id):
    try:
        datoContacto = DatosContacto.objects.get(id=id)
        datoContacto.delete()
        return True
    except EmptyResultSet as e:
        print('NO SE ENCONTRO EL REGISTRO')
        return False
    except Error as e:
        print('ERROR: {1}'.format(e))
        return False

def buscar_por_id(id):
    try:
        datoContacto = DatosContacto.objects.get(id=id)
        return datoContacto
    except EmptyResultSet as e:
        print('NO SE ENCONTRO EL REGISTRO')
        return []
    except Error as e:
        print('ERROR: {1}'.format(e))
        return []

def actualizar(datoContacto):
    try:
        datoContacto.save(force_update=True)
        return True
    except EmptyResultSet as e:
        print('NO SE ENCONTRO EL REGISTRO')
        return False
    except Error as e:
        print('ERROR: {1}'.format(e))
        return False                    

