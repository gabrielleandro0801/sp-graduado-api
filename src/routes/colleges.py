from flask_restful import Api

from src.common.constants import CONSTANTS
from src.controllers.colleges import CollegeController, CollegeControllerById
from src.controllers.validators.college_validator import CollegeValidator
from src.controllers.validators.types_validator import IntValidator
from src.infrastructure.repositories.colleges import CollegesRepository
from src.infrastructure.repositories.course_college import CourseCollegeRepository
from src.models.course_college import Modalities, Periods

PATH = CONSTANTS['APPLICATION']['PATH']
PARAM = CONSTANTS['APPLICATION']['PARAM']


def add_routes(api: Api) -> Api:
    api.add_resource(
        CollegeController,
        f"{PATH['BASE_PATH']}{PATH['COLLEGES']}",
        resource_class_kwargs={
            'college_validator': CollegeValidator(
                int_validator=IntValidator,
                periods=Periods,
                modalities=Modalities
            ),
            'colleges_repository': CollegesRepository
        }
    )

    api.add_resource(
        CollegeControllerById,
        f"{PATH['BASE_PATH']}{PATH['COLLEGES']}{PARAM['COLLEGE_ID']}",
        resource_class_kwargs={
            'college_validator': CollegeValidator(
                int_validator=IntValidator,
                periods=Periods,
                modalities=Modalities
            ),
            'course_college_repository': CourseCollegeRepository
        }
    )
    return api
