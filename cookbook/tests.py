import os
import tempfile

from django.core.files.images import ImageFile
from django.core.urlresolvers import reverse
from django.test import TestCase
from PIL import Image

from thienscorner.cookbook.models import Recipe


class EmptyRecipeListTest(TestCase):
    #to make sure the recipe list page will load without errors
    def test_recipe_list(self):
        recipe_list_url = reverse('thienscorner.cookbook.views.recipe_list')
        response = self.client.get(recipe_list_url)
        self.assertEqual(response.status_code, 200)


class RecipeTest(TestCase):
    def setUp(self):
        image_fd, image_path = tempfile.mkstemp(suffix='.jpg')
        os.close(image_fd)
        Image.new('RGB', (1, 1)).save(image_path, 'JPEG')
        image = open(image_path)
        self.recipe = Recipe.objects.create(name="Test",
                                            picture=ImageFile(image))
        image.close()
        os.remove(image_path)

    #to make sure the recipe page will load without errors
    def test_recipe(self):
        recipe_view = 'thienscorner.cookbook.views.recipe'

        recipe_url = reverse(recipe_view, args=[0])
        response = self.client.get(recipe_url)
        self.assertEqual(response.status_code, 404)

        recipe_url = reverse(recipe_view, args=[self.recipe.id])
        response = self.client.get(recipe_url)
        self.assertEqual(response.status_code, 200)

    def test_recipe_list(self):
        recipe_list_url = reverse('thienscorner.cookbook.views.recipe_list')
        response = self.client.get(recipe_list_url)
        self.assertEqual(response.status_code, 200)
