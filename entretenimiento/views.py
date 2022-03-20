from django.shortcuts import redirect, render
from .models import VideoJuegos, Peliculas, Series
from .forms import VideoJuegosForm, PeliculasForm, SeriesForm, VideoJuegosBusqueda


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

def lista_videojuegos(request):
    
    nombre_a_buscar = request.GET.get('nombre', None)
    
    if nombre_a_buscar is not None:
        videojuegos = VideoJuegos.objects.filter(nombre__icontains = nombre_a_buscar)
    else:
        videojuegos = VideoJuegos.objects.all()
    
    form = VideoJuegosBusqueda()
    return render(request, 'entretenimiento/lista_videojuegos.html', {'form': form, 'videojuegos': videojuegos})


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


def serie(request):
    return render(request, 'entretenimiento/serie.html', {})

def crear_serie(request):
    
    if request.method == 'POST':
        form = SeriesForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            serie = Series(nombre=data['nombre'], categoria=data['categoria'], divertida=data['divertida'])
            serie.save()
            return redirect('index')
        
    context = {'form': SeriesForm}
    return render(request, 'entretenimiento/crear_serie.html', context)