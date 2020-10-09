from django.shortcuts import render

# Create your views here.
from .models import Estudiante
from .serializers import ListaEstudiantes, NuevoEstudiante, CargarEstudiante
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def estudiantes_manager(request):
    """
    List all code Usuarios, or create a new Estudiante.
    """
    if request.method == 'GET':
        estudiantes = Estudiante.objects.all()
        serializer = ListaEstudiantes(estudiantes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializerGuardar = NuevoEstudiante(data=request.data)
        if serializerGuardar.is_valid():
            serializerGuardar.save()
            estudiantes = Estudiante.objects.all()
            serializerDatos = ListaEstudiantes(estudiantes, many=True)
            return Response(serializerDatos.data, status=status.HTTP_201_CREATED)
        return Response(serializerGuardar.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'PUT', 'DELETE'])
def estudiante_manager(request, pk):
    """
    List all code Usuarios, or create a new Estudiante.
    """
    try:
        estudiante = Estudiante.objects.get(pk=pk)
    except Estudiante.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CargarEstudiante(estudiante, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CargarEstudiante(estudiante, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            estudiantes = Estudiante.objects.all()
            serializerDatos = ListaEstudiantes(estudiantes, many=True)
            return Response(serializerDatos.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        estudiante.delete()
        estudiantes = Estudiante.objects.all()
        serializer = ListaEstudiantes(estudiantes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    

    """ permission_classes = (Check_API_KEY_Auth,)

    def get(self, request, format=None):
        content = {
            'status': 'request was permitted'
        }
        return Response(content) """