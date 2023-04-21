import logging
from typing import Union


class Logger:
    def __init__(self, module_name: str, event: str = None):
        logging.basicConfig(
            level=logging.DEBUG,
            format="[%(asctime)s][%(name)s][%(levelname)s] [message: %(message)s]"
        )

        self.__logger = logging.getLogger(module_name)

    @property
    def logger(self) -> logging.Logger:
        return self.__logger

    def info(self, event: str, details: Union[str, dict]):
        self.logger.info({
            'event': event,
            'details': details,
        })

    def warn(self, event: str, warning: Union[str, dict]):
        self.logger.warn({
            'event': event,
            'warning': warning,
        })

    def error(self, event: str, error: Union[str, dict]):
        self.logger.error({
            'event': event,
            'error': error,
        })

    @staticmethod
    def disable_flask_logs():
        flask_logger = logging.getLogger('werkzeug')
        flask_logger.setLevel(logging.ERROR)
