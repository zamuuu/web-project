from django import forms

class VideoJuegosForm(forms.Form):
    nombre = forms.CharField(max_length=40)
    genero = forms.CharField(max_length=20)
    divertido = forms.BooleanField(required=False)

