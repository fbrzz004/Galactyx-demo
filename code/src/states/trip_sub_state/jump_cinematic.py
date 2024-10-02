from src.ui_components.trip_components.trip_background.wormhole_background import WormholeBackground
from src.ui_components.trip_components.trip_entity.spacecraft.spacecraft import Spacecraft


class JumpTrip:
    def __init__(self, screen_instance):

        self.__wormhole_background = WormholeBackground(
            screen_instance=screen_instance
        )

        self.__spacecraft_no_controlled = Spacecraft(
            screen_instance=screen_instance,
            static=True
        )

        self.__count_return = 100

    def draw(self):
        self.__wormhole_background.draw()
        self.__spacecraft_no_controlled.run()

    def return_next_sub_state(self):
        if self.__count_return <= 0:
            return 'Again'
        else:
            self.__count_return -= 1
        return None

    def handle_events(self, event):
        pass