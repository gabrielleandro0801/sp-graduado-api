from src.infrastructure.database.db_connection import db


class Types:
    STUDENT = "Aluno"
    SPONSOR = "Padrinho"


class Person(db.Model):
    __tablename__ = "pessoa"

    id = db.Column('id_pessoa', db.Integer, primary_key=True)
    name = db.Column('nome', db.String(50), nullable=False)
    email = db.Column('email', db.String(50), nullable=False)
    password = db.Column('senha', db.String(30), nullable=False)
    phone = db.Column('tel_celular', db.String(11), nullable=False)
    income = db.Column('renda_mensal', db.Float, nullable=False)
    document = db.Column('doc_cpf_ou_cnpj', db.String(14), nullable=False)
    person_type = db.Column('tipo_pessoa', db.String(8), nullable=False)
    birth_date = db.Column('data_nascimento', db.String(10), nullable=False)

    def __init__(self, **kwargs) -> None:
        self.id = kwargs.get('id')
        self.name = kwargs.get('name')
        self.email = kwargs.get('email')
        self.password = kwargs.get('password')
        self.phone = kwargs.get('phone')
        self.income = kwargs.get('income')
        self.document = kwargs.get('document')
        self.person_type = kwargs.get('person_type')
        self.birth_date = kwargs.get('birth_date')

    def to_json(self) -> dict:
        return {
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'income': self.income,
            'document': self.document,
            'person_type': self.person_type,
            'birth_date': f"{self.birth_date[0:2]}/{self.birth_date[3:5]}/{self.birth_date[6:]}"
        }

    def basic_to_json(self) -> dict:
        return {
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'income': self.income,
            'birth_date': f"{self.birth_date[0:2]}/{self.birth_date[3:5]}/{self.birth_date[6:]}"
        }


class Student(db.Model):
    __tablename__ = "aluno"

    id = db.Column('id_aluno', db.Integer, primary_key=True)
    id_sponsor = db.Column('id_padrinho', db.Integer)
    id_course_college = db.Column('id_curso_faculdade', db.Integer)
    description = db.Column('descricao', db.String(200))
    id_person = db.Column('id_pessoa', db.Integer, nullable=False)

    def __init__(self, **kwargs) -> None:
        self.id = kwargs.get('id')
        self.id_sponsor = kwargs.get('id_sponsor')
        self.description = kwargs.get('description')
        self.id_person = kwargs.get('id_person')

    def set_id_person(self, id_person: int) -> None:
        self.id_person = id_person

    def to_json(self) -> dict:
        return {
            'id': self.id,
            'sponsor_id': self.id_sponsor,
            'course_college_id': self.id_course_college,
            'description': self.description
        }

    def basic_to_json(self) -> dict:
        return {
            'id': self.id,
            'description': self.description
        }


class Sponsor(db.Model):
    __tablename__ = "padrinho"

    id = db.Column('id_padrinho', db.Integer, primary_key=True)
    reasons = db.Column('motivos', db.String(200), nullable=False)
    id_person = db.Column('id_pessoa', db.Integer, nullable=False)

    def __init__(self, **kwargs) -> None:
        self.id = kwargs.get('id')
        self.reasons = kwargs.get('reasons')
        self.id_person = kwargs.get('id_person')

    def to_json(self) -> dict:
        return {
            'id': self.id,
            'reasons': self.reasons
        }
