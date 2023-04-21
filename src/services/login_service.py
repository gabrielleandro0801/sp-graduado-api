from typing import Any

import src.custom_exceptions as ce
from src.infrastructure.repositories.person import PersonRepository, BaseRepository
from src.models.person import Person
from src.translators.person_translator import PersonTranslator


class LoginService:
    def __init__(self, person_repository, person_translator):
        self.__person_repository: PersonRepository = person_repository
        self.__person_translator: PersonTranslator = person_translator

    def do_login(self, body) -> dict:
        person: Person = self.__person_repository.validate_login(body)

        if person is None:
            raise ce.PersonNotFound

        repository: BaseRepository = self.__person_translator.retrieve_repository_from_person_type(person.person_type)
        complementary_data: Any = repository.retrieve_data_from_id_person(person.id)

        response: dict = person.to_json()
        response.update(complementary_data.to_json())
        return response
