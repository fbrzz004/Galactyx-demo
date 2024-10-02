from pygame import Color
from pygame.image import load as load_image
from pygame.transform import scale
from pygame.draw import polygon
from random import randint

class DysonSphere:
    def __init__(self, screen_instance):

        self.__position = (0, 0)
        self.__size = (300, 300)
        self.__screen = screen_instance
        self.__screen_rect = screen_instance.get_rect()
        self.__image = load_image("assets\\images\\dyson_sphere\\dyson_sphere.png")
        self.__image = scale(self.__image, self.__size)

        self.__color = Color(255, 223, 0, 128)

        self.__points = []
        self.__active = True

        self.__time = 0

        self.__rect_energy = None

        self.__transparent_surface = None


    def __set_the_time(self, a, b):
        self.__time = randint(a, b)

    def __set_polygon(self):
        random_range = randint(100, 300)
        p1 = randint(0, self.__screen_rect.width - random_range)
        self.__points = [self.__image.get_rect().center,
                         self.__image.get_rect().center,
                         [p1, self.__screen_rect.height],
                         [p1 + random_range, self.__screen_rect.height]]

    def __draw(self):
        if self.__active:
            polygon(surface=self.__screen, color=self.__color, points=self.__points)

    def __random_behavior(self):
        if self.__time <= 0 and self.__active:
            self.__active = False
            self.__set_the_time(900, 1200)
            self.__set_polygon()

        if self.__time <= 0 and not self.__active:
            self.__active = True
            self.__set_the_time(200, 500)
            self.__set_polygon()

        self.__time -= 1

    def into_energy(self, rect) -> bool:
        if self.__active:
            return is_there_a_collision(points1=self.__points, rect=rect)
        return False

    def run(self):
        self.__screen.blit(self.__image, self.__position)
        self.__random_behavior()
        self.__draw()


def is_there_a_collision(points1: list, rect) -> bool:
    points2 = [
        [rect.x, rect.y],
        [rect.x + rect.width, rect.y],
        [rect.x + rect.width, rect.y + rect.height],
        [rect.x, rect.y + rect.height],
    ]

    rect1 = get_rect(*points1[0], *points1[2])
    rect2 = get_rect(*points1[1], *points1[3])

    for point in points2:
        if (rect1(point[0]) - point[1]) * (rect2(point[0]) - point[1]) <= 0:
            return True
    return False

def get_rect(x1, y1, x2, y2):
    return lambda x: (y2 - y1) * (x - x1) / (x2 - x1) + y1 if x2 != x1 else 0
