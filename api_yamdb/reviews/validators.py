import datetime

from django.core.exceptions import ValidationError


def custom_year_validator(value):
    if value < 1900 or value > datetime.datetime.now().year:
        raise ValidationError(f"{value} is not a correct year")
