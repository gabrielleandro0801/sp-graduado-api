CONSTANTS = {
    'APPLICATION': {
        'PATH': {
            'BASE_PATH': '/v1',
            'COLLEGES': '/colleges',
            'LOGIN': '/login',
            'SPONSORS': '/sponsors',
            'DO': '/do',
            'STUDENTS': '/students'
        },
        'PARAM': {
            'COLLEGE_ID': '/<int:college_id>',
            'SPONSOR_ID': '/<int:sponsor_id>',
            'STUDENT_ID': '/<int:student_id>',
        },
        'PERSON_TYPE': {
            'STUDENT': 'Aluno',
            'SPONSOR': 'Padrinho',
        },
    },
    'EXCEPTION': {
        'SP_GRADUADO': 'SPGraduadoException',
        'REPOSITORY': 'RepositoryException',
    },
    'MESSAGE': {
        'FAILED_TO_EXECUTE_SQL_TRANSACTION': 'An error occured while trying to perform a databse action',
        'INVALID_COURSE_ID': 'The courseId param is required and must be a valid positive integer: {error_msg}',
        'INVALID_STUDENT_ID': 'The studentId param is required and must be a valid positive integer: {error_msg}',
        'INVALID_NAME': 'The name param is required and must be a string between 5 and 50 characters: {error_msg}',
        'INVALID_CONTACT': {
            'DEFAULT': 'The contact param must contain only the person email and cellphoneNumber: {error_msg}',
            'INVALID_EMAIL': 'The email param must be a non empty string and a valid email address',
            'INVALID_CELLPHONE_NUMBER': 'The cellphoneNumber must be a valid non empty string containing 11 digits',
        },
        'INVALID_PASSWORD': {
            'DEFAULT': 'The password param must be a valid non empty string: {error_msg}',
            'NO_UPPER_CASE': 'The passowrd must contain at least one upper case letter',
            'NO_LOWER_CASE': 'The passowrd must contain at least one lower case letter',
            'NO_SPECIAL_CHARACTER': 'The passowrd must contain at least one special character',
        },
        'INVALID_MONTHLY_INCOME': 'The monthlyIncome param is required and must be a positive floating point number: {error_msg}',
        'INVALID_DOCUMENT_NUMBER': 'The given documentNumber is not valid, the document number must be a valid string containing only digits',
        'INVALID_BIRTH_DATE': 'The birthDate param is required and must be a non empty string with the format "YYYY-MM-DD": {error_msg}',
        'INVALID_REASONS_WHY': 'The reasonWhy param must be a non empty string',
        'INVALID_TABLE_ID': 'The given number is not a valid table id',
        'NOT_AN_INTEGER': 'The given value is not a valid integer',
        'NOT_A_FLOAT': 'The given value is not a valid floating point number',
        'NOT_A_STRING': 'The given value is not a valid string',
        'NOT_A_CONTACT_OBJECT': 'The given value is not a valid contact object',
        'NOT_A_POSITIVE_NUMBER': 'The given number is not a positive number',
        'NOT_A_DOCUMENT_NUMBER': 'The documentNumber param is required and must be a valid non empty string containig 11 or 14 digits',
        'NOT_A_PERSON_TYPE': 'The personType param is required and must be a non empty string equal to "Aluno" or "Padrinho"',
        'NOT_A_SHORT_ISO_8601_DATE': 'The given string is not a date in the format "YYYY-MM-DD"',
        'STUDENT_NOT_FOUND': 'Student Not Found',
        'SPONSOR_NOT_FOUND': 'Sponsor Not Found',
        'SPONSOR_ALREADY_EXISTS': 'Sponsor Already Exists',
        'STUDENT_ALREADY_SPONSORED': 'Student Already Sponsored',
        'EMPTY_STRING': 'The given value is an empty string',
        'INVALID_STRING_LENGTH': 'The given string must have {width} than {characters} characters',
    },
    'REGEX': {
        'UPPER_ALPHABET': '[A-Z]+',
        'LOWER_ALPHABET': '[a-z]+',
        'SPECIAL_CHARACTERS': """[!@#$%&*\(\)_\-+='"|\\<,>.:;?\/\}\]\{\[]+""",
        'SHORT_ISO8601': '[0-9]{4}\-[0-9]{2}\-[0-9]{2}'
    }
}
