from flask_restful import reqparse

from src.controllers.validators.types_validator import StringValidator


class LoginValidator:
    def __init__(self, string_validator):
        self.__string_validator: StringValidator = string_validator

    def validate_post(self):
        body = reqparse.RequestParser()

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
        return body.parse_args()
