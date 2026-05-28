import os
import io
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.conf import settings
from docxtpl import DocxTemplate
from .models import PlantillaDocumento

def procesar_formulario(request, plantilla_id):
    
    if request.method == "POST":

        plantilla = get_object_or_404(PlantillaDocumento, pk=plantilla_id)

        ruta_word_original = os.path.join(
            settings.BASE_DIR,
            'formularios',
            'plantillas_origen',
            plantilla.archivo_word
        )

        doc = DocxTemplate(ruta_word_original)

        datos_rellenos = {}
        for campo in plantilla.campos.all():

            valor_usuario = request.POST.get(campo.nombre_variable, '')
            datos_rellenos[campo.nombre_variable] = valor_usuario

        doc.render(datos_rellenos)

        buffer = io.BytesIO()
        doc.save(buffer)
        buffer.seek(0)

        response = HttpResponse(
            buffer.getvalue(),
            content_type = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        )

        response['Content-Disposition'] = f'attachment; filename="{plantilla.archivo_word}"'

        return response

def lista_plantillas(request):

    plantillas = PlantillaDocumento.objects.all()

    return render(request, 'formularios/index.html', {'plantillas': plantillas})

def detalle_plantilla(request, plantilla_id):

    plantilla = get_object_or_404(PlantillaDocumento, pk=plantilla_id)

    return render(request, 'formularios/detalle.html', {'plantilla': plantilla})