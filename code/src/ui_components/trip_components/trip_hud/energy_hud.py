from pygame import Rect
from pygame.draw import rect

from src.ui_components.name_text.name_text import NameText


class EnergyHud:
    def __init__(self, screen_instance, get_current_level, left=None, bottom=None, right=None, title="Default"):
        self.__screen = screen_instance
        self.__screen_rect = screen_instance.get_rect()

        self.__get_current_level = get_current_level()
        self.__outline_color = 'white'

        self.__max_width_rect = 400
        self.__height = 30

        self.__rect_outline = Rect(left if left else (right - self.__max_width_rect), bottom - self.__height, self.__max_width_rect, self.__height)
        self.__rect_energy = self.__rect_outline.copy()

        # title
        self.__title = NameText(
            screen_instance=screen_instance,
            size=22,
            text=title,
            on_top_of_rect=self.__rect_outline
        )

    def __set_color_energy(self):
        level = self.__rect_energy.width
        if level > 450:
            return 144, 238, 144
        elif level > 300:
            return 255, 223, 0
        elif level > 150:
            return 255, 140, 0
        elif level > 0:
            return 200, 0, 0

    def __update_the_rect_energy(self):
        # get current the level energy value
        l, max_l = self.__get_current_level()
        factor = l/max_l
        self.__rect_energy.width = int(self.__max_width_rect * factor) if int(self.__max_width_rect * factor) > 0 else 0

    def run(self):

        self.__title.show()

        self.__update_the_rect_energy()
        if self.__rect_energy.width != self.__max_width_rect:
            rect(self.__screen, self.__outline_color, self.__rect_outline, width=1, border_radius=5)

        if self.__rect_energy.width > 0:
            rect(self.__screen, self.__set_color_energy(), self.__rect_energy, border_radius=5)
