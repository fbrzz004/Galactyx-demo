from src.screen import Screen
from src.states.engine_state.engine_observer import EngineObserver
from sys import exit
from pygame import init, quit

class EngineState:
    def __init__(self):
        self.__context = None
        self.__screen_instance = Screen(size=(800, 600))
        self.__observer = EngineObserver()
        # initialize pygame's modules
        init()
    def exec(self):
        state = None
        while not self.__observer.exit:

            # remove objet from the previous interface if it's not None
            if state:
                del state

            # init new state (ui)
            state = self.__observer.ui_class(screen_instance=self.__screen_instance.get_screen())

            # execute the state
            state.run(machine_observer=self.__observer)

        quit()
        exit()
