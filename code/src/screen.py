from pygame import (
    FULLSCREEN,
    display
)

from pathlib import Path
from pygame.image import load

class Screen:
    def __init__(self,
                 size: tuple[int, int] | None = None,
                 mode = FULLSCREEN
                 ):

        # ---------------- private - attributes ----------------
        self.__screen = display.set_mode(size=size) if size else display.set_mode(flags=mode)

        self.__title = 'Galactyx'
        self.__icon_title_path = Path('assets') / 'images' / 'icon' / 'Galactyx Beta v0.1-icon.png'
        self.__icon_surface = load(str(self.__icon_title_path))

        # ---------------- initial methods execute ----------------
        self.__default()

    # ---------------- privates methods ----------------
    def __default(self):
        display.set_caption(title=self.__title)
        display.set_icon(self.__icon_surface)

    # ---------------- public methods ----------------
    def get_screen(self):
        return self.__screen
