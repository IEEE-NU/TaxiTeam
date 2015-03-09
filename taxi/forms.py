from django import forms

from .models import Taxi_Group

class TaxiGroupForm(forms.ModelForm):

    class Meta:
        model = Taxi_Group
        fields = ('date', 'start_location', 'destination', 'time', 'num_ppl')