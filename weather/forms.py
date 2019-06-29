from django.forms import ModelForm,TextInput
from weather.models import City
from django import forms

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {'name': TextInput(attrs={'class': 'input','placeholder':'City Name'})}


class cityforms(forms.Form):
    name = forms.CharField(label = 'city Name',
        widget = forms.TextInput(attrs = {'maxlength':'30','placeholder':'city Name'}))
        
    temp = forms.DecimalField(label = 'temperature',
        widget = forms.TextInput(attrs = {'placeholder':'temperature'}))

class Modelcityforms(forms.ModelForm):
    class Meta:
        model=City
        fields=('name','temp')

class SearchForm(forms.Form):
    q = forms.CharField(label = '',
        widget = forms.TextInput(attrs = {'maxlength':'30','placeholder':'search','class':'form-control','minlength':'2'}))
        
