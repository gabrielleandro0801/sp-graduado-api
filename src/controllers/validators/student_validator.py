from flask_restful import reqparse

from src.common.constants import CONSTANTS
from src.controllers.validators.document_validator import DocumentValidator
from src.controllers.validators.types_validator import StringValidator, FloatValidator, IntValidator
from src.validators.utils import validate_table_id


class StudentValidator:
    def __init__(self, **kwargs):
        self.__document_validator: DocumentValidator = kwargs.get('document_validator')
        self.__string_validator: StringValidator = kwargs.get('string_validator')
        self.__float_validator: FloatValidator = kwargs.get('float_validator')
        self.__int_validator: IntValidator = kwargs.get('int_validator')

    def validate_post(self):
        body = reqparse.RequestParser()

        body.add_argument(
            'name',
            required=True,
            type=self.__string_validator.str_validation(max_length=50),
            help='Param is required and must be a valid string'
        )

        body.add_argument(
            'email',
            required=True,
            type=self.__string_validator.str_validation(max_length=50),
            help='Param is required and must be a valid string'
        )

        body.add_argument(
            'password',
            required=True,
            type=self.__string_validator.str_validation(max_length=30),
            help='Param is required and must be a valid string'
        )

        body.add_argument(
            'phone',
            required=True,
            type=self.__string_validator.str_validation(max_length=11),
            help='Param is required and must be a valid string'
        )

        body.add_argument(
            'income',
            required=True,
            type=self.__float_validator.validate,
            help='Param is required and must be a valid number'
        )

        body.add_argument(
            'document',
            required=True,
            type=self.__document_validator.validate_document,
            help='Param is required and must be either a valid CPF or CNPJ'
        )

        body.add_argument(
            'birth_date',
            required=True,
            type=self.__string_validator.str_validation(10),
            help='Param is required and must be a valid date'
        )

        body.add_argument(
            'description',
            required=True,
            type=self.__string_validator.str_validation(200),
            help='Param is required and must be a valid string'
        )
        return body.parse_args()

    def validate_get(self):
        body = reqparse.RequestParser()

        body.add_argument(
            'sponsor_id',
            required=False,
            type=self.__int_validator.validate_equals_zero,
            location='args',
            help='Param is optional and must be a valid number'
        )

        body.add_argument(
            'course_college_id',
            required=False,
            type=self.__int_validator.validate_equals_zero,
            location='args',
            help='Param is optional and must be a valid number'
        )

        body.add_argument(
            'page',
            required=False,
            type=self.__int_validator.validate,
            default=0,
            location='args',
            help='Param is optional and must be a valid and positive number',
        )

        body.add_argument(
            'limit',
            required=False,
            type=self.__int_validator.validate,
            default=50,
            location='args',
            help='Param is optional and must be a valid and positive number'
        )
        return body.parse_args()

    def validate_put(self):
        body = reqparse.RequestParser()

        body.add_argument(
            name='courseId',
            required=True,
            type=validate_table_id,
            location='args',
            help=CONSTANTS['MESSAGE']['INVALID_COURSE_ID']
        )

        return body.parse_args()
