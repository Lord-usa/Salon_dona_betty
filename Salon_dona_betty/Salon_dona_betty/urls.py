"""Salon_dona_betty URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Salon_dona_betty.lib.views import home, cuidadocabello, cortes, contactanos, quienessomos, clientes, registrar_contacto, eliminar_contacto, form_editar_contacto, actualizar_contacto, autenticar, logout
from django.urls import path, include

urlpatterns = [
    path('',include('pwa.urls')),
    path('admin/', admin.site.urls),
    path('home/' , home),
    path('', home),
    path('cuidadocabello/', cuidadocabello),
    path('cortes/', cortes),
    path('contactanos/', contactanos),
    path('quienessomos', quienessomos),
    path('clientes/', clientes),
    path('registrar_contacto', registrar_contacto),
    path('eliminar-contacto/', eliminar_contacto),
    path('form-editar-contacto/', form_editar_contacto),
    path('actualizar-contacto', actualizar_contacto),
    path('login', autenticar),
    path('logout/', logout),
]
