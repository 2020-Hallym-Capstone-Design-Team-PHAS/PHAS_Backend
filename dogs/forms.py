from django import forms
from .models import DogInfo

class DogForm(forms.ModelForm):
    class Meta:
        model = DogInfo
        fields = ['dog_breed', 'dog_size', 'dog_birth']
