from django.db import models

class PlantillaDocumento(models.Model):

    nombre = models.CharField(max_length=150 verbose_name="Nombre del Formulario")

    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")

    archivo_word = models.CharField(max_length=255, verbose_name="Nombre del archivo Word (.docx)")

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Plantilla de Documento"
        verbose_name_plural = "Plantillas de Documentos"
        
class CampoFormulario(models.Model):

    plantilla = models.ForeignKey(
        PlantillaDocumento,
        on_delete=models.CASCADE,
        related_name="campos"
    )

    nombre_variable = models.CharField(
        max_length=50,
        verbose_name="Variable en el Word (ej: correo_electrónic)"
    )