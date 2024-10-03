from pygame.font import Font


class NameText:
    def __init__(self, screen_instance, size, text="", on_top_of_rect=None):
        self.__screen = screen_instance
        self.__font = Font(None, size)
        self.__text = text

        self.__render()

        self.__text_rect.x = ((on_top_of_rect.x + on_top_of_rect.width / 2 if on_top_of_rect else
                                             self.__screen.get_rect().x + self.__screen.get_rect().width / 2) -
                                             self.__text_rendered.get_rect().width / 2)

        self.__text_rect.y = ((on_top_of_rect.y if on_top_of_rect else
                                              self.__screen.get_rect().height) - self.__text_rendered.get_height() - 20)

    def __render(self):
        self.__text_rendered = self.__font.render(self.__text, True, (255, 255, 255))
        self.__text_rect = self.__text_rendered.get_rect()

    def show(self):
        self.__screen.blit(self.__text_rendered, (self.__text_rect.x, self.__text_rect.y))
