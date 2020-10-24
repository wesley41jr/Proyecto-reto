from django.urls import path
from .views import home, ListarEventos

urlpatterns = [
    path('', home, name='home'),
    path('eventos', ListarEventos, name='ListarEventos'),
]
