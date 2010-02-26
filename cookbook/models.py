from django.db import models


class Recipe(models.Model):
    """A recipe"""

    name = models.CharField(max_length=32)
    picture = models.ImageField(upload_to='photos/%Y/%m/%d')

    def __unicode__(self):
        return self.name


class Ingredient(models.Model):
    """An ingredient of the recipe."""

    recipe = models.ForeignKey(Recipe)
    """The recipe that the ingredient belongs to"""

    ingredient = models.CharField(max_length=32)
    quantity = models.CharField(max_length=5)
    quantity_unit = models.CharField(max_length=16, blank=True)

    #String representation of the Ingredient object
    def __unicode__(self):
        #Thien's name for an ingredient string (ex: 3/4 cup sugar)
        quantity_of_ingredient = "%s " % self.quantity
        quantity_unit_ingredient = ""
        if len(self.quantity_unit) > 0:
            quantity_unit_ingredient = "%s " % self.quantity_unit
        ingredient = "%s%s%s" % (quantity_of_ingredient,
                                 quantity_unit_ingredient,
                                 self.ingredient)
        return ingredient


class Instruction(models.Model):
    """An instruction of the recipe"""

    recipe = models.ForeignKey(Recipe)
    """The recipe that the instruction belongs to"""

    instruction = models.CharField(max_length=200)
    step_number = models.PositiveIntegerField()

    class Meta:
        ordering = ['step_number']

    def __unicode__(self):
        return self.instruction
