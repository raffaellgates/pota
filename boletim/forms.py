from django.forms import ModelForm
from .models import Nota

class NotaModelForm(ModelForm):
    class Meta:
        model = Nota
        fields = "__all__"
