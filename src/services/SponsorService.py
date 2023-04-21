from http import HTTPStatus

from src.custom_exceptions import SponsorHasStudents, SponsorNotFound
from src.common.constants import CONSTANTS
from src.errors.CustomException import CustomException
from src.errors.ErrorHandler import ErrorHandler
from src.infrastructure.repositories.person import StudentRepository, SponsorRepository
from src.models.person  import Sponsor
from src.models.person  import Student
from src.common.Logger import Logger
from src.models.person import Sponsor, Person
from src.infrastructure.repositories.person import PersonRepository


class SponsorService:
    def __init__(
        self,
        sponsor_repository: SponsorRepository,
        sponsor_logger: Logger,
        person_repository: PersonRepository=None,
        student_repository: StudentRepository=None
    ):
        self.__sponsor_repository = sponsor_repository
        self.__student_repository = student_repository
        self.__sponsor_logger = sponsor_logger
        self.__person_repository = person_repository


    def create(self, person: Person, sponsor: Sponsor) -> Sponsor:
        try:
            self.__sponsor_logger.info('create', 'CREATING A NEW SPONSOR')

            try:
                self.__sponsor_repository.find_one_by_document_number(
                    person.document
                )
                
                ErrorHandler.throw_exception(
                    CONSTANTS['MESSAGE']['SPONSOR_ALREADY_EXISTS'],
                    int(HTTPStatus.CONFLICT),
                    CONSTANTS['EXCEPTION']['REPOSITORY']
                )
            except CustomException as ce:
                if ce.message == CONSTANTS['MESSAGE']['SPONSOR_ALREADY_EXISTS']:
                    raise ce

            sponsor: Sponsor = self.__sponsor_repository.insert(person, sponsor)

            return sponsor.to_json(), int(HTTPStatus.CREATED)

        except CustomException as ce:
            self.__sponsor_logger.error('create', ce.to_json())

            ErrorHandler.throw_exception(
                ce.message,
                ce.status_code,
                ce.name
            )
        except Exception as e:
            self.__sponsor_logger.error('create', str(e))

            ErrorHandler.throw_exception(str(e))
    
    def sponsorize(self, sponsor_id: int, student_id: int) -> Student:
        try:
            self.__sponsor_logger.info('sponsorize', 'SPONSORIZING A STUDENT')

            self.__sponsor_repository.find_one_by_id(sponsor_id)

            student: Student = self.__student_repository.find_one_by_id(
                student_id
            )

            if student.id_sponsor is not None:
                self.__sponsor_logger.warn('sponsorize',
                                   "STUDENT ALREADY SPONSORED")

                ErrorHandler.throw_exception(
                    CONSTANTS['MESSAGE']['STUDENT_ALREADY_SPONSORED'],
                    int(HTTPStatus.CONFLICT),
                    CONSTANTS['EXCEPTION']['REPOSITORY']
                )
            
            student: Student = self.__student_repository.update_sponsor(
                student_id,
                sponsor_id
            )

            return student.to_json(), int(HTTPStatus.OK)

        except CustomException as ce:
            self.__sponsor_logger.error('create', ce.to_json())

            ErrorHandler.throw_exception(
                ce.message,
                ce.status_code,
                ce.name
            )
        except Exception as e:
            self.__sponsor_logger.error('create', str(e))

            ErrorHandler.throw_exception(str(e))
            
    def delete(self, id_sponsor: int) -> None:
        has_students: bool = self.__student_repository.check_if_id_sponsor_has_students(id_sponsor)
        if has_students:
            raise SponsorHasStudents

        sponsor: Sponsor = self.__sponsor_repository.retrieve_sponsor_by_id_sponsor(id_sponsor)
        if sponsor is None:
            raise SponsorNotFound

        person: Person = self.__person_repository.find_by_id(sponsor.id_person)

        self.__sponsor_repository.delete_sponsor(sponsor)
        self.__person_repository.delete_person(person)
