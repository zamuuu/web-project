from django.urls import path
from . import views

urlpatterns = [
    path('videojuego/', views.videojuego, name='videojuego'),
    path('videojuegos/crear',views.crear_videojuego, name='crear_videojuego'),
    path('pelicula/', views.pelicula, name='pelicula'),
    path('peliculas/crear', views.crear_pelicula, name='crear_pelicula'),
    # path('',, name='buscar_videojuego'),
]
