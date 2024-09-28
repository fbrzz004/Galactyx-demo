from src.states.abstract_state import AbstractState
from src.ui_components.button.text_button import TextButton


class ArrivalCinematic(AbstractState):
    def __init__(self, screen_instance):
        AbstractState.__init__(self, screen_instance=screen_instance,
                               path_image_background="assets\\images\\ui\\background\\background_image_arrival.png")

        self.__button_to_end = TextButton(
            position=(self._screen_rect.width - 20 - 100,
                      self._screen_rect.height - 20 - 30),
            dimension=(100, 30),
            label='To End',
            backgrounds_button_color_default='White',
            backgrounds_button_color_on_top_of='Gray',
            label_button_color='Black'
        )

    def draw(self):
        self.__button_to_end.draw(self._screen)

    def handle_events(self, event, machine_observer):
        if self.__button_to_end.handle_event():
            machine_observer.ui_class = 'end'
            self._exit = True
