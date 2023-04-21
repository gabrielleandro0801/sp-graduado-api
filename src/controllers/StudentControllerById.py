from flask_restful import Resource
from typing import Tuple

from src.common.Logger import Logger
from src.services.StudentService import StudentService
from src.controllers.validators.student_validator import StudentValidator
from src.errors.CustomException import CustomException
from src.errors.ErrorHandler import ErrorHandler


class StudentControllerById(Resource):
    def __init__(
        self,
        student_validator: StudentValidator,
        student_service: StudentService,
        student_logger: Logger
    ):
        self.__student_validator = student_validator
        self.__student_service = student_service
        self.__student_logger = student_logger

    def get(self, student_id: int) -> Tuple[dict, int]:
        try:
            self.__student_logger.info('get', 'GET /students/student_id')

            response = self.__student_service.find(student_id)

            return response
        except CustomException as ce:
            self.__student_logger.error('get', ce.to_json())

            return ErrorHandler.get_error_response(ce)

    def put(self, student_id: int) -> Tuple[dict, int]:
        try:
            self.__student_logger.info('put', 'PUT /students/student_id?course_id')

            put_args = self.__student_validator.validate_put()

            response = self.__student_service.update(student_id, put_args['courseId'])

            return response
        except CustomException as ce:
            self.__student_logger.error('put', ce.to_json())

            return ErrorHandler.get_error_response(ce)

    def delete(self, student_id: int) -> Tuple[dict, int]:
        try:
            self.__student_logger.info('delete', 'DELETE /students/student_id')
            
            response = self.__student_service.delete(student_id)

            return response
        except CustomException as ce:
            self.__student_logger.error('delete', ce.to_json())

            return ErrorHandler.get_error_response(ce)
