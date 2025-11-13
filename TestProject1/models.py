from django.db import models

class UserModel(models.Model):
    Name = models.CharField(max_length=20)
    Email = models.EmailField()
    Password = models.CharField(max_length=10)
    Age = models.IntegerField()
    