from flask_sqlalchemy import BaseQuery, Pagination

from src.infrastructure.database.db_connection import add_entities, paginated_join_result
from src.models.category import Category
from src.models.course import Course
from src.models.course_college import CourseCollege


class CourseCollegeRepository:

    @classmethod
    def retrieve_by_id_college(cls, id_college: int, **kwargs) -> dict:
        query: BaseQuery = CourseCollege.query.filter(CourseCollege.id_college == id_college)\
            .join(Course, CourseCollege.id_course == Course.id)\
            .join(Category, Course.id_category == Category.id)

        if kwargs.get('period') is not None:
            query = query.filter(CourseCollege.period == kwargs.get('period'))

        if kwargs.get('modality') is not None:
            query = query.filter(CourseCollege.modality == kwargs.get('modality'))

        if kwargs.get('category_id') is not None:
            query = query.filter(Course.id_category == kwargs.get('category_id'))

        page, limit = kwargs.get('page'), kwargs.get('limit')
        query = add_entities(query, Course, Category)

        response: Pagination = query.paginate(page=page, per_page=limit, error_out=False, max_per_page=limit)
        return paginated_join_result(response, limit, [CourseCollege.to_json, Course.basic_to_json,
                                                       Category.basic_to_json])
