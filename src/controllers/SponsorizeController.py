from flask_restful import Resource

from src.common.Logger import Logger
from src.errors.CustomException import CustomException
from src.errors.ErrorHandler import ErrorHandler
from src.services.SponsorService import SponsorService
from src.validators.SponsorValidator import SponsorValidator


class SponsorizeController(Resource):
    def __init__(
            self,
            sponsor_validator: SponsorValidator,
            sponsor_service: SponsorService,
            sponsor_logger: Logger
    ):
        self.__sponsor_service = sponsor_service
        self.__sponsor_validator = sponsor_validator
        self.__sponsor_logger = sponsor_logger

    def put(self, sponsor_id: int):
        try:
            self.__sponsor_logger.info(
                'put',
                'PUT /sponsors/sponsorId/sponsorize'
            )

            put_args = self.__sponsor_validator.validate_put()

            response = self.__sponsor_service.sponsorize(
                sponsor_id,
                put_args['studentId']
            )

            return response

        except CustomException as ce:
            self.__sponsor_logger.error('put', ce.to_json())

            return ErrorHandler.get_error_response(ce)
