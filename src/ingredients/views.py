from django.shortcuts import render
from django.views.generic import ListView
from .models import Ingredient

# Create your views here.
class IngredientListView(ListView):
   model = Ingredient
   template_name = 'ingredients/main.html'