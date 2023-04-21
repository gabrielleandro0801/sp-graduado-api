from flask_restful import Api

from src.common.constants import CONSTANTS
from src.controllers.login import LoginController
from src.controllers.login import LoginController
from src.controllers.validators.login_validator import LoginValidator
from src.controllers.validators.types_validator import StringValidator
from src.infrastructure.repositories.person import PersonRepository
from src.services.login_service import LoginService
from src.translators.person_translator import PersonTranslator


PATH = CONSTANTS['APPLICATION']['PATH']


def add_routes(api: Api) -> Api:
    api.add_resource(
        LoginController,
        f"{PATH['BASE_PATH']}{PATH['LOGIN']}",
        resource_class_kwargs={
            'login_validator': LoginValidator(
                string_validator=StringValidator
            ),
            'login_service': LoginService(
                person_repository=PersonRepository,
                person_translator=PersonTranslator
            )
        }
    )
    return api
