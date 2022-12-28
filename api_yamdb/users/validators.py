from django.core.exceptions import ValidationError


def custom_username_validator(username):
    """Проверяет что username НЕ me"""
    if username == "me":
        raise ValidationError("username can't be <me>")
