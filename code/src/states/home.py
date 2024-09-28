from src.states.abstract_state import AbstractState
from src.ui_components.button.button_group import ButtonGroup

class Home(AbstractState):
    def __init__(self, screen_instance):
        AbstractState.__init__(self, screen_instance=screen_instance,
                               path_image_background="assets\\images\\ui\\background\\background_image_home.jpg",
                               background_opacity=100)

        self.__buttons = ButtonGroup(
            screen_rect=self._screen_rect,
            labels=['Play', 'Exit'],
            dimension=(100, 100),
            vertical_center=True,
            horizontal_center=True,
            backgrounds_button_color_default='White',
            backgrounds_button_color_on_top_of='Gray',
            labels_button_color='Black'
        )

    def draw(self):
        self.__buttons.draw(self._screen)

    def handle_events(self, event, machine_observer):
        label_button_pressed = self.__buttons.handle_events()

        if label_button_pressed == 'Play':
            machine_observer.ui_class = 'origin_cinematic'
            self._exit = True

        elif label_button_pressed == 'Exit':
            machine_observer.exit = True
            self._exit = True
