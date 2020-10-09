from django.shortcuts import render

# Create your views here.
from .models import Docente
from .serializers import ListaDocentes, NuevoDocente, CargarDocente
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def docentes_manager(request):
    """
    List all code Usuarios, or create a new Docente.
    """
    if request.method == 'GET':
        docentes = Docente.objects.all()
        serializer = ListaDocentes(docentes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializerGuardar = NuevoDocente(data=request.data)
        if serializerGuardar.is_valid():
            serializerGuardar.save()
            docentes = Docente.objects.all()
            serializerDatos = ListaDocentes(docentes, many=True)
            return Response(serializerDatos.data, status=status.HTTP_201_CREATED)
        return Response(serializerGuardar.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'PUT', 'DELETE'])
def docente_manager(request, pk):
    """
    List all code Usuarios, or create a new Docente.
    """
    try:
        docente = Docente.objects.get(pk=pk)
    except Docente.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = CargarDocente(docente, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CargarDocente(docente, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            docentes = Docente.objects.all()
            serializerDatos = ListaDocentes(docentes, many=True)
            return Response(serializerDatos.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        docente.delete()
        docentes = Docente.objects.all()
        serializer = ListaDocentes(docentes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    

    """ permission_classes = (Check_API_KEY_Auth,)

    def get(self, request, format=None):
        content = {
            'status': 'request was permitted'
        }
        return Response(content) """