from pygame import KEYDOWN
from pygame.rect import Rect
from pygame.font import SysFont
from pygame.mouse import get_pos, get_pressed
from pygame.draw import arc, circle
from math import radians

class Card:
    def __init__(self, screen_instance, letter: str, state: str, get_factor, activator: list | None =None, max_factor=.5):
        self.__screen = screen_instance
        self.__screen_rect = screen_instance.get_rect()

        self.__letter = letter.upper()
        self.__state = state
        self.__activator = activator

        self.__get_factor = get_factor
        self.__max_factor = max_factor

        width = 60
        self.__init_angle = 0
        self.__end_angle = 180
        self.__rect = Rect((self.__screen_rect.width - width) / 2, self.__screen_rect.height - 10 - width, width, width)

        self.__render_letter()

        self.__color_load = 'green'
        self.__color_circle = 'darkgray'


    def __render_letter(self):
        font = SysFont('Arial', 35, bold=True)
        self.__text_rendered = font.render(self.__letter, True, (255, 255, 255))
        self.__text_rendered_rect = self.__text_rendered.get_rect(center=self.__rect.center)

    def __update_angle(self):
        self.__end_angle = self.__get_factor() * 360 if self.__get_factor() > self.__max_factor else 360

    def __draw(self):

        self.__update_angle()

        circle(
            surface=self.__screen,
            color=self.__color_circle,
            center=self.__rect.center,
            radius=self.__rect.width / 2,
            width=5
        )
        arc(
            surface=self.__screen,
            color=self.__color_load,
            rect=self.__rect,
            start_angle=radians(self.__init_angle),
            stop_angle=radians(self.__end_angle),
            width=5
        )

        self.__screen.blit(self.__text_rendered, self.__text_rendered_rect)

    def __is_clicked(self):
        if self.__rect.collidepoint(get_pos()) and get_pressed()[0]:
            return True
        return False

    def run(self):
        self.__draw()

    def handler(self, event):
        if self.__is_clicked():
            return self.__state

        if event.type == KEYDOWN:
            if event.key in self.__activator:
                return self.__state
        return None


