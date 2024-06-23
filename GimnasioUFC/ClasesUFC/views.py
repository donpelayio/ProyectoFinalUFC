from django.shortcuts import render
from ClasesUFC.models import *
from ClasesUFC.forms import *

# Create your views here.

def inicio (request):
    return render(request,"ClasesUFC/inicio.html")

def login (request):
    return render(request,"ClasesUFC/login.html")

def logout (request):
    return render(request,"ClasesUFC/logout.html")

def clases (request):
    return render(request,"ClasesUFC/clases.html")

def register(request):
    
    if request.method == 'POST':
        
        miformulario= FormularioAlumnos(request.POST)
        print(miformulario)
        
        if miformulario.is_valid:
            
            informacion = miformulario.cleaned_data
            alumno = Alumno(nombre=informacion['nombre'],apellido=informacion['apellido'],email=informacion['email'],edad=informacion['edad'])
            alumno.save()
            return render(request, "ClasesUFC/inicio.html",)
        
    else:
        miformulario = FormularioAlumnos()
        
    return render(request,"ClasesUFC/register.html", {"miformulario":miformulario})