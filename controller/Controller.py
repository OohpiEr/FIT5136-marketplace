from abc import ABC, abstractmethod

class Controller(ABC):

    @abstractmethod
    def handle_input(self, input):
        ...