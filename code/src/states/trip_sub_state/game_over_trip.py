from ...ui_components.trip_components.trip_background.star_background import StarBackground
from ...ui_components.button.button_group import ButtonGroup

class GameOverTrip:
    def __init__(self, screen_instance):

        self.__screen = screen_instance
        self._screen_rect = screen_instance.get_rect()

        self.__background_start = StarBackground(
            screen_instance=screen_instance
        )

        self.__buttons = ButtonGroup(
            screen_rect=self._screen_rect,
            labels=['Again', 'Home' ,'Exit'],
            dimension=(100, 150),
            vertical_center=True,
            horizontal_center=True,
            backgrounds_button_color_default='White',
            backgrounds_button_color_on_top_of='Gray',
            labels_button_color='Black'
        )

        self.__next_sub_state = None

    def draw(self):
        self.__background_start.draw()
        self.__buttons.draw(self.__screen)

    def handle_events(self, event):
        self.__next_sub_state = self.__buttons.handle_events()

    def return_next_sub_state(self):
        return self.__next_sub_state


