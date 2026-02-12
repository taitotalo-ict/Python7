from django import forms
from .models import Country

class CountryModifyForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['name', 'population', 'region', 'area', 'gdp']
        # fields = ['__all__']