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
            datos_rellenos[campos.nombre_variable] = valor_usuario

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