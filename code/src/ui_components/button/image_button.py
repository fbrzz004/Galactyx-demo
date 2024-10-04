from pygame.transform import scale
from src.ui_components.button.abstract_button import AbstractButton
from pygame.image import load as load_image

from ...fix_file_paths_compiler import resource_path

class ImageButton(AbstractButton):
    def __init__(self,
                 position: list[float] | tuple[float, float],
                 dimension: list[float] | tuple[float, float],
                 label: str,
                 path_image: str):

        AbstractButton.__init__(self,
                                position=position,
                                dimension=dimension,
                                label=label,
                                scale_on_top_of=True)

        # original and scaled image
        self.__image = self.__original_image = scale(load_image(resource_path(path_image)).convert_alpha(), dimension)
        self.__scaled_image = None

        # flag to manage the one pressed on unpressed actions
        self.__scaled = True
        self.__un_scaled = True

    def _on_pressed(self):
        pass

    def _on_top_of(self):
        if self.__scaled:
            self.__un_scaled = True
            self.__scaled = False
            self._scale()

            if not self.__scaled_image:
                self.__scaled_image = scale(self.__original_image,
                                            (self._rect.width, self._rect.height)).convert_alpha()

            self.__image = self.__scaled_image

    def _on_top_of_reset(self):
        if self.__un_scaled:
            self.__scaled = True
            self.__un_scaled = False
            self._un_scale()
            self.__image = self.__original_image

    def draw(self, screen_instance):
        screen_instance.blit(self.__image, self._rect)