from abc import abstractmethod, ABC
from typing import Any
from http import HTTPStatus
from flask_sqlalchemy import BaseQuery, Pagination

from src.infrastructure.database.db_connection import db, paginated_join_result, add_entities
from src.models.person import Person, Student, Sponsor, Types
from src.errors.ErrorHandler import ErrorHandler
from src.common.Logger import Logger
from src.common.constants import CONSTANTS


class BaseRepository(ABC):
    @abstractmethod
    def retrieve_data_from_id_person(self, id_person: int) -> Any:
        pass


class PersonRepository:

    @classmethod
    def validate_login(cls, kwargs) -> Person or None:
        query: BaseQuery = Person.query.filter(Person.email == kwargs.get('email'),
                                               Person.password == kwargs.get('password'))
        person: Person or None = query.first()
        return person

    @classmethod
    def find_by_document_and_person_type(cls, document: str, person_type: str) -> Person or None:
        query: BaseQuery = Person.query.filter(Person.document == document, Person.person_type == person_type)
        person: Person or None = query.first()
        return person

    @classmethod
    def find_by_id(cls, id_person: int) -> Person:
        query: BaseQuery = Person.query.filter(Person.id == id_person)
        person: Person = query.first()
        return person

    @classmethod
    def delete_person(cls, person: Person) -> None:
        db.session.delete(person)
        db.session.commit()

    @classmethod
    def save(cls, person: Person) -> Person:
        db.session.add(person)
        db.session.commit()
        return person


class StudentRepository(BaseRepository):
    def __init__(self, logger: Logger):
        self.__repository_logger = logger
    
    def find_one_by_id(self, student_id: int) -> Student:
        self.__repository_logger.info('find_one_by_id',
                           'SEARCHING FOR THE STUDENT IN THE DATABASE')

        query: BaseQuery = Student.query.filter_by(id=student_id)
        student = query.first()

        if student is None:
            self.__repository_logger.warn('find_one_by_id', 'STUDENT NOT FOUND IN THE DATABASE')

            ErrorHandler.throw_exception(
                CONSTANTS['MESSAGE']['STUDENT_NOT_FOUND'],
                int(HTTPStatus.NOT_FOUND),
                CONSTANTS['EXCEPTION']['REPOSITORY']
            )
        
        self.__repository_logger.info(
            'find_one_by_id',
            {
                'message': 'STUDENT FOUND',
                'student': student.to_json()
            }
        )

        return student

    def update_course(self, student_id: int, course_id: int) -> Student:
        self.__repository_logger.info('update_course', 'UPDATING STUDENT COURSE')

        updated_student_quantity: int = db.session.query(Student).filter(
            Student.id == student_id
        ).update({Student.id_course_college: course_id})

        if updated_student_quantity == 0:
            self.__repository_logger.warn('update_course',
                               "STUDENT NOT FOUND. CAN'T UPDATE IT")

            ErrorHandler.throw_exception(
                CONSTANTS['MESSAGE']['STUDENT_NOT_FOUND'],
                int(HTTPStatus.NOT_FOUND),
                CONSTANTS['EXCEPTION']['REPOSITORY']
            )
        
        db.session.commit()

        updated_student: Student = self.find_one_by_id(student_id)

        self.__repository_logger.info(
            'update_course',
            {
                'message': 'STUDENT COURSE UPDATED',
                'student': updated_student.to_json()
            }
        )

        return updated_student
    
    def update_sponsor(self, student_id: int, sponsor_id: int) -> Student:
        self.__repository_logger.info('update_sponsor', 'UPDATING THE STUDENT SPONSOR')

        updated_student_quantity: int = db.session.query(Student).filter(
            Student.id == student_id
        ).update({Student.id_sponsor: sponsor_id})

        if updated_student_quantity == 0:
            self.__repository_logger.warn('update_sponsor',
                               "STUDENT NOT FOUND. CAN'T UPDATE IT")

            ErrorHandler.throw_exception(
                CONSTANTS['MESSAGE']['STUDENT_NOT_FOUND'],
                int(HTTPStatus.NOT_FOUND),
                CONSTANTS['EXCEPTION']['REPOSITORY']
            )
        
        db.session.commit()

        updated_student: Student = self.find_one_by_id(student_id)

        self.__repository_logger.info(
            'update_sponsor',
            {
                'message': 'STUDENT SPONSOR UPDATED',
                'student': updated_student.to_json()
            }
        )

        return updated_student

    def delete_one(self, student_id: int) -> Student:
        student: Student = self.find_one_by_id(student_id)

        self.__repository_logger.info('delete_one', 'DELETING STUDENT FROM THE DATABASE')
        
        db.session.delete(student)

        db.session.commit()

        self.__repository_logger.info(
            'delete_one',
            {
                'message': 'STUDENT DELETED',
                'student': student.to_json()
            }
        )

        return student
    
    
    @classmethod
    def retrieve_data_from_id_person(cls, id_person: int) -> Student:
        query: BaseQuery = Student.query.filter(Student.id_person == id_person)
        student: Student = query.first()
        return student

    @classmethod
    def check_if_id_sponsor_has_students(cls, id_sponsor: int) -> bool:
        query: BaseQuery = Student.query.filter(Student.id_sponsor == id_sponsor)
        amount: int = query.count()
        return amount > 0

    @classmethod
    def save(cls, student: Student) -> Student:
        db.session.add(student)
        db.session.commit()
        return student

    @classmethod
    def find_by_sponsor_id(cls, **kwargs) -> Person or None:
        query: BaseQuery = Student.query.filter()\
            .join(Person, Person.id == Student.id_person)

        if 'sponsor_id' in kwargs:
            query = query.filter(Student.id_sponsor == kwargs.get('sponsor_id'))

        if 'course_college_id' in kwargs:
            query = query.filter(Student.id_course_college == kwargs.get('course_college_id'))

        page, limit = kwargs.get('page'), kwargs.get('limit')
        query = add_entities(query, Person)
        persons: Pagination = query.paginate(page=page, error_out=False, per_page=limit, max_per_page=limit)

        response: dict = paginated_join_result(persons, limit, [Student.to_json, Person.basic_to_json])
        return response


class SponsorRepository(BaseRepository):
    def __init__(self, logger: Logger):
        self.__repository_logger = logger
        
    @classmethod
    def retrieve_data_from_id_person(cls, id_person: int) -> Sponsor:
        query: BaseQuery = Sponsor.query.filter(Sponsor.id_person == id_person)
        sponsor: Sponsor = query.first()
        return sponsor

    @classmethod
    def retrieve_sponsor_by_id_sponsor(cls, id_sponsor: int) -> Sponsor or None:
        query: BaseQuery = Sponsor.query.filter(Sponsor.id == id_sponsor)
        sponsor: Sponsor = query.first()
        return sponsor

    @classmethod
    def delete_sponsor(cls, sponsor: Sponsor) -> None:
        db.session.delete(sponsor)
        db.session.commit()

    def insert(self, person: Person, sponsor: Sponsor) -> Sponsor:
        try:
            self.__repository_logger.info(
                'insert',
                {
                    'message':'INSERTING THE NEW SPONSOR INTO THE DATABASE',
                    'sponsor': sponsor.to_json()
                }
            )

            person = PersonRepository.save(person)
            sponsor.id_person = person.id
            
            db.session.add(sponsor)
            db.session.commit()

        except Exception as e:
            self.__repository_logger.error(
                'insert',
                {
                    'message': 'FAILED TO INSERT SPONSOR INTO THE DATABASE',
                    'error': str(e)
                }
            )

            ErrorHandler.throw_exception(
                CONSTANTS['MESSAGE']['FAILED_TO_EXECUTE_SQL_TRANSACTION'],
                int(HTTPStatus.INTERNAL_SERVER_ERROR),
                CONSTANTS['EXCEPTION']['REPOSITORY']
            )


        return sponsor

    def find_one_by_id(self, sponsor_id: int):
        self.__repository_logger.info('find_one_by_id',
                           'SEARCHING FOR THE SPONSOR IN THE DATABASE')
        
        query: BaseQuery = Sponsor.query.filter_by(id=sponsor_id)
        sponsor = query.first()

        if sponsor is None:
            self.__repository_logger.warn('find_one_by_id',
                               'SPONSOR NOT FOUND IN THE DATABASE')
            
            ErrorHandler.throw_exception(
                CONSTANTS['MESSAGE']['SPONSOR_NOT_FOUND'],
                int(HTTPStatus.NOT_FOUND),
                CONSTANTS['EXCEPTION']['REPOSITORY']
            )

        self.__repository_logger.info('find_one_by_id',
            {
                'message': 'SPONSOR FOUND',
                'sponsor': sponsor.to_json()
            }
        )

        return sponsor
    
    def find_one_by_document_number(self, sponsor_document_number: int):
        self.__repository_logger.info('find_one_by_document_number',
                           'SEARCHING FOR THE SPONSOR IN THE DATABASE')
        
        sponsor = PersonRepository.find_by_document_and_person_type(sponsor_document_number, Types.SPONSOR)

        if sponsor is None:
            self.__repository_logger.warn('find_one_by_document_number',
                               'SPONSOR NOT FOUND IN THE DATABASE')
            
            ErrorHandler.throw_exception(
                CONSTANTS['MESSAGE']['SPONSOR_NOT_FOUND'],
                int(HTTPStatus.NOT_FOUND),
                CONSTANTS['EXCEPTION']['REPOSITORY']
            )

        self.__repository_logger.info('find_one_by_document_number',
            {
                'message': 'SPONSOR FOUND',
                'sponsor': sponsor.to_json()
            }
        )

        return sponsor
