from abc import ABC, abstractmethod
import pygame.time
from pygame.display import flip as ui_update
from pygame.event import get as get_event
from pygame import QUIT

from pygame import image
from pygame.transform import scale

class AbstractState(ABC):
    def __init__(self, screen_instance,
                 background_color = None,
                 path_image_background = None,
                 background_opacity = 255):
                 #fps=60): add FPS parameter)

        # screen instance
        self._screen = screen_instance
        self._screen_rect = self._screen.get_rect()

        # appearance features
        self._image_background = None
        self._background = background_color or 'Black'

        if path_image_background:
            self._image_background = scale(
                surface=image.load(path_image_background),
                size=self._screen_rect.size
            )
            self._image_background.set_alpha(background_opacity)

        # flag for exit of ui loop
        self._exit = False

        # Clock and FPS
        #self.clock = pygame.time.Clock()
        #self.fps = fps
        
        self.machine_observer = None  # Initialize machine_observer
    def run(self, machine_observer):
        self.machine_observer = machine_observer  # Keep machine_observer
        # man loop for this interface
        while not self._exit:
            # fill the screen with a color
            self._screen.fill(self._background)
            if self._image_background:
                self._screen.blit(self._image_background, (0, 0))

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
            # update the interface
            #pygame.display.flip()

            # Control FPS
            #self.clock.tick(self.fps)

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def handle_events(self, event, machine_observer):
        pass