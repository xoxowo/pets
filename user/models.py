from django.db import models

class TimeStempModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class StoreUser(TimeStempModel):
    user_name     = models.CharField(max_length=20, unique=True)
    password      = models.CharField(max_length=200)
    name          = models.CharField(max_length=20)
    post_number   = models.CharField(max_length=10)
    address_1     = models.CharField(max_length=100)
    address_2     = models.CharField(max_length=100)
    phone_number  = models.CharField(max_length=50)
    email         = models.EmailField(max_length=100)

    class Meta:
        db_table = 'storeusers'

    def __str__(self):
        return self.user_name