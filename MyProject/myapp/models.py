from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    image = models.ImageField()
    description = models.TextField()

    def __str__(self) -> str:
        return self.name
    

# class Product1(models.Model):
#     name = models.CharField(max_length=20)
#     price = models.IntegerField()
#     image = models.ImageField()
#     description = models.TextField()
#     createdOn = models.DateTimeField(auto_now_add=True)
#     category = models.ForeignKey("Category", on_delete=models.CASCADE)


# Note :  User = username, email, password, first_name, last_name, date_joined and some other fields

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    money = models.IntegerField()

    def __str__(self) -> str:
        return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=20)

