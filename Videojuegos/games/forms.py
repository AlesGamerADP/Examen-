from django import forms
from .models import games,requerimientos_sistema



class RequerimientosFrom():
    class Meta:
        model = requerimientos_sistema
        fields = ['sistema', 'procesador', 'memoria','grafica', 'almacenamiento']

class GamesForm(forms.ModelForm):
    class Meta:
        model = games
        fields = ['titulo', 'estado', 'imagen', 'descripcion_pequeña', 'descricpcion', 'genero', 'editor', 'fecha', 'game_url', 'requerimientos_sistema']
