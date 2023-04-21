from http import HTTPStatus

from flask_restful import Resource

import src.custom_exceptions as ce
from src.controllers.validators.login_validator import LoginValidator
from src.services.login_service import LoginService


class LoginController(Resource):
    def __init__(self, login_validator, login_service):
        self.__login_validator: LoginValidator = login_validator
        self.__login_service: LoginService = login_service

    def post(self):
        body: dict = self.__login_validator.validate_post()

        try:
            response: dict = self.__login_service.do_login(body)
        except ce.PersonNotFound:
            return {
                "message": "Not found"
            }, HTTPStatus.NOT_FOUND

        return response, HTTPStatus.OK
