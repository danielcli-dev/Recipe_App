from django.test import TestCase
from .models import Ingredient

# Create your tests here.
class MyTestClass(TestCase):
    def setUpTestData():
        # Set up non-modified objects used by all test methods
        Ingredient.objects.create(name='Carrot')

    def test_ingredient_name(self):
        # Get a ingredient object to test
        ingredient = Ingredient.objects.get(id=1)

        #  Get the metadata for the 'name' field and use it to query its data
        field_label = ingredient._meta.get_field('name').verbose_name

        # Compare the value to the expected result
        self.assertEqual(field_label, 'name')