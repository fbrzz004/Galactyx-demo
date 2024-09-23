from pygame import Rect, Color
from pygame.draw import rect
from pygame.font import Font

class Button:
    def __init__(self,
                 position: list[float] | tuple[float, float],
                 dimension: list[float] | tuple[float, float],
                 label: str,
                 background_color: str,
                 label_color: str):

        self.__rect = Rect(*position, *dimension)
        self.__label = label
        self.__background_color = Color(background_color)
        self.__label_color = Color(label_color)

        self.__font = Font(None, 20)

    def draw(self, screen_instance):
        # draw the container button
        rect(screen_instance, self.__background_color, self.__rect)

        # instance a surface with label
        text_surface = self.__font.render(self.__label, True, self.__label_color)

        # get the surface centered on container
        text_rect = text_surface.get_rect(center=self.__rect.center)

        # Place the surface at the specified position using the text_rect object
        screen_instance.blit(text_surface, text_rect)
