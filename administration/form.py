from django.forms import ModelForm
from eventos.models import Evento


class EventForm(ModelForm):

    class Meta:
        model = Evento
        fields = {'id', 'nombre', 'descripcion', 'lugar', 'fecha', 'hora', 'boletos', 'precio'}
