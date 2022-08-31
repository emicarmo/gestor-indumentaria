from django.forms import ModelForm
from shop.models import Remera

class RemeraForm(ModelForm):
    class Meta:
        model= Remera
        fields = '__all__'