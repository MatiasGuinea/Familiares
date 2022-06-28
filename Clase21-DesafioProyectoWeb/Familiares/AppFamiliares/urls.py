from django.contrib import admin
from django.urls import path
from AppFamiliares.models import Familiares, Amigos, Mascotas
from AppFamiliares.views  import familiaresformulario, familiares1, inicio_v1,amigos,amigosformulario,amigosbuscar,mascotas, mascotasformulario, mascotabuscar

urlpatterns = [
  #  path('admin/', admin.site.urls),
    #path('familiar/', familiar),
   # path('ListadoFamiliares/', probandoTemplateMejorado),
    #path('Listado/', lista_familiares),
    #path('Listado1/', lista_familiares1),
    #path('agregarfamiliares/', familiares1),
    #path('', views.inicio), #esta era nuestra primer view
    #path('', inicio), #esta era nuestra primer view
    path('', inicio_v1,name= "Inicio"), #esta era nuestra primer view
    path('familiares/', familiares1,name= "Familiares"), 
    path('familiares/familiaresformulario/', familiaresformulario), 
    path('amigos/', amigos,name= "Amigos"), 
    path('amigos/amigosformulario/', amigosformulario), 
    path('mascotas/', mascotas,name= "Mascotas"), 
    path('mascotas/mascotasformulario/', mascotasformulario), 
    path('mascotas/buscar/', mascotabuscar,name= "Mascotasbuscar"), 
    #path('familiares_listado/', lista_familiares,name= "Listado_Familiares"), 
]