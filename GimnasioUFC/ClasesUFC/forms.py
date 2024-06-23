from django import forms

class FormularioAlumnos(forms.Form):
    nombre=forms.CharField()
    apellido=forms.CharField()
    email=forms.EmailField()
    edad=forms.IntegerField()
    #horario=forms.ModelMultipleChoiceField()
    
    
    