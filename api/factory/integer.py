from random import randint
from rest_framework.exceptions import ValidationError


def values_validation(field: dict):
    if 'range' in field:
        if type(field['range']) is not str:
            raise ValidationError("The attribute 'range' must be a string")
        try:
            int(field['range'].split("-")[0])
            int(field['range'].split("-")[1])
        except ValueError as error:
            raise ValidationError(error.__str__() + " in range field")


def build_integer(field: dict):
    # print(f"{field=}")
    # print(f"{type(field)=}")
    values_validation(field)

    # Range of numbers
    _range = field['range'] if 'range' in field else "0-100"
    # print(f"{_range=}")
    return randint(int(_range.split("-")[0]), int(_range.split("-")[1]))

