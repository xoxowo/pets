import email
from django.db import models

class Owner(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    email = models.EmailField(max_length=128)

    class Meta:
        db_table = 'owners'

class Pet(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE)

    class Meta:
        db_table = 'pets'