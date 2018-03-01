from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    user_name = models.TextField(default='')
    first_name = models.TextField(default='')
    last_name = models.TextField(default='')
    gender = models.TextField(default='')

    USERNAME_FIELD = 'username'
