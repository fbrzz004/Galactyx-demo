from src.states.abstract_state import AbstractState
from src.states.trip_sub_state.game_trip import GameTrip
from src.ui_components.button.text_button import TextButton

class Trip(AbstractState):
    def __init__(self, screen_instance):
        AbstractState.__init__(self, screen_instance=screen_instance)

        self.__button_to_jump = TextButton(
            position=(self._screen_rect.width - 20 - 150,
                      self._screen_rect.height - 20 - 30),
            dimension=(150, 30),
            label='Exit',
            backgrounds_button_color_default='White',
            backgrounds_button_color_on_top_of='Gray',
            label_button_color='black'
        )

        # test the jump interface
        self.__game_trip = GameTrip(screen_instance)

    def draw(self):

        # test the jump interface
        self.__game_trip.draw()


        self.__button_to_jump.draw(self._screen)



    def handle_events(self, event, machine_observer):
        if self.__button_to_jump.handle_event():
            machine_observer.exit = True
            self._exit = True
