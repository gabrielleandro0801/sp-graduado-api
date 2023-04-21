from http import HTTPStatus
from typing import Any, Tuple

from src.models.person import Person, Student, Types
from src.common.Logger import Logger
from src.errors.CustomException import CustomException
from src.custom_exceptions import StudentAlreadyExists
from src.errors.ErrorHandler import ErrorHandler
from src.infrastructure.repositories.person import StudentRepository, PersonRepository
from src.translators.person_translator import PersonTranslator
from src.models.person  import Student

NONE_SPONSOR_ID = 0
NONE_COURSE_COLLEGE_ID = 0


class StudentService:
    def __init__(self, student_repository: StudentRepository, student_logger: Logger, person_repository=None, person_translator=None):
        self.__student_repository = student_repository
        self.__student_logger = student_logger
        self.__person_repository: PersonRepository = person_repository
        self.__person_translator: PersonTranslator = person_translator

    def find(self, student_id: int) -> Tuple[dict, int]:
        try:
            self.__student_logger.info('find', 'FINDING ONE STUDENT')

            student: Student = self.__student_repository.find_one_by_id(student_id)

            return student.to_json(), int(HTTPStatus.OK)

        except CustomException as ce:
            self.__student_logger.error('find', ce.to_json())

            ErrorHandler.throw_exception(
                ce.message,
                ce.status_code,
                ce.name
            )
        except Exception as e:
            self.__student_logger.error('find', str(e))

            ErrorHandler.throw_exception(str(e))
    
    def update(self, student_id: int, course_id: int) -> Tuple[dict, int]:
        try:
            self.__student_logger.info('update', "UPDATING STUDENT'S COURSE")

            student: Student = self.__student_repository.update_course(
                student_id,
                course_id
            )

            return student.to_json(), int(HTTPStatus.OK)

        except CustomException as ce:
            self.__student_logger.error('update', ce.to_json())

            ErrorHandler.throw_exception(
                ce.message,
                ce.status_code,
                ce.name
            )
        except Exception as e:
            self.__student_logger.error('update', str(e))

            ErrorHandler.throw_exception(str(e))

    def delete(self, student_id: int) -> Tuple[dict, int]:
        try:
            self.__student_logger.info('delete', 'DELETING STUDENT')

            student: Student = self.__student_repository.delete_one(student_id)

            person: Person = self.__person_repository.find_by_id(student.id_person)
            self.__person_repository.delete_person(person)

            return student.to_json(), int(HTTPStatus.OK)

        except CustomException as ce:
            self.__student_logger.error('delete', ce.to_json())

            ErrorHandler.throw_exception(
                ce.message,
                ce.status_code,
                ce.name
            )
        except Exception as e:
            self.__student_logger.error('delete', str(e))

            ErrorHandler.throw_exception(str(e))
            
    def create(self, body: dict):
        student: Person = self.__person_repository.find_by_document_and_person_type(body.get('document'),
                                                                                    Types.STUDENT)

        if student is not None:
            raise StudentAlreadyExists

        person, student = self.__person_translator.retrieve_person_and_student_from_request(body)
        person: Person = self.__person_repository.save(person)

        student.set_id_person(person.id)
        student: Student = self.__student_repository.save(student)

        return {**person.to_json(), **student.basic_to_json()}

    def retrieve(self, arguments: dict):
        # se for passado 0 -> buscar os que sao none
        # se for passado X -> buscar os que sao X
        # se nao for passado -> buscar todos (nao filtrar)
        arguments = check_argument(arguments, "sponsor_id", NONE_SPONSOR_ID)
        arguments = check_argument(arguments, "course_college_id", NONE_COURSE_COLLEGE_ID)

        return self.__student_repository.find_by_sponsor_id(**arguments)


def check_argument(dictionary: dict, key: str, value: Any) -> dict:
    if dictionary.get(key) is None:
        del dictionary[key]

    if dictionary.get(key) == value:
        dictionary[key] = None

    return dictionary