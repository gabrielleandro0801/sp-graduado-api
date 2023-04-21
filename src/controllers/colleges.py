from http import HTTPStatus

from flask_restful import Resource

from src.controllers.validators.college_validator import CollegeValidator
from src.infrastructure.repositories.colleges import CollegesRepository
from src.infrastructure.repositories.course_college import CourseCollegeRepository


class CollegeController(Resource):
    def __init__(self, college_validator, colleges_repository):
        self.__college_validator: CollegeValidator = college_validator
        self.__colleges_repository: CollegesRepository = colleges_repository

    def get(self):
        arguments: dict = self.__college_validator.validate_get()
        colleges: dict = self.__colleges_repository.retrieve_colleges(**arguments)
        return colleges, HTTPStatus.OK


class CollegeControllerById(Resource):
    def __init__(self, college_validator, course_college_repository):
        self.__college_validator: CollegeValidator = college_validator
        self.__course_college_repository: CourseCollegeRepository = course_college_repository

    def get(self, college_id: int):
        arguments: dict = self.__college_validator.validate_get_by_id()
        response: dict = self.__course_college_repository.retrieve_by_id_college(college_id, **arguments)
        return response, HTTPStatus.OK
