from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from AppFamiliares.forms import AmigosFormulario, FamiliaresFormulario, MascotasFormulario
from AppFamiliares.models import Familiares, Amigos, Mascotas

# Create your views here.

def inicio_v1(request):

      return render(request, "inicio_v1.html")


# --- Amigos ----
def amigos (request):
    personas = Amigos.objects.all()
    context  = {"amigos":personas}
    return render(request,"amigos.html",context)  # Retorna el HTML amigos

def amigosformulario (request):
    if request.method == 'POST':

        miFormulario = AmigosFormulario(request.POST) # Le llega todas la informacion del html

        print(miFormulario)

        if miFormulario.is_valid:   #Si paso la validacion de Django
            informacion = miFormulario.cleaned_data  #presenta la informacion como un diccionario, a la variable informacion
            
            amigo = Amigos(nombre = informacion['nombre'],apellido = informacion['apellido'],email=informacion['email'],Nacionalidad=informacion['Nacionalidad'],edad=informacion['edad'])
        
            amigo.save()
            
            #return render(request,"inicio_v1.html")
            return render(request,"amigos.html")
    else:
        miFormulario = AmigosFormulario()  #Formulario vacion para construir el html
    
    return render(request,"amigosFormulario.html",{"miFormulario":miFormulario}) #Envia a la pagina HTML, con el formulario vacio

def amigosbuscar (request):
  if  request.GET["mombre"]: #if request.method == 'Get':

	    #respuesta = f"Estoy buscando la camada nro: {request.GET['camada'] }" 
        nombreamigo = request.GET['nombre'] 
        print(nombreamigo)
        amigos = Amigos.objects.filter(nombre__icontains=nombreamigo)
        print(amigos)
        #return render(request, "amigosbuscar.html", {"amigos":amigos})
        return render(request, "amigosbuscar.html", {"nombre":nombreamigo})
  else: 
    respuesta = "No enviaste datos"
    #No olvidar from django.http import HttpResponse
  return render(request,"inicio_v1.html", {"respuesta":respuesta})

# --- FAMILIARES ----
def familiares1 (request):
    personas = Familiares.objects.all()
    context  = {"familiares":personas}
    return render(request,"familiares.html",context)  # Retorna el HTML familiares

def familiaresformulario (request):
    if request.method == 'POST':

        miFormulario = FamiliaresFormulario(request.POST) # Le llega todas la informacion del html

        print(miFormulario)

        if miFormulario.is_valid:   #Si paso la validacion de Django
            informacion = miFormulario.cleaned_data  #presenta la informacion como un diccionario, a la variable informacion
            
            familiar = Familiares(tipo = informacion['tipo'],nombre = informacion['nombre'],apellido = informacion['apellido'],fecha_nacimiento=informacion['fecha_nacimiento'],edad=informacion['edad'])
        
            familiar.save()

            return render(request,"familiares.html")
    else:
        miFormulario = FamiliaresFormulario()  #Formulario vacion para construir el html
    
    return render(request,"familiaresFormulario.html",{"miFormulario":miFormulario}) #Envia a la pagina HTML, con el formulario vacio

def familiarbuscar (request):
  if  request.GET["mombre"]: #if request.method == 'Get':

	    #respuesta = f"Estoy buscando la camada nro: {request.GET['camada'] }" 
        nombrefamiliar = request.GET['nombre'] 
        print(nombrefamiliar)
        familiares = Familiares.objects.filter(nombre__icontains=nombrefamiliar)
        print(familiares)
        return render(request, "familiaresbuscar.html", {"familiares":familiares})
  else: 
    respuesta = "No enviaste datos"
    #No olvidar from django.http import HttpResponse
  return render(request,"inicio_v1.html", {"respuesta":respuesta})


  # --- Mascotas ----
def mascotas (request):
    mascota = Mascotas.objects.all()
    context  = {"mascotas":mascota}
    return render(request,"mascotas.html",context)  # Retorna el HTML mascotas

def mascotasformulario (request):
    if request.method == 'POST':

        miFormulario = MascotasFormulario(request.POST) # Le llega todas la informacion del html

        print(miFormulario)

        if miFormulario.is_valid:   #Si paso la validacion de Django
            informacion = miFormulario.cleaned_data  #presenta la informacion como un diccionario, a la variable informacion
            
            mascota = Mascotas(nombre = informacion['nombre'],Tipo = informacion['tipo'],)
        
            mascota.save()

            return render(request,"mascotas.html")
    else:
        miFormulario = MascotasFormulario()  #Formulario vacion para construir el html
    
    return render(request,"mascotasFormulario.html",{"miFormulario":miFormulario}) #Envia a la pagina HTML, con el formulario vacio

def mascotabuscar (request):
  if  request.GET['serch']: #if request.method == 'Get':

	    #respuesta = f"Estoy buscando la camada nro: {request.GET['camada'] }" 
        nombremascota = request.GET['serch'] 
        print(nombremascota)
        mascotas = Mascotas.objects.filter(nombre__icontains=nombremascota)
        print(mascotas)
        contexto = {"mascotas":mascotas}
        #return render(request, "mascotabuscar.html", {"nombre":nombremascota,"tipo":mascotas})
        return render(request, "mascotabuscar.html", context = contexto)
  else: 
    respuesta = "No enviaste datos"
    #No olvidar from django.http import HttpResponse
  return render(request,"inicio_v1.html", {"respuesta":respuesta})