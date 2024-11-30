from django.shortcuts import render, get_object_or_404
from .models import Estudiante
# Create your views here.

def home(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'principal/home.html', {'estudiantes': estudiantes})

def detalle_estudiante(request, estudiante_id):
    estudiante = get_object_or_404(Estudiante, pk=estudiante_id)
    return render(request, 'principal/detalle.html', {'estudiante': estudiante})


def grafico_edades(request):
    # Consultar datos del modelo Estudiante
    estudiantes = Estudiante.objects.all()

    # Obtener edades y contarlas
    edades = {}
    for estudiante in estudiantes:
        edades[estudiante.edad] = edades.get(estudiante.edad, 0) + 1

    # Preparar datos para el gráfico
    labels = list(edades.keys())  # Edades únicas
    values = list(edades.values())  # Cantidad de estudiantes por edad

    return render(request, 'principal/grafico_edades.html', {'labels': labels, 'values': values})