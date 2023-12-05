from django.db import models
from ingredients.models import Ingredient
from django.shortcuts import reverse

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
    pic=models.ImageField(upload_to='recipes', default='no_picture.jpg')

    def __str__(self):
        return str(self.name)
    
    def get_absolute_url(self):
        return reverse ('recipes:detail', kwargs={'pk': self.pk})
    
    def calc_difficulty(self):
        if self.cooking_time < 10 and self.ingredients.count() < 4:
            self.difficulty = "Easy"
        elif (
            self.cooking_time < 10 and self.ingredients.count() >= 4
        ):
            self.difficulty = "Medium"
        elif (
            self.cooking_time >= 10 and self.ingredients.count() < 4
        ):
            self.difficulty = "Intermediate"
        elif (
            self.cooking_time >= 10 and self.ingredients.count() >= 4
        ):
            self.difficulty = "Hard"
        return self.difficulty