from flask_restful import Api
from validate_docbr import CPF, CNPJ

from src.common.Logger import Logger
from src.common.constants import CONSTANTS
from src.controllers.StudentController import StudentController
from src.controllers.StudentControllerById import StudentControllerById
from src.controllers.validators.document_validator import DocumentValidator
from src.controllers.validators.student_validator import StudentValidator
from src.controllers.validators.types_validator import FloatValidator, IntValidator, StringValidator
from src.infrastructure.repositories.person import PersonRepository, StudentRepository
from src.services.StudentService import StudentService
from src.translators.person_translator import PersonTranslator

PATH = CONSTANTS['APPLICATION']['PATH']
PARAM = CONSTANTS['APPLICATION']['PARAM']


def add_routes(api: Api) -> Api:
    api.add_resource(
        StudentController,
        f"{PATH['BASE_PATH']}{PATH['STUDENTS']}",
        resource_class_kwargs={
            "student_service": StudentService(
                person_repository=PersonRepository,
                student_repository=StudentRepository,
                person_translator=PersonTranslator,
                student_logger=Logger(StudentService.__name__)
            ),
            "student_validator": StudentValidator(
                document_validator=DocumentValidator(
                    cpf_validator=CPF(),
                    cnpj_validator=CNPJ(),
                ),
                string_validator=StringValidator,
                int_validator=IntValidator,
                float_validator=FloatValidator
            )
        }
    )

    api.add_resource(
        StudentControllerById,
        f"{PATH['BASE_PATH']}{PATH['STUDENTS']}{PARAM['STUDENT_ID']}",
        resource_class_kwargs={
            'student_validator': StudentValidator(
                document_validator=DocumentValidator(
                    cpf_validator=CPF(),
                    cnpj_validator=CNPJ(),
                ),
                string_validator=StringValidator,
                int_validator=IntValidator,
                float_validator=FloatValidator
            ),
            'student_service': StudentService(
                student_repository=StudentRepository(Logger(StudentRepository.__name__)),
                student_logger=Logger(StudentService.__name__),
                person_repository=PersonRepository,
                person_translator=PersonTranslator
            ),
            'student_logger': Logger(StudentControllerById.__name__)
        }
    )
    return api
