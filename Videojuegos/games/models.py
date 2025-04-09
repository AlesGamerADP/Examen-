from django.db import models

# Create your models here.

class requerimientos_sistema(models.Model):
    sistema = models.CharField(max_length=100)
    procesador = models.CharField(max_length=100)
    memoria = models.CharField(max_length=50)
    grafica = models.CharField(max_length=100)
    almacenamiento = models.CharField(max_length=50)

    def __str__(self):
        return self.sistema

class games(models.Model):
    titulo = models.CharField(max_length=255)
    estado = models.CharField(max_length=50)
    imagen = models.URLField()
    descripcion_pequeña = models.CharField(max_length=200)
    descricpcion = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    editor = models.CharField(max_length=255)
    fecha = models.DateField()
    game_url = models.URLField(blank=True, null=True)
    requerimientos_sistema = models.OneToOneField(requerimientos_sistema, on_delete=models.CASCADE, related_name='game')

    def __str__(self):
        return self.titulo
