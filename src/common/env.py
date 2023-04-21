import os
from dotenv import load_dotenv

load_dotenv()

PROPS = {
    'ENV': os.getenv('ENV', 'dev'),
    'HOST': os.getenv('HOSTNAME', '0.0.0.0'),
    'PORT': os.getenv('PORT', 5000),
    'DATABASE': {
        '_HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '5432'),
        'USER': os.getenv('DB_USER', 'postgres'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'password'),
        'NAME': os.getenv('DB_DATABASE', 'postgres'),
        'URI': os.getenv(
            'DATABASE_URI',
            f'postgresql://postgres:password@localhost:5432/postgres'
        ),
    }
}
