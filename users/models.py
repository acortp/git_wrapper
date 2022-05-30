from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    git_access_token = models.TextField(null=False, blank=False)
