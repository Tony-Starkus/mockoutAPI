from rest_framework.validators import ValidationError
from cpf_generator import CPF


def values_validation(field: dict):
    if 'formated' in field and type(field['formated']) is not bool:
        raise ValidationError("The attribute 'formated' must be a boolean (true or false)")


def build_cpf(field: dict):
    values_validation(field)

    cpf = CPF.generate()

    # Check if cpf must be formated
    formated = True if 'formated' in field else False

    if formated:
        cpf = CPF.format(cpf)

    return cpf
