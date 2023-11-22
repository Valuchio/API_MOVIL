from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Alumno
from .serializers import AlumnoSerializer
from core.models import Profesor
from .serializers import ProfesorSerializer
# Create your views here.
@csrf_exempt
@api_view(['GET'])
def lista_alumnos(request):
    alumnos = Alumno.objects.all()
    serializer = AlumnoSerializer(alumnos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def detalle_alumno(request, idAlumno):
    try:
        alumno = Alumno.objects.get(idAlumno=idAlumno)
    except Alumno.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = AlumnoSerializer(alumno)
    return Response(serializer.data)

@csrf_exempt
@api_view(['GET'])
def lista_profesores(request):
    profesores = Profesor.objects.all()
    serializer = ProfesorSerializer(profesores, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def detalle_profesor(request, idProfesor):
    try:
        profesor = Profesor.objects.get(idProfesor=idProfesor)
    except Profesor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ProfesorSerializer(profesor)
    return Response(serializer.data)