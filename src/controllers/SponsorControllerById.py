from http import HTTPStatus

from flask_restful import Resource

from src.custom_exceptions import SponsorHasStudents, SponsorNotFound
from src.services.SponsorService import SponsorService


class SponsorControllerById(Resource):
    def __init__(self, sponsor_service):
        self.__sponsor_service: SponsorService = sponsor_service

    def delete(self, sponsor_id: int):
        try:
            self.__sponsor_service.delete(sponsor_id)
        except SponsorNotFound:
            return {
                "message": "Sponsor not found"
            }, HTTPStatus.NOT_FOUND
        except SponsorHasStudents:
            return {
                "message": "This sponsor has students"
            }, HTTPStatus.UNPROCESSABLE_ENTITY

        return '', HTTPStatus.NO_CONTENT
