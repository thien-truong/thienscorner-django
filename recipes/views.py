from django.shortcuts import render_to_response
from cookbook.recipes.models import Recipe

def recipe_list(request):
	recipe_list = Recipe.objects.all()
	#{"object_list":recipe_list} -- a dictionary.
	#'object_list' -- a key in the html template
	return render_to_response('recipes/recipe_list.html',
	                          {'object_list': recipe_list})
