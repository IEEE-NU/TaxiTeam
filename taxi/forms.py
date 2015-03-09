from django import forms

from .models import Group

class TaxiGroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = ('start_location', 'destination')