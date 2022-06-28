from django import forms

class AmigosFormulario (forms.Form):
    #Especificamos los campos

    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length= 50)
    email = forms.EmailField(max_length=50)
    Nacionalidad = forms.CharField(max_length= 50)
    edad = forms.IntegerField()

class FamiliaresFormulario (forms.Form):

    tipo = forms.CharField(max_length= 30)
    nombre = forms.CharField(max_length= 50)
    apellido = forms.CharField(max_length= 50)
    fecha_nacimiento = forms.DateField()
    edad = forms.IntegerField()

class MascotasFormulario (forms.Form):
    
    nombre = forms.CharField(max_length= 50)
    tipo = forms.CharField(max_length= 30)
    