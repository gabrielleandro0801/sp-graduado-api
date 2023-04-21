class IntValidator:

    @classmethod
    def validate(cls, value: int) -> int:
        try:
            value = int(value)
        except ValueError:
            raise Exception

        if type(value) is not int:
            raise Exception

        if value <= 0:
            raise Exception

        return value

    @classmethod
    def validate_equals_zero(cls, value: int) -> int:
        try:
            value = int(value)
        except ValueError:
            raise Exception

        if type(value) is not int:
            raise Exception

        return value


class StringValidator:

    @classmethod
    def str_validation(cls, max_length=None):
        def validate(string: str) -> str:
            if type(string) is not str:
                raise Exception

            if len(string) == 0:
                raise Exception

            if max_length is not None:
                if len(string) > max_length:
                    raise Exception

            return string

        return validate


class FloatValidator:

    @classmethod
    def validate(cls, value: float) -> float:
        if type(value) not in [float, int]:
            raise Exception

        if value <= 0:
            raise Exception

        return value
