from django.db import models
from django.contrib.auth.models import User
from django.conf.urls.static import static
from django.utils import timezone


class AccountAvatar(models.Model):
    user   = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default="images/default_icon.jpg")

    def __str__(self):
        return f"{self.user.username}"
    
class UserRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings_given')
    rated_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings_received')
    comment = models.TextField(default = '')
    rating = models.PositiveIntegerField()
    date_reviewed = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} : {self.rating}"

class VerifiedUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}"