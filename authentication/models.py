from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    
    name=models.CharField(max_length=25)
    last_name=models.CharField(max_length=25)
    email=models.EmailField(max_length=80, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'name',
        'lastname'
    ]
    def __str__(self) -> str:
        return f"User -> {self.email}"
