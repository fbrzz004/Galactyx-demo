from pygame import Rect, Color
from pygame.draw import rect
from pygame.font import Font

from pygame.mouse import get_pos as get_pos_mouse, get_pressed

class Button:
    def __init__(self,
                 position: list[float] | tuple[float, float],
                 dimension: list[float] | tuple[float, float],
                 label: str,
                 backgrounds_button_color_default: str,
                 backgrounds_button_color_on_top_of: str,
                 label_button_color: str):

        self.__rect = Rect(*position, *dimension)
        self.__label = label

        self.__colors = {
            'default': backgrounds_button_color_default,
            'on_top_of': backgrounds_button_color_on_top_of,
        }
        self.__type_color_background = 'default'

        self.__label_color = Color(label_button_color)

        self.__font = Font(None, 20)

    def draw(self, screen_instance):
        # draw the container button
        rect(screen_instance, self.__colors[self.__type_color_background], self.__rect)

        # instance a surface with label
        text_surface = self.__font.render(self.__label, True, self.__label_color)

        # get the surface centered on container
        text_rect = text_surface.get_rect(center=self.__rect.center)

        # Place the surface at the specified position using the text_rect object
        screen_instance.blit(text_surface, text_rect)

    def __on_top_of(self):
        self.__type_color_background = 'on_top_of'

    def __on_pressed(self):
        pass

    def handle_event(self):
        if self.__rect.collidepoint(*get_pos_mouse()):
            self.__on_top_of()

            if get_pressed()[0]:
                self.__on_pressed()
                return self.__label
        else:
            self.__type_color_background = 'default'

        return None