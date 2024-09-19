from django.db import models


# Create your models here.
class tareas(models.Model):   
    titulo=models.CharField(max_length=200)
    fecha_vencimiento=models.DateField()
    correo=models.CharField(max_length=300)
    estado_choices=[
        ('Finalizada','Finalizada'),
        ('pendiente', 'pendiente'),
        ('vencida','vencida'),
        ('terminada/vencida','terminada/vencida')
    ]
    Estado = models.CharField( max_length=20, choices=estado_choices)

def __str__(self):
        return self.titulo 