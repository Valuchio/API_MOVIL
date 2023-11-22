from rest_framework import serializers
from core.models import Alumno, Asistencia, Profesor,Curso

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):
    alumnos = AlumnoSerializer(many=True, read_only=True)

    class Meta:
        model = Curso
        fields = '__all__'

class AsistenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = '__all__'

class ProfesorSerializer(serializers.ModelSerializer):
    cursos = CursoSerializer(many=True, read_only=True)

    class Meta:
        model = Profesor
        fields = '__all__'