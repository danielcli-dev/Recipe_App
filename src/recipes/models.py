from django.db import models
from ingredients.models import Ingredient
# Create your models here.

difficulty_choices=(
('easy','Easy'),
('medium', 'Medium'),
('hard', 'Hard'),
('intermediate', 'Intermediate')
)

class Recipe(models.Model):
    name=models.CharField(max_length=120)
    ingredients=models.ManyToManyField(Ingredient)
    cooking_time=models.PositiveIntegerField(help_text='in minutes')
    difficulty= models.CharField(max_length=12, choices=difficulty_choices, default='easy') 

    def __str__(self):
        return str(self.name)