from . import models
from rest_framework import serializers

class IngredientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Ingredient
        fields = model.CREATE_OBJECT_FIELDS

class GetIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ingredient
        fields = model.get_get_fields()