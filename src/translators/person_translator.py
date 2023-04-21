from typing import Tuple

from src.infrastructure.repositories.person import SponsorRepository, StudentRepository, BaseRepository
from src.models.person import Person, Student, Types


class PersonTypes:
    STUDENT = 'Aluno'
    SPONSOR = 'Padrinho'


class PersonTranslator:

    @classmethod
    def retrieve_repository_from_person_type(cls, person_type: int) -> BaseRepository:
        options: dict = {
            PersonTypes.STUDENT: StudentRepository,
            PersonTypes.SPONSOR: SponsorRepository
        }

        return options[person_type]

    @classmethod
    def retrieve_person_and_student_from_request(cls, body: dict) -> Tuple[Person, Student]:
        person = Person(
            name=body.get('name'),
            email=body.get('email'),
            password=body.get('password'),
            phone=body.get('phone'),
            income=body.get('income'),
            document=body.get('document'),
            birth_date=body.get('birth_date'),
            person_type=Types.STUDENT
        )
        student = Student(
            id_person=body.get('id_person'),
            description=body.get('description')
        )

        return person, student
