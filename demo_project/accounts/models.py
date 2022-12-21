from enum import Enum


from django.contrib.auth.models import AbstractUser
from django.core import validators, exceptions
from django.db import models


def validate_only_letters(value):
    for ch in value:
        if not ch.isalpha():
            raise exceptions.ValidationError('The name must contain only letters!')


class ChoicesMixin:
    @classmethod
    def choices(cls):
        return [(c.name, c.value) for c in cls]

    @classmethod
    def max_len(cls):
        return max(len(name) for name, _ in cls.choices())


class Gender(ChoicesMixin, Enum):
    male = 'Male'
    female = 'Female'
    Other = 'Other'


class AppUser(AbstractUser):
    MIN_LEN_NAME = 2
    MAX_LEN_NAME = 30
    MIN_AGE = 1
    MAX_AGE = 150

    username = models.CharField(
        unique=True,
        max_length=MAX_LEN_NAME,
        validators=(validators.MinLengthValidator(MIN_LEN_NAME),
                    validate_only_letters,
                    ),
    )

    email = models.EmailField(
        unique=True,
        null=True,
        blank=True,
    )

    gender = models.CharField(
        choices=Gender.choices(),
        max_length=Gender.max_len(),
        null=True,
        blank=True,
    )

    age = models.IntegerField(
        validators=(
            validators.MinValueValidator(MIN_AGE),
            validators.MaxValueValidator(MAX_AGE),
        ),
        null=True,
        blank=True,
    )


