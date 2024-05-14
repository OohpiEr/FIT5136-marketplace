
class RowNotFoundError(Exception):
    def __init__(self, message="Row not found in database."):
        self.message = message
        super().__init__(self.message)
