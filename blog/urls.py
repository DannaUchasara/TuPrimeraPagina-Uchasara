from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('entrada/nueva/', views.entrada_form, name='entrada_form'),
    path('autor/nuevo/', views.autor_form, name='autor_form'),
    path('categoria/nueva/', views.categoria_form, name='categoria_form'),
    path('buscar/', views.buscar_entradas, name='buscar_entradas'),
    path('entradas/', views.lista_entradas, name='lista_entradas'),
]