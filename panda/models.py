from django.db import models

class FoodItem(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(unique=True, max_length=30)
    description = models.CharField(max_length=250)
    restaurant = models.CharField(max_length=30)
    price = models.IntegerField()
    image = models.ImageField(default="http://placehold.it/700x400")

    def __str__(self):
        return self.name