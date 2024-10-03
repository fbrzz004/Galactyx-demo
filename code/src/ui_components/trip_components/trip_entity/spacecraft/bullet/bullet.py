from pygame.draw import rect
from pygame import Rect
from math import pow

class Bullet:
    def __init__(self, screen_instance,
                 x_muzzle: list, y_muzzle: int,
                 velocity_y=-20):
        self.__screen = screen_instance
        self.__screen_rect = screen_instance.get_rect()

        self.__min_length = 5
        self.__max_length = 200

        self.__length = lambda y: ((-4 * (self.__max_length - self.__min_length) / pow(self.__screen_rect.height, 2)) * pow(y, 2) +
                                   (4 * (self.__max_length - self.__min_length) / self.__screen_rect.height) * y +
                                   5)

        self.__velocity_y = velocity_y

        self.__rects = [Rect(x, y_muzzle, 4, self.__min_length) for x in x_muzzle]

    def __auto_move(self):
        for r in self.__rects:
            r.y += self.__velocity_y
            r.height = self.__length(r.y)
            if not (0 < r.y < self.__screen_rect.height):
                self.__rects.remove(r)

    def __draw(self):
        for r in self.__rects:
            rect(self.__screen, (255, 0, 0), r)

    def get_rects(self):
        return self.__rects

    def run(self):
        self.__auto_move()
        self.__draw()