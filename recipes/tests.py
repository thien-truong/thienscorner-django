from django.test import TestCase

class RecipeListTest(TestCase):
	#to make sure the recipe list page will load without errors
	def test_recipe_list(self):
		response = self.client.get("/cookbook/recipes/")
		self.assertEqual(response.status_code, 200)
		
class RecipeTest(TestCase):
	#to make sure the recipe page will load without errors
	def test_recipe(self):
		response = self.client.get("/cookbook/recipes/1/")
		self.assertEqual(response.status_code, 404)
		