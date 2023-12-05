from django import forms
from .models import Ingredient, Recipe

CHART__CHOICES = (('#1', 'Bar chart'), ('#2', 'Pie chart'), ('#3', 'Line chart'))

class RecipeSearchForm(forms.Form):
    recipe_name = forms.CharField(max_length=120, required=False)
    chart_type = forms.ChoiceField(choices=CHART__CHOICES)

class RecipeAddForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = "__all__"


