from django.shortcuts import render
from eventos.models import Evento, Usergeneral
from .form import NuevoUsuario


# Create your views here.


def home(request):
    return render(request, 'core/home.html')


def ListarEventos(request):
    eventos = Evento.objects.all()
    data = {
        'eventos': eventos,
        'usergeneral': Usergeneral,
        'form': NuevoUsuario()
    }
    if request.method == 'POST':
        formulario = NuevoUsuario(request.POST)
        if formulario.is_valid():
            formulario.save()

        data['mensaje'] = "Usted sea registrado al Evento con exito"
    return render(request, 'core/eventos.html', data)
