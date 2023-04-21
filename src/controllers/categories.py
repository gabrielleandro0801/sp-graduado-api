from http import HTTPStatus

from flask_restful import Resource

from src.infrastructure.repositories.categories import CategoriesRepository


class CategoryController(Resource):
    def __init__(self, categories_repository):
        self.__categories_repository: CategoriesRepository = categories_repository

    def get(self):
        categories: dict = self.__categories_repository.retrieve_categories()
        return categories, HTTPStatus.OK
