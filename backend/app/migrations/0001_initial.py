# Generated by Django 5.0.2 on 2024-04-18 12:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('members', '0002_alter_member_user_alter_membership_expiry_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.FloatField()),
                ('carb', models.FloatField()),
                ('fat', models.FloatField()),
                ('energy', models.FloatField()),
                ('protein', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='IngredientCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CustomMeal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('schedule', models.CharField(max_length=100)),
                ('preparation_instructions', models.TextField(blank=True, null=True)),
                ('share', models.BooleanField(default=False)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member_meals', to='members.member')),
                ('ingredients', models.ManyToManyField(related_name='custom_meals', to='app.ingredient')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='ingredient',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category_ingredients', to='app.ingredientcategory'),
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('schedule', models.CharField(max_length=100)),
                ('preparation_instructions', models.TextField(blank=True, null=True)),
                ('ingredients', models.ManyToManyField(related_name='meals', to='app.ingredient')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DietPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member_dietPlan', to='members.member')),
                ('meals', models.ManyToManyField(related_name='diet_plans', to='app.meal')),
            ],
        ),
        migrations.CreateModel(
            name='Nutrients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='additonal_nutrients', to='app.meal')),
            ],
        ),
    ]