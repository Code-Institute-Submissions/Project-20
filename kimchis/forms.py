from django import forms
from .models import Kimchi
from django.db.models import Q


class SearchForm(forms.Form):
    title = forms.CharField(max_length=100, required=False)

