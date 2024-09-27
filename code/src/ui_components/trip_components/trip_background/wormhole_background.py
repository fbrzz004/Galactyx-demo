from random import randint, uniform
from pygame.draw import rect

class WormholeBackground:
    def __init__(self, screen_instance):
        # screen
        self.__screen = screen_instance
        self.__screen_rect = screen_instance.get_rect()

        self.__random_color_pattern = [
            [0, 50, 0, 50, 150, 255],
            [0, 50, 100, 200, 200, 255],
            [100, 180, 0, 50, 150, 255],
            [200, 255, 200, 255, 200, 255],
            [150, 255, 0, 50, 0, 50],
            [100, 255, 100, 255, 100, 255],
        ]

    def __draw_segments(self):
        # segments attributes
        min_width = 1
        max_width = 4

        for _ in range(randint(int(self.__screen_rect.width / max_width), int(self.__screen_rect.width / min_width))):
            rect(surface=self.__screen,
                color=random_color(*self.__random_color_pattern[randint(0, len(self.__random_color_pattern) - 1)]),
                rect=(randint(0, self.__screen_rect.width), 0,
                      uniform(min_width, max_width), self.__screen_rect.height))

    def draw(self):
        self.__draw_segments()

random_color = lambda a1, b1, a2, b2, a3, b3: (randint(a1, b1), randint(a2, b2), randint(a3, b3))