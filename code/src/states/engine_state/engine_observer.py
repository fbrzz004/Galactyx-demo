from src.states.engine_state.states import navigation

class EngineObserver:
    def __init__(self):
        self.__exit = False
        self.__ui_class = navigation['origin_cinematic']

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
    def ui_class(self, name_ui: str):
        if name_ui in list(navigation.keys()):
            self.__ui_class = navigation[name_ui]
        else:
            raise "Not found a ui class."



