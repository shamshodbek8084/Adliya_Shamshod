from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    photo = models.ImageField(upload_to="users", null=True, blank=True)

    def __str__(self):
        return self.username 