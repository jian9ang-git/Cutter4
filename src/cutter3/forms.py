from django import forms
from .models import UrlShort


class UrlShortForm(forms.ModelForm):
    class Meta:
        model = UrlShort
        fields = ['user_url', 'short_url', 'num_visits']
