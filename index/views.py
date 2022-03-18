from django.shortcuts import render

def index(request):
    return render(request, 'index/index.html', {})

def about(request):
    
    datos = {
        'lista': ['primero', 'segundo', 'tercero'],
        'nombre': 'Juancho',
        'apellido': 'Fort'
    }
    
    return render(request, 'index/about.html', datos)