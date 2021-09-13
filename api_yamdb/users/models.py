from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from rest_framework.response import Response
from rest_framework import status


def username_validator(name):
    if name == 'me':
        raise ValidationError("Username can't be 'me'")
    else:
        return name


class User(AbstractUser):
    username = models.CharField(
        # default='user',
        max_length=150,
        unique=True,
        validators=[username_validator]
    )
    bio = models.TextField(
        'Биография',
        blank=True,
        null=True,
    )
    role = models.TextField(
        'Роль',
        blank=True,
        null=True,
    )
    confirmation_code = models.PositiveIntegerField(
        'Code',
        blank=True,
        null=True,
    )


#class Registration(models.Model):
#    username = models.TextField(
#        unique=True,
#        blank=False,
#        null=False,
#        max_length=150
#    )
#    email = models.EmailField('Email', unique=True, max_length=254)
#    confirmation_code = models.PositiveIntegerField('Code')


class Code(models.Model):
    username = models.TextField(
        unique=True,
        blank=False,
        null=False,
        max_length=150
    )
    confirmation_code = models.PositiveIntegerField('Code')
