from django.urls import path
from . import views

urlpatterns = [

    path('', views.landing, name='landing'),

    path('listado/', views.lista_plantillas, name='lista_plantillas'),

    path('<int:plantilla_id>/', views.detalle_plantilla, name='detalle_plantilla'),

    path('generar/<int:plantilla_id>/', views.procesar_formulario, name='procesar_formulario'),
]