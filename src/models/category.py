from src.infrastructure.database.db_connection import db


class Category(db.Model):
    __tablename__ = "categoria"

    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('nome', db.String(50), nullable=False)

    def __init__(self, **kwargs) -> None:
        self.id = kwargs.get('id')
        self.name = kwargs.get('name')

    def to_json(self) -> dict:
        return {
            'id': self.id,
            'name': self.name
        }

    def basic_to_json(self) -> dict:
        return {
            "category": self.name
        }
