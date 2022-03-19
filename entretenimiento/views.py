from django.shortcuts import redirect, render
from .models import VideoJuegos
from .forms import VideoJuegosForm


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
