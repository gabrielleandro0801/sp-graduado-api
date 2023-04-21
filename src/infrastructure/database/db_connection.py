from typing import List, Any

from flask import Flask
from flask_sqlalchemy import SQLAlchemy, Pagination, BaseQuery

from src.common.env import PROPS


db: SQLAlchemy = SQLAlchemy()


def start_connection(app: Flask) -> None:
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = PROPS['DATABASE']['URI']
    db.init_app(app=app)


def add_entities(query: BaseQuery, *args) -> BaseQuery:
    for arg in args:
        query = query.add_entity(arg)
    return query


def get_page_number(p: int) -> int or None:
    return p - 1 if p is not None else None


def paginated_result(method: Any, result: Pagination, limit: int) -> dict:
    items: List[dict] = list(
        map(
            method,  # Method we are iterating the loop
            result.items  # Loop we are iterating
        )
    )

    return {
        "previousPage": get_page_number(result.prev_num),
        "currentPage": get_page_number(result.page),
        "nextPage": get_page_number(result.next_num),
        "last": not result.has_next,
        "totalPages": result.pages,
        "totalItems": result.total,
        "maxItemsPerPage": limit,
        "totalItemsPage": len(items),
        "items": items
    }


def paginated_join_result(result: Pagination, limit: int, methods: List) -> dict:
    items: List[dict] = []

    for item in result.items:
        item_for_list = {}
        for index, element in enumerate(item):
            item_for_list.update(methods[index](element))
        items.append(item_for_list)

    return {
        "previousPage": get_page_number(result.prev_num),
        "currentPage": get_page_number(result.page),
        "nextPage": get_page_number(result.next_num),
        "last": not result.has_next,
        "totalPages": result.pages,
        "totalItems": result.total,
        "maxItemsPerPage": limit,
        "totalItemsPage": len(items),
        "items": items
    }
