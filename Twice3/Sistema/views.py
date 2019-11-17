from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
# Correos
from django.core.mail import send_mail
# Validaciones
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
# Importacion de Modelos
from .models import Persona
# Importacion de Formularios
from .forms import RegistrarPersonaForm, LoginForm

# Create your views here.

#------------------------------------------ INDEX ------------------------------------------
def index(request):
    plantilla=loader.get_template("index.html")
    return HttpResponse(plantilla.render({'titulo':"Twice"},request))

# ------------------------------------------ FORMULARIOS ------------------------------------------
# Registro de Personas (DESDE FUERA DEL SISTEMA, USUARIOS NUEVOS)
def registroPersona(request):
    mensaje=""
    registro=1 #Dependiendo este número, es el Formulario que Mostrará
    personas=Persona.objects.all()
    form=RegistrarPersonaForm(request.POST or None)
    if form.is_valid():
        data=form.cleaned_data
        new=User.objects.create_user(data.get("UsuPersona"),data.get("mailPersona"),data.get("passwordPersona"))
        new.is_staff=False
        new.save()
        regDB=Persona(usuario=new,nombrePersona=data.get("nombrePersona"),fechaNacimiento=data.get("fechaNacimiento"))
        regDB.save()
        mensaje='Usuario '+regDB.nombrePersona+' Registrado'
    form=RegistrarPersonaForm()
    return render(request,"registro.html",{'form':form,'personas':personas,'registro':registro,'titulo':"Registro",'mensaje':mensaje})

@login_required(login_url='login')
def album(request):
    plantilla=loader.get_template("album.html")
    return HttpResponse(plantilla.render({'titulo':"Twice"},request))

# Login
def ingreso(request):
    mensaje=""
    form=LoginForm(request.POST or None)
    if form.is_valid():
        data=form.cleaned_data
        user=authenticate(username=data.get("username"),password=data.get("password"))
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            mensaje='Datos Invalidos'
    return render(request,"login.html",{'form':form,'titulo':"Login",'mensaje':mensaje})

# Logout
def salir(request):
    logout(request)
    return redirect('/index/')

@login_required(login_url='login')
def integrantes(request):
    plantilla=loader.get_template("integrantes.html")
    return HttpResponse(plantilla.render({'titulo':"Twice"},request))

@login_required(login_url='login')
def backstage(request):
    plantilla=loader.get_template("backstage.html")
    return HttpResponse(plantilla.render({'titulo':"Twice"},request))