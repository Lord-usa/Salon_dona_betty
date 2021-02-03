# TAV 2021

## Conexion a bd
## Puerto en settings debe ser cambiado a 3306
## No olvidar


## COMANDOS PARA INSTALAR LIBRERIA DJANGO
python.exe -m pip install Django

## CREACIÓN DE PROYECTO WEB
django-admin startproject bazar_web

## DESPLEGAR APLICACIÓN WEB
python.exe .\manage.py runserver

## DESPLEGAR CON IP DE RED LOCAL
python.exe .\manage.py runserver  192.168.43.216:8000

## INSTALAR LIBRERIA PARA CONEXIÓN CON MYSQL
python.exe -m pip install mysqlclient

## INSPECCIÓN DB + CREACIÓN MODELS
python.exe .\manage.py inspectdb

## _______________________________________________________________________

## CREACIÓN PROYECTO WEB SERVICE 
django-admin startproject bazar_ws
## 
cd bazar_ws
## MODULO CONEXIÓN BASE DE DATOS
python.exe .\manage.py startapp persistencia
## INSTALAR LIBRERIA DJANGO REST FRAMEWORK
python.exe -m pip install djangorestframework
## _______________________________________________________________________

## MODULO CONEXIÓN BASE DE DATOS
python.exe .\manage.py startapp integracion

python.exe -m pip install requests

## _______________________________________________________________________

## AUTENTICACIÓN
python.exe .\manage.py startapp autenticacion

python.exe .\manage.py makemigrations autenticacion

python.exe .\manage.py migrate

python.exe .\manage.py createsuperuser

## ---------SUPER USUARIO SALON DOÑA BETTY-------------

Username : DnBetty
Email address: salondonabetty@beautysalon.cl
Password: salonbetty1999
