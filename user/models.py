from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.email