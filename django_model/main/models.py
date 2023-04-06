from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_id = models.IntegerField()
    bio = models.TextField(blank=True, null=True)
    profession = models.CharField(max_length=100, blank=True, null=True)
    workplace = models.CharField(max_length=100, blank=True, null=True)
    genter = models.CharField(max_length=64, blank=True, null=True)
    relationStatus = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username
