from django.shortcuts import render_to_response, get_object_or_404
from cookbook.recipes.models import Recipe


def recipe_list(request):
	recipe_list = Recipe.objects.all()
	#{"object_list":recipe_list} -- a dictionary.
	#'object_list' -- a key in the html template
	return render_to_response('recipes/recipe_list.html',
	                          {'object_list': recipe_list})
							  
def recipe(request, object_id):
	recipe = get_object_or_404(Recipe, id=object_id)
	return render_to_response('recipes/recipe.html',
	                           {'object': recipe})