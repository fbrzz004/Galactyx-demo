from pygame import (
    FULLSCREEN,
    display
)

class Screen:
    def __init__(self,
                 size: tuple[int, int] | None = None,
                 mode = FULLSCREEN
                 ):

        # ---------------- private - attributes ----------------
        self.__screen = display.set_mode(size=size) if size else display.set_mode(flags=mode)

        self.__title = 'Galactyx'
        self.__icon_title = None

        # ---------------- initial methods execute ----------------
        self.__default()

    # ---------------- privates methods ----------------
    def __default(self):
        display.set_caption(title=self.__title)

    # ---------------- public methods ----------------
    def get_screen(self):
        return self.__screen
