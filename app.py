from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from src.common.env import PROPS
from src.common.Logger import Logger

import src.infrastructure.database.db_connection as db
import src.routes.categories as category_routes
import src.routes.colleges as college_routes
import src.routes.login as login_routes
import src.routes.sponsors as sponsor_routes
import src.routes.students as student_routes


def main():
    app: Flask = Flask(__name__)
    api: Api = Api(app)

    CORS(app)
    db.start_connection(app)

    logger = Logger('app')
    logger.disable_flask_logs()
    logger.info('main', f"SERVER UP AND RUNNING ON ADDRESS: {PROPS['HOST']}:{PROPS['PORT']}")

    api = category_routes.add_routes(api)
    api = college_routes.add_routes(api)
    api = login_routes.add_routes(api)
    api = sponsor_routes.add_routes(api)
    api = student_routes.add_routes(api)
    app.run(host=PROPS['HOST'], port=PROPS['PORT'])

    
if __name__ == '__main__':
    main()
