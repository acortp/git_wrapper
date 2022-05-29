from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    github_user = models.CharField(null=False, blank=False, max_length=300)
