from django.shortcuts import render, redirect
from .models import Entrada, Autor, Categoria
from .forms import EntradaForm, AutorForm, CategoriaForm, BuscarEntradasForm

def index(request):
    return render(request, 'blog/index.html')

def entrada_form(request):
    if request.method == 'POST':
        form = EntradaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_entradas')
    else:
        form = EntradaForm()
    return render(request, 'blog/entrada_form.html', {'form': form})

def autor_form(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AutorForm()
    return render(request, 'blog/autor_form.html', {'form': form})

def categoria_form(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CategoriaForm()
    return render(request, 'blog/categoria_form.html', {'form': form})

def buscar_entradas(request):
    entradas = None
    if request.method == 'POST':
        form = BuscarEntradasForm(request.POST)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            entradas = Entrada.objects.filter(titulo__icontains=titulo)
    else:
        form = BuscarEntradasForm()
    
    return render(request, 'blog/buscar_entradas.html', {
        'form': form,
        'entradas': entradas
    })

def lista_entradas(request):
    entradas = Entrada.objects.all().order_by('-fecha_publicacion')
    return render(request, 'blog/lista_entradas.html', {'entradas': entradas})