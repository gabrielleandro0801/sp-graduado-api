from flask_restful import Api

from src.controllers.categories import CategoryController
from src.infrastructure.repositories.categories import CategoriesRepository


def add_routes(api: Api) -> Api:
    api.add_resource(
        CategoryController,
        '/v1/categories',
        resource_class_kwargs={
            'categories_repository': CategoriesRepository
        }
    )
    return api
