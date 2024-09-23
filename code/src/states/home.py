from src.states.engine_state.abstract_state import AbstractState

from src.ui_components.button.button_group import ButtonGroup

class Home(AbstractState):
    def __init__(self, screen_instance):
        AbstractState.__init__(self, screen_instance=screen_instance,
                               background_color="White")

        self.__buttons = ButtonGroup(
            screen_rect=self._screen_rect,
            labels=['Play', 'Options', 'Exit'],
            dimension=(100, 200),
            vertical_center=True,
            horizontal_center=True
        )

    def draw(self):
        self.__buttons.draw(self._screen)

    def handle_events(self, event):
        self.__buttons.handle_events(event)


