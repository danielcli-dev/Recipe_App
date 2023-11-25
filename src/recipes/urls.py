from django.urls import path
from .views import home, records, RecipeListView, RecipeDetailView

app_name = 'recipes' 

urlpatterns = [
   path('', home, name='home'),
   path('recipes/records', records, name='records'),
   path('recipes/', RecipeListView.as_view(), name='list'),
   path('recipes/<pk>', RecipeDetailView.as_view(), name='detail'),
]

