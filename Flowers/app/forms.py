from django import forms
from .models import Flower

class FlowerForm(forms.ModelForm):
    class Meta:
        model = Flower
        fields = ['name', 'type', 'image', 'price', 'country_of_origin']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Flower Name'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'country_of_origin': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country of Origin'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }