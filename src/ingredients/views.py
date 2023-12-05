from django.shortcuts import render
from django.views.generic import ListView
from .models import Ingredient
from django.contrib.auth.mixins import LoginRequiredMixin

# LoginRequiredMixin requires the user login before gaining access to this view
# ListView provides access to object_list which contains all objects of the model Ingredient
class IngredientListView(LoginRequiredMixin, ListView):
   model = Ingredient
   template_name = 'ingredients/list.html'