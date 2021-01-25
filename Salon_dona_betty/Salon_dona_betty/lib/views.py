from django.http import HttpResponse
from django.template import Template, Context 
from django.template.loader import get_template
from django.shortcuts import render 
from persistencia.models import DatosContacto
from persistencia.lib.dao import guardar, buscarTodo, eliminar_por_id, buscar_por_id, actualizar


def home(request):
    return render(request, "index.html")

def cuidadocabello(request):
    return render(request, "cuidadocabello.html")

def cortes(request):
    return render(request, "cortes.html")

def contactanos(request):
    return render(request, "contactanos.html")


def registrar_contacto(request):
    print('REGISTRAR CONTACTO')

    message_error = ''
    message_success= ''
    if request.method =='POST':

        nombres = request.POST['nombres']
        apellido_paterno = request.POST['apellido_paterno']
        apellido_materno = request.POST['apellido_materno']
        email = request.POST['email']
        telefono = request.POST['telefono']
        asunto = request.POST['asunto']
        
        print('nombres: {0}'.format(nombres))
        print('apellido_paterno: {0}'.format(apellido_paterno))
        print('apellido_materno: {0}'.format(apellido_materno))
        print('email: {0}'.format(email))
        print('telefono: {0}'.format(telefono))
        print('asunto: {0}'.format(asunto))

        datosContacto = DatosContacto(nombres=nombres,
            apellido_pat=apellido_paterno, apellido_mat=apellido_materno,
            email=email, telefono=telefono,asunto=asunto)
        resultado = guardar(datosContacto)
        print('RESULTADO: {0}'.format(resultado))
        if resultado:
            message_success = 'DATOS GUARDADOS.'
        else:
            message_error = 'ERROR AL GUARDAR EL REGISTRO'
    else:
        print('METODO NO SOPORTADO')
    return render(request, "contactanos.html",
    {'message_error': message_error, 'message_success': message_success})

def quienessomos(request):
    return render(request, "quienessomos.html")

def clientes(request):

    print('BUSCAR DATOS CONTACTOS')
    datosContactos = buscarTodo()

    for dato in datosContactos:
        print(dato)

    return render(request, "clientes.html",{'datosContactos': datosContactos})    

def eliminar_contacto(request):
    print('ELIMINAR CONTACTO')

    if request.method == 'GET':

        id = request.GET['id']
        resultado = eliminar_por_id(id)

        if resultado:
            print('REGISTRO ELIMINADO CORRECTAMENTE.')

        else:
            print('REGISTRO NO SE PUDO ELIMINAR.')
    else:
        print('METODO NO SOPORTADO')

    datosContactos = buscarTodo()
    return render(request, "clientes.html", {'datosContactos': datosContactos})

def form_editar_contacto(request):
    print('EDITAR CONTACTO')
    resultado = []
    if request.method == 'GET':
        id = request.GET['id']
        resultado = buscar_por_id(id)

    return render(request, "edit-contactanos.html", {'contacto': resultado})

def actualizar_contacto(request):
    print  ('ACTUALIZAR CONTACTO')

    message_error = ''
    message_success = ''
    if request.method == 'POST': 
        id = request.POST['id']
        nombres = request.POST['nombres']
        apellido_paterno = request.POST['apellido_paterno']
        apellido_materno = request.POST['apellido_materno']
        email = request.POST['email']
        telefono = request.POST['telefono']
        asunto = request.POST['asunto']

        print('id: {0}'.format(id))
        print('nombres: {0}'.format(nombres))
        print('apellido_paterno: {0}'.format(apellido_paterno))
        print('apellido_materno: {0}'.format(apellido_materno))
        print('email: {0}'.format(email))
        print('telefono: {0}'.format(telefono))
        print('asunto: {0}'.format(asunto))

        datosContacto = DatosContacto(id=id, nombres=nombres,
            apellido_pat=apellido_paterno, apellido_mat=apellido_materno,
            email=email, telefono=telefono, asunto=asunto)
        resultado = actualizar(datosContacto)
        print('RESULTADO: {0}'.format(resultado))
        if resultado:
            message_success = 'DATOS ACTUALIZADOS.'
        else:
            message_error = 'ERROR AL ACTUALIZAR EL REGISTRO.'
    else:
        print('METODO NO SOPORTADO.')
    return render(request, "edit-contactanos.html", 
        {'message_error': message_error, 'message_success': message_success}) 

def autenticar(request):
    print('AUTENTICA CONTACTO')
    usuario = []
    if request.method == 'POST': 
        usuario = request.POST['usuario']
        password = request.POST['password']
        
        print('usuario: {0}'.format(usuario))
        print('password: {0}'.format(password))
        
        if usuario == 'ADMIN' and password == 'qwerty':
            print('AUTENTICACIÓN CORRECTA')           
            usuario = 'admin'
            request.COOKIES['username'] = usuario
            print('CREACIÓN VARIABLE DE SESION username')           
    
    return render(request, "index.html", {'username': usuario})

