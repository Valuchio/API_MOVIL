from django.db import models

# Create your models here.
class Alumno(models.Model):
    ROLES_CHOICES = [
        ('alumno', 'Alumno'),
        ('profesor', 'Profesor'),
    ]

    idAlumno = models.IntegerField(primary_key=True, verbose_name="Id de Usuario")
    Gmail = models.CharField(max_length=50, verbose_name="Gmail")
    Contrasena = models.CharField(max_length=50, verbose_name="Contrasena")
    nombreAlumno = models.CharField(max_length=50, verbose_name="Nombre de Usuario")
    rol = models.CharField(max_length=10, choices=ROLES_CHOICES, default='alumno', verbose_name="Rol")

    def __str__(self):
        return f"{self.nombreAlumno} - {self.rol}"

