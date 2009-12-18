from django.db import models


class Recipe(models.Model):
	"""A recipe"""
	
	name = models.CharField(max_length=32)
	picture = models.ImageField(upload_to='photos/%Y/%m/%d')
	
	
class Ingredient(models.Model):
	"""An ingredient of the recipe."""

	recipe = models.ForeignKey(Recipe)
	"""The recipe that the ingredient belongs to"""
	
	ingredient = models.CharField(max_length=32)
	quantity = models.DecimalField(max_digits=5, decimal_places=3)
	quantity_unit = models.CharField(max_length=16)
	
	
class Instruction(models.Model):
	"""An instruction of the recipe"""
	
	recipe = models.ForeignKey(Recipe)
	"""The recipe that the instruction belongs to"""
	
	intruction = models.CharField(max_length=200)
	step_number = models.PositiveIntegerField()
	

