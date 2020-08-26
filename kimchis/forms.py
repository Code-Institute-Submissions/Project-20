from django import forms
from .models import MainIngredient


class SearchForm(forms.Form):
    title = forms.CharField(max_length=100, required=False,
                            label="Product name",
                            widget=forms.TextInput(
                                attrs={'placeholder': 'E.g. Radish Kimchi'}))
    main_ingredient = forms.ModelChoiceField(
        queryset=MainIngredient.objects.all(), required=False)
