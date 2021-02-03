from persistencia.models import DatosContacto
from django.core.exceptions import ObjectDoesNotExist, EmptyResultSet
from django.db import IntegrityError, Error
from datetime import datetime

def guardar(datosContacto):
    try:
        datosContacto.save()
        print('Datos Contacto Guardado')
        print(datosContacto)
        return {'codigo': 1, 
                'descripcion': 'CONTACTO GUARDADO', 
                'timestamp': datetime.now()}
    except IntegrityError as e:
        print(e)
        print('ERROR: Datos Contacto no fue almecenado.')
        return {'codigo': 0, 
                'descripcion': 'IMPOSIBLE REGISTRAR EL CONTACTO', 
                'timestamp': datetime.now()}

def buscarTodo():
    try:
        contactos = DatosContacto.objects.all().order_by('id')
        return {'codigo': 1, 
                'descripcion': 'BUSQUEDA EXITOSA', 
                'timestamp': datetime.now(),
                'datos': list(contactos.values())}
    except EmptyResultSet as e:
        print('NO SE ENCONTRARON REGISTROS')
        return {'codigo': 0, 
                'descripcion': 'IMPOSIBLE REGISTRAR EL CONTACTO', 
                'timestamp': datetime.now(),
                'datos': []}
    except Error as e:
        print('ERROR: {0}'.format(e))
        return {'codigo': 0, 
                'descripcion': 'PROBLEMAS CON EL SERVIDOR, INTENTELO MAS TARDE', 
                'timestamp': datetime.now(),
                'datos': []}

def eliminar_por_id(id):
    try:
        datoContacto = DatosContacto.objects.get(id=id)
        datoContacto.delete()
        print('Datos Contacto Eliminar')
        if datoContacto is None: 
            print(datoContacto)        
        return {'codigo': 1, 
                'descripcion': 'REGISTRO ELIMINADO CORRECTAMENTE', 
                'timestamp': datetime.now()}        
    except ObjectDoesNotExist  as e:
        print('NO SE ENCONTRO EL REGISTRO')
        return {'codigo': 0, 
                'descripcion': 'NO SE ENCONTRO EL REGISTRO', 
                'timestamp': datetime.now()}                     
    except Error as e:
        print('ERROR: {0}'.format(e))
        print('NO SE ENCONTRO EL REGISTRO')
        return {'codigo': 0, 
                'descripcion': 'IMPOSIBLE ELIMINAR EL REGISTRO', 
                'timestamp': datetime.now()}           

def buscar_por_id(id):
    print('INICIO buscar_por_id')
    try:
        datoContacto = DatosContacto.objects.get(pk=id)        
        print('datoContacto: {0}'.format(datoContacto))
        return {'codigo': 1, 
                'descripcion': 'BUSQUEDA REALIZADA CON EXITO', 
                'timestamp': datetime.now(),
                'dato': datoContacto.json_serializer()}                     
    except ObjectDoesNotExist as e:
        print('NO SE ENCONTRO EL REGISTRO')
        return {'codigo': 0, 
                'descripcion': 'CONTACTO NO REGISTRADO', 
                'timestamp': datetime.now()} 
    except Error as e:
        print('ERROR: {0}'.format(e))
        return {'codigo': 0, 
                'descripcion': 'CONTACTO NO REGISTRADO', 
                'timestamp': datetime.now()} 

def actualizar(datoContacto):
    try:
        datoContacto.save(force_update=True)
        return {'codigo': 1, 
                'descripcion': 'ACTUALIZACION REALIZADA CON EXITO', 
                'timestamp': datetime.now(),
                'dato': datoContacto.json_serializer()}         
    except EmptyResultSet as e:
        print('NO SE ENCONTRO EL REGISTRO')
        return {'codigo': 0, 
                'descripcion': 'CONTACTO NO REGISTRADO', 
                'timestamp': datetime.now()} 
    except Error as e:
        print('ERROR: {0}'.format(e))
        return {'codigo': 0, 
                'descripcion': 'NO SE PUDO ACTUALIZAR EL REGISTRO', 
                'timestamp': datetime.now()} 