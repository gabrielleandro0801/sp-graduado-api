from flask_restful import Api

from src.common.constants import CONSTANTS
from src.common.Logger import Logger
from src.controllers.SponsorController import SponsorController
from src.controllers.SponsorizeController import SponsorizeController
from src.services.SponsorService import SponsorService
from src.validators.SponsorValidator import SponsorValidator

from src.controllers.SponsorControllerById import SponsorControllerById
from src.infrastructure.repositories.person import StudentRepository, SponsorRepository, PersonRepository
from src.services.SponsorService import SponsorService

PATH = CONSTANTS['APPLICATION']['PATH']
PARAM = CONSTANTS['APPLICATION']['PARAM']


def add_routes(api: Api) -> Api:
    api.add_resource(
        SponsorController,
        f"{PATH['BASE_PATH']}{PATH['SPONSORS']}",
        resource_class_kwargs={
            'sponsor_validator': SponsorValidator(),
            'sponsor_service': SponsorService(
                SponsorRepository(Logger(SponsorRepository.__name__)),
                Logger(SponsorService.__name__)
            ),
            'sponsor_logger': Logger(SponsorController.__name__)
        }
    )

    api.add_resource(
        SponsorControllerById,
        f"{PATH['BASE_PATH']}{PATH['SPONSORS']}{PARAM['SPONSOR_ID']}",
        resource_class_kwargs={
            'sponsor_service': SponsorService(
                student_repository=StudentRepository,
                sponsor_repository=SponsorRepository,
                person_repository=PersonRepository,
                sponsor_logger=Logger(SponsorControllerById.__name__)
            )
        }
    )
    
    api.add_resource(
        SponsorizeController,
        f"{PATH['BASE_PATH']}{PATH['SPONSORS']}{PARAM['SPONSOR_ID']}/sponsorize",
        resource_class_kwargs={
            'sponsor_validator': SponsorValidator(),
            'sponsor_service': SponsorService(
                sponsor_repository=SponsorRepository(Logger(SponsorRepository.__name__)),
                sponsor_logger=Logger(SponsorService.__name__),
                student_repository=StudentRepository(Logger(StudentRepository.__name__))
            ),
            'sponsor_logger': Logger(SponsorizeController.__name__)
        }
    )
        
    return api
