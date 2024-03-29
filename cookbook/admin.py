from thienscorner.cookbook.models import Recipe, Ingredient, Instruction
from django.contrib import admin


class IngredientInline(admin.TabularInline):
    model = Ingredient
    fields = ['quantity', 'quantity_unit', 'ingredient']
    extra = 5


class InstructionInline(admin.TabularInline):
    model = Instruction
    fields = ['step_number', 'instruction']
    extra = 5


class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientInline, InstructionInline]


admin.site.register(Recipe, RecipeAdmin)
