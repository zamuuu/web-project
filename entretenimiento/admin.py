from django.contrib import admin

from entretenimiento.models import Peliculas, Series, VideoJuegos

# Register your models here.

admin.site.register(VideoJuegos)
admin.site.register(Series)
admin.site.register(Peliculas)