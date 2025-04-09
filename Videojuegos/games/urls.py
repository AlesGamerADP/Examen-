from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_juegos, name='lista_juegos'),  # Cambié 'lista_personajes' por 'lista_juegos'
    path('juego/<int:id>/', views.detalle_juego, name='detalle_juego'),
    path('crear/', views.crear_juego, name='crear_juego'),
    path('editar/<int:id>/', views.editar_juego, name='editar_juego'),
    path('eliminar/<int:id>/', views.eliminar_juego, name='eliminar_juego'),
]