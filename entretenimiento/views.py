from django.shortcuts import redirect, render
from .models import VideoJuegos, Peliculas
from .forms import VideoJuegosForm, PeliculasForm

def videojuego(request):
    return render(request, 'entretenimiento/videojuego.html', {})


def crear_videojuego(request):
    
    if request.method == 'POST':
        form = VideoJuegosForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            videojuego = VideoJuegos(nombre=data['nombre'], genero=data['genero'], divertido=data['divertido'])
            videojuego.save()
            return redirect('index')
        
    context = {'form': VideoJuegosForm}
    return render(request, 'entretenimiento/crear_videojuego.html', context)



def pelicula(request):
    return render(request, 'entretenimiento/pelicula.html', {})


def crear_pelicula(request):
    
    if request.method == 'POST':
        form = PeliculasForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            pelicula = Peliculas(nombre=data['nombre'], categoria=data['categoria'], divertida=data['divertida'])
            pelicula.save()
            return redirect('index')
        
    context = {'form': PeliculasForm}
    return render(request, 'entretenimiento/crear_pelicula.html', context)


def pelicula(request):
    return render(request, 'entretenimiento/pelicula.html', {})


def crear_pelicula(request):
    
    if request.method == 'POST':
        form = PeliculasForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            pelicula = Peliculas(nombre=data['nombre'], categoria=data['categoria'], divertida=data['divertida'])
            pelicula.save()
            return redirect('index')
        
    context = {'form': PeliculasForm}
    return render(request, 'entretenimiento/crear_pelicula.html', context)