from django.urls import path
from .views import IngredientListView

app_name = 'ingredients' 

urlpatterns = [
   path('ingredients/', IngredientListView.as_view(), name='list'),
]

