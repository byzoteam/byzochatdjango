from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    status = models.CharField(max_length=20, default='offline')

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Unique related_name to avoid clash
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='custom_user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',  # Unique related_name to avoid clash
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='custom_user_permissions',
    )

    def set_status(self, status):
        self.status = status
        self.save()
