from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name = 'index'),
    path('notas/', notas, name = 'notas'),
    path('cursos/', cursos, name = 'cursos'),
    path('foro/', foro, name = 'foro'),
    path('<slug:slug>/', detallePost , name = 'detalle_post'),
    
]
