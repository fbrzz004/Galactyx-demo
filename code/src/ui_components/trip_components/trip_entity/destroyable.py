from abc import ABC, abstractmethod

class Destroyable(ABC):
    def __init__(self):
        self.__destroyed = False
        self.__energy_absorbed_capacity = 100

    def destroyed(self):
        self.__destroyed = True

    def _un_destroyed(self):
        self.__destroyed = False

    def _get_destroyed(self):
        return self.__destroyed

    @abstractmethod
    def get_rect(self):
        pass