from typing import Any
from django.db import models

class IngredientCategory(models.Model):
    name = models.CharField(max_length=100)
    

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(IngredientCategory,on_delete=models.SET_NULL,null=True,related_name='category_ingredients')
    amount = models.FloatField()
    carb = models.FloatField()  # in grams
    fat = models.FloatField()  # in grams
    energy = models.FloatField()  # in calories
    protein = models.FloatField()  # in grams
    
    CREATE_OBJECT_FIELDS = '__all__'

    @classmethod
    def get_get_fields(self):
        return [
        'name',
        'category',
        'amount',
        'carb',
        'fat',
        'energy',
        'protein'
    ]

    def __str__(self):
        return self.name





class BaseMeal(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(Ingredient, related_name='meals')
    schedule = models.CharField(max_length=100)
    preparation_instructions = models.TextField(blank=True, null=True)

    def total_carb(self):
        return sum(ingredient.amount * ingredient.ingredient.carb for ingredient in self.ingredients.all())

    def total_fat(self):
        return sum(ingredient.amount * ingredient.ingredient.fat for ingredient in self.ingredients.all())

    def total_energy(self):
        return sum(ingredient.amount * ingredient.ingredient.energy for ingredient in self.ingredients.all())

    def total_protein(self):
        return sum(ingredient.amount * ingredient.ingredient.protein for ingredient in self.ingredients.all())

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
        
class Meal(BaseMeal):
    pass


class CustomMeal(BaseMeal):
    member = models.ForeignKey("members.Member",on_delete=models.CASCADE,related_name='member_meals')
    share  = models.BooleanField(default=False)
    ingredients = models.ManyToManyField(Ingredient, related_name='custom_meals')


class Nutrients(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE,related_name='additonal_nutrients')
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=5, decimal_places=2)



class DietPlan(models.Model):
    member = models.ForeignKey('members.Member',on_delete=models.CASCADE,related_name='member_dietPlan')
    meals = models.ManyToManyField(Meal, related_name='diet_plans')

    def __str__(self):
        return self.name
