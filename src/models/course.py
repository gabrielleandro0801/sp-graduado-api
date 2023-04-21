from src.infrastructure.database.db_connection import db


class Course(db.Model):
    __tablename__ = "curso"

    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('nome', db.String(75), nullable=False)
    id_category = db.Column('id_categoria', db.Integer, nullable=False)

    def __init__(self, **kwargs) -> None:
        self.id = kwargs.get('id')
        self.name = kwargs.get('name')
        self.id_category = kwargs.get('id_category')

    def basic_to_json(self) -> dict:
        return {
            "course": self.name
        }
