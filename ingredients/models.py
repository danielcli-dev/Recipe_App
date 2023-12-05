from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Ingredient(models.Model):
    name=models.CharField(max_length=120)
    pic=models.ImageField(upload_to='ingredients', default='no_picture.jpg')
    # upload_to where inside media folder you want to save image. (e.g. media/ingredients)

    def __str__(self):
        return str(self.name)
