from flask_restful import Resource

from src.common.Logger import Logger
from src.errors.CustomException import CustomException
from src.errors.ErrorHandler import ErrorHandler
from src.models.person import Person, Sponsor
from src.services.SponsorService import SponsorService
from src.validators.SponsorValidator import SponsorValidator


class SponsorController(Resource):
    def __init__(
            self,
            sponsor_validator: SponsorValidator,
            sponsor_service: SponsorService,
            sponsor_logger: Logger
    ):
        self.__sponsor_validator = sponsor_validator
        self.__sponsor_service = sponsor_service
        self.__sponsor_logger = sponsor_logger

    def post(self):
        try:
            self.__sponsor_logger.info('post', 'POST /sponsors')

            post_body = self.__sponsor_validator.validate_post()

            new_person = Person(
                name=post_body['name'],
                password=post_body['password'],
                email=post_body['contact']['email'],
                phone=post_body['contact']['cellphoneNumber'],
                income=post_body['monthlyIncome'],
                document=post_body['documentNumber'],
                person_type="Padrinho",
                birth_date=post_body['birthDate'],
            )
            new_sponsor: Sponsor = Sponsor(
                reasons=post_body['reasonsWhy'],
            )

            response = self.__sponsor_service.create(new_person, new_sponsor)

            return response

        except CustomException as ce:
            self.__sponsor_logger.error('post', ce.to_json())

            return ErrorHandler.get_error_response(ce)
