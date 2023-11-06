from django.db import models
from recipes.models import Recipe
from ingredients.models import Ingredient

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=120)
    recipes=models.ManyToManyField(Recipe)

    def __str__(self):
        return str(self.name)