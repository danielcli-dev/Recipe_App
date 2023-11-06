from django.test import TestCase
from .models import User
from .models import Recipe
from .models import Ingredient

# Create your tests here.
class MyTestClass(TestCase):
    def setUpTestData():
        # Set up non-modified objects used by all test methods      
        User.objects.create(name='Daniel')
        Recipe.objects.create(name='Carrot Sticks', cooking_time=5, difficulty='Easy')
        user = User.objects.get(id=1)
        recipe = Recipe.objects.get(id=1)
        carrot = Ingredient.objects.create(name='Carrot')
        recipe = Recipe.objects.get(pk=1)
        recipe.ingredients.add(carrot)
        user.recipes.add(recipe)

    def test_user_name(self):
        # Get a ingredient object to test
        user = User.objects.get(id=1)

        #  Get the metadata for the 'name' field and use it to query its data
        field_label = user._meta.get_field('name').verbose_name

        # Compare the value to the expected result
        self.assertEqual(field_label, 'name')

    def test_user_recipes(self):
        user = User.objects.get(id=1)

        self.assertEqual(user.recipes.count(), 1)

