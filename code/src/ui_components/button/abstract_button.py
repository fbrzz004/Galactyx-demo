from abc import ABC, abstractmethod
from pygame import Rect
from pygame.mouse import get_pos as get_pos_mouse, get_pressed


class AbstractButton(ABC):
    def __init__(self,
                 position: list[float] | tuple[float, float],
                 dimension: list[float] | tuple[float, float],
                 label: str,
                 scale_on_top_of: bool = False):

        self.__scale_factor = 1.05

        less_left = dimension[0] * (self.__scale_factor - 1) / 2
        less_top = dimension[1] * (self.__scale_factor - 1) / 2

        self.__rects = {
            'default': Rect(*position, *dimension),
            'scaled' : Rect(position[0] - less_left, position[1] - less_top, dimension[0] * self.__scale_factor, dimension[1] * self.__scale_factor) if scale_on_top_of else None
        }

        self._rect = self.__rects['default']
        self._label = label

    @abstractmethod
    def draw(self, screen_instance):
        pass

    def _scale(self):
        self._rect = self.__rects['scaled'] if self.__rects['scaled'] else self.__rects['default']

    def _un_scale(self):
        self._rect = self.__rects['default']

    @abstractmethod
    def _on_top_of(self):
        pass

    @abstractmethod
    def _on_top_of_reset(self):
        pass

    @abstractmethod
    def _on_pressed(self):
        pass

    def handle_event(self):
        if self._rect.collidepoint(*get_pos_mouse()):
            self._on_top_of()

            if get_pressed()[0]:
                self._on_pressed()
                return self._label
        else:
            self._on_top_of_reset()

        return None