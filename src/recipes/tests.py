from django.test import TestCase
from .models import Recipe
from .models import Ingredient
from .forms import RecipeSearchForm
from django.urls import reverse, resolve
from .views import RecipeListView

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

    def test_get_absolute_url(self):
       recipe = Recipe.objects.get(id=1)
       self.assertEqual(recipe.get_absolute_url(), '/recipes/1')

    def test_recipe_form(self):
       form = RecipeSearchForm(data={'recipe_name': 'Chocolate Cake', 'chart_type': "#1"})
       self.assertTrue(form.fields['recipe_name'].label is None or form.fields['recipe_name'].label == 'recipe_name')
       self.assertTrue(form.fields['chart_type'].label is None or form.fields['chart_type'].label == 'chart_type')
       self.assertTrue(form.is_valid())
    
    def test_recipe_form_name_too_long(self):
       form = RecipeSearchForm(data={'recipe_name': 'Chocolate Cake'*12, 'chart_type': "#1"})
       self.assertFalse(form.is_valid())

class RecipeListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_recipes = 15

        for recipe_id in range(number_of_recipes):
            Recipe.objects.create(
                name=f'Recipe {recipe_id}',
                cooking_time=15,
                difficulty='easy') 
          
            carrot = Ingredient.objects.create(name="Carrot")
            recipe = Recipe.objects.get(pk=1)
            recipe.ingredients.add(carrot)
  

    def test_listview_load(self):
        url = reverse("recipes:list")
        # self.client.login(username='testUser', password='testPassword')  
        # # defined in fixture or with factory in setUp()
        # response = self.client.get(reverse("recipes:list"))
        # self.assertEqual(response.status_code, 302)
        # response = self.client.get(reverse("recipes:list"))
        # self.assertEqual(response.status_code, 200)
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, RecipeListView)