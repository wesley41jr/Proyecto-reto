from django.shortcuts import render, redirect
from eventos.models import Evento
from administration.form import EventForm


def panel(request):
    eventos = Evento.objects.all()
    data = {
        'eventos': eventos,
    }
    return render(request, 'administration/panel.html',data)


def show(request):
    eventos = Evento.objects.all()
    data = {
        'eventos': eventos,
    }
    return render(request, 'administration/showevent.html', data)


def create(request):
    eventos = Evento.objects.all()
    data = {
        'eventos': eventos,
        'evento': Evento,
        'form': EventForm()
    }
    if request.method == 'POST':
        formulario = EventForm(request.POST)
        if formulario.is_valid():
            formulario.save()

    return render(request, 'administration/createEvent.html', data)


def modify(request, id):
    evento = Evento.objects.get(id=id)
    data = {
        'form': EventForm(instance=evento)
    }
    if request.method == 'POST':
        formulario = EventForm(data=request.POST, instance=evento)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "modificado con exito"
            data['form'] = formulario

    return render(request, 'administration/modifyEvent.html', data)

def delete(request, id):
    evento = Evento.objects.get(id=id)
    evento.delete()

    return redirect(to="panel")



