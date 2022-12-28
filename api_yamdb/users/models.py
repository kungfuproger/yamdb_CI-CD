from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models

from .validators import custom_username_validator

USER = "user"
MODERATOR = "moderator"
ADMIN = "admin"

ROLES = (
    (USER, USER),
    (MODERATOR, MODERATOR),
    (ADMIN, ADMIN),
)


class User(AbstractUser):
    """Модель пользователя."""

    username = models.CharField(
        "username",
        max_length=150,
        unique=True,
        blank=False,
        null=False,
        help_text="Required. 150 characters or fewer. "
        "Letters, digits and @/./+/-/_ only. Can't be 'me'.",
        validators=(custom_username_validator, UnicodeUsernameValidator),
        error_messages={
            "unique": "A user with that username already exists.",
        },
    )
    email = models.EmailField(
        "email",
        unique=True,
        blank=False,
        null=False,
        max_length=254,
    )
    first_name = models.CharField(
        "имя",
        blank=True,
        max_length=150,
    )
    bio = models.TextField(
        "Биография",
        blank=True,
    )
    role = models.CharField(
        "Роль",
        choices=ROLES,
        max_length=20,
        default=USER,
    )

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.username

    @property
    def is_admin(self):
        return self.role == ADMIN

    @property
    def is_moderator(self):
        return self.role == MODERATOR

    @property
    def is_user(self):
        return self.role == USER
