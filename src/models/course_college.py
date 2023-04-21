from src.infrastructure.database.db_connection import db


class Periods:
    MORNING = "Matutino"
    EVENING = "Noturno"


class Modalities:
    PRESENTIAL = "Presencial"
    DISTANCE = "EAD"


class CourseCollege(db.Model):
    __tablename__ = "curso_faculdade"

    id_course_college = db.Column('id_curso_faculdade', db.Integer, primary_key=True)
    id_college = db.Column('id_faculdade', db.Integer, nullable=False)
    id_course = db.Column('id_curso', db.Integer, nullable=False)
    semesters = db.Column('semestres', db.Integer, nullable=False)
    period = db.Column('turno', db.String(10), nullable=False)
    modality = db.Column('modalidade', db.String(10), nullable=False)

    def __init__(self, kwargs):
        self.id_course_college = kwargs.get('id_course_college')
        self.id_course = kwargs.get('id_course')
        self.id_college = kwargs.get('id_college')
        self.semesters = kwargs.get('semesters')
        self.period = kwargs.get('period')
        self.modality = kwargs.get('modality')

    def to_json(self) -> dict:
        return {
            'id': self.id_course_college,
            'semesters': self.semesters,
            'period': self.period,
            'modality': self.modality
        }
