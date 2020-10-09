import random
import string
from django.shortcuts import render

# Create your views here.
from .models import Sesiones
from docente.models import Docente
from estudiante.models import Estudiante
from .serializers import ItemSesion
from docente.serializers import CargarDocenteSesion
from estudiante.serializers import CargarEstudianteSesion
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def iniciar_sesion(request):
    """
    List all code Usuarios, or create a new Estudiante.
    """
    print(request.data)
    if request.data['rol'] == 2:
        print("Entró a docente")
        try:
            usuario = Docente.objects.get(idInicioSesion=request.data['username'], contrasena=request.data['password'])
        except Docente.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        """ serializerDocente = CargarDocenteSesion(docente, context={'request': request})
        usuario = serializerDocente.data """
    if request.data['rol'] == 3:
        try:
            usuario = Estudiante.objects.get(idInicioSesion=request.data['username'], contrasena=request.data['password'])
        except Estudiante.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        """ serializerEstudiante = CargarEstudianteSesion(estudiante, context={'request': request})
        usuario = serializerEstudiante.data """
    print(usuario)
    try:
        sesion = Sesiones.objects.get(rol=request.data['rol'], idUsuario=usuario.id)
        serializerSesion = ItemSesion(sesion)
        return Response(serializerSesion.data, status=status.HTTP_200_OK)
    except Sesiones.DoesNotExist:
        token = get_random_string(20)
        serializerSesion = ItemSesion(data={
            'token': token,
            'rol': request.data['rol'],
            'idUsuario': usuario.id
        })
        if serializerSesion.is_valid():
            serializerSesion.save()
            return Response(serializerSesion.data, status=status.HTTP_201_CREATED)
        print(serializerSesion.errors)
        return Response(serializerSesion.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def cerrar_sesion(request):
    """
    List all code Usuarios, or create a new Estudiante.
    """
    try:
        sesion = Sesiones.objects.get(token=request.data['token'])
        sesion.delete()
        return Response({}, status=status.HTTP_200_OK)
    except Sesiones.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

def get_random_string(length):
    # Random string with the combination of lower and upper case
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str