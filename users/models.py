from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(
        verbose_name='Name of User',
        max_length=100, null=True, blank=True
    )

    class Meta:
        permissions = (
            ("can_get_username", "Can get a username"),
            ("can_get_name", "Can get a name"),
        )

    def __str__(self):
        return f'{self.username}-{self.id}'




