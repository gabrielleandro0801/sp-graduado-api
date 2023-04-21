from typing import Final

from flask_sqlalchemy import BaseQuery, Pagination

from src.infrastructure.database.db_connection import paginated_result
from src.models.category import Category

DEFAULT_PAGE: Final = 1
DEFAULT_LIMIT: Final = 50


class CategoriesRepository:

    @classmethod
    def retrieve_categories(cls) -> dict:
        query: BaseQuery = Category.query.filter()
        categories: Pagination = query.paginate(page=DEFAULT_PAGE, error_out=False, max_per_page=DEFAULT_LIMIT)

        response: dict = paginated_result(Category.to_json, categories, DEFAULT_LIMIT)
        return response
