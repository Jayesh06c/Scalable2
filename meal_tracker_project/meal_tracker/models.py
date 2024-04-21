from django.db import models

class Meal(models.Model):
    name = models.CharField(max_length=100)

class Consumption(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    grams_consumed = models.PositiveIntegerField()


# Create your models here.
