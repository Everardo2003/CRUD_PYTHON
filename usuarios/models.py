from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'usuarios'  

