from src.states.abstract_state import AbstractState
from src.ui_components.button.image_button import ImageButton


class MapLevels(AbstractState):
    def __init__(self, screen_instance):
        AbstractState.__init__(self, screen_instance=screen_instance,
                               path_image_background="..\\assets\\images\\ui\\background\\background_image_map.jpg",
                               background_opacity=100)

        self.__andromeda = ImageButton(
            dimension=(100, 200),
            position=(200, 300),
            label='andromeda',
            path_image="..\\assets\\images\\galaxies\\galaxy-andromeda.png"
        )

        self.__triangulum = ImageButton(
            dimension=(200, 200),
            position=(450, 40),
            label='triangulum',
            path_image="..\\assets\\images\\galaxies\\galaxy-triangulum.png"
        )

    def draw(self):
        self.__andromeda.draw(self._screen)
        self.__triangulum.draw(self._screen)

    def handle_events(self, event, machine_observer):
        if self.__andromeda.handle_event():
            machine_observer.ui_class = 'trip'
            self._exit = True

        if self.__triangulum.handle_event():
            machine_observer.ui_class = 'trip'
            self._exit = True
