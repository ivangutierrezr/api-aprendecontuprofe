from django.shortcuts import render

# Create your views here.
from .models import Asignatura
from docente.models import Docente
from estudiante.models import Estudiante
from sesiones.models import Sesiones
from .serializers import ListaAsignaturas, NuevaAsignatura, CargarAsignatura
from docente.serializers import ListaDocentes, CargarDocente
from estudiante.serializers import ListaEstudiantes, CargarEstudiante
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def asignaturas_manager(request):
    """
    List all code Usuarios, or create a new Asignatura.
    """
    if request.method == 'GET':
        asignaturas = Asignatura.objects.all()
        serializer = ListaAsignaturas(asignaturas, many=True)
        docentes = Docente.objects.all()
        serializerDocentes = ListaDocentes(docentes, many=True)
        estudiantes = Estudiante.objects.all()
        serializerEstudiantes = ListaEstudiantes(estudiantes, many=True)
        datos = {
            "asignaturas": serializer.data,
            "docentes": serializerDocentes.data,
            "estudiantes": serializerEstudiantes.data
        }
        return Response(datos)

    elif request.method == 'POST':
        serializerGuardar = NuevaAsignatura(data=request.data)
        if serializerGuardar.is_valid():
            serializerGuardar.save()
            asignaturas = Asignatura.objects.all()
            serializerDatos = ListaAsignaturas(asignaturas, many=True)
            return Response(serializerDatos.data, status=status.HTTP_201_CREATED)
        print(serializerGuardar.errors)
        return Response(serializerGuardar.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def asignatura_manager(request, pk):
    """
    List all code Usuarios, or create a new Asignatura.
    """
    try:
        asignatura = Asignatura.objects.get(pk=pk)
    except Asignatura.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CargarAsignatura(asignatura, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CargarAsignatura(asignatura, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            asignaturas = Asignatura.objects.all()
            serializerDatos = ListaAsignaturas(asignaturas, many=True)
            return Response(serializerDatos.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        asignatura.delete()
        asignaturas = Asignatura.objects.all()
        serializer = ListaAsignaturas(asignaturas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def asignatura_manager_estudiantes(request, pk):
    """
    List all code Usuarios, or create a new Asignatura.
    """
    try:
        asignatura = Asignatura.objects.get(pk=pk)
    except Asignatura.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CargarAsignatura(asignatura, context={'request': request})
        estudiantes = []
        if len(asignatura.estudiantes) > 0:
            for estudiante in asignatura.estudiantes:
                newEstudiante = Estudiante.objects.get(pk=estudiante)
                serializerEst = ListaEstudiantes(newEstudiante)
                estudiantes.append(serializerEst.data)
        docente = Docente.objects.get(pk=asignatura.docente)
        serializerDoc = ListaDocentes(docente)
        datos = {
            "asignatura": serializer.data,
            "estudiantes": estudiantes,
            "docente": serializerDoc.data,
        }
        return Response(datos)
        
@api_view(['GET', 'POST'])
def asignaturas_usuario(request):
    """
    List all code Usuarios, or create a new Asignatura.
    """
    print(request.data)
    try:
        sesion = Sesiones.objects.get(token=request.data['token'])
    except Sesiones.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    rol = int(sesion.rol)
    idUsuario = int(sesion.idUsuario)
    if rol == 1: 
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    if request.method == 'POST':
        if rol == 2:
            asignaturas = list(Asignatura.objects.filter(docente=idUsuario).order_by('pk'))
            serializer = ListaAsignaturas(asignaturas, many=True)
            docente = Docente.objects.get(pk=idUsuario)
            serializerDocente = CargarDocente(docente, context={'request': request})
            datos = {
                "asignaturas": serializer.data,
                "usuario": serializerDocente.data,
                "rol": rol,
            }
            return Response(datos, status=status.HTTP_200_OK)            
        elif rol == 3:
            asignaturas = list(Asignatura.objects.filter(estudiantes__contains=[idUsuario]).order_by('pk'))
            serializer = ListaAsignaturas(asignaturas, many=True)
            estudiante = Estudiante.objects.get(pk=idUsuario)
            serializerEstudiante = CargarEstudiante(estudiante, context={'request': request})
            datos = {
                "asignaturas": serializer.data,
                "usuario": serializerEstudiante.data,
                "rol": rol,
            }
            return Response(datos, status=status.HTTP_200_OK)

@api_view(['PUT'])
def items_asignatura(request, pk):
    """
    List all code Usuarios, or create a new Asignatura.
    """
    print(request.data)
    pos = request.data['pos']
    try:
        asignatura = Asignatura.objects.get(pk=pk)
    except Asignatura.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        if request.data['tipo'] == 1:
            asignatura.introduccion = request.data['introduccion']
        if request.data['tipo'] == 2:
            asignatura.clases.append({
                'texto': '<p><br></p>',
            })
        if request.data['tipo'] == 3:
            asignatura.clases[pos]['texto'] = request.data['texto']
        if request.data['tipo'] == 4:
            del asignatura.clases[pos]
        if request.data['tipo'] == 5:
            asignatura.foro.append({
                'title': request.data['title'],
                'date': request.data['date'],
                'post': request.data['post'],
                'replicas': []
            })
        if request.data['tipo'] == 6:
            del asignatura.foro[pos]
        if request.data['tipo'] == 7:
            asignatura.foro[pos]['replicas'].append({
                'autor': request.data['autor'],
                'comentario': request.data['comentario'],
                'fecha': request.data['fecha'],
                'rol': request.data['rol'],
            })
        if request.data['tipo'] == 8:
            posC = request.data['posC']
            del asignatura.foro[pos]['replicas'][posC]
        asignatura.save()
        serializer = CargarAsignatura(asignatura, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)