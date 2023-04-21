from flask_restful import reqparse

from src.controllers.validators.types_validator import IntValidator
from src.models.course_college import Periods, Modalities


class CollegeValidator:
    def __init__(self, int_validator, periods, modalities):
        self.__int_validator: IntValidator = int_validator
        self.__periods: Periods = periods
        self.__modalities: Modalities = modalities

    def validate_get(self) -> dict:
        body = reqparse.RequestParser()

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

    def validate_get_by_id(self) -> dict:
        body = reqparse.RequestParser()

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

        body.add_argument(
            'period',
            required=False,
            choices=(
                self.__periods.MORNING,
                self.__periods.EVENING
            ),
            location='args',
            default=None,
            help='Param is optional and must be a valid option - MATUTINO or NOTURNO'
        )

        body.add_argument(
            'modality',
            required=False,
            choices=(
                self.__modalities.PRESENTIAL,
                self.__modalities.DISTANCE,
            ),
            location='args',
            help='Param is optional and must be a valid and positive number'
        )

        body.add_argument(
            'category_id',
            required=False,
            type=self.__int_validator.validate,
            location='args',
            help='Param is optional and must be a valid and positive number'
        )
        return body.parse_args()
