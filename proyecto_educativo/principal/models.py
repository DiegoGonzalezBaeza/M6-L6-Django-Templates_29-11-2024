from django.db import models

# Create your models here.
class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(unique=True)
    edad = models.IntegerField()
    fecha_registro = models.DateTimeField(auto_now_add=True)

# Funcion de retorno para mostrar _ lo ve el superusuario (admin) en la vista
    def __str__(self):
        return f"{self.nombre} {self.apellido}"