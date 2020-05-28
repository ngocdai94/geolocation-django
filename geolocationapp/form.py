from django import forms
from .models import GeolocationData

class GeoDataForm (forms.ModelForm):
    class Meta:
        model=GeolocationData
        fields='__all__'