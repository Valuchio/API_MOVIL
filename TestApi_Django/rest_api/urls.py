from django.urls import path
from rest_api.views import lista_alumnos, detalle_alumno,lista_profesores,detalle_profesor

urlpatterns=[
    path('alumnos', lista_alumnos, name="Lista de Alumnos"),
    path('alumno/<int:idAlumno>', detalle_alumno, name="Detalle Alumno"),
    path('profesores', lista_profesores, name="Lista de Profesores"),
    path('profesor/<int:idProfesor>', detalle_profesor, name="Detalle de profesores"),
]

