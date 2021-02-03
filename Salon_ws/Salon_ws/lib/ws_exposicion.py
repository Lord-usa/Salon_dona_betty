from django.http import JsonResponse
from rest_framework.decorators import api_view
from datetime import datetime
from persistencia.lib.dato_contacto_dao import buscarTodo, guardar, eliminar_por_id, actualizar, buscar_por_id
from persistencia.models import DatosContacto

@api_view(['GET'])
def buscar_contacto_por_id(request, id):
    
    print('id: {0}'.format(id))
    response = buscar_por_id(id)
    return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def contactos(request):
    if request.method == 'POST':
        return guardarContacto(request)
    if request.method == 'GET':    
        return buscarTodosLosContacto(request)
    if request.method == 'DELETE':
        return eliminarContacto(request)
    if request.method == 'PUT':
        return actualizarContacto(request)


def buscarTodosLosContacto(request):
    print('INICIO buscarTodosLosContacto')
    response = buscarTodo()
    print('FIN buscarTodosLosContacto')
    return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})

def guardarContacto(request):

    print('INICIO guardarContacto')
    nombres = request.data.get('nombres')
    apellido_paterno = request.data.get('apellido-paterno')
    apellido_materno = request.data.get('apellido-materno')
    email = request.data.get('email')
    telefono = request.data.get('telefono')
    asunto = request.data.get('asunto')

    contacto = DatosContacto(nombres=nombres,
                            apellido_pat=apellido_paterno, 
                            apellido_mat=apellido_materno,
                            email=email, 
                            telefono=telefono, 
                            asunto=asunto)
    response = guardar(contacto) 
    print('FIN guardarContacto')
    return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})

def eliminarContacto(request):

    print('INICIO eliminarContacto')
    id = request.data.get('id')

    response = eliminar_por_id(id)
    print('FIN eliminarContacto')
    return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})

def actualizarContacto(request):

    print('INICIO actualizarContacto')
    id = request.data.get('id')
    nombres = request.data.get('nombres')
    apellido_paterno = request.data.get('apellido-paterno')
    apellido_materno = request.data.get('apellido-materno')
    email = request.data.get('email')
    telefono = request.data.get('telefono')
    asunto = request.data.get('asunto')

    contacto = DatosContacto(id = id,
                            nombres=nombres,
                            apellido_pat=apellido_paterno, 
                            apellido_mat=apellido_materno,
                            email=email, 
                            telefono=telefono, 
                            asunto=asunto)
    response = actualizar(contacto) 
    print('FIN actualizarContacto')
    return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})
