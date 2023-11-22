from django.urls import path
from rest_api.views import lista_alumnos, detalle_alumno, lista_cursos, lista_profesores, lista_asistencias

urlpatterns = [
    path('alumnos/', lista_alumnos, name="Lista de Alumnos"),
    path('alumnos/<int:idAlumno>/', detalle_alumno, name="Detalle Alumno"),  
    path('cursos/', lista_cursos, name="Lista de Cursos"),
    path('profesores/', lista_profesores, name="Lista de Profesores"),
    path('asistencias/', lista_asistencias, name="Lista de Asistencias"),
]