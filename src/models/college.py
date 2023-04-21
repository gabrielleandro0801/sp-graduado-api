from src.infrastructure.database.db_connection import db


class College(db.Model):
    __tablename__ = "faculdade"

    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('nome', db.String(70), nullable=False)
    city = db.Column('cidade', db.String(50), nullable=False)

    def __init__(self, **kwargs) -> None:
        self.id = kwargs.get('id')
        self.name = kwargs.get('name')
        self.city = kwargs.get('city')

    def to_json(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'city': self.city
        }
