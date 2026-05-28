from django.urls import path
from . import views

urlpatterns = [
    path('generar/<int:plantilla_id>/', views.procesar_formulario, name='procesar_formulario'),
]