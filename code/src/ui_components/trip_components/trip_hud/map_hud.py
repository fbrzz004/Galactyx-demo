from pygame.rect import Rect
from pygame.draw import rect
from pygame.image import load as load_image
from pygame.transform import scale
from pathlib import Path


class MapHud:
    def __init__(self, screen_instance):
        self.__screen = screen_instance
        self.__screen_rect = screen_instance.get_rect()

        # initialize the rects objects
        self.__width = 50
        self.__height = 400
        self.__rect = Rect(self.__screen_rect.width - self.__width - 20,
                           (self.__screen_rect.height - self.__height) / 2, self.__width, self.__height)

        self.__time_line = Rect(self.__screen_rect.width - self.__width - 20 + self.__width / 2,
                           (self.__screen_rect.height - self.__height) / 2 + self.__width / 2,
                                self.__width / 2, self.__height - self.__width)

        # set a color
        self.__outline_color = 'white'
        self.__time_line_color = 'lightgreen'

        # initialize a levels controllers
        self.__amount_jump = 5
        self.__current_jump = 0

        # load and scale the wormhole image
        self.__load_image()

        # set a four level over the time_line
        self.__list_pos_wormhole = [[self.__time_line.x + (self.__time_line.width - self.__icon_wormhole_rect.width) / 2,
                                      self.__time_line.y + self.__time_line.height * f - self.__icon_wormhole_rect.height / 2]
                                     for f in [0, .2, .4, .6, .8]]

        self.__list_pos_wormhole[0] = [self.__time_line.x + (self.__time_line.width - self.__icon_galaxy_rect.width) / 2,
                                       self.__time_line.y - self.__icon_galaxy_rect.height / 2]

        self.__icon_spacecraft_rect.x = self.__rect.x

        self.__list_pos_icon_spacecraft = [[self.__rect.x - self.__icon_spacecraft_rect.width / 2,
                                      self.__time_line.y + self.__time_line.height * f - self.__icon_spacecraft_rect.height / 2]
                                         for f in [0.9, 0.7, 0.5, 0.3, 0.1]]

        self.__activate = False

    def __load_image(self):
        factor = .25
        self.__icon_wormhole = load_image(Path('assets') / 'images' / 'wormhole' / 'icon_wormhole_hud.png')
        self.__icon_wormhole_rect = self.__icon_wormhole.get_rect()
        self.__icon_wormhole = scale(self.__icon_wormhole,
                                     (self.__icon_wormhole_rect.width * factor,
                                      self.__icon_wormhole_rect.height * factor))
        self.__icon_wormhole_rect = self.__icon_wormhole.get_rect()

        factor = .1
        self.__icon_galaxy = load_image(Path('assets') / 'images' / 'galaxies' / 'galaxy-andromeda.png')
        self.__icon_galaxy_rect = self.__icon_galaxy.get_rect()
        self.__icon_galaxy = scale(self.__icon_galaxy, (self.__icon_galaxy_rect.width * factor,
                                                        self.__icon_galaxy_rect.height * factor))
        self.__icon_galaxy_rect = self.__icon_galaxy.get_rect()

        factor = .5
        self.__icon_spacecraft = load_image(Path('assets') / 'images' / 'player' / 'spacecraft_icon.png')
        self.__icon_spacecraft_rect = self.__icon_galaxy.get_rect()
        self.__icon_spacecraft = scale(self.__icon_spacecraft, (self.__icon_spacecraft_rect.width * factor,
                                                        self.__icon_spacecraft_rect.height * factor))
        self.__icon_spacecraft_rect = self.__icon_spacecraft.get_rect()

    def __draw(self):
        # draw the time_line rect
        rect(self.__screen, self.__time_line_color, self.__time_line)

        # blit wormhole icon in all positions
        for pos in self.__list_pos_wormhole:
            if self.__list_pos_wormhole.index(pos) == 0:
                self.__screen.blit(self.__icon_galaxy, pos)
            else:
                self.__screen.blit(self.__icon_wormhole, pos)

        self.__screen.blit(self.__icon_spacecraft, self.__list_pos_icon_spacecraft[self.__current_jump])

    def set_jump(self):
        self.__current_jump += 1

    def is_end(self):
        return self.__current_jump == self.__amount_jump

    def get_level_jump(self):
        return self.__current_jump

    def activate(self):
        self.__activate = True

    def deactivate(self):
        self.__activate = False

    def run(self):
        if self.__activate:
            self.__draw()