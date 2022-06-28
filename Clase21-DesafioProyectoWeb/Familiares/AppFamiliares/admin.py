from django.contrib import admin
from  .models import * #importamos el archivo models
# Register your models here.

#registramos los modelos

admin.site.register(Familiares)

admin.site.register(Amigos)

admin.site.register(Mascotas)