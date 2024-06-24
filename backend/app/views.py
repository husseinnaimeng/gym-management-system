from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = models.Ingredient.objects.all()
    serializer_class = serializers.GetIngredientSerializer
    