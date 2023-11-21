from django.db import models
from django.utils import timezone


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

class Profesor(models.Model):
   
    idProfesor = models.IntegerField(primary_key=True, verbose_name="Id de Usuario")
    Gmail = models.CharField(max_length=50, verbose_name="Gmail")
    Contrasena = models.CharField(max_length=50, verbose_name="Contrasena")
    nombreProfesor = models.CharField(max_length=50, verbose_name="Nombre de Usuario")


    def __str__(self):
        return self.nombreProfesor


class Asistencia(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    curso = models.ForeignKey('Curso', on_delete=models.CASCADE)
    fecha = models.DateField(default=timezone.now)
    presente = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.alumno} - {self.curso} - {self.fecha}"

class Curso(models.Model):
    nombre = models.CharField(max_length=255)
    codigo = models.CharField(max_length=255)
    seccion = models.CharField(max_length=255)
    alumnos = models.ManyToManyField('Alumno', related_name='cursos')

    def __str__(self):
        return self.nombre