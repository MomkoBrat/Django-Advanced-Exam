from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth import models as auth_models


auth_models.AbstractUser


def validate_username(value):
    if len(value) <= 1 or len(value) > 20:
        raise ValidationError("Username must be between 1 and 30 characters (non-inclusive).")

    else:
        return value


def validate_user_last_first_name(value):
    if not value.isalpha():
        raise ValidationError("Name must only include letters.")

    else:
        return value


class DjigitAutoUser(auth_models.AbstractBaseUser):
    email = models.EmailField(
        'email address',
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.'
        },
    )
    username = models.CharField(
        unique=True,
        max_length=20,
        validators=[validate_username],
        error_messages={
            'unique': 'A user with that username already exists.'
        }
    )
    first_name = models.CharField(
        max_length=20,
        blank=True,
        null=False,
        validators=[validate_user_last_first_name]
    )
    last_name = models.CharField(
        max_length=20,
        blank=True,
        null=False,
        validators=[validate_user_last_first_name]
    )

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']
