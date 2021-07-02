from random import uniform
from rest_framework.exceptions import ValidationError


def values_validation(field: dict) -> None:
    if 'range' in field:

        # Check if range value is a string
        if type(field['range']) is not str:
            raise ValidationError("The attribute 'range' must be a string")
        try:
            int(field['range'].split("-")[0])
            int(field['range'].split("-")[1])
        except ValueError as error:
            raise ValidationError(error.__str__() + " in range field")

    if 'decimal_places' in field:

        # Check if decimal_places is an integer
        if type(field['decimal_places']) is not int:
            raise ValidationError("The attribute 'decimal_places' must be an integer")

        # Check if decimal_places value is between 1 and 10
        if field['decimal_places'] > 10 or field['decimal_places'] < 1:
            raise ValidationError("The attribute 'decimal_place' must be an intenger between from 1 to 10")


def build_float(field: dict) -> int:
    # print(f"{field=}")
    # print(f"{type(field)=}")
    values_validation(field)

    # Range of numbers
    _range = field['range'] if 'range' in field else "0-100"
    _decimal_places = field['decimal_places'] if 'decimal_places' in field else 2
    # print(f"{_range=}")

    # Return rounded random float
    return round(uniform(int(_range.split("-")[0]), int(_range.split("-")[1])), _decimal_places)

