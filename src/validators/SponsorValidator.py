from flask_restful import reqparse

from src.validators.utils import validate_string, validate_table_id
from src.validators.person_sign_up import *
from src.common.constants import CONSTANTS


class SponsorValidator:

    def __init__(self):
        self.parser = reqparse.RequestParser()
    
    def validate_post(self):
        self.parser.add_argument(
            name='name',
            required=True,
            type=validate_string(),
            help=CONSTANTS['MESSAGE']['INVALID_NAME']
        )

        self.parser.add_argument(
            name='contact',
            required=True,
            type=validate_contact,
            help=CONSTANTS['MESSAGE']['INVALID_CONTACT']['DEFAULT']
        )

        self.parser.add_argument(
            name='password',
            required=True,
            type=validate_password,
            help=CONSTANTS['MESSAGE']['INVALID_PASSWORD']['DEFAULT']
        )

        self.parser.add_argument(
            name='monthlyIncome',
            required=True,
            type=validate_monthly_income,
            help=CONSTANTS['MESSAGE']['INVALID_MONTHLY_INCOME']
        )

        self.parser.add_argument(
            name='documentNumber',
            required=True,
            type=validate_document_number,
            help=CONSTANTS['MESSAGE']['INVALID_DOCUMENT_NUMBER']
        )

        self.parser.add_argument(
            name='birthDate',
            required=True,
            type=validate_birth_date,
            help=CONSTANTS['MESSAGE']['INVALID_BIRTH_DATE']
        )

        self.parser.add_argument(
            name='reasonsWhy',
            required=False,
            type=validate_string(),
            help=CONSTANTS['MESSAGE']['INVALID_REASONS_WHY']
        )

        return self.parser.parse_args()
    
    def validate_put(self):
        self.parser.add_argument(
            name='studentId',
            required=True,
            type=validate_table_id,
            location='args',
            help=CONSTANTS['MESSAGE']['INVALID_STUDENT_ID']
        )

        return self.parser.parse_args()
