from random import choice, randint
from rest_framework.exceptions import ValidationError


def values_validation(field: dict) -> None:

    if 'length' in field and type(field['length']) is not int:
        raise ValidationError("The attribute 'length' must be an integer")

    if 'max_length' in field and type(field['max_length']) is not int:
        raise ValidationError("The attribute 'max_length' must be an integer")

    if 'mask' in field and type(field['mask']) is not str:
        raise ValidationError("The attribute 'mask' must be a string")


def generate_string(min_length: int, max_length: int, random_rage: bool):
    letters = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
               't', 'u', 'v', 'w', 'x', 'y', 'z')
    response = ""
    for i in range(0, randint(0, max_length) if random_rage else max_length):
        if randint(1, 100) <= 20 and i != 0 and response[i - 1] != " ":
            response += " "
        else:
            response += choice(letters)
    return response


def build_string(field: dict) -> str:
    values_validation(field)

    # String length
    length = field['length'] if 'length' in field else None

    # String max length
    max_length = field['max_length'] if 'max_length' in field else 20

    # String mask
    mask = field['mask'] if 'mask' in field else None

    # Variable that safe data to return
    data = ""

    if mask:
        for p in mask:
            data += str(randint(0, 9)) if p == 'X' else p

    elif length:
        data = generate_string(0, length, False)

    else:
        # Generating random string using letters tuple
        data = generate_string(0, max_length, True)

    return data
