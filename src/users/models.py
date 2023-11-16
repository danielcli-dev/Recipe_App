from django.db import models
from recipes.models import Recipe
from ingredients.models import Ingredient
from django.shortcuts import reverse

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=120)
    recipes=models.ManyToManyField(Recipe)
    pic=models.ImageField(upload_to='users', default='no_picture.jpg')
    
    def __str__(self):
        return str(self.name)
    
    def get_absolute_url(self):
        return reverse ('users:detail', kwargs={'pk': self.pk})