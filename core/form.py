from django.forms import ModelForm
from eventos.models import Usergeneral


class NuevoUsuario(ModelForm):

    class Meta:
        model = Usergeneral
        fields = {'nombre', 'apellido', 'boletos', 'telefono', 'email', 'evento'}
