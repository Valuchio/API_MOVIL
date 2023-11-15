from rest_framework import serializers
from core.models import Alumno

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = ['idAlumno', 'Gmail', 'Contrasena', 'nombreAlumno']