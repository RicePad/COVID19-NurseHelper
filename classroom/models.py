from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.html import escape, mark_safe

PAYMENT_CHOICES = (
    ('1', 'Fruits'),
    ('2', 'Vegetables'),
    ('3', 'Dairy')
)

class User(AbstractUser):
    is_helper = models.BooleanField(default=False)
    is_nurse = models.BooleanField(default=False)


class Nurse(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    telepone = models.IntegerField()
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    payment_type = models.CharField(choices=PAYMENT_CHOICES, max_length=50)
    description = models.TextField()


    def __str__(self):
        return self.user.username

class Helper(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    telepone = models.IntegerField()
    address = models.CharField(max_length=100)
    payment_type = models.CharField(choices=PAYMENT_CHOICES, max_length=50)
    description = models.TextField()
    
    def __str__(self):
        return self.user.username
