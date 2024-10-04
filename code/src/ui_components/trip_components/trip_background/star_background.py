from random import randint, uniform
from pygame.draw import circle
from pygame.image import load as load_image

from pathlib import Path
from pygame.transform import scale

from ....fix_file_paths_compiler import resource_path


class StarBackground:
    def __init__(self, screen_instance, get_level_jump=None):
        # screen
        self.__screen = screen_instance
        self.__screen_rect = screen_instance.get_rect()

        # config star amount
        self.__density = .00008 # star/px^2
        self.__amount_star = int(self.__density * self.__screen_rect.width * self.__screen_rect.height)

        # star color
        self.__star_color = 'white'

        # load
        self.__load_star()

        # observer level
        self.__get_level_jump = get_level_jump

        # path for image folder
        if self.__get_level_jump is not None:
            self.__directory_path = Path('assets') / 'images' / 'ui' / 'background'
            self.__load_background()

    def __load_star(self):
        self.__star_attributes = [] # (position, velocity, radio)
        # config
        min_radio = 1
        max_radio = 2

        velocity = lambda r: .5 * r

        for _ in range(self.__amount_star):
            radio = uniform(min_radio, max_radio)

            self.__star_attributes.append([
                [randint(int(radio), int(self.__screen_rect.width - radio)), randint(0, self.__screen_rect.height)],
                velocity(radio),
                radio
            ])

    def __load_background(self):
        self.__background_image = scale(load_image(resource_path(str(self.__directory_path /
                                              f'background_game_trip_{self.__get_level_jump()}.png'))), self.__screen_rect.size)

    def __draw_stars(self):
        for position, velocity, radio in self.__star_attributes:
            circle(surface=self.__screen,
                   color=self.__star_color,
                   center=position,
                   radius=radio)

        circle(self.__screen, self.__star_color, (100, 100), 0.9)

    def __update_positions_star(self):
        for index, star_attribute in enumerate(self.__star_attributes):
            position, velocity, radio = star_attribute

            # update center position
            self.__star_attributes[index][0][1] += velocity

            # verify that the star is off the screen
            if self.__star_attributes[index][0][1] > self.__screen_rect.height + radio:
                self.__star_attributes[index][0] = [randint(int(radio), int(self.__screen_rect.width - radio)), -radio]

    def draw(self):
        if self.__get_level_jump is not None:
            self.__screen.blit(self.__background_image, (0, 0))
        self.__draw_stars()
        self.__update_positions_star()
