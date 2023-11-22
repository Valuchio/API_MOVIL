from rest_framework import serializers
from core.models import Alumno
from core.models import Profesor
from core.models import Asistencia
from core.models import Curso
class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = ['idAlumno', 'Gmail', 'Contrasena', 'nombreAlumno','rol']

class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = ['idProfesor', 'Gmail', 'Contrasena', 'nombreProfesor']

class AsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = ['alumno', 'curso', 'fecha', 'presente']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ['nombre', 'codigo', 'seccion', 'alumnos']