from rest_framework.validators import ValidationError
from datetime import date


def values_validation(field: dict):
    if 'range' in field and type(field['range']) is not str:
        raise ValidationError("The attribute 'range' must be an integer")


def build_date(field: dict):
    values_validation(field)
    pass
