from pygame import Rect
from pygame.draw import rect 


class EnergyHud:
    def __init__(self, screen_instance, get_current_level):
        self.__screen = screen_instance
        self.__screen_rect = screen_instance.get_rect()

        self.__get_current_level = get_current_level()
        self.__outline_color = 'white'

        self.__max_width_rect = 400
        self.__height = 60

        self.__rect_outline = Rect(10, self.__screen_rect.height - self.__height - 10, self.__max_width_rect, self.__height)
        self.__rect_energy = self.__rect_outline.copy()

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
        self.__update_the_rect_energy()
        if self.__rect_energy.width != self.__max_width_rect:
            rect(self.__screen, self.__outline_color, self.__rect_outline, width=1, border_radius=5)

        if self.__rect_energy.width > 0:
            rect(self.__screen, self.__set_color_energy(), self.__rect_energy, border_radius=5)
