import re
import validate_docbr

from src.validators.utils import validate_string, validate_int, validate_float
from src.common.constants import CONSTANTS


def validate_email(email: str) -> str:
    email = validate_string()(email)

    email_components = email.split('@')
    
    if len(email_components) != 2:
        raise Exception(CONSTANTS['MESSAGE']['INVALID_EMAIL'])
    
    if email_components[0] and email_components[1]:
        return email
    
    raise Exception(CONSTANTS['MESSAGE']['INVALID_EMAIL'])


def validate_password(passowrd: str) -> str:
    passowrd = validate_string(min_length=8)(passowrd)

    if not re.findall(CONSTANTS['REGEX']['UPPER_ALPHABET'], passowrd):
        raise Exception(
            CONSTANTS['MESSAGE']['INVALID_PASSWORD']['NO_UPPER_CASE']
        )

    if not re.findall(CONSTANTS['REGEX']['LOWER_ALPHABET'], passowrd):
        raise Exception(
            CONSTANTS['MESSAGE']['INVALID_PASSWORD']['NO_LOWER_CASE']
        )

    if not re.findall(CONSTANTS['REGEX']['SPECIAL_CHARACTERS'], passowrd):
        raise Exception(
            CONSTANTS['MESSAGE']['INVALID_PASSWORD']['NO_SPECIAL_CHARACTER']
        )
    
    return passowrd


def validate_cellphone_number(cellphone_number: str) -> str:
    try:
        cellphone_number = validate_string(min_length=11,
                                           max_length=11)(cellphone_number)

        cellphone_number = validate_int(cellphone_number)
    except Exception:
        raise Exception(
            CONSTANTS['MESSAGE']['INVALID_CONTACT']['INVALID_CELLPHONE_NUMBER']
        )

    return cellphone_number


def validate_contact(contact: dict):
    if tuple(contact.keys()) != ('email', 'cellphoneNumber'):
        raise Exception(CONSTANTS['MESSAGE']['NOT_A_CONTACT_OBJECT'])

    validate_email(contact['email'])

    validate_cellphone_number(contact['cellphoneNumber'])

    return contact


def validate_monthly_income(monthly_income: float):
    monthly_income = validate_float(monthly_income)

    if monthly_income < 0:
        raise Exception(CONSTANTS['MESSAGE']['NOT_A_POSITIVE_NUMBER'])
    
    return monthly_income


def validate_document_number(document_number: str):
    document_number = validate_string(min_length=11, max_length=14)(document_number)

    CPF_validator = validate_docbr.CPF()

    is_valid_CPF = CPF_validator.validate(document_number)

    CNPJ_validator = validate_docbr.CNPJ()

    is_valid_CNPJ = CNPJ_validator.validate(document_number)

    if is_valid_CPF or is_valid_CNPJ:
        return document_number
    
    raise Exception(CONSTANTS['MESSAGE']['INVALID_DOCUMENT_NUMBER'])


def validate_birth_date(birth_date: str):
    birth_date = validate_string(min_length=10, max_length=10)(birth_date)

    if re.match(CONSTANTS['REGEX']['SHORT_ISO8601'], birth_date):
        return birth_date
    
    raise Exception(CONSTANTS['MESSAGE']['NOT_A_SHORT_ISO_8601_DATE'])
