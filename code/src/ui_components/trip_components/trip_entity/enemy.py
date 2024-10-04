from random import uniform

from pygame.image import load as load_image
from pygame.transform import rotate, scale

# for initial behavior of enemy's auto moving
from pygame.mouse import get_pos

from pathlib import Path

from ....fix_file_paths_compiler import resource_path


class Enemy:
    def __init__(self, screen_instance):
        self.__screen = screen_instance
        self.__screen_rect = screen_instance.get_rect()

        self.__image = rotate(surface=load_image(resource_path(str(Path("assets/images/enemy/enemy.png")))),
                              angle=180)

        self.__standard_scale_factor = 1/6
        self.__image = scale(surface=self.__image, size=(self.__image.get_width() * self.__standard_scale_factor,
                                                         self.__image.get_height() * self.__standard_scale_factor))

        self.__image_rect = self.__image.get_rect()
        self.__image_rect.y = 10
        self.__image_rect.x = uniform(self.__screen_rect.width * 1/4, self.__screen_rect.width * 3/4)

    def __auto_behavior(self):
        self.__image_rect.x = get_pos()[0]

    def run(self):
        self.__auto_behavior()
        self.__screen.blit(self.__image, self.__image_rect)