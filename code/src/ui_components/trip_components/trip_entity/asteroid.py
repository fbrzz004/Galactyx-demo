from random import uniform, randint

from pygame.image import load as load_image
from pygame.transform import scale, rotate

from src.ui_components.trip_components.trip_entity.destroyable import Destroyable

from pathlib import Path

from ....fix_file_paths_compiler import resource_path

class Asteroid(Destroyable):
    def __init__(self, screen_instance):
        Destroyable.__init__(self)

        self.__screen = screen_instance
        self.__screen_rect = screen_instance.get_rect()

        # initial config image
        self.__standard_size_factor = 1/8
        self.__image = load_image(resource_path(str(Path("assets/images/asteroid/asteroid.png"))))
        self.__image = scale(self.__image, (self.__image.get_rect().width * self.__standard_size_factor,
                                            self.__image.get_rect().height * self.__standard_size_factor))
        self.__original_image = self.__image.copy()


        self.__random_scale_image()
        self.__random_rotate_image()
        self.__random_initial_position()
        self.__random_initial_velocity()


    def __random_scale_image(self):
        # random size config
        randon_size_factor = uniform(0.5, 1.5)
        self.__image_rect = self.__original_image.get_rect()
        self.__image_rect.width *= randon_size_factor
        self.__image_rect.height *= randon_size_factor

        self.__image = scale(self.__original_image, (self.__image_rect.width, self.__image_rect.height))

    def __random_rotate_image(self):
        # random rotate config
        self.__image = rotate(self.__image, uniform(0, 360))
        self.__image_rect = self.__image.get_rect()

    def __random_initial_position(self):
        self.__image_rect.x = randint(0, self.__screen_rect.width - self.__image_rect.width)
        self.__image_rect.y = -150

    def __random_initial_velocity(self):
        self.__velocity_x = uniform(-1, 1)
        self.__velocity_y = uniform(1, 8)

    def __moving(self):
        if self.__image_rect.y > self.__screen_rect.height + 5 or self._get_destroyed():
            self.__random_scale_image()
            self.__random_rotate_image()
            self.__random_initial_position()
            self.__random_initial_velocity()

            self._un_destroyed()
        else:
            self.__image_rect.y += self.__velocity_y
            self.__image_rect.x += self.__velocity_x

    def get_rect(self):
        return self.__image_rect

    def run(self):
        self.__moving()

        # draw on the screen
        self.__screen.blit(self.__image, self.__image_rect)