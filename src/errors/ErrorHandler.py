from http import HTTPStatus

from src.common.constants import CONSTANTS
from src.errors.CustomException import CustomException


class ErrorHandler:
    @staticmethod
    def throw_exception(
            message: str,
            status_code: int = int(HTTPStatus.INTERNAL_SERVER_ERROR),
            exception_type: str = CONSTANTS['EXCEPTION']['SP_GRADUADO']
    ):
        raise CustomException(message, status_code, exception_type)

    @staticmethod
    def get_error_response(exception: CustomException):
        return {'error': exception.message}, exception.status_code,
