from django.db import models


class Pizza(models.Model):
    dough = models.CharField(max_length=30)
    size = models.CharField(max_length=30)
    class Meta:
        db_table = 'Pizzas'

class Topping(models.Model):
    opsion1 = models.CharField(max_length=50)
    opsion2 = models.CharField(max_length=50)

    class Meta:
        db_table = 'toppings'

class Pizza_topping(models.Model):
    pizza = models.ForeignKey('Pizza', on_delete=models.CASCADE)
    topping = models.ForeignKey('Topping', on_delete=models.CASCADE)

    class Meta:
        db_table = 'pizza_topping'