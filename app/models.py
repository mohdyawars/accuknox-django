from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """Model to save extra user data"""
    # has one-to-one relationship with User model
    user = models.OneToOneField( 
        to=User, on_delete=models.CASCADE
    )
    bio = models.TextField(null=True)


    def __str__(self):
        return self.user.username
