from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=500, null=True, blank=True)
    #contenido = models.TextField()
    #fecha_publicacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nombre
    
class Juego(models.Model):
    codigo_isbn = models.CharField(max_length=200, unique=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(null=True)
    #imagen = models.ImageField(upload_to='juegos/', null=True, blank=True)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE, related_name='juegos')
    
    def __str__(self):
        return self.nombre 
