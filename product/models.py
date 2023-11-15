from django.db import models
from user.models import User

class Product(models.Model):
    tag_choices = [
        ('el', 'Electronics'),
        ('cl', 'Clothes'),
        ('fo', 'Food'),
        ('ot', 'Other'),
    ]

    name = models.CharField(max_length=50)
    description = models.TextField(default='')
    tag = models.CharField(default='ot', choices=tag_choices, max_length=2)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='')
    date_listed = models.DateTimeField(auto_now=True, auto_now_add=False)
    currently_listed = models.BooleanField(default=True)

    def __str__(self):
        return self.name
