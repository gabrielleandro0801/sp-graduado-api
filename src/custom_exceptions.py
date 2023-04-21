class PersonNotFound(Exception):
    def __init__(self):
        super().__init__('PersonNotFound')


class SponsorNotFound(Exception):
    def __init__(self):
        super().__init__('SponsorNotFound')


class SponsorHasStudents(Exception):
    def __init__(self):
        super().__init__('SponsorHasStudents')


class StudentAlreadyExists(Exception):
    def __init__(self):
        super().__init__('StudentAlreadyExists')
