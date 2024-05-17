
class RowNotFoundError(Exception):
    """Exception for when the row is not found in the database. Extends from python Exception.

    :param Exception: python Exception class
    """
    def __init__(self, message="Row not found in database."):
        self.message = message
        super().__init__(self.message)
