from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Alumno , Curso, Profesor,  Asistencia
from .serializers import AlumnoSerializer, CursoSerializer, ProfesorSerializer, AsistenciaSerializer

# Create your views here.
@csrf_exempt

@api_view(['GET'])
def lista_alumnos(request):
    alumnos = Alumno.objects.all()
    serializer = AlumnoSerializer(alumnos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detalle_alumno(request, idAlumno):
    alumno = get_object_or_404(Alumno, id=idAlumno)
    serializer = AlumnoSerializer(alumno)
    return Response(serializer.data)

@api_view(['GET'])
def lista_cursos(request):
    cursos = Curso.objects.all()
    serializer = CursoSerializer(cursos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def lista_profesores(request):
    profesores = Profesor.objects.all()
    serializer = ProfesorSerializer(profesores, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def lista_asistencias(request):
    asistencias = Asistencia.objects.all()
    serializer = AsistenciaSerializer(asistencias, many=True)
    return Response(serializer.data)