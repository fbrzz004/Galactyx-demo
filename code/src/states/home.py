from pygame.display import flip as ui_update
from pygame.color import Color
from pygame.event import get as get_event
from pygame import QUIT

from src.ui_components.button.button_group import ButtonGroup

class Home:
    def __init__(self, screen_instance):
        # screen instance
        self.__screen = screen_instance
        self.__screen_rect = self.__screen.get_rect()

        # appearance features
        self.__background = Color("white")

        self.__buttons = ButtonGroup(
            screen_rect=self.__screen_rect,
            labels=['Play', 'Options', 'Exit'],
            dimension=(100, 200),
            vertical_center=True,
            horizontal_center=True
        )

        # flag for exit of ui loop
        self.__exit = False

    def run(self, machine_observer):
        # man loop for this interface
        while not self.__exit:
            # fill the screen with a color
            self.__screen.fill(self.__background)

            # draw buttons
            self.__buttons.draw(self.__screen)

            # manage the events queue
            for event in get_event():
                if event.type == QUIT:
                    self.__exit = True
                    machine_observer.exit = True

            # update the interface
            ui_update()