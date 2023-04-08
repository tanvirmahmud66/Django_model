from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    userId = models.IntegerField()
    bio = models.TextField(blank=True, null=True)
    profession = models.CharField(max_length=100, blank=True, null=True)
    workplace = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=64, blank=True, null=True)
    relationStatus = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username


class PostDB(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        verbose_name = "PostDB"
        verbose_name_plural = "user's Post"
        ordering = ['profile', 'body', 'created', 'updated']

    def __str__(self):
        return f"{self.profile.user.first_name} {self.profile.user.last_name}"
