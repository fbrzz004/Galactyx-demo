from pygame import Color
from pygame.draw import rect
from pygame.font import Font

from src.ui_components.button.abstract_button import AbstractButton

class TextButton(AbstractButton):
    def __init__(self,
                 position: list[float] | tuple[float, float],
                 dimension: list[float] | tuple[float, float],
                 label: str,
                 backgrounds_button_color_default: str,
                 backgrounds_button_color_on_top_of: str,
                 label_button_color: str):

        AbstractButton.__init__(self,
                                position=position,
                                dimension=dimension,
                                label=label,
                                scale_on_top_of=True)

        self.__colors = {
            'default': backgrounds_button_color_default,
            'on_top_of': backgrounds_button_color_on_top_of,
        }
        self.__type_color_background = 'default'

        self.__label_color = Color(label_button_color)

        self.__font = Font(None, 20)
        # instance a surface with label
        self.text_surface = self.__font.render(self._label, True, self.__label_color)

    def draw(self, screen_instance):
        # draw the container button
        rect(screen_instance, self.__colors[self.__type_color_background], self._rect)

        # get the surface centered on container
        text_rect = self.text_surface.get_rect(center=self._rect.center)

        # Place the surface at the specified position using the text_rect object
        screen_instance.blit(self.text_surface, text_rect)

    def _on_top_of(self):
        self.__type_color_background = 'on_top_of'
        self._scale()

    def _on_top_of_reset(self):
        self.__type_color_background = 'default'
        self._un_scale()

    def _on_pressed(self):
        pass

