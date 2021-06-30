from rest_framework.validators import ValidationError
from random import randint
from datetime import datetime, timedelta


def values_validation(field: dict) -> None:
    if 'range' in field:
        if type(field['range']) is not str:
            raise ValidationError("The attribute 'range' must be an integer")

        try:
            min_date = datetime.strptime(field['range'].split(" ")[0], "%Y-%m-%d")
            max_date = datetime.strptime(field['range'].split(" ")[1], "%Y-%m-%d")

            # If min date is in the future of max date
            if min_date > max_date:
                raise ValidationError("The min date can't be greater than max date")

        except ValueError:
            raise ValidationError(f"Incorret format in 'range' attribute in field '{field['field_name']}'")


def get_date_between(min_date: datetime, max_date: datetime):
    # Get days between the two dates
    days_delta = max_date - min_date

    # Create a random date using timedelta with random days
    random_date = min_date + timedelta(days=randint(0, days_delta.days))

    return random_date


def build_date(field: dict) -> datetime.date:
    values_validation(field)

    # Check if field has range
    _range = True if 'range' in field else False

    min_date = datetime.strptime(field['range'].split(" ")[0], "%Y-%m-%d")
    max_date = datetime.strptime(field['range'].split(" ")[1], "%Y-%m-%d")
    date = None

    if _range:
        date = get_date_between(min_date, max_date)
    print(f"{type(date.date())=}")
    return date.date()
