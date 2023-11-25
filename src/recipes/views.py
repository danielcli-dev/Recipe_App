from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipe
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RecipeSearchForm
import pandas as pd
from IPython.display import HTML
from .utils import get_chart, make_clickable_both, make_image
from django.contrib.auth.decorators import login_required



# Create your views here.
def home(request):
   return render(request, 'recipes/recipes_home.html')

@login_required
def records(request):
   form = RecipeSearchForm(request.POST or None)
   recipe_df = None
   chart = None

   if request.method == 'POST':
      recipe_name = request.POST.get('recipe_name')
      chart_type = request.POST.get('chart_type')

      print(recipe_name, chart_type)

      print('Exploring querysets:')
      print('Case 1: Output of Recipe.objects.all()')
      qs = Recipe.objects.all()

      if recipe_name:
         qs =Recipe.objects.filter(name__icontains = recipe_name) 
         
         #if using model from another app, use "app"_name

      if qs:
         recipe_df = pd.DataFrame(qs.values())
         ingredient_df = []
         temp_url_df = []
         temp_recipe_df = pd.DataFrame()

         for q in qs:
            temp_df = []

            for ingredient in q.ingredients.all():
               temp_df.append(ingredient)

            ingredient_list = ', '.join(str(a) for a in temp_df)
            ingredient_df.append(ingredient_list)
            g = q.get_absolute_url()
            temp_url_df.append("http://127.0.0.1:8000" + g)

         temp_recipe_df['name'] = recipe_df['name']
         temp_recipe_df['url'] = temp_url_df
         temp_recipe_df['ingredients'] = ingredient_df
         temp_recipe_df['nameurl'] = temp_recipe_df['name']+'#' + temp_recipe_df['url']

         recipe_df['name'] = temp_recipe_df['nameurl'].apply(make_clickable_both)
         recipe_df['pic'] = recipe_df['pic'].apply(make_image)
         

      
      print ('Case 3: Output of qs.values')
      print (qs.values())

      print ('Case 4: Output of qs.values_list()')
      print (qs.values_list())

      print ('Case 5: Output of Recipe.objects.get(id=1)')
      obj = Recipe.objects.get(id=1)
      obj = obj.ingredients.all()
      print (obj)

      chart=get_chart(chart_type, recipe_df, labels=['easy','medium','hard','intermediate'])

      recipe_df=recipe_df.to_html(render_links=True, escape=False)

   context = {
      'form': form,
      'recipe_df': recipe_df,
      'chart': chart
   }
   return render(request, 'recipes/records.html', context)

class RecipeListView(LoginRequiredMixin, ListView):
   model = Recipe
   template_name = 'recipes/list.html'

class RecipeDetailView(LoginRequiredMixin, DetailView):
   model = Recipe
   template_name = 'recipes/detail.html'

