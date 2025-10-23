from django.contrib import admin
from .models import Entrada, Autor, Categoria

admin.site.register(Entrada)
admin.site.register(Autor)
admin.site.register(Categoria)