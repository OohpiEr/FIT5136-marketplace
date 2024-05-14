
class UserInputError(Exception):
    """Exception raised for errors in the user input.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="Invalid user input."):
        self.message = message
        super().__init__(self.message)
