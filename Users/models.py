from django.db import models
from django.contrib.auth.models import User
#from Main.panda.models import FoodItem

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.user.username} Account'
