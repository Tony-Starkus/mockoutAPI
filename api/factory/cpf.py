from rest_framework.validators import ValidationError
from cpf_generator import CPF


def values_validation(field: dict) -> None:
    if 'formated' in field and type(field['formated']) is not bool:
        raise ValidationError("The attribute 'formated' must be a boolean (true or false)")

    if 'funique' in field and type(field['unique']) is not bool:
        raise ValidationError("The attribute 'unique' must be a boolean (true or false)")


def build_cpf(field: dict, cpf_list: list) -> str:
    values_validation(field)

    # Check if cpf must be formated
    formated = True if 'formated' in field else False
    unique = True if 'unique' in field else False
    cpf = CPF.generate()

    if unique:
        while cpf in cpf_list:
            cpf = CPF.generate()

    if formated:
        cpf = CPF.format(cpf)

    return cpf
