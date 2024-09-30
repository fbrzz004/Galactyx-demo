from pathlib import Path
from src.states.abstract_state import AbstractState
from src.ui_components.button.image_button import ImageButton


class MapLevels(AbstractState):
    def __init__(self, screen_instance):
        path_image_background = Path("assets/images/ui/background/background_image_map.png")
        path_image_andromeda = Path("assets/images/galaxies/galaxy-andromeda.png")
        path_image_triangulum = Path("assets/images/galaxies/galaxy-triangulum.png")
        path_image_pegasus = Path("assets/images/galaxies/galaxy - pegasus.png")
        path_image_phoenix = Path("assets/images/galaxies/galaxy - phoenix.png")
        path_image_sculptor = Path("assets/images/galaxies/galaxy - sculptor.png")

        super().__init__(
            screen_instance=screen_instance,
            path_image_background=str(path_image_background),
            background_opacity=100
        )

        screen_width, screen_height = self._screen.get_size()

        center_position = (screen_width // 2, screen_height // 2)

        self.__andromeda = ImageButton(
            dimension=(100, 100),
            position=center_position,
            label='andromeda',
            path_image=str(path_image_andromeda)
        )

        self.__triangulum = ImageButton(
            dimension=(200, 200),
            position=(450, 40),
            label='triangulum',
            path_image=str(path_image_triangulum)
        )

        self.__pegasus = ImageButton(
            dimension=(150, 150),
            position=(100, 500),
            label='pegasus',
            path_image=str(path_image_pegasus)
        )

        self.__phoenix = ImageButton(
            dimension=(150, 150),
            position=(1150, 300),
            label='phoenix',
            path_image=str(path_image_phoenix)
        )

        self.__sculptor = ImageButton(
            dimension=(150, 150),
            position=(300, 600),
            label='sculptor',
            path_image=str(path_image_sculptor)
        )

    def draw(self):
        self.__andromeda.draw(self._screen)
        self.__triangulum.draw(self._screen)
        self.__pegasus.draw(self._screen)
        self.__phoenix.draw(self._screen)
        self.__sculptor.draw(self._screen)

    def handle_events(self, event, machine_observer):
        if self.__andromeda.handle_event():
            machine_observer.ui_class = 'trip'
            self._exit = True

        if self.__triangulum.handle_event():
            machine_observer.ui_class = 'trip'
            self._exit = True

        if self.__pegasus.handle_event():
            machine_observer.ui_class = 'trip'
            self._exit = True

        if self.__phoenix.handle_event():
            machine_observer.ui_class = 'trip'
            self._exit = True

        if self.__sculptor.handle_event():
            machine_observer.ui_class = 'trip'
            self._exit = True
