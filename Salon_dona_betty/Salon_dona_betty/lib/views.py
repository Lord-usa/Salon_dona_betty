from django.http import HttpResponse, HttpResponseRedirect
from django.template import Template, Context 
from django.template.loader import get_template
from django.shortcuts import render 
from integracion.lib.cliente_datos_ws import buscarTodo, guardar, eliminar_por_id, buscar_por_id, actualizar
from django.contrib.auth import authenticate
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout


def home(request):
    usuario = request.user.username
    print('USERNAME: {0}'.format(usuario)) 
    print('LOGIN: {0}'.format(request.user.is_authenticated))     
    return render(request, "index.html",  {'username': usuario})

def cuidadocabello(request):
    usuario = request.user.username
    print('USERNAME: {0}'.format(usuario)) 
    print('LOGIN: {0}'.format(request.user.is_authenticated))
    return render(request, "cuidadocabello.html", {'username': usuario})

def cortes(request):
    usuario = request.user.username
    print('USERNAME: {0}'.format(usuario)) 
    print('LOGIN: {0}'.format(request.user.is_authenticated))
    return render(request, "cortes.html", {'username': usuario})

def contactanos(request):
    usuario = request.user.username
    print('USERNAME: {0}'.format(usuario)) 
    print('LOGIN: {0}'.format(request.user.is_authenticated))
    return render(request, "contactanos.html", {'username': usuario})


def registrar_contacto(request):
    usuario = request.user.username
    print('USERNAME: {0}'.format(usuario)) 
    print('LOGIN: {0}'.format(request.user.is_authenticated))

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

        datosContactoJson = {
                                'nombres': nombres,
                                'apellido-paterno': apellido_paterno,
                                'apellido-materno': apellido_materno,
                                'email': email,
                                'telefono': telefono,
                                'asunto': asunto,
                            }
        resultado = guardar(datosContactoJson)
        print('RESULTADO: {0}'.format(resultado))
        if resultado:
            message_success = 'DATOS GUARDADOS.'
        else:
            message_error = 'ERROR AL GUARDAR EL REGISTRO.'
    else:
        print('METODO NO SOPORTADO.')
    return render(request, "contactanos.html",
    {'message_error': message_error, 'message_success': message_success, 'username': usuario})

def quienessomos(request):
    usuario = request.user.username
    print('USERNAME: {0}'.format(usuario)) 
    print('LOGIN: {0}'.format(request.user.is_authenticated))
    return render(request, "quienessomos.html", {'username': usuario})

def clientes(request):
    usuario = request.user.username
    print('USERNAME: {0}'.format(usuario)) 
    print('LOGIN: {0}'.format(request.user.is_authenticated))

    print('BUSCAR DATOS CONTACTOS')
    datosContactos = buscarTodo()

    for dato in datosContactos:
        print(dato)

    return render(request, "clientes.html",{'datosContactos': datosContactos, 'username': usuario})    

def eliminar_contacto(request):
    usuario = request.user.username
    print('USERNAME: {0}'.format(usuario)) 
    print('LOGIN: {0}'.format(request.user.is_authenticated))

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
    return render(request, "clientes.html", {'datosContactos': datosContactos, 'username': usuario})

def form_editar_contacto(request):
    usuario = request.user.username
    print('USERNAME: {0}'.format(usuario)) 
    print('LOGIN: {0}'.format(request.user.is_authenticated))

    print('EDITAR CONTACTO')
    resultado = []
    if request.method == 'GET':
        id = request.GET['id']
        resultado = buscar_por_id(id)

    return render(request, "edit-contactanos.html", {'contacto': resultado, 'username': usuario})

def actualizar_contacto(request):
    usuario = request.user.username
    print('USERNAME: {0}'.format(usuario)) 
    print('LOGIN: {0}'.format(request.user.is_authenticated))

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

        datosContactoJson = {
                                'id': id,
                                'nombres': nombres,
                                'apellido-paterno': apellido_paterno,
                                'apellido-materno': apellido_materno,
                                'email': email,
                                'telefono': telefono,
                                'asunto': asunto,
                            }
        resultado = guardar(datosContactoJson)
        print('RESULTADO: {0}'.format(resultado))
        if resultado:
            message_success = 'DATOS GUARDADOS.'
        else:
            message_error = 'ERROR AL GUARDAR EL REGISTRO.'
    else:
        print('METODO NO SOPORTADO.')
    return render(request, "edit-contactanos.html", 
        {'message_error': message_error, 'message_success': message_success, 'username': usuario}) 

def autenticar(request):
    usuario = request.user.username
    print('USERNAME: {0}'.format(usuario)) 
    print('LOGIN: {0}'.format(request.user.is_authenticated))

    print('AUTENTICA CONTACTO')
    usuario = []
    if request.method == 'POST': 
        usuario = request.POST['usuario']
        password = request.POST['password']
        
        print('usuario: {0}'.format(usuario))
        print('password: {0}'.format(password))
        
        user = authenticate(username=usuario, password=password)

        if user is not None:
            print('AUTENTICACIÓN CORRECTA')           
            do_login(request, user)
        else:
            print('USUARIO O CONTRASEÑAS INCORRECTOS')           
    
    return render(request, "index.html", {'username': usuario})

def logout(request):
    do_logout(request)
    request.user.username = None
    return HttpResponseRedirect('/home')