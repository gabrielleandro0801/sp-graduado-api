from flask_sqlalchemy import BaseQuery, Pagination

from src.infrastructure.database.db_connection import paginated_result
from src.models.college import College


class CollegesRepository:

    @classmethod
    def retrieve_colleges(cls, page: int, limit: int) -> dict:
        query: BaseQuery = College.query.filter()
        colleges: Pagination = query.paginate(page=page, error_out=False, max_per_page=limit)

        response: dict = paginated_result(College.to_json, colleges, limit)
        return response
