from UserInputError import UserInputError
from AdminInterface import AdminInterface
from RowNotFoundError import RowNotFoundError
from domain.Admin import Admin


class Controller():
    def __init__(self, inventory):
        self.inventory = inventory
