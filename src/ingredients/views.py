from django.shortcuts import render
from django.views.generic import ListView
from .models import Ingredient
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class IngredientListView(LoginRequiredMixin, ListView):
   model = Ingredient
   template_name = 'ingredients/list.html'