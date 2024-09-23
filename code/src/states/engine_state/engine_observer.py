from ..home import Home as DefaultState

class EngineObserver:
    def __init__(self):
        self.__exit = False
        self.__ui_class = DefaultState

    @property
    def exit(self) -> bool:
        return self.__exit

    @property
    def ui_class(self):
        return self.__ui_class

    @exit.setter
    def exit(self, value):
        self.__exit = value

    @ui_class.setter
    def ui_class(self, value):
        self.__ui_class = value

