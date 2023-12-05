from django.urls import path
from .views import about, home, records, add_recipe, RecipeListView, RecipeDetailView, RecipeDeleteView

app_name = 'recipes' 

urlpatterns = [
   path('', home, name='home'),
   path('about', about, name='about'),
   path('recipes/records', records, name='records'),
   path('recipes/add', add_recipe, name='add_recipe'),
   path('recipes/', RecipeListView.as_view(), name='list'),
   path('recipes/<pk>', RecipeDetailView.as_view(), name='detail'),
   path('recipes/<pk>/delete', RecipeDeleteView.as_view(), name='delete'),
]

