from src.common.constants import CONSTANTS


def validate_int(value: int) -> int:
    if isinstance(value, str):
        value = int(value)

    if isinstance(value, int):
        return value
    
    raise Exception(CONSTANTS['MESSAGE']['NOT_AN_INTEGER'])


def validate_float(value: float) -> float:
    if isinstance(value, float):
        return value

    raise Exception(CONSTANTS['MESSAGE']['NOT_A_FLOAT'])


def validate_string(min_length: int = None, max_length: int = None):
    def validate(value: str) -> str:
        if not isinstance(value, str):
            raise Exception(CONSTANTS['MESSAGE']['NOT_A_STRING'])

        value_length = len(value)
        
        if value_length == 0:
            raise Exception(CONSTANTS['MESSAGE']['EMPTY_STRING'])
        
        if min_length is not None:
            if value_length < min_length:
                raise Exception(
                    CONSTANTS['MESSAGE']['INVALID_STRING_LENGTH'].format(
                        width='more',
                        characters=min_length
                    )
                )
        
        if max_length is not None:
            if value_length > max_length:
                raise Exception(
                    CONSTANTS['MESSAGE']['INVALID_STRING_LENGTH'].format(
                        width='less',
                        characters=max_length
                    )
                )
        
        return value
    
    return validate


def validate_table_id(table_id: int):
    table_id = validate_int(table_id)

    if table_id < 1:
        raise Exception(CONSTANTS['MESSAGE']['INVALID_TABLE_ID'])
    
    return table_id      
