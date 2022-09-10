from django.db import models

# Create your models here.

class Animal(models.Model):
    name = models.CharField(max_length=20)
    predator = models.BooleanField()
    venomous = models.BooleanField()
    domestic = models.BooleanField()


    def __str__(self):
        return self.name
