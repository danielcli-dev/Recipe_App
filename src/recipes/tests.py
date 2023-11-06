from django.test import TestCase
from .models import Recipe
from .models import Ingredient

# Create your tests here.
class MyTestClass(TestCase):
    def setUpTestData():
        # Set up non-modified objects used by all test methods
        Recipe.objects.create(name='Chocolate Cake', cooking_time=5, difficulty='Easy')
        

    def test_recipe_name(self):
        # Get a ingredient object to test
        recipe = Recipe.objects.get(id=1)

        #  Get the metadata for the 'name' field and use it to query its data
        field_label = recipe._meta.get_field('name').verbose_name

        # Compare the value to the expected result
        self.assertEqual(field_label, 'name')
    
    def test_recipe_name_max_length(self):
        # Get a recipe object to test
        recipe = Recipe.objects.get(id=1)

        # Get the metadata for the 'author_name' field and use it to query its max_length
        max_length = recipe._meta.get_field('name').max_length

        # Compare the value to the expected result i.e. 120
        self.assertEqual(max_length, 120)

    def test_recipe_ingredients(self):
        # Get a ingredient object to test
        recipe = Recipe.objects.get(id=1)
        carrot = Ingredient.objects.create(name='Carrot')
        recipe = Recipe.objects.get(pk=1)
        recipe.ingredients.add(carrot)
        # Compare the value to the expected result
        self.assertEqual(recipe.ingredients.count(), 1)

    def test_cooking_time_positive_integer(self):
        # Get a recipe object to test
        recipe = Recipe.objects.get(id=1)

        # Get the metadata for the 'author_name' field and use it to query its max_length
        cooking_time = recipe.cooking_time

        # Compare the value to the expected result i.e. 120
        self.assertTrue(cooking_time >= 0 )


    def test_recipe_difficulty_max_length(self):
           # Get a recipe object to test
           recipe = Recipe.objects.get(id=1)

           # Get the metadata for the 'author_name' field and use it to query its max_length
           max_length = recipe._meta.get_field('difficulty').max_length

           # Compare the value to the expected result i.e. 120
           self.assertEqual(max_length, 12)
