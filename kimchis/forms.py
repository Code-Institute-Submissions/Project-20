from django import forms
from .models import MainIngredient


class SearchForm(forms.Form):
    title = forms.CharField(max_length=100, required=False)
    main_ingredient = forms.ModelChoiceField(
        queryset=MainIngredient.objects.all(), required=False)
