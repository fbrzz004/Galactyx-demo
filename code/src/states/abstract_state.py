from abc import ABC, abstractmethod

from pygame.display import flip as ui_update
from pygame.event import get as get_event
from pygame import QUIT

class AbstractState(ABC):
    def __init__(self, screen_instance, background_color = None, image_background = None):
        # screen instance
        self._screen = screen_instance
        self._screen_rect = self._screen.get_rect()

        # appearance features
        self._image_background = image_background
        self._background = background_color

        # flag for exit of ui loop
        self._exit = False

    def run(self, machine_observer):
        # man loop for this interface
        while not self._exit:
            # fill the screen with a color
            self._screen.fill(self._background)

            # drawing zone
            self.draw()

            # manage the events queue
            for event in get_event():
                if event.type == QUIT:
                    self._exit = True
                    machine_observer.exit = True
                else:
                    # manage other events
                    self.handle_events(event, machine_observer)

            # update the interface
            ui_update()

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def handle_events(self, event, machine_observer):
        pass