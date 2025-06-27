from django.shortcuts import render, get_object_or_404
from .models import Estudiante, Calificacion,Materia
from django.shortcuts import redirect
from .forms import EstudianteForm
import openpyxl
from django.http import HttpResponse
from .models import Estudiante
from django.db.models import Avg

def student_list(request):
    query = request.GET.get('q')
    materia_id = request.GET.get('materia')
    min_promedio = request.GET.get('promedio')

    estudiantes = Estudiante.objects.all()

    # Filtro por nombre
    if query:
        estudiantes = estudiantes.filter(nombre__icontains=query)

    # Filtro por materia
    if materia_id:
        estudiantes = estudiantes.filter(calificacion__materia__id=materia_id).distinct()

    # Anotar promedio
    estudiantes = estudiantes.annotate(promedio=Avg('calificacion__nota'))

    # Filtro por promedio mínimo
    if min_promedio:
        estudiantes = estudiantes.filter(promedio__gte=float(min_promedio))

    # Orden descendente por promedio
    estudiantes = estudiantes.order_by('-promedio')

    materias = Materia.objects.all()

    return render(request, 'core/student_list.html', {
        'estudiantes': estudiantes,
        'materias': materias,
        'query': query,
        'materia_id': materia_id,
        'min_promedio': min_promedio
    })

def student_detail(request, id):
    estudiante = get_object_or_404(Estudiante, pk=id)
    calificaciones = Calificacion.objects.filter(estudiante=estudiante)
    if calificaciones:
        promedio = sum(c.nota for c in calificaciones) / calificaciones.count()
    else:
        promedio = 0
    return render(request, 'core/student_detail.html', {
        'estudiante': estudiante,
        'calificaciones': calificaciones,
        'promedio': promedio
    })

def agregar_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')  # Redirige al listado
    else:
        form = EstudianteForm()

    return render(request, 'core/agregar_estudiante.html', {'form': form})

def exportar_excel(request):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Calificaciones de Estudiantes"

    # Cabecera
    ws.append(['Nombre', 'Correo', 'Materia', 'Nota', 'Promedio'])

    estudiantes = Estudiante.objects.all()

    for estudiante in estudiantes:
        calificaciones = Calificacion.objects.filter(estudiante=estudiante)
        if calificaciones.exists():
            promedio = sum(c.nota for c in calificaciones) / calificaciones.count()
            for c in calificaciones:
                ws.append([
                    f"{estudiante.nombre} {estudiante.apellido}",
                    estudiante.correo,
                    c.materia.nombre,
                    float(c.nota),
                    float(promedio)
                ])
        else:
            # Si no tiene calificaciones
            ws.append([
                f"{estudiante.nombre} {estudiante.apellido}",
                estudiante.correo,
                'Sin materias',
                'N/A',
                '0.00'
            ])

    # Preparar archivo Excel
    response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response['Content-Disposition'] = 'attachment; filename=estudiantes_calificaciones.xlsx'
    wb.save(response)
    return response