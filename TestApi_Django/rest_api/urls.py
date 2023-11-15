from django.urls import path
from rest_api.views import lista_alumnos, detalle_alumno

urlpatterns=[
    path('alumnos', lista_alumnos, name="Lista de Alumnos"),
    path('alumno/<int:idAlumno>', detalle_alumno, name="Detalle Alumno"),
]