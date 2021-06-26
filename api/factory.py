from random import choice, randint
from rest_framework.exceptions import ValidationError


def values_validation(field: dict):
    if 'max_length' in field and type(field['max_length']) is not int:
        raise ValidationError("The field max_length must be an integer")


def build_string(field: dict):
    print(f"{field=}")
    print(f"{type(field)=}")
    values_validation(field)

    letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u')

    # String max length
    max_length = field['max_length'] if 'max_length' in field else 20

    # Variable that safe data to return
    data = ""

    # Generating random string using letters tuple
    for i in range(0, randint(0, max_length)):
        if randint(1, 100) <= 20 and i != 0 and data[i - 1] != " ":
            data += " "
        else:
            data += choice(letters)

    return data
