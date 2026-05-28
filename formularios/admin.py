from django.contrib import admin

from .models import PlantillaDocumento, CampoFormulario

class CampoFormularioInLine(admin.StackedInline):
    model = CampoFormulario
    extra = 3 # La cantidad de pregunta/campos por defecto

@admin.register(PlantillaDocumento)
class PlantillaDocumentoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'archivo_word')
inlines = [CampoFormularioInLine]

admin.site.register(CampoFormulario)