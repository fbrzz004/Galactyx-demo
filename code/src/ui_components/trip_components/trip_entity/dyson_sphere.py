from pathlib import Path
from pygame.image import load as load_image
from pygame.transform import scale


class DysonSphere:
    def __init__(self, screen_instance):

        self.__position = (-100, -100)
        self.__size = (300, 300)
        self.__screen = screen_instance
        self.__screen_rect = screen_instance.get_rect()
        path_image_dyson_sphere = Path("assets/images/dyson_sphere/dyson_sphere.png")
        self.__image = load_image(str(path_image_dyson_sphere))
        self.__image = scale(self.__image, self.__size)

    def __auto_move(self):
        pass

    def run(self):
        self.__screen.blit(self.__image, self.__position)
