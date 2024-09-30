from pathlib import Path
from pygame import (KEYDOWN,
                    KEYUP,
                    K_LEFT,
                    K_RIGHT,
                    K_ESCAPE,
                    K_a,
                    K_d)
from pygame.image import load as load_image
from pygame.transform import scale


class Spacecraft:
    def __init__(self, screen_instance):
        # screen
        self.__screen = screen_instance
        self.__screen_rect = screen_instance.get_rect()

        # player image
        self.__standard_size_factor = 1/5
        path_image_player = Path("assets/images/player/player_spaceship.png")
        self.__image = scale(self.__image, (self.__image.get_rect().width * self.__standard_size_factor,
                                            self.__image.get_rect().height * self.__standard_size_factor))
        self.__image_rect = self.__image.get_rect()

        # initial position config
        self.__image_rect.y = self.__screen_rect.height - self.__image_rect.height - 150

        # velocity x config
        self.__velocity_x = 10
        self.__vx = 0

    def handler(self, event):
        if event.type == KEYDOWN:
            if event.key in [K_LEFT, K_a]: # to move on the left
                self.__to_left()

            if event.key in [K_RIGHT, K_d]: # to move on the right
                self.__to_right()

            if event.key == K_ESCAPE: # to shoot
                self.__shoot()

        if event.type == KEYUP:
            if event.key in [K_LEFT, K_RIGHT, K_a, K_d]:
                self.__vx = 0


    def __to_right(self):
        self.__vx = self.__velocity_x

    def __to_left(self):
        self.__vx = -self.__velocity_x

    def __move(self):
        self.__image_rect.x += self.__vx

        if self.__image_rect.x < 0:
            self.__image_rect.x = 0

        if self.__image_rect.x > self.__screen_rect.width - self.__image_rect.width:
            self.__image_rect.x = self.__screen_rect.width - self.__image_rect.width

        if self.__vx < 0:
            self.__propulsion_left()
        elif self.__vx > 0:
            self.__propulsion_right()

    def __shoot(self):
        pass

    def __propulsion_left(self):
        pass

    def __propulsion_right(self):
        pass

    def __propulsion_up(self):
        pass

    def run(self):
        self.__propulsion_up()
        self.__move()
        self.__screen.blit(self.__image, self.__image_rect)
