from http import HTTPStatus

from flask_restful import Resource

from src.controllers.validators.student_validator import StudentValidator
from src.custom_exceptions import StudentAlreadyExists
from src.services.StudentService import StudentService


class StudentController(Resource):
    def __init__(self, student_validator, student_service):
        self.__student_validator: StudentValidator = student_validator
        self.__student_service: StudentService = student_service

    def post(self):
        body: dict = self.__student_validator.validate_post()

        try:
            response: dict = self.__student_service.create(body)
        except StudentAlreadyExists:
            return {
                "message": "There is already a student registered with this document"
            }, HTTPStatus.UNPROCESSABLE_ENTITY

        return response, HTTPStatus.CREATED

    def get(self):
        arguments: dict = self.__student_validator.validate_get()
        response: dict = self.__student_service.retrieve(arguments)
        return response, HTTPStatus.OK
