class CustomException(Exception):

    def __init__(self, message: str, status_code: int, name: str):
        super().__init__()
        self.message = message
        self.status_code = status_code
        self.name = name
    
    def to_json(self) -> dict:
        return {
            'message': self.message,
            'status_code': self.status_code,
            'name': self.name
        }
